---
title: About this library
summary: What this site is, how the notes are made, and what the labels on every page mean.
---

## What this is

A reading library. Someone accumulated several hundred trading and finance PDFs — the usual mix of
classics, course manuals, vendor systems, forum ebooks and academic papers — and rather than let them
sit unread in a folder, worked through them and wrote a page for each one.

There are **582 notes on individual documents**, **151 sub-pages** covering a specific method inside a
book, and **14 topic pages** that read across the whole library and try to say where the books agree,
where they contradict each other, and where a famous method turns out to be a renamed version of an
older one.

It is closer to an encyclopedia than a blog. Nothing is sequenced by date; everything is cross-linked,
and the [search](search.html) covers the full text of every note.

## What it is not

It is **not the books**. Notes paraphrase; they do not reproduce chapters, quote at length, or host the
source PDFs. Where a book is worth reading, the note says so — go and buy it.

It is **not advice**, and it is not a record of trading results. A note that describes a method
faithfully is saying "this is what the author claims," not "this works." Several topic pages end at
the evidence that a popular method does not survive testing.

It is **not complete**. Four source files are damaged and stay marked unavailable rather than being
guessed at from their filenames.

## How a note is made

1. The PDF's text is extracted and the document is classified — subject, difficulty, and whether it is
   a book, a course, a paper, a manual or a vendor system.
2. The document is read against that extracted text, and the note is written from it.
3. Concrete parameters are kept. Where a book gives a lookback, a stop distance, or a risk fraction,
   the note keeps the number and cites the page it came from.
4. Numeric and rule claims are checked back against the source pages before the note is published.
   This pass has caught real errors — a formula missing a factor, a rule credited to the wrong author,
   a threshold off by a quarter point, a percentage that appears nowhere in the book.
5. What was actually read is recorded on the page. This is the part most study notes leave out.

Nothing is filled in from memory or inferred from a title. If a source does not state a stop, a size or
a parameter, the note says the source does not state it.

## The labels on every page

**Tier A — a deep note.** A full synthesis of the book, usually with separate sub-pages for its
individual methods.

**Tier B — a concise note.** A shorter summary: what the source argues, what is worth taking from it,
what to ignore.

**Full source review.** The document's entire extractable text was read.

**Partial source review.** Specific pages were read, and the note names them. Partial is not a gap in
the record — it is the record. Two things cause it: a long book where particular chapters were read
closely, and a scanned PDF whose pages are images rather than text, so only a sampled set of pages can
be extracted at all. Where the second applies, the note says so.

Every one of the 582 notes carries one of those two coverage labels. The
[source coverage page](coverage.html) lists all of them, alongside every duplicate, off-topic and
damaged file in the original collection.

## Corrections

The notes are wrong in places — that is the nature of reading several hundred books and writing
about them. Corrections are welcome through the
[repository](https://github.com/ninad-k/trading-playbook), which holds the Markdown sources, the build
scripts and the full revision history of every page here.

## Licence

The site's code is GPL-3.0. The notes are CC BY-NC-SA 4.0 — reuse them non-commercially with
attribution, and share adaptations under the same terms.
