# Brief for Notion-population agents

Goal: mirror every page in `content/books/` into the Notion **Books** database under the "Trading Playbook" page, with system sub-pages nested under their parent book. Repo root `D:\Projects\trading-playbook`, Python `.venv/Scripts/python`.

IDs (also in `data/notion_ids.json`):
- Parent page: `3d2dd5611ab08137a637dd7023b62ea9`
- Books data source id: `b22506e0-bbed-4f02-9837-f4b5bbd0ae1d` (use `parent: {"type":"data_source_id","data_source_id": ...}` for **book** pages)
- `data/notion_ids.json` → `pages` maps slug → Notion page id for everything already created. Never create a page for a slug that is already in that map.

## Loop (books first, then systems)

1. `.venv/Scripts/python scripts/08_notion_payload.py --pending --kind book --limit 8` prints a JSON list of payloads (`slug`, `title`, `properties`, `content`). If it prints `[]`, books are done.
2. Call the Notion `create-pages` tool ONCE with all payloads from that output: `parent` = the Books data source, `pages` = `[{"properties": <properties>, "content": <content>}, ...]`. Pass `properties` and `content` verbatim; do not rewrite or shorten the content. `allow_async: false`.
3. From the result, record ids: `.venv/Scripts/python scripts/08_notion_payload.py --record slug1=<id> slug2=<id> ...` (ids without dashes are fine).
4. Repeat until `--pending --kind book` prints `[]`.
5. Systems: `.venv/Scripts/python scripts/08_notion_payload.py --pending --kind system --limit 8`. Each payload has `parent_slug`; create system pages with `parent: {"type":"page_id","page_id": <pages[parent_slug]>}` (look the id up in `data/notion_ids.json`). Because the parent is a normal page, not the data source, pass only `{"title": <title>}` in `properties` for system pages, and prepend a one-line summary of the properties (category, tier, parent book) to the content. Record ids the same way. Repeat until `[]`.

If a create call fails validation, fix only what the error names (e.g. an unsupported tag value) and retry; do not drop the page. Group pages by parent for system batches: one create-pages call can only have one parent, so call once per parent book.

Do not edit any files except `data/notion_ids.json` (via `--record`). Final message: how many book pages and system pages you created, any failures with the error text, and the count remaining per `--pending`.
