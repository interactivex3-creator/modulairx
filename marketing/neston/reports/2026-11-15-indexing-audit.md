# neston.com.au — indexing audit and fix plan (15 Nov 2026)

Prepared for approval. **Nothing has been changed on the site.**

## What Search Console reported (email of 9 Nov 2026)
1. **Duplicate without user-selected canonical**
2. **Alternate page with proper canonical tag**
3. **Blocked due to other 4xx issue**

Search Console isn't connected to any tool in this workspace, so the exact URLs aren't visible. The findings below come from reading the live HTML of the site.

## Finding 1 — category content lives at two URLs (cause of #1)
Each range has a hand-built landing page **and** a WooCommerce category archive, with near-identical content: the same product grid, the same `<title>`, and each one canonical to itself.

| Landing page (Elementor/HTML) | WooCommerce category | Title on both |
|---|---|---|
| /linear-drains/ (page 340) | /product-category/linear-drains/ (cat 20, 16 products) | "Linear Drains - Neston Architectural Drains" |
| /square-tile-insert-grates/ (page 359) | /product-category/square-tile-insert-grates/ (cat 21, 10 products) | same pattern (to confirm) |
| /outdoor-drains/ (page 350) | /product-category/outdoor-drains/ (cat 22, 10 products) | same pattern (to confirm) |

Google sees two pages with the same content, neither pointing to the other, so it picks one itself and reports the other as "duplicate without user-selected canonical". Internal links are split as well: the footer links to `/product-category/...`, the home page links to `/shop/#...`, and product cards link to `/product-category/...`.

**The landing pages are the better versions.** They carry the guide copy, sizing and FAQ, a breadcrumb (Home / Shop / Linear Drains) and a better meta description. (The category description claims "compliance with Australian standards", which is vague; BRAND.md rules say we should name the requirement.)

### Fix (recommended)
1. **301-redirect each category archive to its landing page.** First page only; paged URLs `/page/2/` redirect to the same landing page. Done with a small PHP snippet in WPCode (already installed), so it's easy to switch off:
   ```php
   add_action( 'template_redirect', function () {
       if ( ! is_product_category() ) { return; }
       $map = array(
           'linear-drains'             => '/linear-drains/',
           'square-tile-insert-grates' => '/square-tile-insert-grates/',
           'outdoor-drains'            => '/outdoor-drains/',
       );
       $term = get_queried_object();
       if ( $term && isset( $map[ $term->slug ] ) ) {
           wp_safe_redirect( home_url( $map[ $term->slug ] ), 301 );
           exit;
       }
   } );
   ```
2. **Point internal links at the landing pages:** the footer SHOP column (on the custom chrome and on the Elementor pages) and the home-page category cards (`/shop/#linear-drains` → `/linear-drains/`).
3. **Leave product categories out of the AIOSEO sitemap** (AIOSEO › Sitemaps › Taxonomies: untick Product categories) so Google stops being sent the redirected URLs.
4. **In Search Console:** resubmit the sitemap, then use URL Inspection → "Request indexing" on the three landing pages.

*Alternative if you'd rather not redirect:* set each category's canonical to its landing page. That needs AIOSEO Pro or a snippet using the `aioseo_canonical_url` filter. It's weaker, because Google treats a canonical as a hint, not an instruction.

## Finding 2 — "Alternate page with proper canonical tag" (#2)
This is usually harmless: URLs with parameters (`?add-to-cart=`, variation `?attribute_...=`, `?orderby=`) correctly pointing to the clean URL. **No action needed** unless the report shows a page that *should* be indexed. Check the example URLs in the report.

## Finding 3 — "Blocked due to other 4xx issue" (#3)
I can't see which URLs from here. Likely candidates: `/my-account/` sub-pages, `/wp-json/` or REST URLs, cart and checkout actions, or deleted products or images. **Needed from you:** open Search Console → Indexing → Pages → "Blocked due to other 4xx issue" and paste the example URLs. Or connect Search Console to the Easy MCP plugin (wp-admin → Easy MCP AI › Tools › External data → Google Search Console) so the team can read it directly.

## Other things found while checking
- **Two headers render on every page.** The custom Neston header (`nx-chrome`) **and** Blocksy's default header, whose menu is an automatic list of *every* page, including Cart, Checkout and My account. That's poor UX and it spreads internal links to pages that shouldn't be indexed. Fix: turn off the Blocksy header in the Customizer, or assign a real menu.
- **`og:site_name` reads "Neston Architectural Drains -"** because the site tagline is empty. Fix: set a tagline (Settings › General), e.g. "Premium 316 stainless steel drainage".
- **`og:locale` is `en_US`.** Fix: set Site Language to English (Australia).
- The empty "Uncategorized" product category: leave it, it's harmless.
- AIOSEO (5.0.4 → 5.0.5.1), WooCommerce and Elementor have updates pending. Take a Duplicator backup first and use the `safe-updates` skill (separate task).

## Approval checklist
- [ ] Add the WPCode redirect snippet (Fix 1)
- [ ] Update footer and home-page links (Fix 2)
- [ ] Exclude product categories from the AIOSEO sitemap (Fix 3)
- [ ] Set the site tagline and the en_AU language
- [ ] Hide the duplicate Blocksy header
- [ ] You: resubmit the sitemap and request indexing in Search Console (Fix 4)
- [ ] You: send the 4xx example URLs, or connect Search Console

## Progress log
**21 Nov 2026: owner approved fixes 1–3.**
- Done: site tagline set to "Premium 316 stainless steel drainage" (was empty).
- Done: AIOSEO XML sitemap now includes only posts, pages, products and post categories. Product categories, tags and attachment pages are out. /outdoor-drains/ and /technical-documents/ are confirmed in page-sitemap.xml.
- Waiting on the owner: two WPCode snippets, each needing WPVibe approval and then switching on in WPCode:
  - "Neston: redirect duplicate product-category pages to range landing pages" (fix 1);
  - "Neston: one-off - point range links at the landing pages (runs once)" (fix 2). It rewrites /product-category/<range>/ and /shop/#<range> links on Home, About, Contact, Terms, Reseller and Finishes (post_content and _elementor_data), then records the changed IDs in the option `neston_range_links_fixed`. Switch it off once that option exists.
- Owner to do: Settings › General › Site Language → English (Australia). WPVibe can't install language packs.
- No Duplicator backup since early Nov. Every change above can be undone (revisions, snippets off, the sitemap toggle).
**21 Nov 2026 (later): fixes 1–4 live and checked.**
- Snippet 381 (redirects) active: all 3 /product-category/<range>/ URLs return 301 to the landing pages.
- Snippet 380 (one-off link fix) ran, then was switched off. No old links remain on Home, About, Contact, Reseller, Finishes or Terms.
- Snippet 388 (term_link filter) active: product cards, the shop page and product pages link straight to /linear-drains/ etc. 0 /product-category/ links on the range, shop and product pages checked.
- Blocksy default header hidden with Additional CSS (revision 387). The Neston header shows on every page that had it.
- Site language is now en-AU (owner). Tagline and sitemap were done earlier.
- Search Console: /zero-threshold-drain-building-entries/ is submitted and indexed (crawled 16 Nov). /outdoor-linear-drains/ is still "Google chose different canonical" from a 1 Oct crawl. The no-slash URL now 301s, so the owner should click Request indexing in Search Console (the API can't).
- 21 Nov 2026: owner clicked Request indexing for /outdoor-linear-drains/ in Search Console. Check its status in the 30 Nov report.
- 21 Nov 2026: published "Shower Drain Outlet Sizes in Australia" (post 378, featured image 132). Applied the approved product copy plus AIOSEO title and description to products 21, 34, 23, 26, 235 and 236. The 52mm kits (235/236) are now variable with Outlet Size DN100/DN80 (SKUs NS105WW52SS-1000DN100/-1000DN80/-2000DN100/-2000DN80, same prices). The NCC "Suitable for…" claim is gone. The 3D viewers were stripped by the REST save and have been restored and checked live.
