> **ON HOLD: email marketing paused by the owner on 11 Nov 2026. Do not send.**

# Email draft: Package quote (Lucito brushed brass example)

**Author:** bd-email-marketer · **Date:** 11 Nov 2026 · **Brief:** `drafts/2026-11-10-weekly-plan.md`, section D
**Status:** DRAFT ONLY. Not sent, not scheduled, not loaded into Klaviyo or Gmail. Must go through `bd-compliance-reviewer`, then a named person approves the exact content and audience before anything is sent.
> **Compliance review (11 Nov): FIX, all edits applied.** **SEND ON HOLD (hard gate):** don't send until (1) the `{{ UNSUBSCRIBE_LINK }}` and `{{ CONSENT_REASON }}` placeholders are replaced with the sending tool's real unsubscribe tag and consent basis, (2) a proof send shows the unsubscribe link works, and (3) consent is confirmed for every contact on the list. Klaviyo isn't connected, so we can't see list size or consent status. Optional: add the ABN to the sender footer. The reviewer read "ABN 44 526 646 497" from the site footer; confirm it before use. The sign-off "Real products, real value, real savings." is allowed, as long as it stays apart from any price or the $705 total.

**Goal:** package-quote enquiries via https://bathroomdeals.au/contact/ ("Package Quote" option on the form).

**Facts used (checked 11 Nov 2026):**
- Contact page: phone 07 4271 4620, Mon–Fri 8:30am–5:00pm AEST, info@bathroomdeals.au, "We reply within one business day", warehouse Acacia Ridge QLD 4110, collection by appointment. The form has a "Package Quote" option but no file-upload field (schedules go to info@bathroomdeals.au).
- Example set: five Lucito Brushed Brass products, all listed on the site at regular prices (no sale prices). Sum of current prices = $705 ($199 + $159 + $229 + $81 + $37).
- Warranty: all five product pages state a 7-year finish warranty (matches BRAND.md: every non-black Lucito finish = 7-year finish). Cartridge terms are **not** quoted because they are inconsistent across pages (the Wall Mixer page says 20-year cartridge in its features and 10-year in its footer). See open questions.
- Deliberately left out: stock levels or scarcity (only 2–5 units per line), dispatch times, any bundle price or saving, was/now pricing, "cheapest"/"best price".

---

## 1. Subject lines and preview text

| # | Angle | Subject line (≤50) | Chars | Preview text (≤90) | Chars |
|---|---|---|---|---|---|
| A | Benefit | Send your schedule, get a matched set and a price | 49 | One person matches every piece to one finish and sends back a real price. | 73 |
| B | Curiosity | What one finish looks like across a bathroom | 44 | A Lucito brushed brass set, piece by piece, and how to get one matched to your room. | 84 |
| C | Specific number | 5 pieces, 1 finish: $705 at today's prices | 42 | Five Lucito brushed brass pieces at current shop prices, added up. Yours may differ. | 84 |

**Recommendation:** A as the control (it is the brief's own subject idea, trimmed to fit 50 characters). If the list is large enough to split-test (see open questions), test A vs C. C must only go out if all five prices are re-checked on the send date and still total $705; if any price changes, update the number or drop C.

---

## 2. Body copy (HTML-ready markdown)

> Links carry suggested UTM tags so the owner can see email-driven quote visits in GA4. Remove them if the sending tool adds its own tracking.

**[HEADER IMAGE: see design brief, section 4]**

# Send us your bathroom. We'll send back a matched set and a price.

Hi {{ first_name|default:"there" }},

Planning a bathroom, ensuite or laundry? Buying tapware piece by piece means checking that every finish matches, that the parts suit your rough-in, and that the sizes work for your room.

Our package quote does that for you:

- **Send us your schedule or describe your room.** A plumber's or builder's schedule, a list, or a few photos and measurements all work. Describe it in the form, or email the file to info@bathroomdeals.au.
- **A person matches the set.** Mixers, shower, towel rail and accessories in one finish, chosen from our range.
- **You get a real price back.** Current prices for each item, itemised, so you can see what you're paying for.
- **One point of contact.** The person who helps you choose is the same person who helps if something goes wrong later.

We reply within one business day (Mon–Fri, 8:30am–5:00pm AEST).

### Here's what a matched set looks like

Lucito in Brushed Brass, five pieces for a typical bathroom:

| Product | Price |
|---|---|
| [Lucito Curved Spout Basin Mixer Brushed Brass](https://bathroomdeals.au/product/lucito-curved-spout-basin-mixer-brushed-brass/?utm_source=email&utm_medium=email&utm_campaign=package-quote-nov26) | $199 |
| [Lucito Wall Mixer Brushed Brass](https://bathroomdeals.au/product/lucito-wall-mixer-brushed-brass/?utm_source=email&utm_medium=email&utm_campaign=package-quote-nov26) | $159 |
| [Lucito Shower On Rail Brushed Brass](https://bathroomdeals.au/product/lucito-shower-on-rail-brushed-brass/?utm_source=email&utm_medium=email&utm_campaign=package-quote-nov26) | $229 |
| [Lucito 750 Double Towel Rail Brushed Brass](https://bathroomdeals.au/product/lucito-750-double-towel-rail-brushed-brass/?utm_source=email&utm_medium=email&utm_campaign=package-quote-nov26) | $81 |
| [Lucito Toilet Roll Holder Brushed Brass](https://bathroomdeals.au/product/lucito-toilet-roll-holder-brushed-brass/?utm_source=email&utm_medium=email&utm_campaign=package-quote-nov26) | $37 |
| **Sum of current prices** | **$705** |

Prices are each product's current price on our site at the time of writing. This is an example, not a bundle price; your quote is built around your room.

**Warranty:** 7-year finish warranty across the set; other terms are listed on each product page. The mixer and shower warranties apply when they are installed by a licensed plumber, and all warranties are in addition to your rights under the Australian Consumer Law.

### Good to know

- **Tapware and accessories** are delivered Australia-wide, tracked on every order.
- **Vanities and quartz sinks (Forio)** are collection only from our Acacia Ridge warehouse (by appointment). If your quote includes them, we'll arrange a pickup time with you.
- **Installation:** in Queensland and most other states, tapware and showers must be installed by a licensed plumber.

[**Request a package quote**](https://bathroomdeals.au/contact/?utm_source=email&utm_medium=email&utm_campaign=package-quote-nov26)
*(button; choose "Package Quote" on the form)*

Prefer to talk it through? Call 07 4271 4620 and you'll get someone who knows the range.

The Bathroom Deals team
Real products, real value, real savings.

---

**[FOOTER]**
You're receiving this email because {{ CONSENT_REASON: e.g. "you subscribed to the Bathroom Deals newsletter at bathroomdeals.au" (team to confirm, see open questions) }}.
Bathroom Deals · Acacia Ridge QLD 4110 · 07 4271 4620 · info@bathroomdeals.au · https://bathroomdeals.au
[Unsubscribe]({{ UNSUBSCRIBE_LINK }})

---

## 3. Plain-text version

```
SEND US YOUR BATHROOM. WE'LL SEND BACK A MATCHED SET AND A PRICE.

Hi {{ first_name|default:"there" }},

Planning a bathroom, ensuite or laundry? Buying tapware piece by piece
means checking that every finish matches, that the parts suit your
rough-in, and that the sizes work for your room.

Our package quote does that for you:

- Send us your schedule or describe your room. A plumber's or builder's
  schedule, a list, or a few photos and measurements all work. Describe
  it in the form, or email the file to info@bathroomdeals.au.
- A person matches the set. Mixers, shower, towel rail and accessories
  in one finish, chosen from our range.
- You get a real price back. Current prices for each item, itemised.
- One point of contact. The person who helps you choose is the same
  person who helps if something goes wrong later.

We reply within one business day (Mon-Fri, 8:30am-5:00pm AEST).

HERE'S WHAT A MATCHED SET LOOKS LIKE
Lucito in Brushed Brass, five pieces for a typical bathroom:

Lucito Curved Spout Basin Mixer Brushed Brass .... $199
https://bathroomdeals.au/product/lucito-curved-spout-basin-mixer-brushed-brass/

Lucito Wall Mixer Brushed Brass .................. $159
https://bathroomdeals.au/product/lucito-wall-mixer-brushed-brass/

Lucito Shower On Rail Brushed Brass .............. $229
https://bathroomdeals.au/product/lucito-shower-on-rail-brushed-brass/

Lucito 750 Double Towel Rail Brushed Brass ....... $81
https://bathroomdeals.au/product/lucito-750-double-towel-rail-brushed-brass/

Lucito Toilet Roll Holder Brushed Brass .......... $37
https://bathroomdeals.au/product/lucito-toilet-roll-holder-brushed-brass/

Sum of current prices ............................ $705

Prices are each product's current price on our site at the time of
writing. This is an example, not a bundle price; your quote is built
around your room.

WARRANTY: 7-year finish warranty across the set; other terms are listed
on each product page. The mixer and shower warranties apply when they
are installed by a licensed plumber, and all warranties are in addition
to your rights under the Australian Consumer Law.

GOOD TO KNOW
- Tapware and accessories are delivered Australia-wide, tracked on
  every order.
- Vanities and quartz sinks (Forio) are collection only from our
  Acacia Ridge warehouse (by appointment).
- In Queensland and most other states, tapware and showers must be
  installed by a licensed plumber.

REQUEST A PACKAGE QUOTE (choose "Package Quote" on the form):
https://bathroomdeals.au/contact/

Prefer to talk it through? Call 07 4271 4620.

The Bathroom Deals team
Real products, real value, real savings.

--
You're receiving this email because {{ CONSENT_REASON }}.
Bathroom Deals, Acacia Ridge QLD 4110 | 07 4271 4620 | info@bathroomdeals.au
Unsubscribe: {{ UNSUBSCRIBE_LINK }}
```

---

## 4. Design notes / header brief (Canva)

- **Format:** single column, 600px wide, mobile-first. Header image 1200×600px (2:1), exported under 200 KB. Live text everywhere except the header, so the email still reads with images off.
- **Header image:** our own product photos of the five Lucito Brushed Brass pieces, laid out as a flat-lay or a clean row on a light neutral (warm white or pale stone) background. No stock photos of a finished luxury bathroom, since that implies a fitted room we didn't supply. If Unsplash is needed, use it only for a subtle texture background, never for product shots.
- **Header text (optional, keep small):** "One finish. One person. One price." No price, no "deal", no "save", no badges or countdowns.
- **Alt text:** "Lucito Brushed Brass basin mixer, wall mixer, shower on rail, double towel rail and toilet roll holder."
- **Product block:** simple table or 5-row list (name, price, link). Thumbnails optional (80×80px) from the product pages. No strikethrough prices, no sale tags.
- **CTA button:** one button only, "Request a package quote", high contrast, at least 44px tall, full width on mobile. Product names are plain text links, not buttons, so the quote button stays the single main CTA.
- **Colour/type:** site brand colours; body 16px minimum; plenty of white space. Brushed brass tones can carry the accent colour for this send.
- **Emoji:** none.

---

## 5. Audience and send time

- **Audience:** DIY renovators/homeowners and trades on the existing **consented** list only (Klaviyo, or whatever list the team confirms). Exclude anyone who has unsubscribed or bounced, and anyone who has already sent a package-quote enquiry in the last 30 days (if that data is available; otherwise note it for the person sending).
- **If the list can be segmented:** a version for trades could swap the first line to "Send us the schedule for your next job", but the same body works for both. Don't build a second version until list size is known.
- **Send time:** Tuesday 17 Nov or Wednesday 18 Nov 2026, **7:00am AEST** (Brisbane). Reasons: renovators often read email before work, and a weekday send means replies and form entries land while the phone is staffed (Mon–Fri 8:30am–5:00pm AEST), so the "reply within one business day" promise is easy to keep. Note that NSW/VIC/TAS/ACT are on daylight saving (AEDT, 8:00am there), which is still fine.
- **Avoid:** Friday afternoon and weekend sends (enquiries would sit until Monday).
- **Before sending:** re-check all five prices and that each page still shows a 7-year finish warranty. Products must still be listed as available; if any line has sold out, swap it for another Brushed Brass Lucito item at its current price and recalculate the sum, or drop the sum.
- **Measure:** quote-form entries tagged "Package Quote" in the 7 days after send (owner to read WPForms manually), plus clicks to `/contact/` with `utm_campaign=package-quote-nov26` in GA4, and calls to 07 4271 4620 if the owner can log them.

---

## 6. Compliance footer checklist (Spam Act 2003, ACL)

- [ ] **Sender identified:** "From" name Bathroom Deals; footer shows Bathroom Deals, Acacia Ridge QLD 4110, 07 4271 4620, info@bathroomdeals.au.
- [ ] **Working unsubscribe link:** replace `{{ UNSUBSCRIBE_LINK }}` with the sending tool's real unsubscribe tag (in Klaviyo, `{% unsubscribe %}`); test it in a proof send. It must work for at least 30 days after sending and be actioned within 5 business days.
- [ ] **Consent basis:** replace `{{ CONSENT_REASON }}` with the real reason (e.g. newsletter sign-up on bathroomdeals.au). Send only to people with express consent, or a documented inferred-consent basis the team is comfortable with (e.g. existing customers who were told they'd hear from us). If consent can't be confirmed for a contact, don't send to them.
- [ ] **No was/now, "save $X", "% off", bundle discount or implied saving.** The $705 is labelled "sum of current prices" and "not a bundle price".
- [ ] **No "cheapest", "lowest price", "best price".** (The sign-off line is BRAND.md's approved line.)
- [ ] **No stock or scarcity claims, no dispatch-time promises, no countdowns.**
- [ ] **Warranty:** 7-year finish only, conditional on licensed plumber install, stated as in addition to ACL rights. No cartridge term quoted.
- [ ] **Collection only:** vanities and Forio quartz sinks stated as collection from Acacia Ridge, never delivered.
- [ ] **Licensed plumber** note included.
- [ ] **No products from the do-not-feature list** (Brighton, Catral, Akala, Vattaro, Balun, Muccia, KODI, Tarnos 900). None used.
- [ ] Reviewed by `bd-compliance-reviewer`, then approved by a named person (content and audience).

---

## 7. Open questions for the team

1. **List size and consent status are unknown.** Klaviyo is not connected (via Windsor.ai or otherwise), so we can't see how many contacts there are, where they came from, or whether consent was recorded. Before approval, someone needs to confirm: which list or tool holds the contacts, how many, and the consent basis for each source (newsletter form, past customers, quote enquiries, trade contacts). If the list is under a few hundred, skip the A/B subject test and send subject A.
2. **Newsletter form wording on /contact/.** The site's newsletter sign-up says "Deals before they sell out". That is mild urgency/scarcity language and sits awkwardly with our "no fake urgency" rule and with the low stock levels on many lines. Suggest the owner consider a plainer line, e.g. "New stock and honest price updates, about once a fortnight." Not changed by us. This also matters for consent: we should know what people were promised when they signed up, so the content we send matches it.
3. **Who will physically send this, and from what tool?** Klaviyo (needs the account connected and a sender profile/domain set up), or a person through Gmail (fine for a small list, but Gmail isn't built for bulk sends and has no built-in unsubscribe handling, so the team would have to manage opt-outs by hand). The unsubscribe placeholder depends on this choice.
4. **Who answers the quote enquiries?** The email promises one point of contact and a reply within one business day. Please confirm who handles "Package Quote" entries in the week after sending, and that cover is in place if they're away.
5. **Lucito cartridge warranty inconsistency.** The Lucito Wall Mixer Brushed Brass page says 20-year cartridge in its features but 10-year in its footer. We left cartridge terms out of the email; the owner should confirm the correct term and get the page fixed (separate, approved site edit).
6. **Reply-to address.** Should replies go to info@bathroomdeals.au? If yes, set it as the reply-to so people can reply to the email with their schedule attached, which is also a valid quote path.
7. **Suggested follow-up:** the quote follow-up flow in the agent brief (written for a person to send from Gmail) doesn't exist yet. Worth drafting before this goes out so enquiries get a consistent reply.
