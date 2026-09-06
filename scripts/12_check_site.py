"""Check generated local navigation, source coverage, and search inventory."""
import json
import re
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

import frontmatter
from common import BOOKS, DOCS, load_manifest


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])


def main():
    pages = {p.resolve(): Page(p.read_text(encoding='utf-8')) for p in DOCS.rglob('*.html')}
    errors = []
    links = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                if re.search(r'\.(pdf|epub|djvu|chm|zip|rar)$', url.path, re.I):
                    errors.append(f'Link to a source file leaked onto {path.name}: {link}')
                continue
            links += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{path.name}: missing {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.name}: missing fragment {link}')

    search = json.loads((DOCS / 'search-index.json').read_text(encoding='utf-8'))
    book_slugs = {p.stem for p in BOOKS.glob('*.md')}
    indexed = {r['slug'] for r in search if r['doc_type'] != 'topic'}
    if book_slugs != indexed:
        errors.append('Search inventory differs from Markdown notes')
    if len({r['url'] for r in search}) != len(search):
        errors.append('Duplicate search URLs')
    for row in search:
        if not (DOCS / row['url']).is_file():
            errors.append(f'Missing search destination: {row["slug"]}')
        if row['slug'] in book_slugs:
            body = frontmatter.load(BOOKS / (row['slug'] + '.md'), encoding='utf-8').content
            if len(row['text']) < len(body) * .80:
                errors.append(f'Truncated search content: {row["slug"]}')
    coverage = pages[(DOCS / 'coverage.html').resolve()]
    pdfs = {r['slug'] for r in load_manifest() if r.get('ext') == 'pdf'}
    if not pdfs.issubset(coverage.ids):
        errors.append('Coverage page omits source PDFs')
    print(f'Checked {len(pages)} HTML pages, {links} local links, {len(search)} search entries, {len(pdfs)} source records')
    for error in errors:
        print('ERROR:', error)
    print(f'{len(errors)} errors')
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
