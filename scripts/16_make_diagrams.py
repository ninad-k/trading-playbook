"""Generate the site's explanatory diagrams as original SVG into content/diagrams/.

Usage: python scripts/16_make_diagrams.py

Every diagram is schematic. Shapes are drawn to explain a generic concept; they are
not traced from any book's figure and they assert no price, parameter or result.
Colours are CSS custom properties from assets/site.css, so the SVGs follow the
site's light and dark themes once inlined.
"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "content" / "diagrams"

FG, MUTED, LINE, ACC, ACC2, LNK = (
    "var(--fg,#1c1c1a)", "var(--muted,#6b6b66)", "var(--line,#e4e2dc)", "var(--accent,#0b6e4f)", "var(--accent2,#b8862b)", "var(--a,#0a5f8f)",
)

CSS = """
.d-bg{fill:var(--card,#ffffff)}
.d-ax{stroke:var(--line,#e4e2dc);stroke-width:1}
.d-grid{stroke:var(--line,#e4e2dc);stroke-width:1;stroke-dasharray:3 4}
.d-px{fill:none;stroke:var(--fg,#1c1c1a);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.d-hi{fill:none;stroke:var(--accent,#0b6e4f);stroke-width:2.2;stroke-linejoin:round;stroke-linecap:round}
.d-hi2{fill:none;stroke:var(--accent2,#b8862b);stroke-width:2.2;stroke-linejoin:round;stroke-linecap:round}
.d-dash{fill:none;stroke:var(--accent,#0b6e4f);stroke-width:1.6;stroke-dasharray:5 4}
.d-t{fill:var(--fg,#1c1c1a);font:600 13px -apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif}
.d-s{fill:var(--muted,#6b6b66);font:12px -apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif}
.d-k{fill:var(--accent,#0b6e4f);font:600 12px -apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif}
.d-k2{fill:var(--accent2,#b8862b);font:600 12px -apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif}
.d-up{fill:var(--card,#ffffff);stroke:var(--fg,#1c1c1a);stroke-width:1.5}
.d-dn{fill:var(--fg,#1c1c1a);stroke:var(--fg,#1c1c1a);stroke-width:1.5}
.d-zone{fill:var(--accent,#0b6e4f);opacity:.10}
.d-zone2{fill:var(--accent2,#b8862b);opacity:.12}
"""


def svg(name: str, w: int, h: int, title: str, desc: str, body: str) -> None:
    doc = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" '
        f'aria-labelledby="{name}-t {name}-d" class="diagram">'
        f'<title id="{name}-t">{title}</title><desc id="{name}-d">{desc}</desc>'
        f"<style>{CSS}</style>{body}</svg>\n"
    )
    (OUT / f"{name}.svg").write_text(doc, encoding="utf-8")


def pts(seq) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in seq)


def txt(x, y, s, cls="d-s", anchor="start") -> str:
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{s}</text>'


def frame(w, h) -> str:
    return f'<rect x="0" y="0" width="{w}" height="{h}" rx="8" class="d-bg"/>'


def arrow_defs() -> str:
    return (
        '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        'markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="var(--accent,#0b6e4f)"/></marker>'
        '<marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        'markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="var(--accent2,#b8862b)"/></marker>'
        "</defs>"
    )


def d_market_structure() -> None:
    w, h = 720, 300
    path = [(40, 235), (110, 162), (150, 192), (215, 120), (255, 156),
            (320, 78), (382, 142), (430, 112), (500, 182), (548, 150),
            (620, 218), (680, 236)]
    b = frame(w, h) + arrow_defs()
    b += f'<line x1="30" y1="268" x2="692" y2="268" class="d-ax"/>'
    b += f'<rect x="320" y="30" width="372" height="238" class="d-zone2"/>'
    b += f'<line x1="255" y1="156" x2="430" y2="156" class="d-dash"/>'
    b += f'<polyline points="{pts(path)}" class="d-px"/>'
    for x, y, lab in [(110, 162, "HH"), (215, 120, "HH"), (320, 78, "HH")]:
        b += f'<circle cx="{x}" cy="{y}" r="4" fill="{ACC}"/>' + txt(x, y - 12, lab, "d-k", "middle")
    for x, y, lab in [(150, 192, "HL"), (255, 156, "HL")]:
        b += f'<circle cx="{x}" cy="{y}" r="4" fill="{ACC}"/>' + txt(x, y + 20, lab, "d-k", "middle")
    for x, y, lab in [(430, 112, "LH"), (548, 150, "LH")]:
        b += f'<circle cx="{x}" cy="{y}" r="4" fill="{ACC2}"/>' + txt(x, y - 12, lab, "d-k2", "middle")
    for x, y, lab in [(500, 182, "LL"), (620, 218, "LL")]:
        b += f'<circle cx="{x}" cy="{y}" r="4" fill="{ACC2}"/>' + txt(x, y + 20, lab, "d-k2", "middle")
    b += f'<circle cx="382" cy="142" r="4" fill="{ACC2}"/>'
    b += f'<line x1="382" y1="138" x2="382" y2="116" stroke="{ACC2}" stroke-width="1.4"/>'
    b += txt(382, 108, "break of structure", "d-k2", "middle")
    b += txt(150, 52, "Uptrend: each high above the last, each low above the last", "d-s")
    b += txt(560, 60, "Downtrend", "d-k2", "middle")
    b += txt(40, 288, "The first lower low after a run of higher lows is the signal that structure has changed.", "d-s")
    svg("market-structure", w, h, "Swing structure and break of structure",
        "A price line making higher highs and higher lows, then failing to hold the last higher low and "
        "turning into a sequence of lower highs and lower lows.", b)


def d_candle_anatomy() -> None:
    w, h = 720, 300
    b = frame(w, h)
    b += txt(40, 34, "Anatomy", "d-t")
    b += f'<line x1="86" y1="70" x2="86" y2="230" stroke="{FG}" stroke-width="1.5"/>'
    b += f'<rect x="70" y="110" width="32" height="80" class="d-up"/>'
    for y, lab, ax in [(70, "high", 0), (110, "close", 0), (190, "open", 0), (230, "low", 0)]:
        b += f'<line x1="106" y1="{y}" x2="140" y2="{y}" class="d-grid"/>' + txt(146, y + 4, lab)
    b += txt(86, 254, "one bar =<tspan> one period</tspan>", "d-s", "middle")
    b += f'<line x1="215" y1="50" x2="215" y2="270" class="d-ax"/>'
    for i, (x, name, note) in enumerate([(285, "Doji", "open &#8776; close"),
                                         (415, "Hammer", "long lower wick"),
                                         (560, "Engulfing", "body covers prior body")]):
        b += txt(x, 34, name, "d-t", "middle") + txt(x, 262, note, "d-s", "middle")
    b += f'<line x1="285" y1="90" x2="285" y2="200" stroke="{FG}" stroke-width="1.5"/>'
    b += f'<rect x="269" y="142" width="32" height="4" class="d-dn"/>'
    b += f'<line x1="415" y1="96" x2="415" y2="215" stroke="{FG}" stroke-width="1.5"/>'
    b += f'<rect x="399" y="96" width="32" height="36" class="d-up"/>'
    b += f'<line x1="540" y1="120" x2="540" y2="185" stroke="{FG}" stroke-width="1.5"/>'
    b += f'<rect x="528" y="132" width="24" height="34" class="d-dn"/>'
    b += f'<line x1="582" y1="100" x2="582" y2="205" stroke="{FG}" stroke-width="1.5"/>'
    b += f'<rect x="568" y="118" width="28" height="66" class="d-up"/>'
    b += txt(40, 288, "Shapes only. Whether any pattern carries an edge is argued case by case in the notes.", "d-s")
    svg("candle-anatomy", w, h, "Candlestick anatomy and three common shapes",
        "A labelled candlestick showing high, low, open and close, beside a doji, a hammer and a "
        "bullish engulfing pair.", b)


def d_divergence() -> None:
    w, h = 720, 344
    b = frame(w, h) + arrow_defs()
    b += txt(40, 28, "Price", "d-t")
    price = [(40, 150), (110, 90), (160, 125), (240, 105), (300, 130),
             (380, 62), (450, 108), (530, 58), (600, 120), (680, 165)]
    b += f'<polyline points="{pts(price)}" class="d-px"/>'
    b += f'<line x1="380" y1="62" x2="530" y2="58" class="d-hi"/>'
    b += f'<circle cx="380" cy="62" r="4" fill="{ACC}"/><circle cx="530" cy="58" r="4" fill="{ACC}"/>'
    b += txt(455, 44, "higher high", "d-k", "middle")
    b += f'<line x1="30" y1="185" x2="692" y2="185" class="d-ax"/>'
    b += txt(40, 210, "Oscillator", "d-t")
    osc = [(40, 285), (110, 245), (160, 268), (240, 250), (300, 272),
           (380, 224), (450, 262), (530, 245), (600, 275), (680, 292)]
    b += f'<polyline points="{pts(osc)}" class="d-px"/>'
    b += f'<line x1="380" y1="224" x2="530" y2="245" class="d-hi2"/>'
    b += f'<circle cx="380" cy="224" r="4" fill="{ACC2}"/><circle cx="530" cy="245" r="4" fill="{ACC2}"/>'
    b += txt(455, 300, "lower high", "d-k2", "middle")
    b += f'<line x1="530" y1="70" x2="530" y2="238" class="d-grid"/>'
    b += txt(546, 160, "same bar", "d-s")
    b += txt(40, 330, "Bearish divergence: price prints a higher high, the oscillator does not. "
                      "The reverse pattern at lows is bullish divergence.", "d-s")
    svg("divergence", w, h, "Bearish divergence between price and an oscillator",
        "Two stacked panels. The upper price panel makes a higher high while the lower oscillator "
        "panel makes a lower high at the same bar.", b)


def d_elliott_fibonacci() -> None:
    w, h = 720, 320
    b = frame(w, h) + arrow_defs()
    wave = [(40, 268), (130, 190), (185, 232), (300, 118), (365, 168),
            (470, 70), (545, 130), (600, 96), (668, 152)]
    labels = ["", "1", "2", "3", "4", "5", "A", "B", "C"]
    b += f'<line x1="30" y1="292" x2="692" y2="292" class="d-ax"/>'
    b += f'<rect x="470" y="40" width="222" height="252" class="d-zone2"/>'
    b += f'<polyline points="{pts(wave)}" class="d-px"/>'
    for (x, y), lab in zip(wave, labels):
        if not lab:
            continue
        cls = "d-k2" if lab in "ABC" else "d-k"
        col = ACC2 if lab in "ABC" else ACC
        dy = -12 if y < 170 else 20
        b += f'<circle cx="{x}" cy="{y}" r="4" fill="{col}"/>' + txt(x, y + dy, lab, cls, "middle")
    b += txt(255, 60, "five-wave impulse", "d-k", "middle")
    b += txt(580, 60, "three-wave correction", "d-k2", "middle")
    for frac, lab in [(0.382, "38.2%"), (0.5, "50%"), (0.618, "61.8%")]:
        y = 118 + frac * (232 - 118)
        b += f'<line x1="185" y1="{y:.1f}" x2="330" y2="{y:.1f}" class="d-grid"/>'
        b += txt(180, y + 4, lab, "d-s", "end")
    b += txt(40, 312, "Wave labels and retracement ratios are the vocabulary; the notes record where each "
                      "author disagrees about applying them.", "d-s")
    svg("elliott-fibonacci", w, h, "Elliott five-three wave count with Fibonacci retracement levels",
        "An impulse of five waves followed by a three-wave A-B-C correction, with the common "
        "38.2, 50 and 61.8 percent retracement levels marked.", b)


def _series(n=130, x0=40, x1=688):
    import math
    out = []
    for i in range(n):
        t = i / (n - 1)
        y = 206 - 90 * t + 30 * math.sin(t * 9.2) + 15 * math.sin(t * 24.0) + 9 * math.sin(t * 47.0) + 5 * math.sin(t * 78.0)
        out.append((x0 + t * (x1 - x0), y))
    return out


def _sma(series, win):
    out = []
    for i in range(len(series)):
        if i < win - 1:
            continue
        seg = series[i - win + 1:i + 1]
        out.append((series[i][0], sum(p[1] for p in seg) / win))
    return out


def d_ma_crossover() -> None:
    w, h = 720, 320
    px = _series()
    fast, slow = _sma(px, 9), _sma(px, 25)
    b = frame(w, h)
    b += f'<line x1="30" y1="292" x2="692" y2="292" class="d-ax"/>'
    b += f'<polyline points="{pts(px)}" class="d-px" style="stroke:var(--muted,#6b6b66);stroke-width:1.2"/>'
    b += f'<polyline points="{pts(fast)}" class="d-hi"/>'
    b += f'<polyline points="{pts(slow)}" class="d-hi2"/>'
    lookup = {round(x): y for x, y in slow}
    crosses, prev = [], None
    for x, y in fast:
        sy = lookup.get(round(x))
        if sy is None:
            continue
        side = y < sy
        if prev is not None and side != prev:
            crosses.append((x, y))
        prev = side
    for cx, cy in crosses:
        b += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="none" stroke="{FG}" stroke-width="2"/>'
    for x, col, lab, cls in [(40, ACC, "Fast average", "d-k"), (168, ACC2, "Slow average", "d-k2"),
                             (296, MUTED, "Price", "d-s")]:
        b += f'<line x1="{x}" y1="26" x2="{x + 22}" y2="26" stroke="{col}" stroke-width="2.2"/>'
        b += txt(x + 30, 30, lab, cls)
    b += f'<circle cx="382" cy="26" r="5" fill="none" stroke="{FG}" stroke-width="2"/>'
    b += txt(394, 30, "crossover", "d-s")
    b += txt(40, 306, f"A bare crossover rule trades every circle — {len(crosses)} of them here.", "d-s")
    b += txt(40, 322, "Most are whipsaws. What each author adds to filter them is the whole subject "
                      "of this topic.", "d-s")
    svg("ma-crossover", w, h, "Fast and slow moving-average crossover",
        "A price line with a fast and a slow moving average drawn over it, every crossing point "
        "circled to show how many signals a naive crossover rule generates.", b)


def d_opening_range() -> None:
    w, h = 720, 330
    b = frame(w, h) + arrow_defs()
    hi, lo = 120, 196
    b += f'<line x1="30" y1="292" x2="692" y2="292" class="d-ax"/>'
    b += f'<rect x="60" y="{hi}" width="170" height="{lo - hi}" class="d-zone"/>'
    b += f'<line x1="60" y1="{hi}" x2="660" y2="{hi}" class="d-dash"/>'
    b += f'<line x1="60" y1="{lo}" x2="660" y2="{lo}" class="d-dash"/>'
    path = [(60, 170), (95, 132), (125, 188), (160, 140), (195, 190), (230, 128),
            (280, 104), (330, 132), (380, 86), (440, 108), (510, 60), (580, 92), (660, 48)]
    b += f'<polyline points="{pts(path)}" class="d-px"/>'
    b += txt(145, 112, "opening range", "d-k", "middle")
    b += txt(145, 214, "first N minutes", "d-s", "middle")
    b += txt(668, hi + 4, "high", "d-k", "start")
    b += txt(668, lo + 4, "low", "d-k", "start")
    b += f'<line x1="262" y1="150" x2="262" y2="118" stroke="{ACC}" stroke-width="2" marker-end="url(#ar)"/>'
    b += txt(266, 162, "break above &#8594; long", "d-k")
    b += f'<line x1="240" y1="{lo}" x2="640" y2="{lo}" stroke="{ACC2}" stroke-width="2" stroke-dasharray="4 4"/>'
    b += txt(560, lo + 18, "stop: other side of the range", "d-k2", "middle")
    b += f'<line x1="60" y1="262" x2="660" y2="262" class="d-ax"/>'
    b += f'<line x1="60" y1="256" x2="60" y2="268" class="d-ax"/>'
    b += f'<line x1="230" y1="256" x2="230" y2="268" class="d-ax"/>'
    b += f'<line x1="660" y1="256" x2="660" y2="268" class="d-ax"/>'
    b += f'<line x1="60" y1="262" x2="230" y2="262" stroke="{ACC}" stroke-width="3"/>'
    b += txt(145, 280, "range window", "d-k", "middle")
    b += txt(445, 280, "rest of session", "d-s", "middle")
    b += txt(40, 320, "The range window, the confirmation and the exit differ book by book; the shape "
                      "of the trade does not.", "d-s")
    svg("opening-range", w, h, "Opening-range breakout",
        "A session where the first N minutes define a high and a low; price later breaks above the "
        "high, which is the entry, with the opposite side of the range as the stop.", b)


def d_pullback_entry() -> None:
    w, h = 720, 348
    b = frame(w, h) + arrow_defs()
    entry, stop, t1, t2 = 168, 208, 128, 88
    b += f'<line x1="30" y1="300" x2="692" y2="300" class="d-ax"/>'
    path = [(40, 262), (110, 210), (150, 238), (215, 176), (268, 205), (330, 168),
            (395, 132), (470, 152), (540, 100), (610, 118), (672, 72)]
    b += f'<polyline points="{pts(path)}" class="d-px"/>'
    for y, lab, cls, col in [(stop, "stop  (below the pullback low)", "d-k2", ACC2),
                             (entry, "entry  (pullback into the trend)", "d-k", ACC),
                             (t1, "target 1  =  1R", "d-s", MUTED),
                             (t2, "target 2  =  2R", "d-s", MUTED)]:
        b += f'<line x1="330" y1="{y}" x2="640" y2="{y}" stroke="{col}" stroke-width="1.6" stroke-dasharray="5 4"/>'
        b += txt(646, y + 4, lab.split("  ")[0], cls)
    b += f'<rect x="330" y="{entry}" width="310" height="{stop - entry}" class="d-zone2"/>'
    b += f'<rect x="330" y="{t1}" width="310" height="{entry - t1}" class="d-zone"/>'
    b += txt(340, entry + 26, "1R of risk", "d-k2")
    b += txt(340, entry - 10, "1R of reward", "d-k")
    b += f'<circle cx="330" cy="168" r="5" fill="{ACC}"/>'
    b += txt(40, 40, "Trend already established", "d-s")
    b += txt(40, 316, "R is the distance from entry to stop.", "d-s")
    b += txt(40, 332, "Sizing so that 1R is a fixed fraction of the account is what makes targets "
                      "comparable across trades.", "d-s")
    svg("pullback-entry", w, h, "Swing entry on a pullback, with stop and R-multiple targets",
        "An uptrending price line pulling back to an entry level, with a stop below the pullback low "
        "and targets at one and two times the entry-to-stop distance.", b)


def d_forex_quote() -> None:
    w, h = 720, 300
    b = frame(w, h)
    b += txt(40, 40, "EUR / USD", "d-t")
    b += txt(40, 62, "base", "d-k") + txt(112, 62, "quote", "d-k2")
    b += f'<line x1="46" y1="46" x2="46" y2="52" stroke="{ACC}" stroke-width="2"/>'
    b += f'<line x1="126" y1="46" x2="126" y2="52" stroke="{ACC2}" stroke-width="2"/>'
    b += txt(40, 92, "One unit of the base currency, priced in the quote currency.", "d-s")
    b += f'<line x1="40" y1="112" x2="680" y2="112" class="d-ax"/>'
    for x, lab, val, cls in [(120, "bid", "1.0842", "d-k2"), (400, "ask", "1.0844", "d-k")]:
        b += txt(x, 148, lab, cls, "middle")
        b += f'<text x="{x}" y="196" class="d-t" text-anchor="middle" style="font-size:30px">{val}</text>'
    b += txt(120, 218, "you sell here", "d-s", "middle")
    b += txt(400, 218, "you buy here", "d-s", "middle")
    b += f'<line x1="180" y1="186" x2="340" y2="186" stroke="{FG}" stroke-width="1.5"/>'
    b += f'<line x1="180" y1="180" x2="180" y2="192" stroke="{FG}" stroke-width="1.5"/>'
    b += f'<line x1="340" y1="180" x2="340" y2="192" stroke="{FG}" stroke-width="1.5"/>'
    b += txt(260, 176, "spread = 2 pips", "d-t", "middle")
    b += f'<line x1="560" y1="160" x2="560" y2="182" stroke="{ACC}" stroke-width="2"/>'
    b += txt(560, 150, "1 pip", "d-k", "middle")
    b += txt(560, 200, "the 4th decimal", "d-s", "middle")
    b += txt(560, 220, "(2nd for JPY pairs)", "d-s", "middle")
    b += txt(40, 258, "The spread is the cost you pay on entry, before any commission or swap. It is the "
                      "first number most retail systems ignore.", "d-s")
    b += txt(40, 280, "Prices shown are an illustration, not a quote.", "d-s")
    svg("forex-quote", w, h, "Anatomy of a foreign-exchange quote",
        "A EUR/USD quote broken into base and quote currency, bid and ask price, the spread between "
        "them and the size of one pip.", b)


def _payoff(x0, y0, pw, ph, knots, title, note):
    mid = y0 + ph / 2
    s = f'<line x1="{x0}" y1="{mid}" x2="{x0 + pw}" y2="{mid}" class="d-ax"/>'
    s += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + ph}" class="d-ax"/>'
    seq = [(x0 + fx * pw, mid - fy * (ph / 2)) for fx, fy in knots]
    s += f'<polyline points="{pts(seq)}" class="d-hi"/>'
    s += txt(x0 + pw / 2, y0 - 12, title, "d-t", "middle")
    s += txt(x0 + pw / 2, y0 + ph + 24, note, "d-s", "middle")
    return s


def d_option_payoffs() -> None:
    w, h = 720, 310
    b = frame(w, h)
    b += txt(40, 30, "Payoff at expiry — profit above the line, loss below", "d-t")
    pw, ph, y0 = 132, 110, 80
    b += _payoff(52, y0, pw, ph, [(0, -0.45), (0.5, -0.45), (1, 0.85)],
                 "Long call", "loss capped at the premium")
    b += _payoff(224, y0, pw, ph, [(0, 0.85), (0.5, -0.45), (1, -0.45)],
                 "Long put", "gains as price falls")
    b += _payoff(396, y0, pw, ph, [(0, -0.9), (0.5, 0.5), (1, 0.5)],
                 "Covered call", "upside sold for income")
    b += _payoff(568, y0, pw, ph, [(0, -0.5), (0.35, -0.5), (0.7, 0.5), (1, 0.5)],
                 "Vertical spread", "both sides capped")
    b += txt(40, 248, "Every options position in the notes reduces to one of these shapes, or a "
                      "combination of them.", "d-s")
    b += txt(40, 266, "The horizontal line is break-even, not zero price.", "d-s")
    b += txt(40, 288, "Axes are unscaled: the point is the shape, not any particular strike or premium.", "d-s")
    svg("option-payoffs", w, h, "Four basic option payoff shapes",
        "Expiry payoff diagrams for a long call, a long put, a covered call and a vertical spread.", b)


def d_position_sizing() -> None:
    w, h = 720, 400
    b = frame(w, h) + arrow_defs()
    b += txt(40, 34, "Sizing from risk, not from conviction", "d-t")
    for x, wd, lab in [(40, 176, "Account equity"), (244, 176, "Risk per trade (%)"), (448, 176, "Stop distance")]:
        b += f'<rect x="{x}" y="52" width="{wd}" height="46" rx="8" fill="none" stroke="{LINE}"/>'
        b += txt(x + wd / 2, 80, lab, "d-s", "middle")
    b += txt(228, 82, "&#215;", "d-t", "middle") + txt(432, 82, "&#247;", "d-t", "middle")
    b += f'<line x1="360" y1="102" x2="360" y2="126" stroke="{ACC}" stroke-width="2" marker-end="url(#ar)"/>'
    b += f'<rect x="272" y="130" width="176" height="46" rx="8" fill="none" stroke="{ACC}" stroke-width="2"/>'
    b += txt(360, 158, "Position size", "d-k", "middle")
    b += txt(360, 200, "Two of the three inputs are chosen before the trade exists.", "d-s", "middle")
    b += txt(360, 218, "Only the stop distance comes from the chart.", "d-s", "middle")
    ax_x, ax_y, aw, ah = 74, 356, 292, 108
    b += f'<line x1="{ax_x}" y1="{ax_y}" x2="{ax_x + aw}" y2="{ax_y}" class="d-ax"/>'
    b += f'<line x1="{ax_x}" y1="{ax_y - ah}" x2="{ax_x}" y2="{ax_y}" class="d-ax"/>'
    curve = []
    for i in range(0, 71):
        d = i / 100
        curve.append((ax_x + (d / 0.7) * aw, ax_y - min(d / (1 - d), 2.4) / 2.4 * ah))
    b += f'<polyline points="{pts(curve)}" class="d-hi2"/>'
    b += txt(ax_x, ax_y - ah - 12, "gain needed to get back to even", "d-s")
    b += txt(ax_x + aw, ax_y + 20, "drawdown &#8594;", "d-s", "end")
    for d, lab, dx, dy in [(0.2, "20% needs 25%", 10, -8), (0.5, "50% needs 100%", -6, -12), (0.65, "65% needs 186%", -14, 24)]:
        x = ax_x + (d / 0.7) * aw
        y = ax_y - min(d / (1 - d), 2.4) / 2.4 * ah
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{ACC2}"/>'
        b += txt(x + dx, y + dy, lab, "d-k2", "end" if dx < 0 else "start")
    b += txt(410, 252, "Why the size rule matters", "d-t")
    for i, line in enumerate(["Recovering a loss takes a bigger gain than the",
                              "loss itself, and the gap widens fast. That is",
                              "arithmetic, not a claim about any method — and",
                              "it is the reason nearly every book in the library",
                              "caps risk per trade at a few percent."]):
        b += txt(410, 278 + i * 19, line, "d-s")
    svg("position-sizing", w, h, "Position sizing inputs and the drawdown-recovery curve",
        "Account equity times risk percent divided by stop distance gives position size; beside it a "
        "curve showing the gain required to recover from a given drawdown.", b)


def d_psychology_loop() -> None:
    import math
    w, h = 720, 384
    cx, cy, r = 360, 176, 116
    b = frame(w, h) + arrow_defs()
    stages = ["A rule is set", "A loss arrives", "The rule feels wrong",
              "The rule is widened", "A larger loss arrives", "Confidence breaks"]
    n = len(stages)
    for i, name in enumerate(stages):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{ACC2 if i else ACC}"/>'
        ax = "middle"
        ox, oy = 0, -18 if y < cy else 26
        if abs(math.cos(a)) > 0.7:
            ax = "start" if x > cx else "end"
            ox, oy = (18 if x > cx else -18), 5
        b += txt(x + ox, y + oy, name, "d-k" if i == 0 else "d-s", ax)
        a2 = -math.pi / 2 + (i + 0.62) * 2 * math.pi / n
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        a1 = -math.pi / 2 + (i + 0.18) * 2 * math.pi / n
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        b += (f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" fill="none" '
              f'stroke="{ACC2}" stroke-width="1.8" marker-end="url(#ar2)"/>')
    b += txt(cx, cy - 6, "The loop", "d-t", "middle")
    b += txt(cx, cy + 14, "every discipline book", "d-s", "middle")
    b += txt(cx, cy + 32, "is trying to break", "d-s", "middle")
    b += txt(40, 352, "The books differ on the remedy: written plans, smaller size, fixed review "
                      "intervals, walking away.", "d-s")
    b += txt(40, 370, "They do not differ much on the sequence.", "d-s")
    svg("psychology-loop", w, h, "The discipline loop described across the psychology books",
        "A six-stage cycle running from setting a rule, through a loss, widening the rule, a larger "
        "loss, and a break in confidence, back to setting a rule.", b)


def d_order_book() -> None:
    w, h = 720, 350
    b = frame(w, h)
    b += txt(40, 32, "One moment of a limit order book", "d-t")
    asks = [("1.0847", 90), ("1.0846", 148), ("1.0845", 62), ("1.0844", 210)]
    bids = [("1.0842", 176), ("1.0841", 84), ("1.0840", 132), ("1.0839", 240)]
    y = 60
    for price, size in asks:
        b += f'<rect x="360" y="{y}" width="{size}" height="20" fill="{ACC2}" opacity=".35"/>'
        b += txt(352, y + 15, price, "d-s", "end") + txt(366 + size, y + 15, str(size), "d-s")
        y += 26
    b += f'<line x1="200" y1="{y + 6}" x2="620" y2="{y + 6}" stroke="{FG}" stroke-width="2"/>'
    b += txt(190, y + 11, "spread", "d-t", "end")
    y += 18
    for price, size in bids:
        b += f'<rect x="360" y="{y}" width="{size}" height="20" fill="{ACC}" opacity=".35"/>'
        b += txt(352, y + 15, price, "d-s", "end") + txt(366 + size, y + 15, str(size), "d-s")
        y += 26
    b += txt(560, 52, "asks — sellers", "d-k2")
    b += txt(560, 300, "bids — buyers", "d-k")
    b += txt(40, 80, "A market order", "d-t")
    b += txt(40, 102, "crosses the spread", "d-s")
    b += txt(40, 120, "and eats the resting", "d-s")
    b += txt(40, 138, "size nearest to it.", "d-s")
    b += txt(40, 172, "A large order walks", "d-s")
    b += txt(40, 190, "up the ladder and", "d-s")
    b += txt(40, 208, "pays a worse average", "d-s")
    b += txt(40, 226, "price. That gap is", "d-s")
    b += txt(40, 244, "market impact.", "d-k")
    b += txt(40, 318, "Microstructure research here is largely about measuring the spread, the depth "
                      "and the impact", "d-s")
    b += txt(40, 336, "— the costs a backtest on closing prices cannot see.", "d-s")
    svg("order-book", w, h, "A limit order book with bids, asks, spread and depth",
        "A price ladder showing resting sell orders above and buy orders below, separated by the "
        "spread, with bar lengths standing for the size resting at each price.", b)


def d_market_cycle() -> None:
    import math
    w, h = 320, 300
    b = frame(w, h)
    curve = []
    for i in range(161):
        t = i / 160
        x = 24 + t * 272
        y = 190 - 92 * math.sin(t * math.pi * 2 - math.pi / 2) / 2 - 46 * t * 0
        curve.append((x, y - 20 * math.sin(t * math.pi)))
    b += f'<line x1="20" y1="252" x2="300" y2="252" class="d-ax"/>'
    b += f'<polyline points="{pts(curve)}" class="d-px"/>'
    for frac, lab, cls in [(0.10, "accumulation", "d-s"), (0.36, "mark-up", "d-k"),
                           (0.62, "distribution", "d-s"), (0.88, "mark-down", "d-k2")]:
        x = 24 + frac * 272
        b += f'<line x1="{x:.1f}" y1="40" x2="{x:.1f}" y2="248" class="d-grid"/>'
    b += txt(52, 268, "accum.", "d-s", "middle") + txt(126, 268, "mark-up", "d-k", "middle")
    b += txt(200, 268, "distrib.", "d-s", "middle") + txt(272, 268, "mark-down", "d-k2", "middle")
    b += txt(160, 28, "The four-phase cycle", "d-t", "middle")
    b += txt(160, 288, "Named since Wyckoff; the argument is over timing it.", "d-s", "middle")
    svg("market-cycle", w, h, "The four-phase market cycle",
        "A single rise and fall divided into accumulation, mark-up, distribution and mark-down "
        "phases.", b)


DIAGRAMS = [d_market_structure, d_candle_anatomy, d_divergence, d_elliott_fibonacci,
            d_ma_crossover, d_opening_range, d_pullback_entry, d_forex_quote,
            d_option_payoffs, d_position_sizing, d_psychology_loop, d_order_book,
            d_market_cycle]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for fn in DIAGRAMS:
        fn()
    made = sorted(p.name for p in OUT.glob("*.svg"))
    print(f"wrote {len(made)} diagrams to {OUT.relative_to(OUT.parent.parent)}/")
    for n in made:
        print(f"  {n}")


if __name__ == "__main__":
    main()
