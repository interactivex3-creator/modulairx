# Updating the team dashboard

**Deploy ONCE A WEEK only (owner rule, 16 Nov 2026: every Netlify deploy uses paid credits).**
- **Monday run:** do steps 1–2, then SAVE the edited data.json to Google Drive (step 3a). Do NOT deploy.
- **Wednesday run:** start from Monday's saved file, do steps 1–2, then DEPLOY (step 3b). This is the only deploy of the week.
- Manual changes in chat sessions (e.g. ticking off a to-do) are saved the same way as Monday's (step 3a) and go live with Wednesday's deploy, unless the owner asks for an immediate update.

Live site: https://bathroom-deals-team.netlify.app (Netlify site id `7cdd48f1-9bae-4d4b-af21-c81dee29240b`).
The page reads everything from `data.json`. Monday saves changes to Drive; Wednesday publishes them with one deploy. Never change `index.html`, `logo.png` or `netlify.toml` in a run.

## 1. Start from the NEWEST data
The repo copy goes stale, because scheduled runs can't push to git.
1. In Google Drive, search folder `1vh18jPiPTbIKZ6VYuOKQwrrBOs6l3VUr` for `title contains 'dashboard-data-'` (orderBy `modifiedTime desc`).
2. Download the live file: `curl -sSf https://bathroom-deals-team.netlify.app/data.json`.
3. Use whichever has the later `updated` date. If they tie, use the Drive file, which holds the unpublished changes. Read the Drive file with the Drive read/download tool.
```bash
mkdir -p /tmp/dash && cp marketing/bathroom-deals/dashboard/{index.html,logo.png,netlify.toml} /tmp/dash/
# then write the chosen JSON to /tmp/dash/data.json
```

## 2. Edit /tmp/dash/data.json (Python json, keep the same structure)
- `updated`: today's date (YYYY-MM-DD, Brisbane).
- For every agent that did work in this run:
  - set `last_update` to today;
  - add new items at the TOP of `done` (`{"date", "text"}`): one short plain-English line per piece of work, in the owner's words, e.g. "4 posts for 23–29 Nov", "Reel: Lucito towel rails in 6 finishes", "New blog article drafted: …";
  - keep at most 6 items per agent and drop the oldest;
  - set `next_run` to the agent's next scheduled day.
- `schedule`: for this run's entry set `last_run` to today and `last_status` to "ok", or "failed" if a main step failed; set `next` to the next date. Set `connectors_ok` and `connector_note` (e.g. "All 5 connectors added" or "ElevenLabs missing").
- `latest`: add this run's outputs at the TOP (`date`, `type`, `title`, `by` = agent id, `url` = Drive file/folder link or website link). Keep the newest 8.
- `calendar` (**Wednesday run only**): replace it with NEXT week (`week_of` = next Monday). Items: the Monday report run (6:47 am, kind "run"), each Facebook/Instagram post (kind "facebook"), the reel (kind "reel", Fri 7:30 pm), each Google update (kind "google"), and the Wednesday run (12:41 pm, kind "run"). `what` is short ("Post 1: … ($price)"), and `link` is the week's Drive folder.
- `waiting`: the owner's to-do list.
  - Add new items for anything only the owner can do (schedule the new pack, approve a WordPress draft, a BLOCK / ON HOLD item, a missing connector, a failed step). Set `priority` high / medium / low and `due` where there's a date. Add `how` (the click path) and `link` where useful.
  - Remove items that are clearly done. For example, remove "Add the Google Drive connector to the Monday task" once Drive works in the Monday run. Leave anything you can't verify.
- Never put sales figures, revenue, customer details or phone numbers or emails in `data.json`. The site is public.

Run `python3 -c "import json;json.load(open('/tmp/dash/data.json'))"` to check the JSON before deploying.

## 3a. Save (Monday, and manual changes)
Upload `/tmp/dash/data.json` to Google Drive folder `1vh18jPiPTbIKZ6VYuOKQwrrBOs6l3VUr` with the title `dashboard-data-YYYY-MM-DD.json`, contentMimeType `application/json` and disableConversionToGoogleType true. Say in the run summary: "Dashboard changes saved; they go live with Wednesday's update."

## 3b. Deploy (Wednesday only)
1. Call the Netlify connector: `netlify-deploy-services-updater` with `{"operation":"deploy-site","params":{"siteId":"7cdd48f1-9bae-4d4b-af21-c81dee29240b"}}`. It returns an `npx -y @netlify/mcp@latest --site-id … --proxy-path "…"` command.
2. Run that command from `/tmp/dash` with `NODE_USE_ENV_PROXY=1 NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt` in front of it (Node's fetch needs this to use the proxy).
3. Wait for "Deploy is ready!".
4. Check it: `curl -sS https://bathroom-deals-team.netlify.app/data.json | head -c 200` should show today's `updated` date.

If the deploy fails (connector missing, or "credit usage exceeded"), do step 3a instead, and say "DASHBOARD NOT UPDATED: <reason>" in the run summary. Never retry a failed deploy more than once: each attempt can use credits.
