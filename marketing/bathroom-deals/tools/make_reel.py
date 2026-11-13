#!/usr/bin/env python3
"""Build a vertical 1080x1920 reel/short (MP4, H.264, 30 fps) with optional voiceover + music from our own
product photos and a JSON storyboard. The build itself is free: Python 3 + Pillow + ffmpeg.
(Voiceover and music files come from ElevenLabs / Runway, which use paid credits.)

Usage:  python3 make_reel.py storyboard.json

Storyboard format (paths are relative to the storyboard file):
{
  "out": "reel-1.mp4",
  "cover": "reel-1-cover.jpg",            # optional: 1080x1920 cover frame
  "scenes": [
    {"image": "img/chrome.jpg",            # product photo (cut-out or scene)
     "fit": "pad",                         # "pad" (cut-out on white) or "crop" (fill the photo box)
     "top": "Pick a finish",               # big text above the photo
     "bottom": "Chrome  $95",              # text under the photo
     "small": "Lucito Shower Shelf",       # optional smaller line under "bottom"
     "seconds": 2.5}
  ],
  # any scene can use "images": [up to 6 paths] instead of "image" for a collage
  "end": {"top": "6 finishes, one shelf", "bottom": "bathroomdeals.au", "seconds": 3},
  "logo": "logo.png",                     # optional; defaults to ../brand-assets/bathroom-deals-logo.png

  # Audio (optional, but every published reel should have both):
  "voiceover": "vo.mp3",                  # ElevenLabs voiceover file
  "voice_delay": 0.3,                     # seconds of silence before the voice starts
  "music": "music.mp3",                   # licensed background track (looped if short)
  "music_volume": 0.22                    # music level under the voice (ducks further while talking)
}

Timing to the voice: instead of "seconds", give every scene (and the end card) an "at"
time in seconds on the final timeline (voice time + voice_delay). Find the cue points
with:  ffmpeg -i vo.mp3 -af silencedetect=noise=-35dB:d=0.2 -f null -
The end card then runs until the voice finishes plus 1.2 s.

Every frame carries the Bathroom Deals logo at the top. Never put the store location
(suburb/city) on screen or in the voiceover (owner rule).
Layout keeps all text inside the Reels/Shorts safe area (clear of the top 220 px and
the bottom 420 px, where the app's buttons and caption sit).
"""
import json
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
FADE = 0.4  # seconds of crossfade between scenes
NAVY = (52, 73, 94)      # logo navy
TEAL = (137, 188, 190)   # logo teal
GREY = (90, 98, 110)
BG = (255, 255, 255)
PHOTO_BOX = (60, 600, 1020, 1360)  # x0, y0, x1, y1
LOGO_BOX = (200, 225, 880, 365)    # logo sits here on every scene, inside the safe area
DEFAULT_LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "brand-assets", "bathroom-deals-logo.png")
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_block(draw, text, fnt, colour, y, max_w=960, gap=12):
    """Centre-aligned wrapped text starting at y. Returns the y after the block."""
    for line in wrap(draw, text, fnt, max_w):
        w = draw.textlength(line, font=fnt)
        draw.text(((W - w) / 2, y), line, font=fnt, fill=colour)
        y += fnt.size + gap
    return y


def text_layer(scene, logo=None):
    """Transparent overlay: the Bathroom Deals logo at the top, then the scene's text."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if logo is not None:
        lw, lh = LOGO_BOX[2] - LOGO_BOX[0], LOGO_BOX[3] - LOGO_BOX[1]
        scale = min(lw / logo.width, lh / logo.height)
        lg = logo.resize((round(logo.width * scale), round(logo.height * scale)), Image.LANCZOS)
        layer.alpha_composite(lg, ((W - lg.width) // 2, LOGO_BOX[1] + (lh - lg.height) // 2))
    d = ImageDraw.Draw(layer)
    big, mid, small = font(FONT_BOLD, 76), font(FONT_BOLD, 60), font(FONT_REG, 40)
    if scene.get("top"):
        size = 76  # shrink long headlines until they fit in the gap between logo and photo
        while True:
            big = font(FONT_BOLD, size)
            block_h = len(wrap(d, scene["top"], big, 960)) * (size + 12)
            if block_h <= PHOTO_BOX[1] - 25 - (LOGO_BOX[3] + 20) or size <= 44:
                break
            size -= 4
        draw_block(d, scene["top"], big, NAVY, max(LOGO_BOX[3] + 20, PHOTO_BOX[1] - 25 - block_h))
    y = PHOTO_BOX[3] + 40
    if scene.get("bottom"):
        y = draw_block(d, scene["bottom"], mid, NAVY, y)
    if scene.get("small"):
        draw_block(d, scene["small"], small, GREY, y + 6)
    return layer


def load_photo(path, fit):
    img = Image.open(path).convert("RGB")
    bw, bh = PHOTO_BOX[2] - PHOTO_BOX[0], PHOTO_BOX[3] - PHOTO_BOX[1]
    if fit == "crop":
        scale = max(bw / img.width, bh / img.height)
        img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
        l, t = (img.width - bw) // 2, (img.height - bh) // 2
        return img.crop((l, t, l + bw, t + bh))
    scale = min(bw / img.width, bh / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    box = Image.new("RGB", (bw, bh), BG)
    box.paste(img, ((bw - img.width) // 2, (bh - img.height) // 2))
    return box


def load_grid(paths, fit):
    """Collage of 2-6 photos (e.g. every finish) filling the photo box."""
    bw, bh = PHOTO_BOX[2] - PHOTO_BOX[0], PHOTO_BOX[3] - PHOTO_BOX[1]
    cols = 2 if len(paths) <= 4 else 3
    rows = -(-len(paths) // cols)
    gap = 12
    cw, ch = (bw - gap * (cols - 1)) // cols, (bh - gap * (rows - 1)) // rows
    box = Image.new("RGB", (bw, bh), BG)
    for k, path in enumerate(paths):
        img = Image.open(path).convert("RGB")
        scale = max(cw / img.width, ch / img.height) if fit == "crop" else min(cw / img.width, ch / img.height)
        img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
        cell = Image.new("RGB", (cw, ch), BG)
        cell.paste(img, ((cw - img.width) // 2, (ch - img.height) // 2))
        box.paste(cell, ((k % cols) * (cw + gap), (k // cols) * (ch + gap)))
    return box


def scene_frames(scene, base_dir, logo=None):
    n = int(round(scene.get("seconds", 2.5) * FPS))
    overlay = text_layer(scene, logo)
    if scene.get("images"):
        photo = load_grid([os.path.join(base_dir, p) for p in scene["images"]], scene.get("fit", "pad"))
    elif scene.get("image"):
        photo = load_photo(os.path.join(base_dir, scene["image"]), scene.get("fit", "pad"))
    else:
        photo = None
    for i in range(n):
        frame = Image.new("RGB", (W, H), BG)
        if photo is not None:
            z = 1.0 + 0.06 * (i / max(n - 1, 1))  # slow push-in
            bw, bh = photo.size
            zw, zh = round(bw * z), round(bh * z)
            big = photo.resize((zw, zh), Image.BILINEAR)
            l, t = (zw - bw) // 2, (zh - bh) // 2
            frame.paste(big.crop((l, t, l + bw, t + bh)), PHOTO_BOX[:2])
        frame.paste(overlay, (0, 0), overlay)
        yield frame


def main(sb_path):
    base = os.path.dirname(os.path.abspath(sb_path))
    sb = json.load(open(sb_path))
    scenes = list(sb["scenes"])
    if sb.get("end"):
        scenes.append(dict(sb["end"]))
    out = os.path.join(base, sb.get("out", "reel.mp4"))
    vo = os.path.join(base, sb["voiceover"]) if sb.get("voiceover") else None
    music = os.path.join(base, sb["music"]) if sb.get("music") else None
    delay = float(sb.get("voice_delay", 0.3))
    if vo and all("at" in sc for sc in scenes):  # cue scenes to the voiceover
        total = max(delay + probe(vo) + 1.2, scenes[-1]["at"] + 2.0)
        cues = [sc["at"] for sc in scenes] + [total]
        for k, sc in enumerate(scenes):
            sc["seconds"] = cues[k + 1] - cues[k] + (FADE if k < len(scenes) - 1 else 0)
    logo_path = os.path.join(base, sb["logo"]) if sb.get("logo") else DEFAULT_LOGO
    logo = Image.open(logo_path).convert("RGBA") if os.path.exists(logo_path) else None
    if logo is None:
        print("WARNING: logo not found, video has no logo:", logo_path)
    silent = out if not (vo or music) else out + ".silent.mp4"
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
         "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", silent],
        stdin=subprocess.PIPE)
    fade_n = int(FADE * FPS)
    prev_tail = []
    cover_saved = False
    for s_idx, scene in enumerate(scenes):
        frames = list(scene_frames(scene, base, logo))
        if s_idx == 0 and sb.get("cover"):
            frames[min(len(frames) - 1, FPS)].save(os.path.join(base, sb["cover"]), quality=90)
            cover_saved = True
        if prev_tail:  # crossfade the previous scene's tail into this scene's head
            for k, (a, b) in enumerate(zip(prev_tail, frames[:fade_n])):
                ff.stdin.write(Image.blend(a, b, (k + 1) / (fade_n + 1)).tobytes())
            frames = frames[fade_n:]
        last = s_idx == len(scenes) - 1
        body = frames if last else frames[:-fade_n]
        for f in body:
            ff.stdin.write(f.tobytes())
        prev_tail = [] if last else frames[-fade_n:]
    ff.stdin.close()
    if ff.wait() != 0:
        sys.exit("ffmpeg failed")
    if silent != out:
        add_audio(silent, out, vo, music, delay, float(sb.get("music_volume", 0.22)))
        os.remove(silent)
    print(f"wrote {out} ({probe(out):.1f}s){' + cover' if cover_saved else ''}"
          f"{' + voiceover' if vo else ''}{' + music' if music else ''}")


def probe(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip())


def add_audio(video, out, vo, music, delay, music_vol):
    """Mix voice + music under the video: music fades in/out and ducks under the voice,
    then the mix is normalised to about -14 LUFS (Instagram/YouTube loudness)."""
    dur = probe(video)
    inputs, chains, mix = ["-i", video], [], []
    idx = 1
    if vo:
        inputs += ["-i", vo]
        ms = int(delay * 1000)
        chains.append(f"[{idx}:a]aresample=48000,adelay={ms}|{ms},apad,atrim=0:{dur:.3f},asplit=2[v][vkey]")
        idx += 1
    if music:
        inputs += ["-stream_loop", "-1", "-i", music]
        fade_out = max(dur - 1.5, 0)
        chains.append(f"[{idx}:a]aresample=48000,atrim=0:{dur:.3f},volume={music_vol},"
                      f"afade=t=in:d=0.5,afade=t=out:st={fade_out:.3f}:d=1.5[m0]")
        if vo:
            chains.append("[m0][vkey]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[m]")
        else:
            chains.append("[m0]anull[m]")
        mix.append("[m]")
    if vo:
        mix.insert(0, "[v]")
    if vo and not music:
        chains.append("[vkey]anullsink")
    chains.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first,"
                  "loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(chains),
           "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
           "-ar", "48000", "-shortest", "-movflags", "+faststart", out]
    if subprocess.run(cmd).returncode != 0:
        sys.exit("audio mix failed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
