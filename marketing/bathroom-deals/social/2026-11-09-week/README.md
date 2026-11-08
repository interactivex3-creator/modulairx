# Meta Business Suite upload pack: Mon 9 – Sun 15 Nov 2026

**Status: DRAFT. Nothing has been posted or scheduled.** A person needs to approve each post exactly as written before it's scheduled.
All times are **Australia/Brisbane** (AEST, no daylight saving). Before scheduling, check that the Business Suite time zone is set to Brisbane.
Stock and prices were checked live through the WooCommerce REST API on **8 Nov 2026**.

## Preview

| # | Date | Time | Platform | First line (hook) | Product(s) and price used | Link |
|---|---|---|---|---|---|---|
| 1 | Tue 10 Nov | 7:30 pm | FB + IG | Which would you pick? Same Lucito Curved Spout Basin Mixer, four finishes. | Lucito Curved Spout Basin Mixer: Chrome $169 (728), Brushed Brass $199 (704), Gun Metal $199 (705), Black $169 (719) | https://bathroomdeals.au/product-category/basin-mixers/ |
| 2 | Thu 12 Nov | 7:30 pm | FB + IG | Small bathroom? Lift the vanity off the floor. | Nimis 900 Wall Hung Vanity $965 (679); Shaker 750mm Double Drawer Vanity $499 (662, floor-mounted, used as the comparison) | https://bathroomdeals.au/wall-hung-vs-freestanding-vanities-which-suits-a-small-bathroom/ |
| 3 | Sat 14 Nov | 9:00 am | FB + IG | The drain that disappears into your tiles. | Neston Square Tile Insert SS, DN80, $49 (651); Square Max Tile Insert SS, DN100, $109 (648); Linear Tile Insert Kit SS 800mm, DN40, $229 (655) | https://bathroomdeals.au/product-category/floor-wastes/ |
| 4 | Sun 15 Nov | 10:00 am | FB + IG | Send us your schedule and we'll match the whole room. | None (package-quote offer, no prices) | https://bathroomdeals.au/contact/ |

## What's in this folder
- `posts.csv`: one row per post, with the columns `scheduled_date, scheduled_time, platforms, post_text, link, image_file, alt_text`. Every field is double-quoted. `post_text` holds the hook, body, CTA and hashtags.
  - No `meta-bulk-template.csv` was found in `marketing/bathroom-deals/social/`, so this file uses the standard column set. If you download Meta's own template, copy each field into its columns.
- `images.md`: the images couldn't be downloaded automatically (the network blocked bathroomdeals.au). It lists the exact URLs to save as `post-1a.jpg` … `post-4.jpg`, cropped to 1080 × 1080.

## Upload steps
1. Download the images in `images.md` and save them in this folder under the names shown.
2. **Recheck stock on the morning of each post** (especially the Neston items in post 3: only one outlet size of each is in stock). If anything has sold out, don't post it, and ask for a replacement.
3. Business Suite › **Planner** › **Bulk upload** (or **Create post › Schedule**) › upload `posts.csv` and the images.
4. **Post 1 has four images.** If Bulk upload won't take several images on one row, create it with **Create post** instead: add the four images in order 1a–1d (an Instagram carousel), paste `post_text`, and add the alt text.
5. Review each post: text, link, image, alt text (Instagram › Advanced settings › Write alt text), and Facebook + Instagram both selected.
6. **Schedule.** Only do this after a named person has approved the exact wording.

## Compliance self-check (against BRAND.md)
| Rule | Result |
|---|---|
| No was/now, "save", "% off", RRP, "lowest"/"cheapest" | Pass. Only current prices are quoted. An automated word scan found none of these terms. |
| Prices are real and current | Pass. All prices came from the live `price` field on 8 Nov. For variable Neston products, the price is that of the in-stock variation. |
| Only in-stock products | Pass on 8 Nov. The Tarnos 900 (draft, out of stock) isn't mentioned. |
| Lucito warranty: black 5-year finish, other finishes 7-year finish, never 10 years on a finish | Pass. The 20-year cartridge term matches each product page. Body warranty isn't mentioned (see open issues). |
| Licensed plumber where relevant | Pass. Posts 1 and 3 say so. |
| WELS quoted only where product data has it | Pass. The product pages list "WELS 6 Star 4L/Min" for all four Lucito mixers. |
| No stock or dispatch-time promises, no fake urgency | Pass. No "in stock", "ships today" or time limits. |
| Australian English, brand voice, at most one emoji, 5–10 hashtags | Pass. 0 emoji; 10 / 9 / 9 / 8 hashtags. |
| No fake reviews, giveaways or testimonials | Pass. |

**Still to do (workflow step 5):** this pack hasn't been through `bd-compliance-reviewer` yet. I had no way to hand it over from this session.

## Open issues for the owner (site data, not the posts)
1. **Linked pages still show was/now pricing.** Nimis 900 ($965, "was" $1,799) and Shaker 750 ($499, "was" $799) are sale-priced on the site, and their descriptions say "Currently reduced from …". The posts quote only the current price, but people who click through will see the strikethrough price. This is one of the 27 products in baseline §4 that need reference-price evidence.
2. **Black Lucito body warranty conflict.** BRAND.md says black carries a 10-year manufacturing/body warranty, but the Curved Spout Black page (719) says "5 Years Body Replacement Warranty". Post 1 avoids the body term. Please check which is right and fix the page.
3. **Vanity pages carry the wrong warranty boilerplate.** Nimis 900 (679) and Shaker 750 (662) both include "Tapware in this range carries a 10-year cartridge warranty and a 10-year finish warranty", which doesn't apply to vanities. Nimis also lists "5 Year Warranty" in its features.
4. **Nimis 900 dimensions don't match.** The description says 900 × 460 × 570mm H, but the dimensions field says 920 × 500 × 600. Post 2 gives only "900mm wide".
5. **Wrong permalink.** Lucito Straight Spout Basin Mixer Brushed Brass (732) has the permalink `/product/vanity-basins/`. It isn't used this week.
6. **Floor Wastes category:** 21 of its 24 products are out of stock, so post 3's link lands on a mostly sold-out page. An alternative is to link the "Why Linear Shower Drains…" blog post or the Square Tile Insert product page.
7. **Neston stock is thin:** only one outlet size of each featured product is in stock (Square Tile Insert DN80, Square Max DN100, Linear 800 DN40). The caption names the outlet size alongside each price.
8. Post 4 would be stronger with a real Acacia Ridge warehouse or team photo. The media library doesn't have one.
