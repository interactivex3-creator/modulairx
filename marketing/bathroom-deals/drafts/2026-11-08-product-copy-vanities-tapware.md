> **Correction (8 Nov):** the owner confirmed the **Nimis 900 has 2 soft-close drawers**, not doors. Read any "doors" reference to the Nimis below as drawers.

# Product copy rewrite: vanities and top tapware (DRAFT)

**Prepared:** 8 Nov 2026 · **Author:** bd-product-copywriter · **Status:** draft for review. Nothing has been changed on the website.
**Source:** live WooCommerce data read on 8 Nov 2026 (`/wc/v3/products/<id>`), plus the brand brief and the 8 Nov baseline report. Every spec below comes from that product's own data. Anything the data doesn't support is marked **TBC**.

## How to read this file
- Each product has: the current short description (quoted), a new short description, a new long description (intro, key features, spec table, pairs well with, good to know), SEO title and meta, image alt text, and data gaps.
- **Prices:** copy shows the current selling price only. No "was", "save $X", "% off" or RRP wording appears anywhere in the new copy. Discounted products are listed under [Reference price evidence needed](#reference-price-evidence-needed).
- **Warranty:** a warranty term appears in the copy only where it is in that product's own data **and** the page doesn't contradict itself. Where the page contradicts itself, the spec table says **TBC** and the issue is listed as a question.
- **Lucito warranty by finish (owner correction, 8 Nov):** this is not a conflict. Black-finish Lucito products carry a different, shorter (5-year) warranty because of the black coating process. Chrome, brushed stainless, brushed brass, brushed bronze and gun metal carry the 10-year manufacturing warranty. For non-black Lucito products, the copy states the terms in that product's own data. For black Lucito products whose live text says "10 year", the copy doesn't repeat the 10-year figure. Those products are listed under [Black products whose live warranty text may be wrong](#black-products-whose-live-warranty-text-may-be-wrong).
- **Stock and dispatch:** the new copy makes no stock or dispatch-time claims. The current boilerplate "dispatched within 1–2 business days" footer should be removed or made conditional (see Open questions).
- **Fields to change on approval:** `description` and `short_description` only. Image alt text is in the media library (separate approval). SEO title/meta go in the SEO plugin fields (separate approval).

## Problems found in the current copy (apply to most pages in scope)
1. **"Currently reduced from $X to $Y"** appears in the long description of every discounted product in scope. That is a was/now claim in body text and needs reference-price evidence or removal.
2. **Vanity pages carry the tapware warranty footer** ("Tapware in this range carries a 10-year cartridge warranty and a 10-year finish warranty…"). Vanities don't have cartridges. This is wrong on all 7 vanity pages.
3. **Vanity spec tables say "WELS registered and WaterMark certified where the product category requires it."** That is not a product-specific certification and shouldn't be on a cabinet page.
4. **Template opener** "sets the tone for the whole bathroom" / "clears the bench entirely" is identical across products, which makes the pages thin for SEO and Shopping.
5. **Template line "here, the soft-close drawers"** appears on the Tarnos Tall Boy, which has soft-close **doors**, not drawers. (The Nimis 900 does have drawers: owner confirmed 8 Nov.)
6. **The warranty footer is boilerplate that sometimes disagrees with the product's own feature list.** For example, 687 says a 20-year cartridge warranty in its features and 10-year in its footer. Details are given per product.

---

# Category: Bathroom Vanities (ID 18, /product-category/bathroom-vanities/)

**Current description (quoted):**
> "Your vanity sets the tone for the whole bathroom, so it is worth getting right. Our range covers wall-hung and freestanding units from 600mm to 1500mm, in matte white, satin and timber-look finishes, with soft-close drawers as standard. …"

Note: the current text says "600mm to 1500mm". The live range is 750, 900, 1200 and 1500mm vanities plus a 350mm tall boy. There is no 600mm vanity in the category. Soft-close drawers are on the Nimis 900 (owner confirmed 8 Nov) and the Shaker range.

### New category intro (approx. 215 words)

Seven vanities and storage units, from a 750mm floor-standing Shaker to a 1500mm double-bowl Akala, all held as Australian stock in our Acacia Ridge, QLD warehouse.

**What's in the range**
- **Wall-hung:** the Tarnos 900 (oak-look laminate, solid surface top) and the Nimis 900 (natural beechwood veneer, matte white solid surface top). Both take an above-counter or semi-inset basin, which is sold separately.
- **Floor-standing Shaker:** 750, 900 and 1200mm units in satin white with a 20mm vitreous china top and integrated bowl, so there's no separate basin to buy.
- **Double bowl:** the Akala 1500 in gloss white, with a vitreous china double-bowl top.
- **Tall storage:** the Tarnos Wall Hung Tall Boy in oak, 350mm wide.

**How to choose**
Start with the wall you have. Measure the width and allow for door swing and the toilet. In a small bathroom or ensuite, a wall-hung unit leaves the floor clear, so the room reads bigger and is easier to mop. A floor-standing unit gives more storage and doesn't need wall reinforcement. Our guide [Wall-Hung vs Freestanding Vanities: Which Suits a Small Bathroom?](https://bathroomdeals.au/wall-hung-vs-freestanding-vanities-which-suits-a-small-bathroom/) goes through the trade-offs in more detail.

If you choose a top without a bowl, pick a [vanity basin](/product-category/vanity-basins/) and a matching [basin mixer](/product-category/basin-mixers/). For help matching finishes across the room, read [How to Match Tapware, Shower Systems & Bathroom Accessories Properly](https://bathroomdeals.au/how-to-match-tapware-shower-systems-amp-bathroom-accessories-properly/). You can also send us your room through [Get a package quote](/contact/).

### Category FAQ

**Do the vanities come with a basin?**
The Shaker 750, 900 and 1200 and the Akala 1500 have a vitreous china top with the bowl built in. The Tarnos 900 and Nimis 900 come with a solid surface top but no basin. They suit an above-counter or semi-inset basin, which is sold separately.

**Is tapware included?**
No. The Akala listing states that tapware, plug and waste are not included. For the other units, check the product page. (TEAM: confirm for Shaker, Tarnos and Nimis before this goes live.)

**Wall-hung or floor-standing for a small bathroom?**
Wall-hung units keep the floor clear and make cleaning easier, but they need solid fixing into the wall framing. Floor-standing units are simpler to install and usually hold more. Our [wall-hung vs freestanding guide](https://bathroomdeals.au/wall-hung-vs-freestanding-vanities-which-suits-a-small-bathroom/) covers the decision in detail.

**Do I need a plumber to install a vanity?**
Connecting the waste and the tap is plumbing work, and in Queensland and most other states it must be done by a licensed plumber.

**Can you price a full bathroom?**
Yes. Send your room size or schedule through [Get a package quote](/contact/) or call 07 4271 4620, and we'll send back a matched set with a real price.

**SEO title:** Bathroom Vanities: Wall-Hung, Shaker & Double Bowl | Bathroom Deals
**Meta description:** Wall-hung, Shaker and double-bowl bathroom vanities from 750mm to 1500mm, held in Australian stock in Brisbane. Compare sizes, tops and finishes.

---

# VANITIES

## 692 · Tarnos 900mm Wall Hung Vanity And Solid Surface Top
**SKU** TAR900WHOAKSS · **Current price** $599 · **Stock: OUT OF STOCK (0)** · Discounted (see reference price list)

> **Out of stock.** The copy below makes no availability claim. Until it's back, consider hiding it from Shopping or adding a real lead time, and pointing visitors to the Nimis 900 (679), the in-stock wall-hung alternative. This product also appears in the About-page imagery.

**Current short description:**
> "Tarnos 900mm Wall Hung Vanity And Solid Surface Top — sets the tone for the whole bathroom. 900mm L x 460mm x 520mm H."

**New short description (55 words):**
A 900mm wall-hung vanity in Autumn Harvest oak-look laminate, with a 20mm matt white solid surface top and two full-width soft-close drawers. It suits a small bathroom or ensuite where you want the floor clear and storage that pulls out fully. Takes an above-counter or semi-inset basin, sold separately.

**New long description:**

The Tarnos 900 lifts off the floor, so a small bathroom reads larger and the mop goes straight underneath. The two drawers run the full width of the cabinet, which holds more than a door-and-shelf unit of the same size and keeps everything visible. The matt white solid surface top is 20mm thick and pairs a warm oak-look front with a clean, flat surface for an above-counter or semi-inset basin.

**Key features**
- 900mm wide x 460mm deep x 520mm high
- Autumn Harvest Oak laminate cabinet finish
- 20mm matt white solid surface top
- 2 x full-width soft-close drawers with graphite interior
- Suits an above-counter or semi-inset basin (basin not included)
- 5-year warranty (as listed; scope TBC)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | TAR900WHOAKSS |
| Dimensions (W x D x H) | 900 x 460 x 520mm |
| Mounting | Wall hung |
| Cabinet finish | Autumn Harvest Oak laminate |
| Cabinet material | TBC (board type not listed; the Tarnos Tall Boy lists E1 HMR) |
| Top | Solid surface, matt white, 20mm |
| Storage | 2 x full-width soft-close drawers, graphite interior |
| Basin | Not included. Suits above-counter or semi-inset |
| Tap holes in top | TBC (none listed) |
| Waste / plumbing cut-outs in drawers | TBC |
| Wall fixing / bracket system | TBC |
| Weight | 45kg (shipping weight) |
| Warranty | 5 years (as listed). What's covered (cabinet, top, hardware) TBC |
| Price | $599 |

**Pairs well with**
- 678 Tarnos Wall Hung Tall Boy Oak: same oak finish, for tall storage beside it
- 665 Muccia 535 Semi Inset Basin White
- 661 Balun Rectangle Semi Recessed Basin Gloss White One Taphole
- 667 Lucito Tower Curved Spout Basin Mixer Brushed Brass (the combination shown in the product photo)

(659 Tarnos 600 Mirror Cabinet Satin White is in the related list but is out of stock and a different finish, so it's not suggested.)

**Good to know**
- **Installation:** wall-hung vanities need solid fixing into the wall framing. Check the fixing points and wall construction with your installer before tiling. Connecting the basin, waste and tap must be done by a licensed plumber.
- **Basin:** not included. Confirm the basin footprint and tap position before cutting the top.
- **Care:** wipe the solid surface top with a soft cloth and mild detergent. Avoid abrasive pads and harsh solvents. Wipe water off the laminate edges and don't leave it pooling. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Tarnos 900mm Wall Hung Oak Vanity, Solid Surface Top | Bathroom Deals
**Meta description:** 900mm wall-hung vanity in oak-look laminate with a 20mm matt white solid surface top and two full-width soft-close drawers. Basin sold separately.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 561 | Tarnos 900mm wall hung vanity in Autumn Harvest oak with matt white solid surface top |
| 560 | Tarnos 900 wall hung vanity cabinet dimension drawing, 900 x 460 x 520mm |
| 559 | Tarnos 900 oak wall hung vanity with brushed brass Lucito tower basin mixer in a bathroom |

**Data gaps / questions**
- Out of stock. When is it due back, and should it stay live in Shopping?
- Cabinet board material isn't listed (the Tall Boy says E1 HMR). Is it the same?
- Does the top come pre-cut for a basin and tap, or is it uncut?
- What does the 5-year warranty cover?
- Shipping dimensions (920 x 500 x 540) differ from product dimensions (900 x 460 x 520). This is fine if the larger figures are the carton, but please confirm.
- Remove the tapware warranty footer and the generic WELS/WaterMark row from this page.

---

## 686 · Akala 1500 Vanity With VC Double Bowl Top White
**SKU** AKA1500CDGWVAC · **Current price** $1,099 · **Stock:** in stock (4) · Discounted (see reference price list)

**Current short description:**
> "Akala 1500 Vanity With VC Double Bowl Top White — sets the tone for the whole bathroom. 1500mm x 460mm D x 880mm H."

**New short description (52 words):**
A 1500mm double-bowl vanity in gloss white, with a 20mm vitreous china top, soft-close drawers in the centre and soft-close doors either side. It's built for a main bathroom or ensuite shared by two people, so you each get a bowl and the storage is split between you. Tapware, plugs and wastes are sold separately.

**New long description:**

Two bowls on one 1500mm vanity mean two people can get ready at the same time without queueing. The top is 20mm vitreous china with both bowls built in, so there are no seams to clean around and no separate basins to buy. The cabinet is HMR E1 board in a gloss white painted finish, with gabled ends, soft-close drawers through the middle and a soft-close door at each end.

**Key features**
- 1500mm wide x 460mm deep x 880mm high
- 20mm vitreous china top with two integrated bowls
- Cabinet in HMR E1 board, gloss white painted finish
- Soft-close drawers in the centre, soft-close doors left and right
- Gabled ends
- 5-year product warranty (as listed; scope TBC)
- Tapware, plugs and wastes not included

**Specifications**
| Spec | Detail |
|---|---|
| SKU | AKA1500CDGWVAC |
| Dimensions (W x D x H) | 1500 x 460 x 880mm |
| Mounting | TBC (gabled ends suggest floor-standing; please confirm) |
| Cabinet material | HMR E1 board |
| Cabinet finish | Gloss white painted |
| Top | Vitreous china, double bowl, 20mm |
| Tap holes | TBC (number per bowl not listed) |
| Overflow | TBC |
| Storage | Centre soft-close drawers (number TBC), soft-close doors left and right |
| Included | Cabinet and top. Tapware, plugs and wastes not included |
| Weight | 60kg (shipping weight) |
| Warranty | 5-year product warranty (as listed). Scope TBC |
| Price | $1,099 |

**Pairs well with** (you need two basin mixers, one per bowl, once the tap-hole count is confirmed)
- 732 Lucito Straight Spout Basin Mixer Brushed Brass (x2)
- 735 Lucito Straight Spout Basin Mixer Chrome (x2)
- 1080 Lucito Tower Curved Spout Basin Mixer Chrome (x2)

**Good to know**
- **Installation:** two bowls means two waste connections and two hot/cold sets, so plan the rough-in for both before the wall is lined. Plumbing connection must be done by a licensed plumber.
- **Not included:** tapware, plugs and wastes.
- **Care:** clean vitreous china with a soft cloth and a non-abrasive cleaner. Wipe the painted cabinet with a damp cloth and dry it, and avoid harsh solvents. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Akala 1500mm Double Bowl Vanity, Gloss White | Bathroom Deals
**Meta description:** 1500mm double-bowl vanity in gloss white with a 20mm vitreous china top, soft-close drawers and doors. HMR E1 cabinet. Tapware sold separately.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 256 | Akala 1500mm gloss white vanity with vitreous china double bowl top |
| 255 | Akala 1500 vitreous china double bowl vanity top in white |

**Data gaps / questions**
- Floor-standing or wall-hung? The data says "gabled ends" but doesn't state mounting.
- How many tap holes per bowl, and is there an overflow?
- How many centre drawers?
- What does the 5-year product warranty cover?
- Image 256 file name has a typo ("WIth"). This doesn't affect the page but is worth fixing on re-upload.

---

## 679 · Nimis 900 Wall Hung Vanity With Matte White Solid Surface Top
**SKU** NIM900WHNBSS · **Current price** $965 · **Stock:** in stock (2) · Discounted (see reference price list)

**Current short description:**
> "Nimis 900 Wall Hung Vanity With Matte White Solid Surface Top — sets the tone for the whole bathroom. 900mm L x 460mm x 570mm H."

**New short description (53 words):**
A 900mm wall-hung vanity with natural beechwood veneer on the front and sides, a matte white solid surface top and two soft-close doors. It suits an ensuite or small bathroom where you want real timber grain rather than a print. Takes an above-counter or semi-inset basin, sold separately.

**New long description:**

The Nimis 900 is veneered in natural beechwood on the front and sides, so the grain is real timber rather than a printed laminate, which gives a small bathroom some warmth. Hung off the floor, it keeps the room feeling open and the floor easy to clean. The matte white solid surface top gives a flat, even base for an above-counter or semi-inset basin, and the two soft-close doors open onto the cabinet's interior.

**Key features**
- 900mm wide x 460mm deep x 570mm high
- Natural beechwood veneer on cabinet front and sides
- Matte white solid surface top
- 2 x soft-close doors
- Suits an above-counter or semi-inset basin (basin not included)
- 5-year warranty (as listed; scope TBC)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | NIM900WHNBSS |
| Dimensions (W x D x H) | 900 x 460 x 570mm |
| Mounting | Wall hung |
| Cabinet finish | Natural beechwood veneer (front and sides) |
| Cabinet core material | TBC |
| Top | Solid surface, matte white. Thickness TBC |
| Storage | 2 x soft-close doors. Interior finish TBC (listed as "Grahipe", probably "graphite") |
| Shelving | TBC |
| Basin | Not included. Suits above-counter or semi-inset |
| Tap holes in top | TBC |
| Wall fixing / bracket system | TBC |
| Weight | 45kg (shipping weight) |
| Warranty | 5 years (as listed). Scope TBC |
| Price | $965 |

**Pairs well with**
- 665 Muccia 535 Semi Inset Basin White
- 661 Balun Rectangle Semi Recessed Basin Gloss White One Taphole
- 667 Lucito Tower Curved Spout Basin Mixer Brushed Brass (brass suits the warm beechwood)
- 1076 Lucito Tower Curved Spout Basin Mixer Black (black finish, so its warranty differs from the brushed brass version)

**Good to know**
- **Installation:** wall-hung, so it needs solid fixing into the wall framing. Plan this before the wall is lined. Basin, waste and tap connection must be done by a licensed plumber.
- **Basin:** not included.
- **Care:** wipe the veneer with a soft, slightly damp cloth and dry it straight away. Don't let water sit on the edges, and don't use abrasive or solvent cleaners. Clean the solid surface top with mild detergent. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Nimis 900 Wall Hung Beechwood Vanity, Matte White Top | Bathroom Deals
**Meta description:** 900mm wall-hung vanity in natural beechwood veneer with a matte white solid surface top and two soft-close doors. Basin sold separately.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 543 | Nimis 900 wall hung beechwood vanity with matte white solid surface top in a bathroom |
| 541 | Nimis 900 wall hung vanity in natural beechwood timber veneer |
| 544 | Nimis 900 beechwood vanity with matte white top, front view |
| 542 | Nimis 900 wall hung vanity dimension drawing, 900 x 460 x 570mm |

**Data gaps / questions**
- The Finish attribute is "Matte White", but the cabinet is beechwood veneer and only the top is white. Should the attribute be "Natural Beechwood"? (It affects filters and the Shopping feed.)
- Interior finish typo ("Grahipe"). Is it graphite?
- Top thickness, cabinet core material, shelving: not listed.
- What does the 5-year warranty cover?
- The current page says "here, the soft-close drawers". This unit has doors, not drawers.
- Image 544 is called "Nimis 900 shot". Please confirm what it shows so the alt text is accurate.

---

## 668 · Shaker 900mm Double Drawer Vanity Unit and Vitreous China Top and Bowl
**SKU** VIE900SWDRDVAC · **Current price** $599 · **Stock:** in stock (2) · Discounted (see reference price list)

**Current short description:**
> "Shaker 900mm Double Drawer Vanity Unit and Vitreous China Top and Bowl — sets the tone for the whole bathroom. Floor mounted Hampton Shaker Style Vanity Unit."

**New short description (54 words):**
A 900mm floor-standing Shaker vanity in satin white, with two soft-close drawers and a 20mm gloss white vitreous china top with the bowl built in. The basin comes with it, so you only need to add a tap. It suits a Hamptons or classic main bathroom where you want proper drawer storage.

**New long description:**

The Shaker 900 brings a Hamptons look to a main bathroom or ensuite without the fiddly parts. The vitreous china top has the bowl moulded in, so there's no seam between basin and bench to collect grime, and no separate basin to choose or buy. Underneath, two soft-close drawers keep everyday things in reach. The cabinet is HMR board with MDF drawer fronts in a satin white finish. Because it stands on the floor, it doesn't need wall reinforcement.

**Key features**
- 910mm wide x 460mm deep x 880mm high
- Floor-standing, Hamptons Shaker-style cabinet
- Satin white finish
- HMR cabinet with MDF drawer fronts
- 2 x soft-close drawers
- 20mm gloss white vitreous china top with integrated bowl, one tap hole

**Specifications**
| Spec | Detail |
|---|---|
| SKU | VIE900SWDRDVAC |
| Dimensions (W x D x H) | 910 x 460 x 880mm |
| Mounting | Floor-standing |
| Cabinet material | HMR board, MDF drawer fronts |
| Cabinet finish | Satin white |
| Top | Vitreous china, gloss white, 20mm, integrated bowl |
| Tap holes | 1 |
| Overflow | TBC |
| Storage | 2 x soft-close drawers |
| Handles | TBC (finish not listed) |
| Kickboard / feet | TBC |
| Tapware, plug and waste included | TBC |
| Weight | 50kg (shipping weight) |
| Warranty | TBC (none listed for this product) |
| Price | $599 |

**Pairs well with**
- 704 Lucito Curved Spout Basin Mixer Brushed Brass
- 735 Lucito Straight Spout Basin Mixer Chrome
- 1080 Lucito Tower Curved Spout Basin Mixer Chrome
- 662 / 660 Shaker 750 and 1200: the same range in other widths

**Good to know**
- **Installation:** floor-standing, but it still needs to be secured to the wall for stability. Connecting the waste and tap must be done by a licensed plumber.
- **Tap:** one tap hole. Choose a single-hole basin mixer.
- **Care:** clean the vitreous china with a non-abrasive cleaner. Wipe the satin white cabinet with a damp cloth and dry it, and don't leave water at the base of the cabinet. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Shaker 900mm Vanity, Satin White, Vitreous China Top | Bathroom Deals
**Meta description:** 900mm Hamptons Shaker vanity in satin white with two soft-close drawers and a 20mm vitreous china top with integrated bowl. One tap hole.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 570 | Shaker 900mm satin white double drawer vanity with gloss white vitreous china top |
| 549 | Shaker 900 double drawer vanity cabinet dimension drawing |

**Data gaps / questions**
- The image file is called "Viesti 900 Kicker Double Drawer Vanity". Is this the same unit (does it have a kickboard?) or a different model's photo? Please confirm before the alt text goes live.
- No warranty is listed for any Shaker vanity, while the other vanities list 5 years. What is it?
- Overflow, handle finish, and what's included (plug and waste?) are not listed.
- The title says "Double Drawer"; the features say "Soft Close Double Drawers" on the 900 but "Twin" on the 750 and 1200. Please confirm all three have two drawers.

---

## 662 · Shaker 750mm Double Drawer Vanity Unit and Vitreous China Top and Bowl
**SKU** VIE750SWDRWVAC · **Current price** $499 · **Stock:** in stock (2) · Discounted (see reference price list)

**Current short description:**
> "Shaker 750mm Double Drawer Vanity Unit and Vitreous China Top and Bowl — sets the tone for the whole bathroom. Floor mounted Hampton Shaker Style Vanity Unit."

**New short description (53 words):**
A 750mm floor-standing Shaker vanity in satin white, with twin soft-close drawers and a 20mm gloss white vitreous china top with the bowl built in. It fits a smaller bathroom, ensuite or powder room where a 900 won't, and the basin is included, so you only need to add a tap.

**New long description:**

At 750mm wide, this is the Shaker for a smaller room: an ensuite, a second bathroom, or a tight main bathroom where a 900 would crowd the door or toilet. It has the same Hamptons Shaker cabinet as the larger sizes, in satin white with MDF drawer fronts on an HMR carcass, and the same 20mm vitreous china top with an integrated bowl. You get two soft-close drawers, one tap hole, and no separate basin to buy.

**Key features**
- 750mm wide x 460mm deep x 880mm high
- Floor-standing, Hamptons Shaker-style cabinet
- Satin white finish
- HMR cabinet with MDF drawer fronts
- Twin soft-close drawers
- 20mm gloss white vitreous china top with integrated bowl, one tap hole

**Specifications**
| Spec | Detail |
|---|---|
| SKU | VIE750SWDRWVAC |
| Dimensions (W x D x H) | 750 x 460 x 880mm |
| Mounting | Floor-standing |
| Cabinet material | HMR board, MDF drawer fronts |
| Cabinet finish | Satin white |
| Top | Vitreous china, gloss white, 20mm, integrated bowl |
| Tap holes | 1 |
| Overflow | TBC |
| Storage | 2 x soft-close drawers |
| Handles | TBC |
| Tapware, plug and waste included | TBC |
| Weight | 40kg (shipping weight) |
| Warranty | TBC (none listed) |
| Price | $499 |

**Pairs well with**
- 704 Lucito Curved Spout Basin Mixer Brushed Brass
- 742 Murcia Basin Mixer Chrome
- 735 Lucito Straight Spout Basin Mixer Chrome
- 1291 Lucito Hand Towel Rail Brushed Brass

**Good to know**
- **Installation:** secure to the wall for stability. Waste and tap connection must be done by a licensed plumber.
- **Tap:** one tap hole. Choose a single-hole basin mixer.
- **Care:** as for the Shaker 900. Use a non-abrasive cleaner on the vitreous china, and wipe and dry the satin cabinet.

**SEO title:** Shaker 750mm Vanity, Satin White, Vitreous China Top | Bathroom Deals
**Meta description:** 750mm Hamptons Shaker vanity in satin white for smaller bathrooms and ensuites. Twin soft-close drawers and a vitreous china top with integrated bowl.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 548 | Shaker 750mm satin white floor-standing vanity with vitreous china top and bowl |
| 547 | Shaker 750 double drawer vanity dimension drawing |

**Data gaps / questions**
- **The URL slug is wrong:** `/product/shaker-900mm-double-drawer-vanity-unit-and-vitreous-china-top-and-bowl-5s6gf/` on a 750mm product. Changing it needs a 301 redirect, so it's for you to decide, not the copywriter.
- Warranty, overflow, handles and inclusions: not listed (same as the Shaker 900).

---

## 660 · Shaker 1200mm Double Drawer Vanity Unit and Vitreous China Top and Bowl
**SKU** VIE1200SWDRWVAC · **Current price** $799 · **Stock:** in stock (1) · Discounted (see reference price list)
*Traffic: 27 page views and 4 Google Shopping clicks in 90 days, so this is the priority vanity page.*

**Current short description:**
> "Shaker 1200mm Double Drawer Vanity Unit and Vitreous China Top and Bowl — sets the tone for the whole bathroom. Floor mounted Hampton Shaker Style Vanity Unit."

**New short description (56 words):**
A 1200mm floor-standing Shaker vanity in satin white, with twin soft-close drawers and a 20mm gloss white vitreous china top with the bowl built in. It suits a main bathroom where you want a wide bench either side of the basin and Hamptons-style storage, and the basin is included, so you only need to add a tap.

**New long description:**

The 1200 is the widest Shaker, and the extra width goes to bench space either side of the bowl, where toothbrushes, soap and a hand towel actually end up. The 20mm vitreous china top has the bowl moulded in, so there's no seam to clean around and nothing extra to buy except a tap. Below, twin soft-close drawers sit in a satin white Hamptons Shaker cabinet made from HMR board with MDF drawer fronts. It stands on the floor, so there's no wall reinforcement to plan for.

**Key features**
- 1200mm wide x 460mm deep x 880mm high
- Floor-standing, Hamptons Shaker-style cabinet
- Satin white finish
- HMR cabinet with MDF drawer fronts
- Twin soft-close drawers
- 20mm gloss white vitreous china top with integrated bowl, one tap hole

**Specifications**
| Spec | Detail |
|---|---|
| SKU | VIE1200SWDRWVAC |
| Dimensions (W x D x H) | 1200 x 460 x 880mm |
| Mounting | Floor-standing |
| Cabinet material | HMR board, MDF drawer fronts |
| Cabinet finish | Satin white |
| Top | Vitreous china, gloss white, 20mm, integrated bowl (centred? TBC) |
| Tap holes | 1 |
| Overflow | TBC |
| Storage | 2 x soft-close drawers |
| Handles | TBC |
| Tapware, plug and waste included | TBC |
| Weight | TBC (40kg listed, identical to the 750; see questions) |
| Warranty | TBC (none listed) |
| Price | $799 |

**Pairs well with**
- 704 Lucito Curved Spout Basin Mixer Brushed Brass
- 1080 Lucito Tower Curved Spout Basin Mixer Chrome
- 742 Murcia Basin Mixer Chrome
- 1279 Lucito 750 Double Towel Rail Brushed Brass

**Good to know**
- **Installation:** secure to the wall for stability. Waste and tap connection must be done by a licensed plumber.
- **Tap:** one tap hole. Choose a single-hole basin mixer.
- **Care:** use a non-abrasive cleaner on the vitreous china, and wipe and dry the satin cabinet.

**SEO title:** Shaker 1200mm Vanity, Satin White, Vitreous China Top | Bathroom Deals
**Meta description:** 1200mm Hamptons Shaker vanity in satin white with twin soft-close drawers and a 20mm vitreous china top with integrated bowl. One tap hole.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 546 | Shaker 1200mm satin white floor-standing vanity with vitreous china top and integrated bowl |
| 545 | Shaker 1200 double drawer vanity dimension drawing |

**Data gaps / questions**
- **Shipping dimensions and weight are wrong:** WooCommerce has 800 x 500 x 900mm and 40kg, the same as the 750. A 1200mm unit can't ship in an 800mm carton. This affects freight quotes at checkout and the Shopping feed. It's a shipping-data field, so I haven't touched it. Please correct it.
- Is the bowl centred in the 1200 top?
- Only 1 left in stock.
- Warranty, overflow, handles and inclusions: not listed.

---

## 678 · Tarnos Wall Hung Tall Boy Oak
**SKU** TARTBOAK · **Current price** $399 · **Stock:** in stock (2) · Discounted (see reference price list)

**Current short description:**
> "Tarnos Wall Hung Tall Boy Oak — sets the tone for the whole bathroom. 350mm W x 450mm D x 1500mm H."

**New short description (50 words):**
A 350mm-wide wall-hung tall boy in Autumn Harvest oak-look laminate, with two soft-close doors and adjustable shelves. It adds 1500mm of upright storage for towels and refills in a bathroom where the vanity alone isn't enough, without taking up floor space. It matches the Tarnos 900 vanity.

**New long description:**

Most bathrooms run out of storage before they run out of wall. The Tarnos Tall Boy uses a 350mm-wide strip of wall for 1500mm of full-depth cupboard space, with adjustable shelves so you can fit towels, toilet rolls and spare bottles. It's wall-mounted, so the floor underneath stays clear, and it comes in the same Autumn Harvest oak finish as the Tarnos 900 vanity.

**Key features**
- 350mm wide x 450mm deep x 1500mm high
- E1 HMR board
- Autumn Harvest Oak laminate finish
- 2 x soft-close doors with graphite interior
- Adjustable shelving, full depth
- Wall-mounted installation
- 5-year warranty (as listed; scope TBC)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | TARTBOAK |
| Dimensions (W x D x H) | 350 x 450 x 1500mm |
| Mounting | Wall mounted |
| Material | E1 HMR board |
| Finish | Autumn Harvest Oak laminate |
| Doors | 2 x soft-close, graphite interior |
| Shelves | Adjustable. Number TBC |
| Door hinge side | TBC (reversible?) |
| Weight | 35kg (shipping weight) |
| Warranty | 5 years (as listed). Scope TBC |
| Price | $399 |

**Pairs well with**
- 692 Tarnos 900mm Wall Hung Vanity (same oak finish; currently out of stock)
- 679 Nimis 900 Wall Hung Vanity (timber-tone alternative; check the oak and beech side by side)
- 1291 Lucito Hand Towel Rail Brushed Brass
- 1297 Lucito Robe Hook Brushed Brass

**Good to know**
- **Installation:** at 1500mm high it must be fixed securely into the wall framing. Plasterboard alone won't hold it once loaded. No plumbing is involved.
- **Care:** wipe with a damp cloth and dry it. Keep it out of direct shower spray.

**SEO title:** Tarnos Wall Hung Tall Boy, Oak, 1500mm | Bathroom Deals
**Meta description:** 350mm-wide wall-hung bathroom tall boy in oak-look laminate, 1500mm high, with soft-close doors and adjustable shelves. Matches the Tarnos 900 vanity.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 564 | Tarnos wall hung tall boy in oak beside a vanity in a bathroom |
| 554 | Tarnos tall boy in Autumn Harvest oak, doors closed |
| 562 | Tarnos wall hung tall boy in Autumn Harvest oak laminate, front view |
| 563 | Tarnos wall hung tall boy dimension drawing, 350 x 450 x 1500mm |
| 555 | Tarnos tall boy open, showing graphite interior and adjustable shelves |

**Data gaps / questions**
- The product sits in the Bathroom Vanities category and the current copy calls it "a vanity". It's tall storage. Should it also be in a storage or cabinets category?
- Number of shelves, and are the doors reversible?
- Shipping width is 400mm against a 350mm product, which is fine if that's the carton. Please confirm.
- The current page mentions "soft-close drawers"; it has doors.
- What does the 5-year warranty cover?
- Image 564: confirm what's in the scene so the alt text is accurate.

---

# TOP TAPWARE

## 688 · Lucito Gooseneck Pull Out Sink Mixer Brushed Brass
**SKU** LUGNPOSM-BB · **Current price** $279 · **Stock:** in stock (4) · Not discounted
*Traffic: 32 page views and 5 Google Shopping clicks in 90 days, 33% engagement.*

**Current short description:**
> "Lucito Gooseneck Pull Out Sink Mixer Brushed Brass — takes more daily use than any other tap in the house. Manufactured from 304 Stainless Steel."

**New short description (60 words):**
A gooseneck kitchen mixer with a pull-out, two-function spray, made from lead-free 304 stainless steel with a PVD brushed brass finish. The high swivel spout clears tall pots, and the pull-out spray reaches every corner of the sink. It suits a kitchen reno where you want brass that lasts, with a 20-year cartridge replacement warranty.

**New long description:**

A kitchen mixer gets used more than any other tap in the house, so the parts that wear matter most. The Lucito Gooseneck has a 35mm Citec cartridge, and its lead-free body is 304 stainless steel rather than brass or zinc. The brushed brass is a PVD finish, which bonds to the metal instead of sitting on top like a plated coating. The tall swivel spout clears big pots, and the pull-out spray has two patterns, so you can rinse vegetables or blast a roasting tray, and reach every corner of a double bowl.

**Key features**
- Lead-free 304 stainless steel body
- PVD brushed brass finish
- 35mm Citec cartridge
- Swivel gooseneck spout with pull-out, two-function spray handpiece
- Polyamide braided flexible hoses
- WELS 6 star, 4L/min
- Warranty: 20-year cartridge replacement, 10-year body replacement, 7-year finish, 5-year labour

**Specifications**
| Spec | Detail |
|---|---|
| SKU | LUGNPOSM-BB |
| Body material | 304 stainless steel, lead free |
| Finish | PVD brushed brass |
| Cartridge | 35mm Citec |
| Spout | Swivel gooseneck. Height and reach TBC (see dimension drawing) |
| Spray | Pull-out handpiece, 2 functions |
| Hoses | Polyamide braided flexible |
| Flow rate / WELS | 6 star, 4L/min |
| WaterMark | TBC (no product-specific licence number listed) |
| Mounting | Hob/bench mounted, single hole. Tap-hole diameter TBC |
| Max bench thickness | TBC |
| Warranty | 20-year cartridge replacement, 10-year body replacement, 7-year finish, 5-year labour (licensed installation required) |
| Price | $279 |

**Pairs well with**
- 948 Forio 813 Double Bowl Quartz Sink White
- 927 Forio 813 Double Bowl Quartz Sink Black
- 730 Forio Quartz Small Single Bowl Sink White
- 667 Lucito Tower Curved Spout Basin Mixer Brushed Brass, to carry the same brass into the bathroom

**Good to know**
- **Installation:** must be installed by a licensed plumber, and licensed installation is a condition of the warranty. Keep your plumber's compliance certificate.
- **Gooseneck or pull-out?** This one is both. See our guide [Gooseneck vs Pull-Out Kitchen Sink Mixers](https://bathroomdeals.au/gooseneck-vs-pull-out-kitchen-sink-mixers-which-one-should-you-choose/).
- **Care:** clean the PVD brushed brass with warm soapy water and a soft cloth, then dry it. Don't use abrasive pads, bleach, vinegar or acid-based cleaners. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Lucito Gooseneck Pull Out Sink Mixer, Brushed Brass | Bathroom Deals
**Meta description:** Brushed brass gooseneck kitchen mixer with pull-out 2-function spray. Lead-free 304 stainless, 35mm cartridge, WELS 6 star. 20-year cartridge warranty.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 447 | Lucito gooseneck pull out sink mixer in brushed brass |
| 342 | Brushed brass Lucito gooseneck pull out mixer on a kitchen benchtop |
| 445 | Lucito brushed brass gooseneck pull out mixer over a kitchen sink |
| 442 | Lucito gooseneck pull out sink mixer dimension drawing |

**Data gaps / questions**
- Spout height, reach, tap-hole size and maximum bench thickness are only on the drawing image, so they aren't searchable or in the feed. Can we get the numbers?
- WaterMark licence number.
- Image 447 file name has a typo ("Pulll").
- Warranty: brushed brass, a non-black finish. The copy uses this product's own data (10-year body replacement, 20-year cartridge, 7-year finish, 5-year labour). The owner's note says non-black Lucito carries a 10-year manufacturing warranty. That matches the 10-year body figure here. Please confirm that the **7-year finish** term is still correct for brushed brass tapware. I haven't changed it to 10.

---

## 746 · Murcia Wall Mixer Black
**SKU** MUWA-BL · **Current price** $55 · **Stock:** in stock (7) · Discounted (see reference price list) · Best seller

**Current short description:**
> "Murcia Wall Mixer Black — clears the bench entirely. Contemporary pin handle design for effortless control."

**New short description (48 words):**
A matt black wall mixer with a slim pin handle and a 35mm ceramic cartridge, WaterMark approved. It's a simple, low-cost way to bring black tapware into a shower, bath or laundry reno, and it's backed by a 10-year cartridge warranty. Spout sold separately (TBC).

**New long description:**

The Murcia Wall Mixer is the plain, reliable option: a pin handle that's easy to work with wet hands, a 35mm ceramic cartridge, and a matt black finish that hides water spots better than chrome. It's WaterMark approved to Australian standards and carries a 10-year cartridge warranty. It suits a shower, a bath with a separate spout, or a laundry, wherever you want the controls on the wall and off the bench.

**Key features**
- Pin handle
- Matt black finish
- 35mm ceramic cartridge
- WaterMark approved
- 10-year cartridge warranty

**Specifications**
| Spec | Detail |
|---|---|
| SKU | MUWA-BL |
| Finish | Matt black |
| Body material | TBC |
| Cartridge | 35mm ceramic |
| Handle | Pin handle |
| Flow rate / WELS | TBC |
| WaterMark | Approved (licence number TBC) |
| Spout included | TBC |
| Backplate / dress ring size | TBC |
| Rough-in / body type | TBC |
| Warranty | 10-year cartridge. Finish TBC (conflict, see questions) |
| Price | $55 |

**Pairs well with**
- 745 Murcia Basin Mixer Black
- 737 Murcia 3 Function Shower On Rail Black
- 743 Murcia Upswept Sink Mixer Black
- 1283 Lucito 750 Single Towel Rail Black (different range, so check the black matches in person)

**Good to know**
- **Installation:** wall mixers are plumbed into the wall cavity and must be installed by a licensed plumber. Licensed installation is required for the warranty.
- **Black vs chrome:** see [Matte Black vs Chrome Tapware](https://bathroomdeals.au/matte-black-vs-chrome-tapware-which-is-best-for-your-bathroom/).
- **Care:** clean matt black with warm soapy water and a soft cloth. Don't use abrasive, bleach or acid-based cleaners, which can mark the finish.

**SEO title:** Murcia Wall Mixer, Matt Black, Pin Handle | Bathroom Deals
**Meta description:** Matt black pin-handle wall mixer with a 35mm ceramic cartridge. WaterMark approved, 10-year cartridge warranty. For showers, baths and laundries.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 300 | Murcia matt black pin handle wall mixer **(HOLD: see questions)** |
| 517 | Murcia wall mixer dimension drawing |

**Data gaps / questions**
- **Image 300 is named "ChatGPT Image Oct 6, 2025".** If it's AI-generated, it may not accurately show the real product, which is an ACL "misleading representation" risk on the main image. Please confirm or replace it with a real product photo before writing final alt text.
- **Warranty conflict:** the feature list says "10-year cartridge warranty". The footer says "10-year cartridge warranty and a 10-year finish warranty". Is there a finish warranty, and how long?
- No WELS rating, body material, dimensions or backplate size. Is a spout included, or is it a mixer only?
- The current short description says "clears the bench entirely", which is the template line for wall mixers. I've dropped it.

---

## 739 · Murcia 3 Function Shower On Rail Chrome
**SKU** MUSORC · **Current price** $79 · **Stock:** in stock (10) · Discounted (see reference price list) · Best seller

**Current short description:**
> "Murcia 3 Function Shower On Rail Chrome — installs onto your existing outlet position. Adjustable Chrome Brass Rail."

**New short description (55 words):**
A chrome shower on rail with a three-function handpiece, a 1.5m hose and an adjustable top bracket that helps when you're replacing an old shower. It's rated WELS 5 star at 6L/min and has a non-return valve fitted to meet Australian Standards. A practical, low-cost upgrade for a rental, ensuite or quick pre-sale refresh.

**New long description:**

If you're swapping out an old fixed shower head, the Murcia's adjustable top bracket lets you set the rail height to suit the wall rather than drilling new holes exactly where an old set sat. The 700mm chrome brass rail lets each person slide the handpiece to their own height, and the three spray functions cover everything from a gentle rinse to washing the dog. At WELS 5 star and 6L/min, it's one of the lower-flow options in the range. A non-return valve is included to meet Australian Standards.

**Key features**
- 700mm adjustable chrome brass rail
- Adjustable-height top bracket, suited to retrofit
- ABS three-function hand piece
- 1.5m smooth PVC shower hose
- WELS 5 star, 6L/min
- Non-return valve included (Australian Standards)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | MUSORC |
| Rail | Chrome brass, 700mm, adjustable |
| Hand piece | ABS, 3 functions. Diameter TBC |
| Hose | Smooth PVC, 1.5m |
| Finish | Chrome |
| Flow rate / WELS | 5 star, 6L/min |
| WaterMark | TBC (licence number not listed) |
| Water inlet | TBC (bottom-entry or wall elbow?) |
| Non-return valve | Included |
| Mixer included | TBC (assumed not) |
| Warranty | 1-year hose. Body/finish TBC (conflict, see questions) |
| Price | $79 |

**Pairs well with**
- 747 Murcia Wall Mixer Chrome
- 742 Murcia Basin Mixer Chrome
- 736 Murcia Upswept Sink Mixer Chrome
- 1156 Lucito Toilet Roll Holder Chrome

**Good to know**
- **Installation:** connection to the water supply must be done by a licensed plumber, and licensed installation is required for the warranty. Keep the compliance certificate.
- **Rail or twin?** See [Shower On Rail vs Twin Shower Systems](https://bathroomdeals.au/shower-on-rail-vs-twin-shower-systems-which-one-should-you-choose/).
- **Care:** wipe the chrome with warm soapy water and dry it to avoid water spots. Rub the rubber nozzles on the handpiece now and then to clear calcium build-up.

**SEO title:** Murcia 3 Function Shower On Rail, Chrome | Bathroom Deals
**Meta description:** Chrome shower on rail with 3-function handpiece, 1.5m hose and adjustable top bracket for retrofits. WELS 5 star, 6L/min, non-return valve included.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 884 | Murcia 3 function shower on rail in chrome on a concrete-look tiled shower wall |
| 509 | Murcia 3 function shower on rail in chrome, front view |
| 501 | Murcia chrome shower on rail with handpiece on rail, front view (duplicate of 509? see questions) |
| 502 | Murcia 3 function shower on rail in chrome, side view |
| 508 | Murcia chrome shower on rail installed in a bathroom |
| 510 | Murcia 3 function shower on rail dimension drawing |

**Data gaps / questions**
- **Warranty conflict:** the feature list says "1 Year Hose Warranty, 10 Years Structural Product Warranty". The footer says "12 months on hoses, 10 years on the chrome finish and a 1 year labour warranty". Is the 10 years structural, finish, or both? Is there a labour warranty?
- Shipping height is 800mm against a 700mm rail. That's fine if it's the carton.
- Water inlet position (bottom-entry or separate wall elbow), WaterMark number, handpiece diameter.
- Images 501 and 509 look like duplicates (URL-encoded file name). Delete one?
- The current copy says it "installs onto your existing outlet position". The data doesn't support that; it only says the top bracket is adjustable. I've reworded it.

---

## 667 · Lucito Tower Curved Spout Basin Mixer Brushed Brass
**SKU** LUTCBM-BB · **Current price** $249 · **Stock:** in stock (2) · Not discounted

**Current short description:**
> "Lucito Tower Curved Spout Basin Mixer Brushed Brass — sits on the vanity you use every morning. Manufactured from 304 Stainless Steel."

**New short description (58 words):**
A tall curved-spout basin mixer in PVD brushed brass, made from lead-free 304 stainless steel, with a 35mm Citec cartridge. The raised spout (194mm high, 160mm reach) is built for above-counter basins on a wall-hung vanity. It's WELS 6 star and has a 20-year cartridge replacement warranty.

**New long description:**

An above-counter basin needs a tap tall enough to clear its rim, and a standard basin mixer usually isn't. The Lucito Tower has a curved spout 194mm high with 160mm reach, so water lands in the middle of the bowl rather than on the edge. The body is lead-free 304 stainless steel with a PVD brushed brass finish, and the cartridge is a 35mm Citec. It's shown on our Tarnos oak vanity, where the brass sets off the warm timber tone.

**Key features**
- Lead-free 304 stainless steel body
- PVD brushed brass finish
- 35mm Citec cartridge
- Curved tower spout: 160mm reach, 194mm height
- Flexible PEX hoses with polyamide braided exterior
- WELS 6 star, 4L/min
- Warranty: 20-year cartridge replacement, 10-year body replacement, 7-year finish, 5-year labour

**Specifications**
| Spec | Detail |
|---|---|
| SKU | LUTCBM-BB |
| Body material | 304 stainless steel, lead free |
| Finish | PVD brushed brass |
| Cartridge | 35mm Citec |
| Spout | Curved, 160mm reach, 194mm height |
| Overall height | TBC |
| Hoses | PEX, polyamide braided |
| Flow rate / WELS | 6 star, 4L/min |
| WaterMark | TBC (licence number not listed) |
| Mounting | Bench/basin mounted, single hole. Tap-hole size TBC |
| Waste included | TBC |
| Warranty | 20-year cartridge replacement, 10-year body replacement, 7-year finish, 5-year labour (licensed installation required) |
| Price | $249 |

**Pairs well with**
- 679 Nimis 900 Wall Hung Vanity (in stock; brass suits the beechwood)
- 692 Tarnos 900 Wall Hung Vanity (the vanity it's photographed on; currently out of stock)
- 665 Muccia 535 Semi Inset Basin White
- 687 Lucito Wall Mixer and Spout Brushed Brass, for a matching bath

**Good to know**
- **Installation:** must be installed by a licensed plumber, and licensed installation is required for the warranty. Check that the spout height clears your basin rim before you buy.
- **Matching:** stay within the Lucito range for an exact brass match. See [How to Match Tapware, Shower Systems & Bathroom Accessories Properly](https://bathroomdeals.au/how-to-match-tapware-shower-systems-amp-bathroom-accessories-properly/).
- **Care:** warm soapy water and a soft cloth, then dry. No abrasive pads, bleach, vinegar or acid cleaners.

**SEO title:** Lucito Tower Basin Mixer, Curved Spout, Brushed Brass | Bathroom Deals
**Meta description:** Tall brushed brass basin mixer for above-counter basins. Curved spout 194mm high, 160mm reach. Lead-free 304 stainless, WELS 6 star, 20-year cartridge warranty.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 464 | Lucito tower curved spout basin mixer in brushed brass |
| 465 | Lucito tower curved spout basin mixer dimension drawing |

**Data gaps / questions**
- Overall height (as opposed to spout height), tap-hole size, whether a waste is included, WaterMark number.
- Only 2 product images. A lifestyle shot (like Tarnos image 559) would help.
- Only 2 in stock.

---

## 687 · Lucito Wall Mixer and Spout Brushed Brass
**SKU** LUWMB60-BB · **Current price** $249 · **Stock:** in stock (5) · Not discounted

**Current short description:**
> "Lucito Wall Mixer and Spout Brushed Brass — clears the bench entirely. Manufactured from 304 Stainless Steel."

**New short description (55 words):**
A wall mixer and 200mm curved spout set in PVD brushed brass, made from lead-free 304 stainless steel with a 35mm Citec cartridge. It suits a wall-mounted basin or a bath where you want the bench or bath edge kept clear. The two pieces arrive together, so the finish matches exactly. WELS 6 star.

**New long description:**

Moving the tap to the wall leaves nothing on the basin or bath edge to clean around, and gives you more usable space on a narrow vanity. This set pairs a Lucito wall mixer with a 200mm curved spout, both with 60mm dress rings and both in PVD brushed brass over a lead-free 304 stainless steel body. Because they come as a set, the finish matches exactly. It works over a basin or a bath.

**Key features**
- Lead-free 304 stainless steel body
- PVD brushed brass finish
- 35mm Citec cartridge
- 200mm curved spout
- 60mm diameter dress rings
- Suitable for wall basin or bath installation
- WELS 6 star, 4L/min

**Specifications**
| Spec | Detail |
|---|---|
| SKU | LUWMB60-BB |
| Includes | Wall mixer and spout |
| Body material | 304 stainless steel, lead free |
| Finish | PVD brushed brass |
| Cartridge | 35mm Citec |
| Spout | Curved, 200mm length |
| Dress rings | 60mm diameter |
| Flow rate / WELS | 6 star, 4L/min |
| WaterMark | TBC (licence number not listed) |
| Rough-in body / wall depth range | TBC |
| Suggested mixer and spout heights | TBC |
| Warranty | TBC (footer disagrees with features, see questions). Feature list says 20-year cartridge replacement, 10-year body replacement, 7-year finish, 5-year labour |
| Price | $249 |

**Pairs well with**
- 691 Lucito Wall Mixer Brushed Brass (for the shower)
- 702 Lucito Twin Shower On Rail With 250mm ABS Shower Head Brushed Brass
- 1230 Lucito 220mm Curved Bath Spout Brushed Brass (if you want a second, longer spout for the bath)
- 1291 Lucito Hand Towel Rail Brushed Brass

**Good to know**
- **Installation:** wall mixers and spouts are set into the wall before tiling, so plan the rough-in and the spout height over the basin or bath with your licensed plumber. Licensed installation is required for the warranty.
- **Care:** warm soapy water and a soft cloth, then dry. No abrasive pads, bleach, vinegar or acid cleaners.

**SEO title:** Lucito Wall Mixer and Spout Set, Brushed Brass | Bathroom Deals
**Meta description:** Brushed brass wall mixer and 200mm curved spout set for basins or baths. Lead-free 304 stainless steel, 35mm Citec cartridge, 60mm dress rings, WELS 6 star.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 483 | Lucito brushed brass wall mixer and curved spout above a basin in a bathroom |
| 484 | Lucito wall mixer and 200mm curved spout set in brushed brass |
| 486 | Lucito wall mixer and spout dimension drawing |

**Data gaps / questions**
- **Footer disagrees with the feature list on this page:** the feature list says a **20-year** cartridge replacement warranty. The generic tapware footer says a **10-year** cartridge warranty, 7-year finish and 1-year hose. This is a page-level inconsistency, separate from the black-vs-other-finishes point. Which cartridge term is right? I've left the warranty out of the short description until it's confirmed. The brushed brass finish takes the non-black Lucito terms.
- Rough-in body type and wall-depth range, recommended heights, WaterMark number.

---

## 702 · Lucito Twin Shower On Rail With 250mm ABS Shower Head Brushed Brass
**SKU** LUTSR250ABS-BB · **Current price** $529 · **Stock:** in stock (5) · Not discounted

**Current short description:**
> "Lucito Twin Shower On Rail With 250mm ABS Shower Head Brushed Brass — gives you an overhead rose and a handpiece on one set. Shower Rail manufactured from 304 Stainless Steel."

**New short description (57 words):**
A twin shower in PVD brushed brass: a 250mm overhead rose and a three-function handpiece on one 304 stainless steel rail, with water fed through the bottom of the rail. The graphite grey shower face hides calcium marks. It suits a main bathroom or ensuite where you want a rain head and a hand shower. WELS 4 star.

**New long description:**

A twin rail gives you both showers on one set: the 250mm overhead rose for everyday use, and the handpiece for rinsing hair, cleaning the shower or bathing kids. The rail is 304 stainless steel with a PVD brushed brass finish, and the water runs up through the bottom of the rail, so there's no separate arm or exposed pipe. The shower faces are graphite grey, which hides calcium marks better than white or chrome, and the hose is finished in matching brushed brass.

**Key features**
- 304 stainless steel rail, PVD brushed brass finish
- 250mm ABS overhead shower head
- ABS three-function hand piece
- Graphite grey shower faces to reduce visible calcium marks
- Smooth PVC hose in brushed brass
- Water fed through the bottom of the rail
- WELS 4 star, 7.5L/min

**Specifications**
| Spec | Detail |
|---|---|
| SKU | LUTSR250ABS-BB |
| Rail material | 304 stainless steel |
| Finish | PVD brushed brass |
| Overhead | ABS, 250mm diameter |
| Hand piece | ABS, 3 functions |
| Hose | Smooth PVC, brushed brass finish. Length TBC |
| Dimensions | 815mm H x 330mm D |
| Water inlet | Bottom of rail |
| Diverter | TBC (type and location not listed) |
| Flow rate / WELS | 4 star, 7.5L/min |
| WaterMark | TBC (licence number not listed) |
| Mixer included | TBC (assumed not) |
| Warranty | 10-year shower head, 7-year finish, 1-year hose, 1-year labour (licensed installation required) |
| Price | $529 |

**Pairs well with**
- 691 Lucito Wall Mixer Brushed Brass
- 1303 Lucito Shower Shelf Brushed Brass
- 1279 Lucito 750 Double Towel Rail Brushed Brass
- 687 Lucito Wall Mixer and Spout Brushed Brass (for the basin or bath)

**Good to know**
- **Installation:** the bottom-inlet rail needs a water point at the right height, so confirm it with your plumber before tiling. It must be installed by a licensed plumber, and licensed installation is required for the warranty. Keep the compliance certificate.
- **Rail or twin?** See [Shower On Rail vs Twin Shower Systems](https://bathroomdeals.au/shower-on-rail-vs-twin-shower-systems-which-one-should-you-choose/).
- **Care:** warm soapy water and a soft cloth on the brass, then dry. No abrasive, bleach or acid cleaners. Rub the nozzles now and then to clear calcium.

**SEO title:** Lucito Twin Shower On Rail, 250mm Head, Brushed Brass | Bathroom Deals
**Meta description:** Brushed brass twin shower on rail with 250mm overhead and 3-function handpiece on a 304 stainless rail. Bottom inlet, WELS 4 star, 7-year finish warranty.

**Image alt text**
| Image ID | New alt text |
|---|---|
| 383 | Lucito brushed brass twin shower on rail with 250mm overhead in a tiled shower |
| 467 | Lucito twin shower on rail with 250mm ABS overhead in brushed brass |
| 473 | Lucito twin shower with 250mm ABS overhead dimension drawing |

**Data gaps / questions**
- **Diverter:** the current copy says the range is "chosen on… the diverter", but the data doesn't describe a diverter at all. Where is it and what type? Does it need a separate mixer?
- Hose length, handpiece diameter, recommended inlet height, WaterMark number.
- **Warranty:** brushed brass, a non-black finish. The copy uses this product's own data (10-year shower head, 7-year finish, 1-year hose, 1-year labour). Please confirm the 7-year finish term still stands for brushed brass. I haven't changed it to 10. Note that the **black** version of this product (714) says "10 Year Warranty On Finish" in its feature list, which conflicts with the owner's note. It's listed in the black-products section below.

---

# Reference price evidence needed

These products show a sale price below a "regular" price. The new copy shows the **current price only**. Before the strikethrough "was" price stays on these pages (or in the Shopping feed), we need evidence that each product genuinely sold at the regular price for a reasonable period. The existing long descriptions also say "Currently reduced from $X to $Y" in body text. The new copy removes that.

| ID | Product | Current price | "Regular" price shown | Discount shown |
|---|---|---|---|---|
| 692 | Tarnos 900mm Wall Hung Vanity (out of stock) | $599 | $1,099 | 45% |
| 686 | Akala 1500 Vanity With VC Double Bowl Top White | $1,099 | $1,990 | 45% |
| 679 | Nimis 900 Wall Hung Vanity | $965 | $1,799 | 46% |
| 668 | Shaker 900mm Vanity | $599 | $949 | 37% |
| 662 | Shaker 750mm Vanity | $499 | $799 | 38% |
| 660 | Shaker 1200mm Vanity | $799 | $1,299 | 38% |
| 678 | Tarnos Wall Hung Tall Boy Oak | $399 | $649 | 39% |
| 746 | Murcia Wall Mixer Black | $55 | $135 | 59% |
| 739 | Murcia 3 Function Shower On Rail Chrome | $79 | $159 | 50% |

Products suggested under "Pairs well with" that are also discounted: 745 Murcia Basin Mixer Black ($55 / $175), 737 Murcia Shower On Rail Black ($90 / $199), 743 Murcia Upswept Sink Mixer Black ($79 / $229), 747 Murcia Wall Mixer Chrome ($35 / $115), 742 Murcia Basin Mixer Chrome ($49 / $129), 736 Murcia Upswept Sink Mixer Chrome ($59 / $169).

Note: every vanity in the category is discounted, and none has sold through the site. If the regular prices were never actually charged, the "was" prices should come off.

---

# Black products whose live warranty text may be wrong

Owner correction (8 Nov): black-finish Lucito products carry a different, shorter (5-year) warranty than the other finishes, because of the black coating process. I checked all 24 live Lucito black products on 8 Nov. The products below mention a **10-year** term somewhere in their live text. For any copy written about these products, the warranty is to read **"TBC: black finish carries a different warranty, confirm length"**. None of them is in this rewrite's scope, but two are suggested as pairings (1283, and 1076, which is listed for reference only).

| ID | Product | What the live text says now |
|---|---|---|
| 714 | Lucito Twin Shower On Rail With 250mm ABS Shower Head Black | Features: "**10 Year Warranty On Finish**", 10-year shower head. Footer: "5 years on the black finish". This is the clearest error. |
| 673 | Lucito Wall Mixer and Spout Black | Features: 10-year body, 20-year cartridge, 5-year finish. Footer: "10-year cartridge warranty and a **10-year finish warranty**" (generic tapware footer). |
| 1244 | Lucito Twin Shower On Rail With 250mm Stainless Steel Shower Head Black | "10 year warranty" / "Product: 10 years", 5-year finish |
| 1093 | Lucito Shower On Rail Black | "Replacement parts or product: 10 years", 5-year finish, 2-year labour (also repeated in the page FAQ) |
| 738 | Lucito Gooseneck Sink Mixer Black | 10-year body, 20-year cartridge, 5-year finish |
| 670 | Lucito Bath Filler Floor Mounted Black | 10-year body, 20-year cartridge, 5-year finish |
| 1222 | Lucito 220mm Curved Bath Spout Black | 10-year manufacturing, 5-year finish |
| 1307 | Lucito Soap Dish Black | Long description: 10-year manufacturing, 5-year finish. Short description: "5 year manufacturing and finish warranty" (contradicts itself) |
| 1301 | Lucito Shower Shelf Black | Same pattern as 1307 |
| 1295 | Lucito Robe Hook Black | Same pattern as 1307 |
| 1289 | Lucito Hand Towel Rail Black | Same pattern as 1307 |
| 1283 | Lucito 750 Single Towel Rail Black | Same pattern as 1307 (suggested as a pairing for 746) |
| 1277 | Lucito 750 Double Towel Rail Black | Same pattern as 1307 |
| 1271 | Lucito 600 Single Towel Rail Black | Same pattern as 1307 |
| 1265 | Lucito 600 Double Towel Rail Black | Same pattern as 1307 |

**Checked and not listed** (no 10-year figure in live text): 945 Toilet Roll Holder Black (5-year manufacturing and finish), 1076 Tower Curved Spout Basin Mixer Black, 731 Straight Spout Basin Mixer Black, 719 Curved Spout Basin Mixer Black (all 20-year cartridge, 5-year body, 5-year finish, 5-year labour).

**Question for the owner:** most of these pages split the terms: 10 years on body or manufacturing, 5 years on finish, and 20 years on cartridge for the tapware. Is the 5-year term **only on the black finish**, with the body and cartridge terms the same as other finishes? Or is the **whole black product** limited to 5 years? The answer decides whether pages like 738 and 670 are actually correct, and whether 1076/731/719 (5-year body) or 738/670/673 (10-year body) are the ones that need fixing.

---

# Summary: open questions for the team

**Compliance (decide first)**
1. **Was/now evidence** for the 9 in-scope products above (and 6 Murcia pairings). Keep, or drop to current price only?
2. **Lucito warranty by finish.** Per the owner, black differs from the other finishes, so the earlier "945 vs others" conflict question has been dropped. Still open:
   - **Black products with "10 year" in live text:** 15 products (see the [section above](#black-products-whose-live-warranty-text-may-be-wrong)). Confirm the black warranty length, and whether it covers the whole product or only the finish. 714 is the clearest error (it states a 10-year finish).
   - **Brushed brass tapware finish term:** 688, 667, 687 and 702 say a **7-year finish** warranty (with 10-year body). Confirm this still stands against the "10-year manufacturing" description for non-black finishes. The draft keeps 7 years as per the product data.
   - **687** footer boilerplate says a 10-year cartridge warranty; its feature list says 20-year. Which is right?
3. **Murcia warranty:** 746 says 10-year cartridge, and the footer adds a 10-year finish. 739 says "10 years structural" in features and "10 years on the chrome finish" in the footer. What is actually covered?
4. **Vanity warranty:** Tarnos, Nimis, Akala and the Tall Boy list "5 years" with no scope. **The Shaker vanities list none.** The vanity pages also carry the *tapware* warranty footer, which should come off.
5. **Remove the generic "WELS registered and WaterMark certified where required" row** from the vanity spec tables, and on tapware replace it with the actual WaterMark licence numbers (none are in the data).
6. **Image 300 on Murcia Wall Mixer Black is named "ChatGPT Image".** Is it a real product photo? If not, replace it.
7. **Dispatch footer:** "In-stock orders are dispatched… within 1–2 business days" is on every page, including the out-of-stock Tarnos 900. Can we stand behind 1–2 days? Can it be hidden when a product is out of stock?

**Data fixes (not copy, so the owner should action them)**
8. **Shaker 1200 (660) shipping dimensions and weight** are copied from the 750 (800mm carton, 40kg). That affects freight quotes and the Shopping feed.
9. **Shaker 750 (662) URL slug** says "900mm". Fix it with a 301 redirect.
10. **Nimis 900 (679) Finish attribute** says "Matte White"; the cabinet is beechwood veneer.
11. **Tarnos 900 (692) is out of stock**, as are the related 659 mirror and the brushed brass Neston wastes (633, 991). When is it due back? Should it stay in Shopping?
12. Is the Shaker 900 image ("Viesti 900 Kicker") the right product?

**Missing specs, in priority order**
13. **Vanities:** tap holes and overflow for each top; what's included (plug/waste/tap) on Shaker, Tarnos and Nimis; Akala mounting type and drawer count; Nimis top thickness and core material; wall fixing method for the wall-hung units.
14. **Tapware:** spout height and reach, and tap-hole size for 688; overall height for 667; rough-in body and wall-depth range for 687 and 746; diverter details and hose length for 702; water inlet for 739; WELS for 746; whether 746 includes a spout.
15. **Care guides:** the care notes are general good practice for each finish. Please confirm them against the manufacturers' care instructions before publishing.

**Category page**
16. The current category text says "600mm to 1500mm"; the range is actually 750–1500mm plus a 350mm tall boy. The new intro corrects this. Should the Tall Boy also sit in a storage category?
