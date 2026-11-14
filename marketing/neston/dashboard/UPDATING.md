# Updating the Neston dashboard (every scheduled run)

Live site: https://neston-marketing-team.netlify.app (Netlify site id `b9453abc-4b3a-4670-ab5a-db4a9a47a3fd`).
The page reads everything from `data.json`. Each run updates `data.json` and redeploys. Never change `index.html`, `favicon.svg` or `netlify.toml` in a run.

## 1. Start from the LIVE data, not the repo copy
Scheduled runs can't push to git, so the repo copy goes stale. The sandbox network may block `*.netlify.app`, so fetch the live data through the WebFetch tool (or the `web-fetch` agent), not curl:
```bash
mkdir -p /tmp/ndash && cp marketing/neston/dashboard/{index.html,favicon.svg,netlify.toml} /tmp/ndash/
```
Then fetch https://neston-marketing-team.netlify.app/data.json and save it, unchanged, as `/tmp/ndash/data.json`. If that fails, copy `marketing/neston/dashboard/data.json` instead, and say "started from the repo copy" in the run summary.

## 2. Edit /tmp/ndash/data.json (Python json, same structure)
- `updated`: today's date (YYYY-MM-DD, Brisbane).
- For every agent that did work in this run: set `last_update` to today; add new items at the TOP of `done` (`{"date", "text"}`), one short plain-English line each; keep at most 6; set `next_run`; set `status` to "active".
- `schedule`: for this run's entry, set `last_run` to today, `last_status` to "ok" (or "failed" if a main step failed), `next` to the next run date, and `connectors_ok` / `connector_note` (e.g. "All 4 connectors added" or "Two Minute Reports missing"). Remove `setup_note` once `next` is set.
- `latest`: add this run's outputs at the TOP (`date`, `type`, `title`, `by` = agent id, `url`). Keep the newest 8.
- `calendar` (**Wednesday run only**): replace it with NEXT week (`week_of` = next Monday). Items: the Monday run (kind "run"), each Google Business Profile post (kind "google"), each LinkedIn post (kind "linkedin"), each Instagram/Facebook post (kind "facebook"), any website item (kind "site"), and the Wednesday run (kind "run"). `link` points to the week's Drive folder.
- `waiting`: the owner's to-do list. Add anything only the owner can do (post the Google updates, review a WordPress draft, a BLOCK or ON HOLD item, a missing connector, a failed step), with `priority`, `due`, `how` and `link`. Remove items that are clearly done (for example, the indexing fixes once Search Console shows them fixed). Leave anything you can't verify.
- Never put trade or reseller prices, revenue, customer or reseller details, phone numbers or emails in `data.json`. The site is public.

Check the JSON before deploying: `python3 -c "import json;json.load(open('/tmp/ndash/data.json'))"`.

## 3. Deploy
1. Call the Netlify connector `netlify-deploy-services-updater` with `{"operation":"deploy-site","params":{"siteId":"b9453abc-4b3a-4670-ab5a-db4a9a47a3fd"}}`. It returns an `npx -y @netlify/mcp@latest --site-id … --proxy-path "…"` command.
2. Run that command from `/tmp/ndash`, with `NODE_USE_ENV_PROXY=1 NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt` in front of it.
3. Wait for "Deploy is ready!". That line is the check. If it doesn't appear, say "DASHBOARD NOT UPDATED" and why.

If the Netlify connector isn't available, upload the edited `data.json` to Google Drive folder `1b-uyw7ih8p2C6xnXhUxhNG_APiBsSat2` as "dashboard-data-YYYY-MM-DD.json" (contentMimeType application/json, disableConversionToGoogleType true), and say "DASHBOARD NOT UPDATED: Netlify connector missing" in the run summary.
