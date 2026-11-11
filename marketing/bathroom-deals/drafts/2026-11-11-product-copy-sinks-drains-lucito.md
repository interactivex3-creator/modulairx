# Product copy rewrite: Forio sinks, Neston drains, Lucito and Tarnos Tall Boy (DRAFT)

> **Compliance review (11 Nov): 5 PASS, 4 FIX (628, 655, 1096, 688), 0 BLOCK. All FIX edits are applied.** Before anything goes on the site, remove or resolve every inline "(TEAM: …)" note. There are 11 of them and they must not reach customers. Site edits need the owner's approval (description and short-description fields only).

**Prepared:** 11 Nov 2026 · **Author:** bd-product-copywriter · **Status:** draft, nothing changed on the site; pending compliance review (`bd-compliance-reviewer`), then a named person's approval.
**Brief:** section B of `drafts/2026-11-10-weekly-plan.md` (9 pages, most-viewed first).
**Source:** live WooCommerce data read on 11 Nov 2026 (`/wc/v3/products/<id>` and `/variations`), the live product pages, and `BRAND.md`. Every spec below comes from that product's own data. Anything the data doesn't support is marked **TBC**.

## How to read this file
- Each product has: the current short description (quoted), a new short description, a new long description (intro, key features, spec table, pairs well with, good to know), SEO title and meta, image alt text, and data gaps.
- **Prices:** current selling price only. None of the 9 products is on sale (`on_sale: false` on every product and variation checked). No "was", "save $X", "% off", RRP, "cheapest" or "lowest" wording appears in the new copy.
- **Warranty:** a term appears only where it's in that product's own data. Lucito follows the owner rule (8 Nov 2026): **black = 10-year body + 5-year finish; every other finish = 7-year finish**. Both Lucito products here are non-black (brushed bronze, brushed brass), so they show a 7-year finish. Every warranty line sits alongside Australian Consumer Law rights and depends on licensed installation where the product says so.
  - Note: the 8 Nov file (`2026-11-08-product-copy-vanities-tapware.md`) says non-black Lucito finishes carry 10-year cover. That is **outdated**. Don't reuse it.
- **Stock and delivery:** the new copy makes no stock-level or dispatch-time claims ("in stock now", "within 1–2 business days" and so on). The four Forio sinks and the Tall Boy are `pickup-only` and are written as **collection only from Acacia Ridge**. The Lucito and Neston items are on the `standard` shipping class.
- **Certifications:** the generic spec row "WELS registered and WaterMark certified where the product category requires it" is removed from every page. Only certifications that the product's own data states are kept (for example "WaterMark certified stainless steel basket waste included" on the 864 sinks, or "WELS 6 Star 4L/Min" on the gooseneck).
- **Pairs well with:** every product suggested was checked on 11 Nov via `/wc/v3/products?include=…`. All are in stock and not on sale, and none is on the excluded list (Brighton 985/983/684, Catral 741, Akala 686, Vattaro 727, Balun 661/663/664/723, Muccia 665, KODI 675, Tarnos 900 vanity 692). Copy shows no stock counts.
- **Fields to change on approval:** `description` and `short_description` only. Image alt text is in the media library (separate approval). SEO title/meta go in the SEO plugin fields (separate approval). The bulleted lists under "Problems found" that sit outside those fields (footer, trust badges, related products) are for the owner/developer.

## Problems found on the current pages
1. **Wrong delivery footer on two collection-only sinks.** 725 and 628 are `pickup-only`, and the top of each page already says "Warehouse collection only — this item cannot be delivered", but the footer on both still says "In-stock orders are dispatched … within 1–2 business days and delivered Australia-wide with tracking." The page contradicts itself. The new copy says collection only from Acacia Ridge, the same as the 864 pages.
2. **Generic compliance row** "WELS registered and WaterMark certified where the product category requires it" is on every page in scope, including the Tall Boy (a cabinet). It isn't a product-specific certification. Remove it.
3. **Dispatch-time boilerplate.** Footers say "within 1–2 business days" (the gooseneck gun metal page says "1–4"), and the trust badge on standard-shipping pages says "Dispatched in 1–5 business days, fully tracked". These figures don't match each other and aren't backed by product data. The new copy makes no dispatch-time claims.
4. **Trust badge "Warranty backed: Up to 15-year manufacturer cover on selected ranges"** shows on every page, including Neston (12-month warranty), Lucito (7-year finish) and the Tall Boy (5-year). "Up to" with "selected ranges" is technically qualified, but on a 12-month product it could mislead. Recommend showing each product's own term, or removing the badge on products below 15 years.
5. **Template filler.** "Every range we stock is chosen on what determines how it ages — here, the soft-close drawers" appears on the Tall Boy, which has **doors**, not drawers. "Changes a kitchen more than any other single item" and "sets the tone for the whole bathroom" are repeated across products, which makes the pages thin.
6. **Neston pages offer outlet sizes that are out of stock.** 655 says "Choose your outlet size from DN40, DN100, DN80" (only DN40 is in stock), and 648 says "from DN100, DN80" (only DN100 is in stock). The new copy names the in-stock size and says "check availability" for the others.
7. **628 dimensions line is garbled:** "Dimensions 73mm x 460mm x 228mm Depth0". The new copy marks the size TBC.
8. **725 name has no colour**, but the SKU (FORSB350BL), the feature list ("Matt Black Finish") and all three images say black, and a separate "Forio Quartz Small Single Bowl Sink White" (730) exists.
9. **WooCommerce "related products" show items we can't sell or must not feature.** These lists are generated automatically (no upsells or cross-sells are set on any of the 9 products), but they currently show: 976 → Muccia 665 and Vattaro 727 (both excluded) and the out-of-stock Tarnos mirror 659; 678 → Akala 686 (excluded) and 659; 655 → 637, 999, 631, 647 (all out of stock); 648 → 1027, 1041, 1037, 1008, 641 (all out of stock); 725 and 974 → Kalina 726 (out of stock); 688 → Neston brushed brass 633 (out of stock). Setting cross-sells to the "Pairs well with" items below would replace these.

---

# KITCHEN SINKS (Forio quartz, collection only)

## 725 · Forio Quartz Small Single Bowl Sink
**SKU** FORSB350BL · **Current price** $649 · **Stock:** in stock (5) · Not on sale · **Shipping class:** pickup-only (collection only)
*Most-viewed product from Australia in the 10 Nov report, plus a Shopping click.*

> **Name question:** the data and images say matt black, but the product name has no colour. A white version (730) exists. See data gaps. The copy below calls it "matt black" in the body and leaves the product name as it is until the team decides.

**Current short description:**
> "Forio Quartz Small Single Bowl Sink — changes a kitchen more than any other single item. Dimensions 350mm x 450mm x 235mm D."

**New short description (59 words):**
A compact 350 x 450mm single bowl sink in matt black quartz composite, 235mm deep, that can be top mounted or undermounted. It suits a small kitchen, a bar or butler's pantry, or a second prep sink. It's made from 75% quartz granite composite for heat and stain resistance, with a 15-year manufacturer's warranty. Collection only from Acacia Ridge.

**New long description:**

Not every kitchen has room for a big double bowl, and not every sink needs to be one. The Forio Small Single Bowl is 350 x 450mm and 235mm deep, which leaves bench space in a tight kitchen and works well as a prep or bar sink beside a main bowl. It's made from Granucol German-sourced quartz granite composite (75% quartz, 25% resin). The high quartz content is what gives a composite sink its heat, stain and impact resistance. The matt black finish and R25 internal corners make it easy to wipe out, and you can top mount it or undermount it to suit your benchtop.

**Key features**
- 350 x 450mm, 235mm deep
- Granucol German-sourced quartz granite composite: 75% quartz, 25% resin
- Matt black finish
- Top mount or undermount installation
- No tap landing, so the mixer goes on the benchtop or the wall
- R25 internal corners for easier cleaning
- WaterMarked stainless steel waste included
- 15-year manufacturer's warranty and 1-year labour warranty (licensed plumber required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | FORSB350BL |
| Dimensions | 350 x 450 x 235mm deep (as listed). Which figure is length and which is width: TBC |
| Bowl internal size | TBC |
| Material | Granucol quartz granite composite, 75% quartz / 25% resin |
| Finish | Matt black |
| Installation | Top mount or undermount |
| Tap holes / tap landing | None |
| Internal corners | R25 |
| Waste | WaterMarked stainless steel waste included |
| Overflow | TBC |
| Cut-out template / minimum cabinet width | TBC |
| Weight | 10kg (shipping weight) |
| Warranty | 15-year manufacturer's warranty, 1-year labour. Installation by a licensed plumber is required for the warranty to apply. This is in addition to your rights under Australian Consumer Law |
| Delivery | Collection only from our Acacia Ridge, Brisbane warehouse |
| Price | $649 |

**Pairs well with** (no tap landing, so choose a bench-mounted mixer)
- 738 Lucito Gooseneck Sink Mixer Black, $165 (same black finish)
- 646 Lucito Gooseneck Pull Out Sink Mixer Gun Metal, $279
- 688 Lucito Gooseneck Pull Out Sink Mixer Brushed Brass, $279 (brass against matt black)

**Good to know**
- **Collection only:** this sink is collected from our Acacia Ridge, Brisbane warehouse. It isn't delivered. Choose local pickup at checkout and we'll contact you to arrange a time.
- **Measure first:** check the cabinet width and benchtop before ordering. Undermounting needs a benchtop that suits it (usually stone) and a fabricator to cut and polish the opening. Check the 235mm bowl depth clears anything below.
- **Installation:** the waste and mixer must be connected by a licensed plumber. Licensed installation is a condition of the warranty, so keep your plumber's compliance certificate.
- **Sizing help:** see [What Size Kitchen Sink Should I Choose?](https://bathroomdeals.au/what-size-kitchen-sink-should-i-choose-a-complete-guide-for-australian-homes-2026/)
- **Care:** wipe out after use with warm soapy water and a soft cloth or sponge. Avoid abrasive pads and harsh chemicals. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Forio Small Single Bowl Quartz Sink, Matt Black 350mm | Bathroom Deals
**Meta description:** Compact 350 x 450mm matt black quartz sink, 235mm deep. Top mount or undermount, R25 corners, 15-year manufacturer's warranty. Collect from Acacia Ridge.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 301 | "Forio+Quartz+Small+Single+Bowl+Black+Installed+in+Kitchen+Bathroom+Deals" | Forio small single bowl sink in matt black quartz installed in a kitchen benchtop |
| 310 | "Forio Quartz Small Single Bowl Sink Black" | Forio quartz small single bowl sink in matt black, top view |
| 311 | "Forio Quartz Small Single Bowl Sink Drawing" | Forio small single bowl sink dimension drawing, 350 x 450mm, 235mm deep |

**Data gaps / questions**
- **Name and colour:** should the product be renamed "Forio Quartz Small Single Bowl Sink Black" to match its SKU, finish and images and sit alongside the White (730)? There's no Finish attribute set, and it has no "Black" tag. Renaming affects the URL and Shopping title, so it's an owner decision. If renamed, keep the old slug or add a 301.
- **Footer says it's delivered Australia-wide** within 1–2 business days. It's `pickup-only` and the top of the page says collection only. Replace the footer with the collection-only text.
- Which of 350 and 450 is the length (left to right)? What's the bowl's internal size?
- Is there an overflow? What's the cut-out size and the minimum cabinet width?
- The page says "Top Mount or Undermount". Is a template or undermount clips supplied?
- Remove the generic WELS/WaterMark row.

---

## 974 · Forio 864 Quartz Single Bowl Sink With Drainer Black
**SKU** FORSB864BL · **Current price** $820 · **Stock:** in stock (1) · Not on sale · **Shipping class:** pickup-only (collection only)
*Organic click at position 4 in the 10 Nov report.*

**Current short description:**
> "Forio 864 Quartz Single Bowl Sink With Drainer Black — a full bowl and drainer in matt black quartz. Reversible, 864mm x 484mm x 235mm deep."

**New short description (54 words):**
An 864mm top-mount sink with a single bowl and a full-length drainer, in matt black quartz composite. There's no tap hole, so it's reversible and the drainer can sit on either side. It suits a family kitchen that wants a drying area without a second bowl. 15-year manufacturer warranty. Collection only from Acacia Ridge.

**New long description:**

A drainer gives you somewhere to put wet pots and rinse produce without taking up the bench. The Forio 864 fits a full bowl and a full-length drainer into one 864 x 484mm top-mount sink, and because there's no tap hole it installs either way round, so the drainer goes on whichever side suits your kitchen. It's made from Granucol German-sourced quartz granite composite (75% quartz, 25% resin), and the matt black finish hides water marks better than a gloss surface. R25 internal corners leave no tight square corner to scrub.

**Key features**
- 864 x 484 x 235mm overall
- Single bowl with full-length drainer
- Reversible: no tap hole, so the drainer can sit left or right
- Granucol German-sourced quartz granite composite: 75% quartz, 25% resin
- Matt black finish
- Top-mount installation
- R25 internal corners
- WaterMark certified stainless steel basket waste included
- 15-year manufacturer warranty (covers manufacturing defects; licensed installation required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | FORSB864BL |
| Overall size | 864mm L x 484mm W x 235mm H |
| Bowl internal size | TBC |
| Material | Quartz granite composite, 75% quartz / 25% resin (Granucol) |
| Finish | Matt black |
| Installation | Top mount |
| Tap holes | None. Use a bench-mounted or wall-mounted mixer |
| Configuration | Single bowl with full-length drainer, reversible |
| Internal corners | R25 |
| Waste | WaterMark certified stainless steel basket waste included |
| Overflow | TBC |
| Cut-out size / minimum cabinet width | TBC (template supplied with the sink, per the current page) |
| Weight | 18kg (shipping weight) |
| Warranty | 15 years, manufacturing defects. Labour warranty TBC. Installation by a licensed tradesperson is required for the warranty to apply. This is in addition to your rights under Australian Consumer Law |
| Delivery | Collection only from our Acacia Ridge, Brisbane warehouse |
| Price | $820 |

**Pairs well with**
- 738 Lucito Gooseneck Sink Mixer Black, $165
- 646 Lucito Gooseneck Pull Out Sink Mixer Gun Metal, $279
- 645 Lucito Gooseneck Pull Out Sink Mixer Chrome, $239
- 743 Murcia Upswept Sink Mixer Black, $79

**Good to know**
- **Collection only:** collected from our Acacia Ridge, Brisbane warehouse. It isn't delivered. Choose local pickup at checkout and we'll contact you to arrange a time.
- **Before you order:** a top-mount sink sits on the benchtop, so the cut-out is smaller than the sink. Your benchtop fabricator works from the template supplied with the sink. Decide which side the drainer goes before you place the mixer, and check the 235mm bowl depth clears any drawer below.
- **Installation:** waste and mixer connection must be done by a licensed plumber. Keep the compliance certificate for the warranty.
- **Sizing help:** [What Size Kitchen Sink Should I Choose?](https://bathroomdeals.au/what-size-kitchen-sink-should-i-choose-a-complete-guide-for-australian-homes-2026/) and [Kitchen Sinks 101](https://bathroomdeals.au/kitchen-sinks-101-how-to-choose-the-right-sink-for-your-kitchen-renovation/).
- **Care:** wipe out with warm soapy water and a soft cloth. Avoid abrasive pads and harsh chemicals. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Forio 864 Quartz Sink With Drainer, Matt Black | Bathroom Deals
**Meta description:** 864 x 484mm matt black quartz sink with full-length drainer. Reversible, top mount, no tap hole, R25 corners. 15-year warranty. Collect from Acacia Ridge.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 973 | "Forio 864 matt black quartz single bowl sink with a full-length drainer, top view" | Keep as is (already descriptive) |

**Data gaps / questions**
- Only one image. Do we have an installed shot and a dimension drawing (bowl size, cut-out)?
- Is there a labour warranty? 725 and 628 state "1 year labour", the 864 pages don't.
- The 864 pages say "licensed tradesperson"; the other Forio pages say "licensed plumber". Should they read the same ("licensed plumber")?
- Bowl internal size, overflow, cut-out size.
- Remove the generic WELS/WaterMark row if present in the spec tab (the 864 pages have a cleaner spec list already).

---

## 976 · Forio 864 Quartz Single Bowl Sink With Drainer White
**SKU** FORSB864WH · **Current price** $820 · **Stock:** in stock (1) · Not on sale · **Shipping class:** pickup-only (collection only)
*Organic click at position 1 and a Shopping click in the 10 Nov report.*

**Current short description:**
> "Forio 864 Quartz Single Bowl Sink With Drainer White — a full bowl and drainer in matt white quartz. Reversible, 864mm x 484mm x 235mm deep."

**New short description (54 words):**
An 864mm top-mount sink with a single bowl and a full-length drainer, in matt white quartz composite. No tap hole means it's reversible, so the drainer sits on whichever side you need. Matt white keeps a kitchen light and suits timber or stone benchtops. 15-year manufacturer warranty. Collection only from our Acacia Ridge warehouse.

**New long description:**

Matt white quartz keeps a kitchen feeling light and sits comfortably against timber and stone benchtops. The Forio 864 puts a full bowl and a full-length drainer into one 864 x 484mm top-mount sink, and with no tap hole it installs either way round, so the drainer can go left or right. It's made from Granucol German-sourced quartz granite composite (75% quartz, 25% resin), which gives it its heat, stain and impact resistance. R25 internal corners make it easier to keep clean.

**Key features**
- 864 x 484 x 235mm overall
- Single bowl with full-length drainer
- Reversible: no tap hole, so the drainer can sit left or right
- Granucol German-sourced quartz granite composite: 75% quartz, 25% resin
- Matt white finish
- Top-mount installation
- R25 internal corners
- WaterMark certified stainless steel basket waste included
- 15-year manufacturer warranty (covers manufacturing defects; licensed installation required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | FORSB864WH |
| Overall size | 864mm L x 484mm W x 235mm H |
| Bowl internal size | TBC |
| Material | Quartz granite composite, 75% quartz / 25% resin (Granucol) |
| Finish | Matt white |
| Installation | Top mount |
| Tap holes | None. Use a bench-mounted or wall-mounted mixer |
| Configuration | Single bowl with full-length drainer, reversible |
| Internal corners | R25 |
| Waste | WaterMark certified stainless steel basket waste included |
| Overflow | TBC |
| Cut-out size / minimum cabinet width | TBC (template supplied with the sink, per the current page) |
| Weight | 18kg (shipping weight) |
| Warranty | 15 years, manufacturing defects. Labour warranty TBC. Installation by a licensed tradesperson is required for the warranty to apply. This is in addition to your rights under Australian Consumer Law |
| Delivery | Collection only from our Acacia Ridge, Brisbane warehouse |
| Price | $820 |

**Pairs well with**
- 688 Lucito Gooseneck Pull Out Sink Mixer Brushed Brass, $279
- 666 Lucito Gooseneck Pull Out Sink Mixer Brushed Stainless, $239
- 645 Lucito Gooseneck Pull Out Sink Mixer Chrome, $239
- 736 Murcia Upswept Sink Mixer Chrome, $59

**Good to know**
- **Collection only:** collected from our Acacia Ridge, Brisbane warehouse. It isn't delivered. Choose local pickup at checkout and we'll contact you to arrange a time.
- **Before you order:** the cut-out is smaller than the sink, and your fabricator works from the supplied template. Decide the drainer side before placing the mixer, and check the 235mm bowl depth clears any drawer below.
- **Installation:** waste and mixer connection must be done by a licensed plumber. Keep the compliance certificate for the warranty.
- **Sizing help:** [What Size Kitchen Sink Should I Choose?](https://bathroomdeals.au/what-size-kitchen-sink-should-i-choose-a-complete-guide-for-australian-homes-2026/)
- **Care:** wipe out with warm soapy water and a soft cloth, and rinse off coffee, tea and beetroot rather than leaving them to sit on a white surface. Avoid abrasive pads and harsh chemicals. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Forio 864 Quartz Sink With Drainer, Matt White | Bathroom Deals
**Meta description:** 864 x 484mm matt white quartz sink with full-length drainer. Reversible, top mount, no tap hole, R25 corners. 15-year warranty. Collect from Acacia Ridge.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 975 | "Forio 864 matt white quartz single bowl sink with a full-length drainer, top view" | Keep as is (already descriptive) |

**Data gaps / questions**
- The automatic related-products list shows **Muccia 665 and Vattaro 727 (both excluded)** and the out-of-stock Tarnos mirror 659. Set cross-sells (see the pairings above) so these stop showing.
- Same questions as 974: labour warranty, "tradesperson" vs "plumber", bowl size, overflow, cut-out, more images.

---

## 628 · Forio Single Bowl Large Sink Black
**SKU** FORSBL730BL · **Current price** $749 · **Stock:** in stock (2) · Not on sale · **Shipping class:** pickup-only (collection only)

**Current short description:**
> "Forio Single Bowl Butler Sink Black — changes a kitchen more than any other single item. Made from "Granucol" German sourced 75% quartz granite composite material, 25% resin."

**New short description (50 words):**
A large single bowl undermount sink in matt black quartz composite, for a kitchen where one big bowl is more useful than two small ones. Made from 75% quartz granite composite with R28 internal corners and a chrome basket waste. 15-year product warranty. Collection only from our Acacia Ridge warehouse.

**New long description:**

A single large bowl gives you one open space for big pots and trays rather than two smaller bowls. The Forio Large Single Bowl is an undermount sink, so it sits below a stone benchtop and you can wipe crumbs straight into it with no rim in the way. It's made from Granucol German-sourced quartz granite composite (75% quartz, 25% resin), finished in matt black, with R28 internal corners for easier cleaning. A WaterMarked chrome basket waste is included.

**Key features**
- Large single bowl, undermount installation
- Granucol German-sourced quartz granite composite: 75% quartz, 25% resin
- Matt black finish
- R28 internal corners for easier cleaning
- WaterMarked chrome basket waste included
- 15-year product warranty, 1-year labour warranty (licensed plumber required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | FORSBL730BL |
| Dimensions | **TBC** (the current page reads "73mm x 460mm x 228mm Depth0", which is garbled. The shipping carton is 800 x 500 x 250mm, which is not the sink size) |
| Bowl internal size | TBC |
| Material | Granucol quartz granite composite, 75% quartz / 25% resin |
| Finish | Matt black |
| Installation | Undermount |
| Tap holes | TBC (none listed) |
| Internal corners | R28 |
| Waste | WaterMarked chrome basket waste included |
| Overflow | TBC |
| Cut-out size / minimum cabinet width | TBC |
| Weight | 30kg (shipping weight) |
| Warranty | 15-year product / manufacturer's warranty, 1-year labour. Installation by a licensed plumber is required for the warranty to apply. This is in addition to your rights under Australian Consumer Law |
| Delivery | Collection only from our Acacia Ridge, Brisbane warehouse |
| Price | $749 |

**Pairs well with** (undermount, so the mixer goes on the benchtop)
- 738 Lucito Gooseneck Sink Mixer Black, $165
- 646 Lucito Gooseneck Pull Out Sink Mixer Gun Metal, $279
- 1061 Lucito Gooseneck Pull Out Sink Mixer Brushed Bronze, $279
- 743 Murcia Upswept Sink Mixer Black, $79

**Good to know**
- **Collection only:** collected from our Acacia Ridge, Brisbane warehouse. It isn't delivered. Choose local pickup at checkout and we'll contact you to arrange a time.
- **Undermount:** the sink is fixed beneath the benchtop, so it suits stone or another solid benchtop that can be cut and edge-polished. Your benchtop fabricator should have the sink (or its template) before cutting. Plan the mixer hole in the benchtop at the same time.
- **Installation:** waste and mixer connection must be done by a licensed plumber. Keep the compliance certificate for the warranty.
- **Sizing help:** [What Size Kitchen Sink Should I Choose?](https://bathroomdeals.au/what-size-kitchen-sink-should-i-choose-a-complete-guide-for-australian-homes-2026/)
- **Care:** wipe out with warm soapy water and a soft cloth. Avoid abrasive pads and harsh chemicals. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Forio Large Single Bowl Undermount Quartz Sink, Black | Bathroom Deals
**Meta description:** Large single bowl undermount sink in matt black quartz composite. R28 corners, chrome basket waste, 15-year product warranty. Collect from Acacia Ridge, Brisbane.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 900 | *(empty)* | Forio large single bowl undermount sink in matt black quartz composite |

**Data gaps / questions**
- **Dimensions are garbled** ("73mm x 460mm x 228mm Depth0"). Please supply the overall size, bowl size and cut-out. (The SKU FORSBL730BL and the image file name "Forio 730 Large Single Bowl" suggest 730mm, but I haven't used that. Please confirm from the spec sheet.)
- **Footer says it's delivered Australia-wide** within 1–2 business days. It's `pickup-only`, and the top of the page says collection only. Replace the footer with the collection-only text.
- **Short description calls it a "Butler Sink"**; the name says "Large Sink". Which is right? (729 is a separate Forio butler sink.)
- The waste is chrome on a black sink. Is a black waste available, or is chrome what ships?
- Tap holes: none are listed. Confirm.
- Features say "15 Year Product Warranty"; footer says "15 years manufacturer's warranty". Use one wording.
- Only one image, with empty alt text. Do we have an installed shot and a drawing?
- Remove the generic WELS/WaterMark row.

---

# DRAINAGE (Neston stainless)

## 655 · Neston Linear Tile Insert Drain Stainless Steel Kit 800mm
**SKU** NS105TI24SS-800 · **Price** $229 (DN40) · Not on sale · **Shipping class:** standard
**Variation stock (11 Nov):** DN40 (656, $229) in stock, 1 · DN80 (658, $259) **out of stock** · DN100 (657, $259) **out of stock**

> The copy names DN40 as the listed outlet and says "check availability" for DN80 and DN100. It doesn't say any size is in stock, and gives no quantity.

**Current short description:**
> "Neston Linear Tile Insert Drain Stainless Steel Kit 800mm — a linear channel that takes a cut strip of your own tile, so the drain reads as a grout line rather than a grate. Manufactured From 316 Stainless Steel."

**New short description (56 words):**
An 800mm linear shower drain in 316 stainless steel with a tile insert tray, so a strip of your own floor tile (up to 10mm) sits in the top and the drain reads as a thin line. It's listed as fully customisable on site. Listed with a DN40 outlet; for DN80 or DN100, check availability.

**New long description:**

A tile insert drain takes a strip of the same tile as your shower floor, so all you see is two thin stainless lines instead of a grate. It also lets the floor fall one way to a single line, which suits large-format tiles. This Neston kit is 800mm long and 105mm wide, made from 316 stainless steel in a brushed finish, with a V-bottom channel to move water to the outlet and a 2mm folded channel edge. It comes with loose end caps and a loose outlet and is listed as fully customisable on site. For the full case for linear drains, read [Why Linear Shower Drains Are the Preferred Choice for Modern Australian Bathrooms](https://bathroomdeals.au/why-linear-shower-drains-are-the-preferred-choice-for-modern-australian-bathrooms/).

**Key features**
- 316 stainless steel, brushed stainless finish
- 800mm long x 105mm wide x 24mm deep
- Tile insert tray, suits tile up to 10mm thick
- V-bottom channel for flow and discharge
- 2mm folded channel edge
- Supplied with loose end caps and a loose outlet; can be customised on site
- WaterMark approved (as listed)
- 12-month warranty (licensed plumber required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | NS105TI24SS-800 (DN40: NS105TI24SS-800DN40) |
| Length x width x depth | 800 x 105 x 24mm (listed in features; the Additional information tab says 106mm wide, see gaps) |
| Material | 316 stainless steel |
| Finish | Brushed stainless steel |
| Tile insert | Suits tile up to 10mm thick |
| Channel | V-bottom, 2mm folded edge |
| Outlet | DN40 ($229). DN80 and DN100 ($259): check availability |
| Outlet position | TBC |
| Included | Loose end caps, loose outlet |
| Customisable on site | Yes, as listed. Whether it can be cut to length, and the minimum length: TBC |
| Flow rate | TBC |
| WaterMark | Listed as "Watermarked Approved". Licence number TBC |
| Weight | 3kg (shipping weight) |
| Warranty | 12 months. Installation by a licensed plumber is required for the warranty to apply. This is in addition to your rights under Australian Consumer Law |
| Price | $229 (DN40) |

**Pairs well with** (same 316 stainless, brushed finish)
- 648 Neston Square Max Tile Insert Floor Waste Grate Stainless Steel, from $109 (listed in DN100; check availability for other sizes)
- 651 Neston Square Tile Insert Floor Waste Grate Stainless Steel, from $49 (listed in DN80; check availability for other sizes)
- 1094 Lucito Shower On Rail Brushed Stainless, $199

**Good to know**
- **Outlet size:** your plumber will confirm which outlet size your floor needs before you order. Choose the size on the product page; if the size you need shows as unavailable, call 07 4271 4620.
- **Installation:** floor wastes are plumbing work and must be installed by a licensed plumber, with waterproofing done before the drain is set. The floor needs to fall to the channel. Licensed installation is a condition of the warranty.
- **Tile:** cut the insert strip from the same tile as the floor. The tray suits tile up to 10mm thick.
- **Care:** lift the insert tray now and then and clear hair and soap build-up from the channel. Clean the stainless with warm soapy water and a soft cloth; avoid steel wool, bleach and chlorine cleaners. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Neston 800mm Tile Insert Linear Shower Drain, 316 Stainless | Bathroom Deals
**Meta description:** 800mm linear shower drain in 316 brushed stainless with a tile insert tray for tiles up to 10mm. Customisable on site, V-bottom channel. 12-month warranty.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 327 | "Neston Linear Tile Insert Drain Stainless Steel" | Neston 800mm linear tile insert shower drain in brushed 316 stainless steel |

**Data gaps / questions**
- **Current long description says "Choose your outlet size from DN40, DN100, DN80"**, but DN80 and DN100 are out of stock. Replace it with the new copy. Owner decision still open (weekly plan): restock date, backorder with a real lead time, or hide the out-of-stock sizes.
- Width: features say 105mm, the Additional information tab says 106mm. Which is right?
- Where does the outlet sit (centre or end), and what's the minimum cut length?
- Flow rate (L/s) for each outlet size, and the WaterMark licence number.
- Only one image. Do we have a drawing and an installed shot?
- The automatic related products are all out of stock (637, 999, 631, 647). Set cross-sells.
- The trust badge says "Up to 15-year manufacturer cover" on a 12-month product. See Problems found, item 4.
- Remove the generic WELS/WaterMark row and the "1–2 business days" footer.

---

## 648 · Neston Square Max Tile Insert Floor Waste Grate Stainless Steel
**SKU** NSSQM120T34SS · **Price** $109 (DN100) · Not on sale · **Shipping class:** standard
**Variation stock (11 Nov):** DN100 (649, $109) in stock, 1 · DN80 (650, $119) **out of stock**

**Current short description:**
> "Neston Square Max Tile Insert Floor Waste Grate Stainless Steel — an oversized tile-insert waste for higher flow, finished with a cut piece of your own tile. Manufactured from 316 Stainless Steel."

**New short description (46 words):**
A 120 x 120mm square floor waste in 316 stainless steel with a tile insert tray that takes floor tile up to 20mm thick, so only a thin stainless frame shows. It suits showers, ensuites and laundries. Listed with a DN100 outlet; for DN80, check availability.

**New long description:**

A tile insert floor waste lets the floor tile run over the drain, so you see a neat stainless square instead of a grate. The Square Max is 120 x 120mm and 33mm deep, and its tray takes tile up to 20mm thick, which suits thicker porcelain and stone. It's made from 316 stainless steel in a brushed finish, with a 2mm external tray edge and a folded internal edge on the insert tray.

**Key features**
- 316 stainless steel, brushed stainless finish
- 120 x 120mm, 33mm deep
- Tile insert tray, suits floor tile up to 20mm thick
- 2mm external tray edge
- Folded internal tile insert tray edge
- WaterMark approved (as listed)
- 12-month warranty (licensed plumber required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | NSSQM120T34SS (DN100: NSSQM120T34SS-DN100) |
| Size | 120 x 120mm, 33mm deep |
| Material | 316 stainless steel |
| Finish | Brushed stainless steel |
| Tile insert | Suits tile up to 20mm thick |
| Edges | 2mm external tray edge; folded internal tile insert tray edge |
| Outlet | DN100 ($109). DN80 ($119): check availability |
| Flow rate | TBC |
| Puddle flange / waterproofing interface | TBC |
| WaterMark | Listed as "Watermarked Approved". Licence number TBC |
| Weight | 1kg (shipping weight) |
| Warranty | 12 months. Installation by a licensed plumber is required for the warranty to apply. This is in addition to your rights under Australian Consumer Law |
| Price | $109 (DN100) |

**Pairs well with** (same 316 stainless, brushed finish)
- 655 Neston Linear Tile Insert Drain Stainless Steel Kit 800mm, $229 (listed in DN40; check availability for other sizes)
- 651 Neston Square Tile Insert Floor Waste Grate Stainless Steel, from $49 (listed in DN80), for a second waste in the same room
- 1094 Lucito Shower On Rail Brushed Stainless, $199

**Good to know**
- **Outlet size:** your plumber will confirm the outlet size your floor needs before you order. If the size you need shows as unavailable, call 07 4271 4620.
- **Installation:** floor wastes must be installed by a licensed plumber, with waterproofing done first and the floor falling to the waste. Licensed installation is a condition of the warranty.
- **Tile:** cut the insert from the same tile as the floor, up to 20mm thick.
- **Care:** lift the insert now and then and clear hair and soap build-up. Clean the stainless with warm soapy water and a soft cloth; avoid steel wool, bleach and chlorine cleaners. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Neston Square Max Tile Insert Floor Waste, 316 Stainless | Bathroom Deals
**Meta description:** 120 x 120mm square tile insert floor waste in brushed 316 stainless steel. Takes floor tile up to 20mm thick. 12-month warranty. Licensed plumber to install.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 531 | "Neston Square Max Tile Insert Grate Stainless Steel" | Neston Square Max 120mm tile insert floor waste in brushed 316 stainless steel |
| 530 | "Neston Square Max Tile Insert Grate Stainless Steel Top View" | Neston Square Max stainless tile insert floor waste, top view showing the tile tray |

**Data gaps / questions**
- **Current long description says "Choose your outlet size from DN100, DN80"**, but DN80 is out of stock. Replace it with the new copy.
- The current copy says "handles a higher flow rate" and "oversized … for higher flow". There's no flow figure in the data, so the new copy doesn't make the claim. Can we get the flow rate (L/s) per outlet?
- Is there a puddle flange, and what does the waste connect to?
- WaterMark licence number.
- All five automatic related products are out of stock (1027, 1041, 1037, 1008, 641). Set cross-sells.
- Trust badge "Up to 15-year manufacturer cover" on a 12-month product (Problems found, item 4).
- Remove the generic WELS/WaterMark row and the "1–2 business days" footer.

---

# LUCITO

## 1096 · Lucito Shower On Rail Brushed Bronze
**SKU** LUWTRS-BR · **Current price** $229 · **Stock:** in stock (2) · Not on sale · **Shipping class:** standard

**Current short description:**
> "Lucito Shower On Rail Brushed Bronze – 304 stainless steel rail with a 3 function ABS hand piece and an adjustable bottom bracket for renovations. WELS 4 star, 7.5L/min."

**New short description (54 words):**
A brushed bronze shower on rail with a 304 stainless steel rail, a three-function hand piece and an adjustable bottom bracket, which helps when you're working with existing wall positions in a reno. Water feeds through the top bracket. WELS 4 star, 7.5L/min, with a 10-year replacement parts warranty and a 7-year finish warranty.

**New long description:**

A shower on rail lets everyone set the hand piece at their own height, and it's simple to swap in during a bathroom refresh. The Lucito rail and brackets are 304 stainless steel in a brushed bronze finish, a warm tone that sits between brass and gun metal. The bottom bracket adjusts, and the bracket spacing goes from 600mm out to 640mm, which helps when the existing fixing points are already set. Water connects through the top bracket (G1/2" thread), and the ABS hand piece has three spray functions. It's rated WELS 4 star at 7.5 litres a minute. For help choosing between this and a twin system, read [Shower On Rail vs Twin Shower Systems](https://bathroomdeals.au/shower-on-rail-vs-twin-shower-systems-which-one-should-you-choose/).

**Key features**
- 304 stainless steel rail and brackets, brushed bronze finish
- ABS hand piece with a grey face, 3 spray functions
- Smooth PVC flexible hose
- Adjustable hand slider position on the rail
- Adjustable bottom bracket; bracket spacing 600mm, adjustable to 640mm
- Water inlet through the top bracket, G1/2" thread
- WELS 4 star, 7.5L/min
- Warranty: 10 years replacement parts or product, 7 years finish, 2 years labour (residential, licensed plumber required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | LUWTRS-BR |
| Finish | Brushed bronze |
| Rail and brackets | 304 stainless steel |
| Hand piece | ABS, grey face, 3 spray functions |
| Hose | Smooth PVC flexible hose. Length TBC |
| Hand slider | Adjustable position |
| Bottom bracket | Adjustable, for renovation applications |
| Bracket spacing | 600mm, adjustable to a maximum of 640mm |
| Rail diameter | 20mm |
| Bracket backplates | 60mm diameter |
| Projection from wall | 63mm |
| Water inlet | Through the top bracket, G1/2" (1/2 inch) thread |
| Flow rate / WELS | WELS 4 star, 7.5L/min |
| WaterMark | TBC (not stated in the product data) |
| Non-return valve | TBC |
| Weight | 2.5kg |
| Packaging | 700 x 100 x 150mm |
| Warranty | Replacement parts or product: 10 years. Finish: 7 years. Labour: 2 years. Residential use, manufacturing defects. Installation by a licensed plumber is required. This is in addition to your rights under Australian Consumer Law |
| Price | $229 |

**Pairs well with** (same brushed bronze finish)
- 1070 Lucito Tower Curved Spout Basin Mixer Brushed Bronze, $249
- 1064 Lucito Curved Spout Basin Mixer Brushed Bronze, $199
- 1292 Lucito Hand Towel Rail Brushed Bronze, $41
- 1208 Lucito Toilet Roll Holder Brushed Bronze, $37

**Other finishes** (the current page lists these; prices checked 11 Nov, all not on sale): Brushed Brass (1091) $229, Gun Metal (1092) $229, Chrome (1088) $199, Brushed Stainless (1094) $199, Black (1093) $199. The black version's page says 10 years replacement parts or product and a **5-year** finish warranty, so don't copy the bronze page's 7-year finish line onto it.

**Good to know**
- **Installation:** must be installed by a licensed plumber. It connects to the shower outlet through the top bracket, and you'll also need a shower mixer to control the water (not included). Licensed installation is a condition of the warranty.
- **Matching finishes:** brushed bronze can vary a little between batches and between product types. See [How to Match Tapware, Shower Systems & Bathroom Accessories Properly](https://bathroomdeals.au/how-to-match-tapware-shower-systems-amp-bathroom-accessories-properly/). (TEAM: confirm whether there's any batch variation note from the supplier before keeping this line.)
- **Care:** clean with warm soapy water and a soft cloth, then dry. Don't use abrasive pads, bleach, vinegar or acid-based cleaners. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Lucito Shower On Rail, Brushed Bronze, WELS 4 Star | Bathroom Deals
**Meta description:** Brushed bronze shower on rail: 304 stainless rail, 3-function hand piece, adjustable bottom bracket for renos. WELS 4 star 7.5L/min. 7-year finish warranty.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 1095 | "Lucito shower on rail in brushed bronze with a 3 function hand piece and flexible hose" | Keep as is (already descriptive) |
| 1089 | "Lucito shower on rail dimensions drawing showing 600mm bracket spacing, 20mm rail and 63mm projection" | Keep as is (already descriptive) |

**Data gaps / questions**
- **There's no brushed bronze wall or shower mixer in the range** (the brushed bronze listing checked on 11 Nov has basin mixers, sink mixers, a bath spout, accessories and showers, but no wall mixer). What should customers pair with this to control the water? If there isn't a bronze option, the copy should say so plainly.
- Hose length, WaterMark licence number, and whether a non-return valve is included.
- The trust badge says "Dispatched in 1–5 business days" while the footer says "1–2 business days". Remove both from the copy, or make them one checked figure.
- An installed photo would help (only a product shot and a drawing exist).

---

## 688 · Lucito Gooseneck Pull Out Sink Mixer Brushed Brass
**SKU** LUGNPOSM-BB · **Current price** $279 · **Stock:** in stock (4) · Not on sale · **Shipping class:** standard
*Repeated Shopping clicks in the baseline; features in social post 2 (16–22 Nov pack).*

**Current short description:**
> "Lucito Gooseneck Pull Out Sink Mixer Brushed Brass — takes more daily use than any other tap in the house. Manufactured from 304 Stainless Steel."

**New short description (53 words):**
A gooseneck kitchen mixer with a pull-out, two-function spray, made from lead-free 304 stainless steel with a PVD brushed brass finish. The swivel gooseneck spout and pull-out spray make it easier to fill pots and rinse out the sink. WELS 6 star, 4L/min. Backed by a 20-year cartridge, 10-year body and 7-year finish warranty.

**New long description:**

A kitchen mixer gets used more than any other tap in the house, so the parts that wear matter most. The Lucito Gooseneck has a 35mm Citec cartridge, and its lead-free body is 304 stainless steel. The brushed brass is a PVD finish. The gooseneck spout swivels, and the pull-out handpiece has two spray patterns, so you can rinse vegetables or clean out a roasting tray. Check spout height and reach on the dimension drawing before ordering. It's rated WELS 6 star at 4 litres a minute. Not sure whether you want a gooseneck or a pull-out? This one is both. Our guide [Gooseneck vs Pull-Out Kitchen Sink Mixers](https://bathroomdeals.au/gooseneck-vs-pull-out-kitchen-sink-mixers-which-one-should-you-choose/) explains the trade-offs.

**Key features**
- Lead-free 304 stainless steel body
- PVD brushed brass finish
- 35mm Citec cartridge
- Swivel gooseneck spout with a pull-out, two-function spray handpiece
- Polyamide braided flexible hoses
- WELS 6 star, 4L/min
- Warranty: 20-year cartridge replacement, 10-year body replacement, 7-year finish, 5-year labour (licensed plumber required)

**Specifications**
| Spec | Detail |
|---|---|
| SKU | LUGNPOSM-BB |
| Body material | 304 stainless steel, lead free |
| Finish | PVD brushed brass |
| Cartridge | 35mm Citec |
| Spout | Swivel gooseneck. Height and reach TBC (shown only on the dimension drawing) |
| Spray | Pull-out handpiece, 2 functions |
| Hoses | Polyamide braided flexible |
| Flow rate / WELS | WELS 6 star, 4L/min |
| WaterMark | TBC (no product-specific licence number in the data) |
| Mounting | Bench mounted. Tap-hole diameter and maximum bench thickness TBC |
| Weight | 3kg (shipping weight) |
| Warranty | 20-year cartridge replacement, 10-year body replacement, 7-year finish, 5-year labour. Installation by a licensed plumber is required. This is in addition to your rights under Australian Consumer Law |
| Price | $279 |

**Pairs well with**
- 976 Forio 864 Quartz Single Bowl Sink With Drainer White, $820 (collection only)
- 948 Forio 813 Double Bowl Quartz Sink White, $785 (collection only)
- 730 Forio Quartz Small Single Bowl Sink White, $649 (collection only)
- 667 Lucito Tower Curved Spout Basin Mixer Brushed Brass, $249, to carry the same brass into the bathroom

**Other finishes** (all not on sale, checked 11 Nov): Chrome (645) $239, Brushed Stainless (666) $239, Gun Metal (646) $279, Brushed Bronze (1061) $279. All non-black, so the same 7-year finish term applies; check each page for its own cartridge and labour terms before quoting them.

**Good to know**
- **Installation:** must be installed by a licensed plumber, and licensed installation is a condition of the warranty. Keep your plumber's compliance certificate. Check your benchtop's tap hole and thickness against the dimension drawing before ordering.
- **Sinks without a tap hole:** the three Forio quartz sinks listed above have no tap hole, so the mixer goes into the benchtop or the wall.
- **Care:** clean the PVD brushed brass with warm soapy water and a soft cloth, then dry. Don't use abrasive pads, bleach, vinegar or acid-based cleaners. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Lucito Gooseneck Pull Out Sink Mixer, Brushed Brass | Bathroom Deals
**Meta description:** Brushed brass gooseneck kitchen mixer with pull-out 2-function spray. Lead-free 304 stainless, 35mm cartridge, WELS 6 star. 20-year cartridge warranty.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 447 | "Lucito Gooseneck Pulll Out Spray Sink Mixer Brushed Brass" | Lucito gooseneck pull out sink mixer in brushed brass |
| 342 | "Lucito+Gooseneck+Pull+Out+Sink+Mixer+Brushed+Brass+in+a+luxury+kitchen" | Brushed brass Lucito gooseneck pull out mixer on a kitchen benchtop |
| 445 | "Lucito Gooseneck Pull Out Sink Mixer In Brushed Brass on a kitchen sink" | Lucito brushed brass gooseneck pull out mixer over a kitchen sink |
| 442 | "Lucito Gooseneck Pull Out Sink Mixer Dimensions" | Lucito gooseneck pull out sink mixer dimension drawing (shared by all finishes) |

**Data gaps / questions**
- Spout height, reach, tap-hole size and maximum bench thickness are only on the drawing image (442), so they aren't searchable or in the feed. Can we get the numbers?
- WaterMark licence number.
- Image 447 file name has a typo ("Pulll"). It doesn't affect the page; fix on re-upload.
- The automatic related products include Neston brushed brass 633 (out of stock). Set cross-sells.
- Warranty: brushed brass is non-black, so the 7-year finish term on the live page matches the current owner rule. (The 8 Nov draft's question about changing it to 10 years is closed: it stays at 7.)
- Remove the generic WELS/WaterMark row and the "1–2 business days" footer.

---

# STORAGE

## 678 · Tarnos Wall Hung Tall Boy Oak
**SKU** TARTBOAK · **Current price** $399 · **Stock:** in stock (2) · Not on sale (the was/now price was removed on 8 Nov) · **Shipping class:** pickup-only (collection only)

> Not the discontinued Tarnos 900 vanity. The copy doesn't mention or link the Tarnos 900.

**Current short description:**
> "Tarnos Wall Hung Tall Boy Oak — sets the tone for the whole bathroom. 350mm W x 450mm D x 1500mm H."

**New short description (49 words):**
A 350mm-wide wall-hung tall boy in Autumn Harvest oak-look laminate, with two soft-close doors and adjustable shelves inside. It adds 1500mm of upright storage for towels and refills where the vanity alone isn't enough, and keeps the floor clear. 5-year product warranty. Collection only from our Acacia Ridge warehouse.

**New long description:**

Most bathrooms run out of storage before they run out of wall. The Tarnos Tall Boy uses a 350mm-wide strip of wall for 1500mm of full-depth cupboard space, behind two soft-close doors, with adjustable shelves so you can fit towels, toilet rolls and spare bottles. It's wall-mounted, so the floor underneath stays clear and easy to mop. The cabinet is E1 HMR board with an Autumn Harvest oak laminate finish and a graphite interior.

**Key features**
- 350mm wide x 450mm deep x 1500mm high
- E1 HMR board
- Autumn Harvest Oak laminate finish
- 2 x soft-close doors with graphite interior
- Adjustable shelving, full depth
- Wall-mounted installation
- 5-year product warranty

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
| Door hinge side / reversible | TBC |
| Wall fixing / bracket system | TBC |
| Weight | 35kg (shipping weight) |
| Warranty | 5-year product warranty. What it covers (cabinet, hinges, finish) TBC. This is in addition to your rights under Australian Consumer Law |
| Delivery | Collection only from our Acacia Ridge, Brisbane warehouse |
| Price | $399 |

**Pairs well with**
- 679 Nimis 900 Wall Hung Vanity With Matte White Solid Surface Top, $965 (wall-hung timber-tone vanity, collection only; it's beechwood veneer, so check the oak and beech side by side)
- 1291 Lucito Hand Towel Rail Brushed Brass, $41
- 1297 Lucito Robe Hook Brushed Brass, $29
- 1292 Lucito Hand Towel Rail Brushed Bronze, $41

**Good to know**
- **Collection only:** this cabinet is collected from our Acacia Ridge, Brisbane warehouse. It isn't delivered. Choose local pickup at checkout and we'll contact you to arrange a time.
- **Installation:** at 1500mm high it must be fixed securely into the wall framing or blocking; plasterboard alone won't hold it once it's loaded. Plan the blocking before the wall is lined. No plumbing is involved.
- **Small-bathroom help:** see [Wall-Hung vs Freestanding Vanities: Which Suits a Small Bathroom?](https://bathroomdeals.au/wall-hung-vs-freestanding-vanities-which-suits-a-small-bathroom/)
- **Care:** wipe with a damp cloth and dry it. Keep it out of direct shower spray, and don't let water sit on the laminate edges. (TEAM: confirm against the manufacturer's care guide.)

**SEO title:** Tarnos Wall Hung Bathroom Tall Boy, Oak, 1500mm | Bathroom Deals
**Meta description:** 350mm-wide wall-hung bathroom tall boy in oak-look laminate, 1500mm high, with two soft-close doors and adjustable shelves. Collect from Acacia Ridge, Brisbane.

**Image alt text**
| Image ID | Current alt | New alt text |
|---|---|---|
| 564 | "Tarnos Wall Hung Tall Boy In Bathroom Scene" | Tarnos wall hung tall boy in oak in a bathroom (TEAM: confirm what else is in the scene; if it shows the discontinued Tarnos 900 vanity, don't name it) |
| 554 | "Tarnos+Tall+Boy+Oak" | Tarnos tall boy in Autumn Harvest oak, doors closed |
| 562 | "Tarnos Wall Hung Tall Boy Autumn Harvest Oak" | Tarnos wall hung tall boy in Autumn Harvest oak laminate, front view |
| 563 | "Tarnos Wall Hung Tall Boy Dimensions" | Tarnos wall hung tall boy dimension drawing, 350 x 450 x 1500mm |
| 555 | "Tarnos+Wall+Hung+Tall+Boy+Internal" | Tarnos tall boy with doors open, showing the graphite interior and adjustable shelves |

**Data gaps / questions**
- **The current page says "here, the soft-close drawers"**; it has two soft-close **doors**. The new copy fixes this.
- The current copy calls it "a vanity" and it sits in Bathroom Vanities. It's tall storage. Should it also be in a storage category?
- Number of shelves; are the doors reversible; what wall fixing is supplied?
- What does the 5-year warranty cover?
- Automatic related products show Akala 686 (excluded) and the out-of-stock Tarnos mirror 659. Set cross-sells.
- Trust badge "Up to 15-year manufacturer cover" on a 5-year product (Problems found, item 4).
- Remove the generic WELS/WaterMark row (it's a cabinet).

---

# Pairing stock check (11 Nov 2026, `/wc/v3/products?include=…`)

All suggested pairings were in stock and not on sale. None is on the excluded list.

| ID | Product | Price | Shipping class |
|---|---|---|---|
| 645 | Lucito Gooseneck Pull Out Sink Mixer Chrome | $239 | standard |
| 646 | Lucito Gooseneck Pull Out Sink Mixer Gun Metal | $279 | standard |
| 666 | Lucito Gooseneck Pull Out Sink Mixer Brushed Stainless | $239 | standard |
| 688 | Lucito Gooseneck Pull Out Sink Mixer Brushed Brass | $279 | standard |
| 1061 | Lucito Gooseneck Pull Out Sink Mixer Brushed Bronze | $279 | standard |
| 738 | Lucito Gooseneck Sink Mixer Black | $165 | standard |
| 743 | Murcia Upswept Sink Mixer Black | $79 | standard |
| 736 | Murcia Upswept Sink Mixer Chrome | $59 | standard |
| 730 | Forio Quartz Small Single Bowl Sink White | $649 | pickup-only |
| 948 | Forio 813 Double Bowl Quartz Sink White | $785 | pickup-only |
| 976 | Forio 864 Quartz Single Bowl Sink With Drainer White | $820 | pickup-only |
| 667 | Lucito Tower Curved Spout Basin Mixer Brushed Brass | $249 | standard |
| 1070 | Lucito Tower Curved Spout Basin Mixer Brushed Bronze | $249 | standard |
| 1064 | Lucito Curved Spout Basin Mixer Brushed Bronze | $199 | standard |
| 1292 | Lucito Hand Towel Rail Brushed Bronze | $41 | standard |
| 1208 | Lucito Toilet Roll Holder Brushed Bronze | $37 | standard |
| 1291 | Lucito Hand Towel Rail Brushed Brass | $41 | standard |
| 1297 | Lucito Robe Hook Brushed Brass | $29 | standard |
| 1094 | Lucito Shower On Rail Brushed Stainless | $199 | standard |
| 679 | Nimis 900 Wall Hung Vanity With Matte White Solid Surface Top | $965 | pickup-only |
| 651 | Neston Square Tile Insert Floor Waste Grate Stainless Steel | from $49; only DN80 (653) in stock, DN40 (654) and DN100 (652) out of stock | standard |
| 648 / 655 | Neston Square Max / Linear 800mm (each other) | $109 DN100 / $229 DN40 | standard |

Re-check stock before the copy goes live: many of these lines hold 1–2 units.

---

# Summary: data gaps and questions for the team

**Compliance and site-wide (decide first)**
1. **725 and 628 footers say "delivered Australia-wide … within 1–2 business days"** but both are `pickup-only` and the top of each page says collection only. Replace with the collection-only footer used on the 864 pages and the Tall Boy.
2. **Generic "WELS registered and WaterMark certified where the product category requires it" row** on all 9 pages. Remove it; keep only certifications the product data states.
3. **Dispatch-time claims** ("1–2 business days" footers, "1–4" on 646, "Dispatched in 1–5 business days" trust badge) disagree with each other and aren't backed by product data. Remove or replace with one checked figure.
4. **"Up to 15-year manufacturer cover" trust badge** shows on Neston (12 months), Lucito (7-year finish) and the Tall Boy (5 years). Show each product's own term, or drop the badge on those pages.
5. **Neston out-of-stock outlet sizes** are offered as choosable in the current copy (655: DN80, DN100; 648: DN80). Owner decision still open: restock date, backorder with a real lead time, or hide the sizes.
6. **Automatic related products** show excluded items (Muccia 665 and Vattaro 727 on 976; Akala 686 on 678) and many out-of-stock items. No cross-sells or upsells are set on any of the 9 products. Recommend setting cross-sells to the "Pairs well with" lists.
7. **Collection pages give a second phone number** for freight quotes ("Need it freighted? Call 0405 804 900"), while BRAND.md lists 07 4271 4620. Is 0405 804 900 current and meant to be public? Is freight on request actually offered for pickup-only items? (The new copy doesn't mention freight.)

**Product names and data**
8. **725 name has no colour** although SKU, finish and images are black and a White (730) exists. Rename to "… Black"? (Owner decision; 301 the slug if it changes.) Also set the Finish attribute and Black tag.
9. **628 dimensions garbled** ("73mm x 460mm x 228mm Depth0"). Supply overall size, bowl size and cut-out. (SKU and image file name suggest 730mm; not used until confirmed.)
10. **628 short description says "Butler Sink"**; the name says "Large Sink". Which is right?
11. **628 ships with a chrome basket waste on a black sink.** Confirm, or is a black waste available?
12. **Forio warranty wording differs:** 725/628 say 15 years + 1-year labour and "licensed plumber"; 974/976 say 15 years, no labour term, and "licensed tradesperson"; 628 features say "Product Warranty" and its footer says "manufacturer's warranty". Confirm the labour term on the 864s and align the wording.
13. **Tall Boy template line says "soft-close drawers"**; it has doors. (Fixed in the new copy.) Should it also sit in a storage category, not only Bathroom Vanities?
14. **655 width:** features say 105mm, Additional information says 106mm.
15. **648 "higher flow rate" claim** has no figure. Supply flow rates, or keep the claim out (the new copy leaves it out).
16. **No brushed bronze wall or shower mixer** exists to go with the 1096 rail. What should customers pair it with?

**Missing specs, in priority order**
17. **Forio sinks:** bowl internal sizes, overflow, cut-out sizes and minimum cabinet widths (all four); length vs width orientation for 725; tap holes for 628; whether undermount clips/templates are supplied (725, 628).
18. **Neston:** outlet position and minimum cut length (655); flow rates per outlet; puddle flange details (648); WaterMark licence numbers (both).
19. **Lucito 1096:** hose length, WaterMark licence number, non-return valve.
20. **Lucito 688:** spout height and reach, tap-hole size, maximum bench thickness (currently only on drawing 442); WaterMark licence number.
21. **Tarnos Tall Boy:** number of shelves, door hinge side / reversible, wall fixing supplied, what the 5-year warranty covers.

**Images**
22. 628 has one image with empty alt text; 974, 976 and 655 have one image each. Installed shots and dimension drawings would help all four.
23. Image 564 (Tall Boy scene): confirm what's in the scene before finalising alt text. Don't name the Tarnos 900 if it appears.
24. Image 447 file name typo ("Pulll").

**Care guides**
25. The care notes are general good practice for each material. Please confirm them against the manufacturers' care instructions before publishing, and confirm whether the supplier has a batch-variation note for brushed bronze (1096).
