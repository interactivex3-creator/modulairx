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
