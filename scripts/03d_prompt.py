"""Print the agent prompt for one or more batch ids from data/batches.json.

Usage: python scripts/03d_prompt.py A06 A07 B50
"""
from __future__ import annotations

import json
import sys

from common import DATA

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HEAD = (
    "You are writing study notes for the Trading Playbook. Repo root: D:\\Projects\\trading-playbook "
    "(run all commands from there; Python is .venv/Scripts/python).\n\n"
    "FIRST: read D:\\Projects\\trading-playbook\\scripts\\AGENT_BRIEF.md in full and follow it exactly "
    "(schema, headings, writing rules, validation).\n\n"
)
TAIL_A = (
    "Read each via `.venv/Scripts/python scripts/04_chunk.py <slug>` (overview), then `--grep` and `--pages` for the "
    "rule-bearing chapters. Write content/books/<slug>.md for each (and content/books/<slug>--<system>.md sub-pages "
    "if warranted). For `related:` use only slugs present in data/slugs.txt (grep it). Do not modify any other files.\n\n"
)
TAIL_B = (
    "Documents under ~60 pages: read with `.venv/Scripts/python scripts/04_chunk.py <slug> --full`. Longer ones: overview "
    "then `--pages` for the key chapters. Write content/books/<slug>.md for each. For `related:` use only slugs present "
    "in data/slugs.txt (grep it). Do not modify any other files.\n\n"
)
OCR_NOTE = (
    "NOTE: these documents are scanned books whose text came from OCR of a SAMPLE of pages (front matter plus evenly "
    "spaced pages); un-sampled pages are empty. Expect OCR noise (broken words, merged words). Work from what is there, "
    "use `--grep` to locate topics, do not invent content for gaps, and state in Caveats that the notes are based on "
    "sampled pages.\n\n"
)


def main() -> None:
    batches = {b["id"]: b for b in json.loads((DATA / "batches.json").read_text(encoding="utf-8"))}
    for bid in sys.argv[1:]:
        b = batches[bid]
        tier = b["tier"]
        items = "\n".join(f"{i}. {x['slug']} | {x['filename']} | {x['pages']}" for i, x in enumerate(b["items"], 1))
        slugs = ",".join(x["slug"] for x in b["items"])
        body = HEAD
        if tier == "A":
            body += f"Your batch: {bid}, Tier A (deep notes, 900–1500 words each, plus system sub-pages where the book has a distinct tradable method).\n\n"
        else:
            body += f"Your batch: {bid}, Tier B (concise notes, 250–450 words each; no system sub-pages).\n\n"
        body += f"Documents (slug | source_file | pages):\n{items}\n\n"
        if b["ocr"]:
            body += OCR_NOTE
        body += TAIL_A if tier == "A" else TAIL_B
        body += f"When done run `.venv/Scripts/python scripts/05_validate.py --only {slugs}` and fix every error it reports. Final message: the table described in the brief."
        print(f"##### {bid} #####\n{body}\n")


if __name__ == "__main__":
    main()
