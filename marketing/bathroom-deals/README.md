# Bathroom Deals — Marketing Agent Team

A set of Claude Code subagents for the Bathroom Deals (bathroomdeals.au) marketing team. The definitions are in `.claude/agents/bd-*.md`. They all share one brief: [`BRAND.md`](./BRAND.md).

| Agent | Role |
|---|---|
| `bd-marketing-lead` | Plans campaigns and content calendars and coordinates the others |
| `bd-seo-content-writer` | Blog posts, buyer's guides, local SEO, meta data (saves WordPress drafts only) |
| `bd-product-copywriter` | WooCommerce product and category copy, spec tables, alt text |
| `bd-social-media-manager` | IG / FB / Pinterest / TikTok posts, reels scripts, Canva creative |
| `bd-email-marketer` | Newsletters, promos, Klaviyo flows, Gmail drafts |
| `bd-paid-ads-specialist` | Google and Meta ad copy, structure, audits, test plans |
| `bd-analytics-reporter` | GA4 / Search Console / ads / email reports (read only) |
| `bd-compliance-reviewer` | ACL, Spam Act and brand-voice check before approval (read only) |

## How to use
In Claude Code, from this repository, just ask. Claude picks the right agent, or you can name one:

- "Use bd-marketing-lead to plan a Black Friday campaign for matte black tapware."
- "Have bd-seo-content-writer write a guide on choosing a vanity size for a Brisbane ensuite."
- "bd-analytics-reporter: October performance report."
- "bd-compliance-reviewer: check marketing/bathroom-deals/drafts/2026-11-10-bf-email.md"

Type `/agents` to see or edit them.

## Guardrails
Agents **draft**. People **approve**. No agent publishes to the site, sends email, posts to social media, or changes ads, budgets or prices without a person's explicit go-ahead. All customer-facing copy goes through `bd-compliance-reviewer` first.

## Folders
- `drafts/`: campaign briefs, posts, emails, ad copy waiting for approval
- `reports/`: analytics reports and audits
