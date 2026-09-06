"""Generate a dated resume report from saved decisions and the current content."""
import json
import argparse
from collections import Counter
from datetime import date

import frontmatter
from common import BOOKS, DATA, ROOT, TOPICS, load_manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=date.today().isoformat(), help='Snapshot date in the project owner\'s timezone (YYYY-MM-DD)')
    args = ap.parse_args()
    outcomes = {}
    for name in ('short_a', 'short_b', 'long', 'root', 'legacy'):
        path = DATA / 'resume_assignments' / (name + '_report.json')
        if path.exists():
            for row in json.loads(path.read_text(encoding='utf-8')):
                outcomes[row['slug']] = row
    notes = {p.stem: frontmatter.load(p, encoding='utf-8') for p in BOOKS.glob('*.md')}
    new = {s: notes[s] for s, r in outcomes.items() if r['outcome'] == 'written' and s in notes}
    parents = {s: p for s, p in notes.items() if p.get('doc_type') != 'system'}
    rows = load_manifest()
    missing = [r['slug'] for r in rows if r.get('tier') in ('A', 'B') and r['slug'] not in notes]
    excluded = [r for r in rows if r.get('ext') == 'pdf' and r.get('tier') == 'C']
    coverage = Counter(p.get('source_review', 'unrecorded') for p in parents.values())
    summary = {'date': date.fromisoformat(args.date).isoformat(), 'new_parent_notes': len(new),
               'parent_notes': len(parents), 'method_pages': len(notes) - len(parents),
               'source_pdfs': sum(r.get('ext') == 'pdf' for r in rows),
               'excluded_pdfs': dict(Counter(r.get('c_status', 'excluded') for r in excluded)),
               'source_review': dict(coverage), 'missing_eligible_notes': missing,
               'topic_synthesis_files': len(list(TOPICS.glob('*.md')))}
    (DATA / 'resume_completion.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    lines = ['# Trading Playbook: resumed books', '',
             f"Snapshot: {summary['date']}. {len(new)} new parent notes; {len(parents)} parent notes and {summary['method_pages']} method pages in the library.", '',
             f"The saved inventory contains {summary['source_pdfs']} PDFs. {len(excluded)} are documented duplicates, exclusions or damaged files. Missing eligible notes: {len(missing)}.", '',
             '## Reading coverage', '',
             f"Full source reviews recorded: {coverage['full']}. Partial source reviews: {coverage['partial']}. Older notes without recorded coverage: {coverage['unrecorded']}.", '',
             'A complete inventory is not a claim that every page of every book has been read. Long-book notes identify the selected PDF pages actually reviewed; damaged equations and unresolved chart details remain qualified.', '',
             '## Review and validation', '',
             'Source-check reports are in [resume_assignments](resume_assignments/). The short-document queues received full source readings; the long-book queues received targeted verification of consequential claims. Author prescriptions, historical results and editorial implications are distinguished.', '',
             'Reproduce structural and navigation checks with `python scripts/05_validate.py`, `python scripts/06_build_site.py`, and `python scripts/12_check_site.py`. These checks do not establish trading profitability.', '',
             '## New notes', '']
    for slug, note in sorted(new.items(), key=lambda x: x[1]['title'].lower()):
        lines.append(f"- [{note['title']}](../content/books/{slug}.md) — {note.get('author', 'Unknown')}; {note.get('source_review', 'unrecorded')} review.")
    lines += ['', '## Unavailable damaged files', '']
    for row in excluded:
        if row.get('c_status') == 'corrupt':
            lines.append(f"- {row['filename']} — {row.get('tier_reason', '')}")
    lines += ['', '## Publication state', '',
              'The searchable HTML site is local in `docs/`. Medium exports are editable drafts; regenerate their links with the actual site URL before posting. Notion payloads preserve reading coverage but have not been synced by this resume run. No remote publication was performed.', '']
    (DATA / 'resume_completion.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
