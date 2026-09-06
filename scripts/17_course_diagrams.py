"""Diagrams the Manual Trader course needs that the book library did not.

Usage: python scripts/17_course_diagrams.py

Same rules as scripts/16_make_diagrams.py: schematic, original, drawn with the site's CSS
custom properties so they follow the light and dark themes, and asserting no price,
parameter or result. Helpers are reused from that module rather than duplicated.
"""
from __future__ import annotations

import importlib.util
import math
from pathlib import Path

_spec = importlib.util.spec_from_file_location("mk", Path(__file__).resolve().parent / "16_make_diagrams.py")
mk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mk)

svg, pts, txt, frame, arrow_defs = mk.svg, mk.pts, mk.txt, mk.frame, mk.arrow_defs
FG, MUTED, LINE, ACC, ACC2 = mk.FG, mk.MUTED, mk.LINE, mk.ACC, mk.ACC2

MDASH, SIGMA, MINUS, TIMES = "&#8212;", "&#963;", "&#8722;", "&#215;"


def d_volume_profile() -> None:
    w, h = 720, 348
    b = frame(w, h)
    rows = [(60, 26), (76, 40), (92, 64), (108, 96), (124, 150), (140, 196), (156, 168),
            (172, 118), (188, 74), (204, 92), (220, 138), (236, 70), (252, 34)]
    poc_y = max(rows, key=lambda r: r[1])[0]
    va = [r for r in rows if 108 <= r[0] <= 220]
    b += f'<rect x="300" y="{va[0][0] - 8}" width="392" height="{va[-1][0] - va[0][0] + 16}" class="d-zone"/>'
    for y, v in rows:
        style = ("fill:var(--accent,#0b6e4f)" if y == poc_y
                 else "fill:var(--muted,#6b6b66);opacity:.5")
        b += f'<rect x="300" y="{y - 6}" width="{v}" height="12" style="{style}"/>'
    b += '<line x1="300" y1="40" x2="300" y2="272" class="d-ax"/>'
    price = [(322, 250), (370, 190), (410, 214), (462, 150), (512, 176), (562, 120),
             (612, 152), (666, 98)]
    b += f'<polyline points="{pts(price)}" class="d-px" style="opacity:.45"/>'
    b += f'<line x1="300" y1="{poc_y}" x2="692" y2="{poc_y}" class="d-dash"/>'
    b += txt(294, poc_y + 4, "POC", "d-k", "end")
    b += txt(294, va[0][0] + 4, "value area high", "d-s", "end")
    b += txt(294, va[-1][0] + 4, "value area low", "d-s", "end")
    b += txt(40, 34, "Volume at price", "d-t")
    for i, line in enumerate(["Each bar is how much traded", "at that price, not when."]):
        b += txt(40, 62 + i * 18, line, "d-s")
    for i, line in enumerate(["The widest row is the point", "of control: the price the",
                              "market spent most effort", "agreeing on."]):
        b += txt(40, 116 + i * 18, line, "d-s")
    for i, line in enumerate(["The shaded band holds", "roughly 70% of the volume", "traded."]):
        b += txt(40, 208 + i * 18, line, "d-s")
    b += txt(40, 300, "Thin rows are prices the market moved through quickly and tends not to linger in.", "d-s")
    b += txt(40, 322, "This is where the support and resistance zones from stage 3 actually come from.", "d-k")
    svg("volume-profile", w, h, "Volume profile with point of control and value area",
        "A horizontal histogram of volume traded at each price, the widest row marked as the point "
        "of control and a shaded band covering the value area, with a faint price line beside it.", b)


def d_vwap_bands() -> None:
    w, h = 720, 330
    b = frame(w, h)
    n, x0, x1 = 130, 60, 660
    vwap, up1, lo1, up2, lo2, price = [], [], [], [], [], []
    for i in range(n):
        t = i / (n - 1)
        x = x0 + t * (x1 - x0)
        v = 198 - 60 * t
        s = 15 + 25 * t
        vwap.append((x, v))
        up1.append((x, v - s)); lo1.append((x, v + s))
        up2.append((x, v - 2 * s)); lo2.append((x, v + 2 * s))
        price.append((x, v - 30 * math.sin(t * 7.5) - 13 * math.sin(t * 19.0)))
    b += f'<polygon points="{pts(up2 + list(reversed(lo2)))}" class="d-zone2"/>'
    b += f'<polygon points="{pts(up1 + list(reversed(lo1)))}" class="d-zone"/>'
    b += f'<polyline points="{pts(price)}" class="d-px" style="stroke-width:1.4"/>'
    b += f'<polyline points="{pts(vwap)}" class="d-hi"/>'
    b += txt(666, vwap[-1][1] + 4, "VWAP", "d-k")
    b += txt(666, up1[-1][1] + 4, "+1" + SIGMA, "d-s")
    b += txt(666, up2[-1][1] + 4, "+2" + SIGMA, "d-s")
    b += txt(666, lo1[-1][1] + 4, MINUS + "1" + SIGMA, "d-s")
    b += txt(60, 44, "above VWAP " + MDASH + " premium", "d-k2")
    b += txt(60, 272, "below VWAP " + MDASH + " discount", "d-k2")
    b += txt(40, 300, "VWAP is the average price weighted by volume since the session anchor. The bands widen as "
                      "the session's", "d-s")
    b += txt(40, 318, "dispersion grows, so they measure how far from consensus price has travelled " + MDASH +
                      " not where it goes next.", "d-s")
    svg("vwap-bands", w, h, "VWAP with standard-deviation bands",
        "A price line oscillating around a volume-weighted average price, with one and two standard "
        "deviation bands widening through the session.", b)


def d_footprint_delta() -> None:
    w, h = 720, 348
    b = frame(w, h)
    cols = [[(12, 40), (34, 61), (88, 52), (41, 30)],
            [(22, 18), (96, 31), (57, 44), (19, 26)],
            [(9, 55), (28, 92), (44, 60), (33, 21)]]
    x0, cw, rh, y0 = 190, 158, 46, 78
    b += txt(40, 34, "One bar, opened up: what traded at each price", "d-t")
    b += txt(190, 62, "bid " + TIMES + " ask, price by price", "d-s")
    for ci, col in enumerate(cols):
        cx = x0 + ci * cw
        for ri, (bid, ask) in enumerate(col):
            y = y0 + ri * rh
            imb = ask >= 2.5 * bid or bid >= 2.5 * ask
            if imb:
                fill = ACC if ask > bid else ACC2
                b += f'<rect x="{cx}" y="{y}" width="{cw - 22}" height="{rh - 8}" rx="4" fill="{fill}" opacity=".2"/>'
            b += f'<rect x="{cx}" y="{y}" width="{cw - 22}" height="{rh - 8}" rx="4" fill="none" stroke="{LINE}"/>'
            b += txt(cx + 46, y + 25, str(bid), "d-s", "end")
            b += txt(cx + 54, y + 25, TIMES, "d-s")
            b += txt(cx + 74, y + 25, str(ask), "d-n" if imb else "d-s")
        d = sum(a - bd for bd, a in col)
        b += txt(cx + (cw - 22) / 2, y0 + 4 * rh + 24, f"delta {d:+d}", "d-k" if d > 0 else "d-k2", "middle")
    for i, line in enumerate(["Bid volume is what", "sellers hit; ask volume", "is what buyers lifted."]):
        b += txt(40, 96 + i * 18, line, "d-s")
    for i, line in enumerate(["A shaded cell is an", "imbalance: one side far", "outweighed the other."]):
        b += txt(40, 176 + i * 18, line, "d-s")
    b += txt(40, 314, "Delta is the running difference. It records who was more aggressive " + MDASH +
                      " a statement about what", "d-s")
    b += txt(40, 332, "already happened, not a forecast of the next bar.", "d-s")
    svg("footprint-delta", w, h, "Footprint cells showing bid, ask and delta",
        "Three bars broken into price rows showing volume traded at the bid and at the ask, with "
        "imbalanced cells shaded and a delta total beneath each bar.", b)


def d_auction_rotation() -> None:
    w, h = 720, 344
    b = frame(w, h) + arrow_defs()
    vy0, vy1 = 122, 198
    b += f'<rect x="40" y="{vy0}" width="652" height="{vy1 - vy0}" class="d-zone"/>'
    b += f'<line x1="40" y1="{vy0}" x2="692" y2="{vy0}" class="d-dash"/>'
    b += f'<line x1="40" y1="{vy1}" x2="692" y2="{vy1}" class="d-dash"/>'
    path = [(48, 178), (100, 134), (150, 96), (198, 142), (250, 184), (300, 224),
            (350, 180), (402, 140), (452, 154), (506, 98), (558, 68), (612, 110), (668, 152)]
    b += f'<polyline points="{pts(path)}" class="d-px"/>'
    for x, y, lab, cls in [(150, 96, "rejected", "d-k2"), (300, 224, "rejected", "d-k2"),
                           (558, 68, "accepted", "d-k")]:
        col = ACC if cls == "d-k" else ACC2
        b += f'<circle cx="{x}" cy="{y}" r="4" fill="{col}"/>'
        b += txt(x, y - 12 if y < 150 else y + 21, lab, cls, "middle")
    b += txt(46, vy0 - 10, "value area", "d-k")
    b += txt(40, 278, "The market is a two-way auction. It probes higher looking for sellers and lower looking "
                      "for buyers,", "d-s")
    b += txt(40, 296, "then returns to the area where trade is easiest. A probe that finds no business is "
                      "rejected quickly.", "d-s")
    b += txt(40, 322, "When price stays out there and volume follows it, the probe was accepted " + MDASH +
                      " and value moves with it.", "d-k")
    svg("auction-rotation", w, h, "Auction rotation: rejection and acceptance around the value area",
        "Price rotating around a shaded value area, probing above and below; two probes are rejected "
        "quickly and a third is accepted.", b)


def d_expectancy() -> None:
    w, h = 720, 336
    b = frame(w, h)
    bars = [(MINUS + "1R", 60, ACC2), ("+1R", 18, ACC), ("+2R", 12, ACC), ("+3R", 10, ACC)]
    x0, bw, gap, base = 80, 76, 40, 236
    b += txt(40, 34, "A 40% win rate that still makes money", "d-t")
    b += txt(40, 60, "Outcome of 100 trades, measured in R", "d-s")
    for i, (lab, pct, col) in enumerate(bars):
        x = x0 + i * (bw + gap)
        ht = pct * 2.3
        b += f'<rect x="{x}" y="{base - ht:.0f}" width="{bw}" height="{ht:.0f}" rx="3" fill="{col}"/>'
        b += txt(x + bw / 2, base - ht - 8, f"{pct}%", "d-n", "middle")
        b += txt(x + bw / 2, base + 21, lab, "d-t", "middle")
    b += f'<line x1="64" y1="{base}" x2="486" y2="{base}" class="d-ax"/>'
    b += txt(516, 96, "40 winners, 60 losers.", "d-t")
    b += txt(516, 126, "(0.18" + TIMES + "1) + (0.12" + TIMES + "2) + (0.10" + TIMES + "3)", "d-s")
    b += txt(516, 144, MINUS + " (0.60" + TIMES + "1)", "d-s")
    b += f'<line x1="516" y1="156" x2="686" y2="156" stroke="{LINE}"/>'
    b += txt(516, 178, "= +0.12R per trade", "d-k")
    for i, line in enumerate(["Losing six times in ten", "and still gaining, because", "the winners are bigger."]):
        b += txt(516, 208 + i * 18, line, "d-s")
    b += txt(40, 288, "Expectancy, not win rate, decides whether a method survives. A 70% win rate with one "
                      "large loss in", "d-s")
    b += txt(40, 306, "the tail is a losing system, and it feels like a winning one right up until it is not.", "d-s")
    b += txt(40, 328, "Illustrative arithmetic. It is not a result from any tested method.", "d-s")
    svg("expectancy", w, h, "Expectancy from a distribution of R multiples",
        "A bar chart of trade outcomes in R multiples where losers outnumber winners, with the "
        "expectancy arithmetic beside it showing a positive result per trade.", b)


def d_ohlc_compression() -> None:
    w, h = 720, 330
    b = frame(w, h) + arrow_defs()
    ticks = [(70, 186), (84, 206), (100, 178), (118, 150), (132, 162), (148, 122),
             (164, 140), (180, 108), (196, 132), (212, 100), (228, 128), (244, 160),
             (258, 144), (274, 176), (288, 158), (302, 168)]
    b += txt(40, 34, "Everything that happened", "d-t")
    b += txt(40, 56, "in one period", "d-s")
    b += f'<polyline points="{pts(ticks)}" class="d-px" style="stroke-width:1.2;opacity:.75"/>'
    for x, y in ticks:
        b += f'<circle cx="{x}" cy="{y}" r="2.6" fill="{MUTED}"/>'
    o, hi, lo, cl = ticks[0][1], 100, 206, ticks[-1][1]
    b += f'<line x1="330" y1="150" x2="392" y2="150" stroke="{ACC}" stroke-width="2" marker-end="url(#ar)"/>'
    b += txt(361, 140, "becomes", "d-k", "middle")
    cx = 470
    b += f'<line x1="{cx}" y1="{hi}" x2="{cx}" y2="{lo}" stroke="{FG}" stroke-width="1.6"/>'
    b += f'<rect x="{cx - 18}" y="{min(o, cl)}" width="36" height="{abs(o - cl)}" class="d-up"/>'
    for y, lab in [(hi, "high"), (cl, "close"), (o, "open"), (lo, "low")]:
        b += f'<line x1="{cx + 20}" y1="{y}" x2="{cx + 56}" y2="{y}" class="d-grid"/>'
        b += txt(cx + 62, y + 4, lab, "d-s")
    b += txt(cx, 78, "one bar", "d-t", "middle")
    b += txt(40, 240, "Gone, and not recoverable from the chart: the order the ticks arrived in, how much "
                      "traded at each", "d-s")
    b += txt(40, 258, "price, whether one large participant or ten thousand small ones, and whether the high "
                      "came before", "d-s")
    b += txt(40, 276, "the low or after.", "d-s")
    b += txt(40, 306, "The longer the bar, the more it discards. A monthly candle is four numbers standing in "
                      "for a month.", "d-k")
    svg("ohlc-compression", w, h, "What a bar keeps and what it discards",
        "A path of individual trades inside one period, collapsed into a single candle whose four "
        "prices are the only surviving record.", b)


def _mini(x0, y0, pw, ph, path, marks, title, note):
    s = txt(x0 + pw / 2, y0 - 12, title, "d-t", "middle")
    s += f'<line x1="{x0}" y1="{y0 + ph}" x2="{x0 + pw}" y2="{y0 + ph}" class="d-ax"/>'
    seq = [(x0 + fx * pw, y0 + fy * ph) for fx, fy in path]
    s += f'<polyline points="{pts(seq)}" class="d-px"/>'
    for fx, fy, lab, up in marks:
        x, y = x0 + fx * pw, y0 + fy * ph
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{ACC}"/>'
        s += txt(x, y - 9 if up else y + 17, lab, "d-k", "middle")
    s += txt(x0 + pw / 2, y0 + ph + 26, note, "d-s", "middle")
    return s


def d_chart_patterns() -> None:
    w, h = 720, 300
    b = frame(w, h)
    b += txt(40, 32, "Three patterns, and the structure each one actually is", "d-t")
    pw, ph, y0 = 186, 120, 74
    b += _mini(48, y0, pw, ph, [(0, 1.0), (0.2, 0.15), (0.38, 0.62), (0.56, 0.17), (0.78, 0.72), (1, 0.95)],
               [(0.2, 0.15, "H", True), (0.56, 0.17, "H", True)],
               "Double top", "a failure to make a higher high")
    b += _mini(266, y0, pw, ph, [(0, 1.0), (0.14, 0.42), (0.26, 0.68), (0.44, 0.06), (0.6, 0.66),
                                 (0.76, 0.38), (1, 0.92)],
               [(0.44, 0.06, "head", True), (0.14, 0.42, "S", True), (0.76, 0.38, "S", True)],
               "Head and shoulders", "the same failure, one peak later")
    b += _mini(484, y0, pw, ph, [(0, 0.86), (0.16, 0.16), (0.3, 0.62), (0.46, 0.18), (0.6, 0.44),
                                 (0.76, 0.17), (0.88, 0.32), (1, 0.05)],
               [(0.3, 0.62, "HL", False), (0.6, 0.44, "HL", False)],
               "Ascending triangle", "a range with rising lows")
    b += f'<line x1="484" y1="{y0 + 0.14 * ph:.0f}" x2="670" y2="{y0 + 0.14 * ph:.0f}" class="d-dash"/>'
    b += txt(40, 254, "None of these is a new idea. Each is the swing structure from stage 3, seen from "
                      "a little further back " + MDASH, "d-s")
    b += txt(40, 272, "which is why you can read one that nobody has given a name to.", "d-k")
    svg("chart-patterns", w, h, "Three classical chart patterns read as swing structure",
        "A double top, a head and shoulders and an ascending triangle, each annotated with the swing "
        "highs and lows that produce it.", b)


DIAGRAMS = [d_volume_profile, d_vwap_bands, d_footprint_delta, d_auction_rotation, d_expectancy,
            d_ohlc_compression, d_chart_patterns]


def main() -> None:
    mk.OUT.mkdir(parents=True, exist_ok=True)
    for fn in DIAGRAMS:
        fn()
    print(f"wrote {len(DIAGRAMS)} course diagrams to content/diagrams/")
    for fn in DIAGRAMS:
        print("  " + fn.__name__.replace("d_", "").replace("_", "-") + ".svg")


if __name__ == "__main__":
    main()
