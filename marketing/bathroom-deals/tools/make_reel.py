#!/usr/bin/env python3
"""Build a vertical 1080x1920 reel/short (MP4, H.264, 30 fps, silent) from our own
product photos and a JSON storyboard. Free: needs only Python 3 + Pillow + ffmpeg.

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
  "end": {"top": "6 finishes, one shelf", "bottom": "bathroomdeals.au", "small": "Pick up from Acacia Ridge, Brisbane", "seconds": 3}
}

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
NAVY = (20, 40, 64)
GREY = (90, 98, 110)
BG = (255, 255, 255)
PHOTO_BOX = (60, 560, 1020, 1380)  # x0, y0, x1, y1
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


def text_layer(scene):
    """Transparent overlay with the scene's text (top block ends above the photo box)."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    big, mid, small = font(FONT_BOLD, 76), font(FONT_BOLD, 60), font(FONT_REG, 40)
    if scene.get("top"):
        lines = wrap(d, scene["top"], big, 960)
        block_h = len(lines) * (big.size + 12)
        draw_block(d, scene["top"], big, NAVY, max(240, PHOTO_BOX[1] - 40 - block_h))
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


def scene_frames(scene, base_dir):
    n = int(round(scene.get("seconds", 2.5) * FPS))
    overlay = text_layer(scene)
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
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
         "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
         "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out],
        stdin=subprocess.PIPE)
    fade_n = int(FADE * FPS)
    prev_tail = []
    cover_saved = False
    for s_idx, scene in enumerate(scenes):
        frames = list(scene_frames(scene, base))
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
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", out], capture_output=True, text=True).stdout.strip()
    print(f"wrote {out} ({float(dur):.1f}s){' + cover' if cover_saved else ''}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
