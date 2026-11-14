# Neston — Marketing Agent Team

A set of Claude Code subagents for marketing **Neston Architectural Drains** (neston.com.au). The definitions are in `.claude/agents/neston-*.md`. They all share one brief: [`BRAND.md`](./BRAND.md).

**Channel phase:** Neston sells through resellers today and will start selling direct in 2027. Every agent works reseller-first until `BRAND.md` says Phase 2 has started.

| Agent | Role |
|---|---|
| `neston-marketing-lead` | Plans campaigns and the calendar, coordinates the team, runs the 2027 launch plan |
| `neston-seo-content-writer` | Journal and technical guides, on-page and technical SEO (WordPress drafts only) |
| `neston-product-copywriter` | WooCommerce product and category copy, spec tables, alt text |
| `neston-compliance-reviewer` | ACL, NCC/AS/WaterMark claims, pricing, Spam Act, channel rules (read only) |
| `neston-analytics-reporter` | Search Console, GA4, Business Profile, Klaviyo, diib, Kevin reports (read only) |
| `neston-trade-specifier-outreach` | Architect, builder, hydraulic and trade outreach; CPD pitches |
| `neston-local-seo-gbp-manager` | Google Business Profile, reviews, directories, consistent business details |
| `neston-spec-sheet-designer` | Spec sheets, install guides, brochures, price-list PDFs (Canva or Moda) |
| `neston-social-media-manager` | LinkedIn, Instagram, Pinterest, Facebook content |
| `neston-paid-ads-specialist` | Google, Meta and LinkedIn ads: lead-gen now, Shopping from 2027 |
| `neston-email-marketer` | Trade and reseller newsletters, Klaviyo flows, sign-up form |
| `neston-chat-optimiser` | Kevin chat reviews and knowledge-base improvement proposals |
| `neston-stockist-channel-agent` | Reseller recruitment, reseller content kits, listing audits, 2027 channel plan |

## How to use
In Claude Code, from this repository, just ask. Claude picks the right agent, or you can name one:

- "neston-marketing-lead: plan a reseller recruitment push for Q1 2027."
- "Have neston-seo-content-writer fix the duplicate-page indexing issue and write a guide on DN50 vs DN100 outlets."
- "neston-local-seo-gbp-manager: audit the Google Business Profile."
- "neston-chat-optimiser: review last week's Kevin summary."
- "neston-compliance-reviewer: check marketing/neston/drafts/2026-11-20-trade-newsletter.md"

## Guardrails
Agents **draft**. People **approve**. No agent publishes to the site, sends email, posts to social or Google Business Profile, contacts resellers or specifiers, edits Kevin, or changes ads, budgets, prices or products without a person's explicit go-ahead. All external material goes through `neston-compliance-reviewer` first.

## To fill in later (BRAND.md TBCs)
Warranty terms, WaterMark licence details, the 2027 direct-launch date, the canonical business name (Drains vs Grates), CPD accreditation, and trade events.

## Folders
- `drafts/`: briefs, posts, emails, outreach, ad copy and collateral notes waiting for approval
- `reports/`: analytics reports, audits and Kevin reviews
