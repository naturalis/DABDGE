#!/usr/bin/env python3
"""
Figures for the DABDGE week 2 lectures.

Writes SVG masters and PNG exports into doc/d1/lecture1/ and doc/d1/lecture2/.

Palette follows the MBCMA "from molecules to ecosystems" axis: molecular green at
one end, environmental blue at the other, so position on that axis carries meaning
rather than decorating. Amber is used once per figure, for the one thing the slide
is actually about.
"""

import math
import os
import cairosvg

INK = "#17262E"
MUTED = "#5C7079"
RULE = "#C3D0D6"
PAPER = "#F2F6F7"
GREEN = "#2E7D4F"
BLUE = "#1B6E93"
AMBER = "#C2711C"

SANS = "IBM Plex Sans, Source Sans Pro, DejaVu Sans, Helvetica, Arial, sans-serif"
MONO = "IBM Plex Mono, DejaVu Sans Mono, Menlo, monospace"

OUT1 = "/mnt/user-data/outputs/lecture1"
OUT2 = "/mnt/user-data/outputs/lecture2"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def txt(x, y, s, size=15, fill=INK, weight="400", anchor="start", family=SANS,
        style="normal", spacing="0"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" '
            f'font-style="{style}" letter-spacing="{spacing}">{esc(s)}</text>')


def box(x, y, w, h, fill="none", stroke=RULE, sw=1.2, rx=2):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(x1, y1, x2, y2, stroke=RULE, sw=1.2, dash=None, marker=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#arrow)"' if marker else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}{m}/>')


def path(d, stroke=RULE, sw=1.2, fill="none", marker=False, dash=None):
    m = ' marker-end="url(#arrow)"' if marker else ""
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"'
            f'{m}{da}/>')


def header(w, h, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">'
            f'<defs>'
            f'<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 0 1 L 9 5 L 0 9 z" fill="{MUTED}"/></marker>'
            f'<marker id="arrowamber" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 0 1 L 9 5 L 0 9 z" fill="{AMBER}"/></marker>'
            f'{defs}</defs>'
            f'<rect width="{w}" height="{h}" fill="#FFFFFF"/>')


def caption(x, y, s, w=None):
    return txt(x, y, s, size=14, fill=MUTED, style="italic")


def write(name, svg, outdir):
    os.makedirs(outdir, exist_ok=True)
    svg_path = os.path.join(outdir, name + ".svg")
    png_path = os.path.join(outdir, name + ".png")
    with open(svg_path, "w") as fh:
        fh.write(svg)
    cairosvg.svg2png(url=svg_path, write_to=png_path, scale=2.0)
    print("wrote", svg_path, "and", png_path)


# ---------------------------------------------------------------- figure 1
def lifecycle_arc():
    W, H = 1240, 400
    grad = (f'<linearGradient id="arc" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0%" stop-color="{GREEN}"/>'
            f'<stop offset="100%" stop-color="{BLUE}"/></linearGradient>')
    s = [header(W, H, grad)]
    s.append(txt(40, 52, "Four weeks, one arc", size=24, weight="600"))
    s.append(txt(40, 78, "Each week opens a different part of the life of a dataset.",
                 size=15, fill=MUTED))

    weeks = [
        ("Week 1", "Generation and deposit", "Pedro, with Giorgio",
         ["Where do biological", "data come from, and", "where do they go?"], GREEN),
        ("Week 2", "Architecture and FAIR", "Rutger",
         ["How is a record", "structured, made", "interoperable, and used?"], "#256B70"),
        ("Week 3", "Analysis and inference", "Pedro",
         ["How do we extract", "biological meaning", "from these data?"], "#20718A"),
        ("Week 4", "Application and integration", "Filipe",
         ["How does this come", "together in a real", "biodiversity question?"], BLUE),
    ]

    x0, gap, top = 40, 18, 116
    bw = (W - 2 * x0 - 3 * gap) / 4
    bh = 196
    for i, (wk, title, who, q, col) in enumerate(weeks):
        x = x0 + i * (bw + gap)
        here = (i == 1)
        s.append(box(x, top, bw, bh, fill=PAPER if here else "none",
                     stroke=AMBER if here else RULE, sw=1.8 if here else 1.2))
        s.append(f'<rect x="{x}" y="{top}" width="{bw}" height="5" fill="{col}"/>')
        s.append(txt(x + 18, top + 38, wk, size=13, fill=MUTED, weight="600"))
        s.append(txt(x + 18, top + 66, title.split(" and ")[0] + " and", size=17,
                     weight="600", fill=INK))
        s.append(txt(x + 18, top + 88, title.split(" and ")[1], size=17,
                     weight="600", fill=INK))
        s.append(txt(x + 18, top + 112, who, size=13, fill=col, weight="600"))
        for j, ln in enumerate(q):
            s.append(txt(x + 18, top + 140 + j * 18, ln, size=13, fill=MUTED))
        if i < 3:
            s.append(line(x + bw + 3, top + bh / 2, x + bw + gap - 4, top + bh / 2,
                          stroke=MUTED, marker=True))
    s.append(txt(x0, top + bh + 42,
                 "You are here. Last week the records were made; next week they are "
                 "computed on. This week we open them.",
                 size=15, fill=AMBER))
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- figure 2
def sample_vs_feature():
    W, H = 1240, 600
    s = [header(W, H)]
    s.append(txt(40, 52, "Two table shapes, one link", size=24, weight="600"))
    s.append(txt(40, 78,
                 "A sample sheet describes the samples. A feature table counts things "
                 "in them. Nothing else connects the two.",
                 size=15, fill=MUTED))

    # sample sheet
    sx, sy = 40, 122
    cols = [("sampleID", 130), ("site", 118), ("eventDate", 110), ("oiled", 70)]
    rows = [("DI-BP-05", "Bayfront Park", "2010-05-12", "no"),
            ("DI-BP-09", "Bayfront Park", "2010-09-14", "yes"),
            ("DI-RC-05", "Ryan Court", "2010-05-12", "no"),
            ("GI-GI-09", "Grand Isle", "2010-09-21", "yes")]
    sw_ = sum(c[1] for c in cols)
    s.append(txt(sx, sy - 14, "Sample sheet", size=15, weight="600", fill=GREEN))
    s.append(txt(sx + 128, sy - 14, "one row per sample", size=13, fill=MUTED))
    s.append(box(sx, sy, sw_, 30 + 30 * len(rows), fill=PAPER, stroke=RULE))
    cx = sx
    for name, cw in cols:
        key = name == "sampleID"
        s.append(txt(cx + 12, sy + 20, name, size=13, weight="600",
                     fill=AMBER if key else MUTED, family=MONO))
        cx += cw
    s.append(line(sx, sy + 30, sx + sw_, sy + 30, stroke=RULE))
    for r, row in enumerate(rows):
        ry = sy + 30 + r * 30
        cx = sx
        for c, (name, cw) in enumerate(cols):
            key = c == 0
            s.append(txt(cx + 12, ry + 20, row[c], size=13, family=MONO,
                         fill=AMBER if key else INK, weight="600" if key else "400"))
            cx += cw
        if r:
            s.append(line(sx, ry, sx + sw_, ry, stroke="#E2EAED"))
    s.append(f'<rect x="{sx}" y="{sy}" width="{cols[0][1]}" '
             f'height="{30 + 30 * len(rows)}" fill="none" stroke="{AMBER}" '
             f'stroke-width="1.8"/>')

    # feature table
    fx, fy = 700, 122
    fcols = ["featureID", "DI-BP-05", "DI-BP-09", "DI-RC-05", "GI-GI-09"]
    fwid = [140, 90, 90, 90, 90]
    frows = [("ASV_0001", "412", "3", "388", "0"),
             ("ASV_0002", "7", "1204", "12", "2871"),
             ("ASV_0003", "96", "44", "121", "18"),
             ("ASV_0004", "0", "271", "5", "402")]
    fw_ = sum(fwid)
    s.append(txt(fx, fy - 14, "Feature table", size=15, weight="600", fill=BLUE))
    s.append(txt(fx + 128, fy - 14, "one row per ASV, one column per sample",
                 size=13, fill=MUTED))
    s.append(box(fx, fy, fw_, 30 + 30 * len(frows), fill=PAPER, stroke=RULE))
    cx = fx
    for i, name in enumerate(fcols):
        s.append(txt(cx + 10, fy + 20, name, size=13, weight="600",
                     fill=AMBER if i else MUTED, family=MONO))
        cx += fwid[i]
    s.append(line(fx, fy + 30, fx + fw_, fy + 30, stroke=RULE))
    for r, row in enumerate(frows):
        ry = fy + 30 + r * 30
        cx = fx
        for c in range(len(fcols)):
            s.append(txt(cx + 10, ry + 20, row[c], size=13, family=MONO, fill=INK))
            cx += fwid[c]
        if r:
            s.append(line(fx, ry, fx + fw_, ry, stroke="#E2EAED"))
    s.append(f'<rect x="{fx + fwid[0]}" y="{fy}" width="{fw_ - fwid[0]}" height="30" '
             f'fill="none" stroke="{AMBER}" stroke-width="1.8"/>')

    # the link, routed through the empty gap rather than across the tables
    s.append(line(sx + 12, sy + 30 + 30 * len(rows) + 14, sx + cols[0][1] - 12,
                  sy + 30 + 30 * len(rows) + 14, stroke=AMBER, sw=2))
    s.append(txt(sx + cols[0][1] / 2, sy + 30 + 30 * len(rows) + 34, "keys",
                 size=13, weight="600", fill=AMBER, anchor="middle"))
    ly = sy + 30 + 30 * len(rows) + 92
    s.append(path(f"M {sx + cols[0][1] / 2} {sy + 30 + 30 * len(rows) + 44} "
                  f"L {sx + cols[0][1] / 2} {ly} L {fx - 62} {ly} "
                  f"L {fx - 62} {fy + 15} L {fx - 8} {fy + 15}",
                  stroke=AMBER, sw=1.6, marker=True))
    s.append(txt(sx + cols[0][1] / 2 + 24, ly - 10,
                 "the same strings, or the join is silently wrong",
                 size=13, fill=AMBER))

    s.append(txt(40, 430,
                 "The sample identifiers in the sheet must match the column names in "
                 "the table, exactly.",
                 size=17, weight="600", fill=INK))
    s.append(txt(40, 458,
                 "When they do not, nothing errors. You get answers about the wrong "
                 "samples.",
                 size=17, weight="600", fill=AMBER))
    s.append(txt(40, 508,
                 "Add a tree whose tips are the feature identifiers and a taxonomy "
                 "table keyed the same way, and you have a phyloseq object. A "
                 "phylogenetic",
                 size=15, fill=MUTED))
    s.append(txt(40, 530,
                 "diversity measure such as UniFrac is a join across all four before "
                 "it is a statistic.",
                 size=15, fill=MUTED))
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- figure 3
def data_life_cycle():
    W, H = 1240, 700
    s = [header(W, H)]
    s.append(txt(40, 52, "The data life cycle", size=24, weight="600"))
    s.append(txt(40, 78,
                 "Analysis is the visible part and the shortest. The decisions that "
                 "make reuse possible are taken before any data exist.",
                 size=15, fill=MUTED))

    cx, cy, r = 600, 390, 175
    stages = [
        ("Plan", ["what will be measured,", "and what travels with it"], GREEN),
        ("Collect", ["specimens, reads,", "images, sensor streams"], GREEN),
        ("Process", ["cleaning and filtering;", "each step is a claim"], "#2A7568"),
        ("Analyse", ["the visible part,", "and the shortest"], "#246F85"),
        ("Preserve", ["deposit, with", "identifiers"], BLUE),
        ("Reuse", ["by you in six months, by", "someone else in ten years"], BLUE),
    ]
    n = len(stages)
    pts = []
    for i in range(n):
        a = -math.pi / 2 + i * 2 * math.pi / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a), a))

    for i in range(n):
        _, _, a1 = pts[i]
        _, _, a2 = pts[(i + 1) % n]
        a1o, a2o = a1 + 0.32, a2 - 0.32
        sx_, sy_ = cx + r * math.cos(a1o), cy + r * math.sin(a1o)
        ex, ey = cx + r * math.cos(a2o), cy + r * math.sin(a2o)
        s.append(path(f"M {sx_:.1f} {sy_:.1f} A {r} {r} 0 0 1 {ex:.1f} {ey:.1f}",
                      stroke=MUTED, sw=1.3, marker=True))

    for i, (name, sub, col) in enumerate(stages):
        x, y, a = pts[i]
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="27" fill="{PAPER}" '
                 f'stroke="{col}" stroke-width="2"/>')
        s.append(txt(x, y + 6, str(i + 1), size=17, weight="600", fill=col,
                     anchor="middle"))
        if abs(math.cos(a)) < 0.3:                      # top or bottom
            if math.sin(a) < 0:                         # top
                ty0 = y - 88
            else:                                       # bottom
                ty0 = y + 54
            s.append(txt(x, ty0, name, size=17, weight="600", fill=col,
                         anchor="middle"))
            for j, ln in enumerate(sub):
                s.append(txt(x, ty0 + 22 + j * 18, ln, size=13, fill=MUTED,
                             anchor="middle"))
        else:
            right = math.cos(a) > 0
            lx = x + (46 if right else -46)
            anchor = "start" if right else "end"
            s.append(txt(lx, y - 8, name, size=17, weight="600", fill=col,
                         anchor=anchor))
            for j, ln in enumerate(sub):
                s.append(txt(lx, y + 14 + j * 18, ln, size=13, fill=MUTED,
                             anchor=anchor))

    s.append(txt(cx, cy - 8, "every dataset", size=15, fill=MUTED, anchor="middle"))
    s.append(txt(cx, cy + 14, "you will meet", size=15, fill=MUTED, anchor="middle"))

    s.append(box(40, 560, 330, 112, fill="none", stroke=AMBER, sw=1.5))
    s.append(txt(60, 592, "Metadata that was never recorded", size=14, fill=AMBER))
    s.append(txt(60, 614, "at step 1 cannot be recovered at", size=14, fill=AMBER))
    s.append(txt(60, 636, "step 6.", size=14, fill=AMBER, weight="600"))
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- figure 4
def serialisations():
    W, H = 1240, 620
    s = [header(W, H)]
    s.append(txt(40, 52, "One tree, four serialisations", size=24, weight="600"))
    s.append(txt(40, 78,
                 "Choosing a format is choosing what you are willing to lose.",
                 size=15, fill=MUTED))

    # the tree, drawn once
    bx, by = 40, 120
    s.append(box(bx, by, 250, 214, fill=PAPER, stroke=RULE))
    tx, ty = bx + 50, by + 40
    tips = [("A", ty + 10), ("B", ty + 50), ("C", ty + 100), ("D", ty + 140)]
    for lbl, y in tips:
        s.append(line(tx + 80, y, tx + 120, y, stroke=INK, sw=1.6))
        s.append(txt(tx + 130, y + 5, lbl, size=15, weight="600", family=MONO))
    s.append(line(tx + 80, ty + 10, tx + 80, ty + 50, stroke=INK, sw=1.6))
    s.append(line(tx + 80, ty + 100, tx + 80, ty + 140, stroke=INK, sw=1.6))
    s.append(line(tx + 40, ty + 30, tx + 80, ty + 30, stroke=INK, sw=1.6))
    s.append(line(tx + 40, ty + 120, tx + 80, ty + 120, stroke=INK, sw=1.6))
    s.append(line(tx + 40, ty + 30, tx + 40, ty + 120, stroke=INK, sw=1.6))
    s.append(line(tx, ty + 75, tx + 40, ty + 75, stroke=INK, sw=1.6))
    s.append(txt(bx + 16, by + 24, "the tree", size=14, weight="600", fill=MUTED))

    panels = [
        ("Newick", ["((A,B),(C,D));"],
         ["topology, branch lengths"], ["provenance, support,", "identifiers"], GREEN),
        ("NEXUS", ["BEGIN TREES;", "  TREE t1 = ((A,B),(C,D));", "END;"],
         ["data and trees together"], ["agreement on what a", "block means"], "#2A7568"),
        ("NeXML / PhyloXML", ["<tree id=\"t1\">", "  <node id=\"n1\" otu=\"A\"/>",
                              "  <meta rel=\"dc:source\" .../>"],
         ["metadata, external links"], ["readers, in practice"], "#246F85"),
        ("Table", ["node parent label", "1     3      A", "2     3      B"],
         ["joins with everything else"], ["the shape, unless you", "rebuild it"], BLUE),
    ]
    px, pw, gap = 320, 214, 16
    for i, (name, code, carries, loses, col) in enumerate(panels):
        x = px + i * (pw + gap)
        s.append(box(x, by, pw, 214, fill="none", stroke=RULE))
        s.append(f'<rect x="{x}" y="{by}" width="{pw}" height="4" fill="{col}"/>')
        s.append(txt(x + 14, by + 32, name, size=15, weight="600", fill=col))
        for j, ln in enumerate(code):
            s.append(txt(x + 14, by + 60 + j * 19, ln, size=11.5, family=MONO,
                         fill=INK))
        s.append(txt(x + 14, by + 134, "carries", size=11, fill=MUTED, weight="600"))
        for j, ln in enumerate(carries):
            s.append(txt(x + 14, by + 151 + j * 17, ln, size=11.5, fill=INK))
        s.append(txt(x + 14, by + 176, "loses", size=11, fill=MUTED, weight="600"))
        for j, ln in enumerate(loses):
            s.append(txt(x + 14, by + 193 + j * 17, ln, size=11.5, fill=AMBER))

    s.append(txt(40, 396,
                 "The same information, in four containers with different capacities.",
                 size=17, weight="600"))
    s.append(txt(40, 424,
                 "Newick cannot carry the provenance of the tree. NeXML can, and "
                 "almost nobody reads it. Neither fact settles which to use.",
                 size=15, fill=MUTED))

    s.append(box(40, 458, 1160, 124, fill=PAPER, stroke=RULE))
    s.append(txt(60, 488, "A hierarchy is a table where each row names its parent",
                 size=15, weight="600", fill=BLUE))
    s.append(txt(60, 514,
                 "Once it is a table it is queryable with the same tools as "
                 "everything else, and you can pre-compute columns that turn "
                 "expensive",
                 size=14, fill=MUTED))
    s.append(txt(60, 536,
                 "traversals into cheap range queries. This is how very large "
                 "phylogenies are served.",
                 size=14, fill=MUTED))
    s.append(txt(60, 564,
                 "So which is the real tree: the string, the document, or the table? "
                 "Your answer decides where you look for the metadata.",
                 size=14, fill=AMBER))
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- figure 5
def occurrence_record():
    W, H = 1240, 600
    s = [header(W, H)]
    s.append(txt(40, 52, "Anatomy of an occurrence record", size=24, weight="600"))
    s.append(txt(40, 78,
                 "One assertion: this taxon was here, at this time, and somebody says "
                 "so. Darwin Core gives every part of it an agreed name.",
                 size=15, fill=MUTED))

    rx, ry, rw = 40, 118, 700
    fields = [
        ("occurrenceID", "URN:catalog:UMB:MOL:88412", "identifier", GREEN, True),
        ("basisOfRecord", "MaterialSample", "evidence", GREEN, True),
        ("materialSampleID", "DI-BP-09", "evidence", GREEN, False),
        ("scientificName", "Cladosporium cladosporioides", "what", "#2A7568", True),
        ("identifiedBy", "J. Sharma", "what", "#2A7568", False),
        ("decimalLatitude", "30.2481", "where", "#246F85", True),
        ("decimalLongitude", "-88.0759", "where", "#246F85", False),
        ("coordinateUncertaintyInMeters", "(empty)", "where", "#246F85", False),
        ("eventDate", "2010-09-14", "when", BLUE, True),
        ("recordedBy", "H. M. Bik", "who", BLUE, True),
    ]
    rh = 34
    s.append(box(rx, ry, rw, rh * len(fields) + 16, fill=PAPER, stroke=RULE))
    groups = {}
    for i, (k, v, grp, col, first) in enumerate(fields):
        y = ry + 12 + i * rh
        empty = v == "(empty)"
        s.append(txt(rx + 20, y + 22, k, size=13.5, family=MONO,
                     fill=AMBER if empty else MUTED))
        s.append(txt(rx + 300, y + 22, v, size=13.5, family=MONO,
                     fill=AMBER if empty else INK,
                     weight="600" if not empty else "400"))
        if i:
            s.append(line(rx + 14, y, rx + rw - 14, y, stroke="#E2EAED"))
        groups.setdefault(grp, [col, y, y])
        groups[grp][2] = y + rh

    gx = rx + rw + 26
    for grp, (col, y0, y1) in groups.items():
        s.append(line(gx, y0 + 6, gx, y1 - 2, stroke=col, sw=2.5))
        s.append(txt(gx + 12, (y0 + y1) / 2 + 5, grp, size=15, weight="600", fill=col))

    s.append(box(900, 118, 300, 150, fill="none", stroke=AMBER, sw=1.5))
    s.append(txt(918, 148, "The field everyone omits", size=14, weight="600",
                 fill=AMBER))
    s.append(txt(918, 174, "Six decimal places of latitude", size=13, fill=MUTED))
    s.append(txt(918, 193, "and no stated uncertainty. The", size=13, fill=MUTED))
    s.append(txt(918, 212, "record looks precise to a metre", size=13, fill=MUTED))
    s.append(txt(918, 231, "and may be accurate to a", size=13, fill=MUTED))
    s.append(txt(918, 250, "province.", size=13, fill=MUTED))

    s.append(box(900, 292, 300, 174, fill=PAPER, stroke=RULE))
    s.append(txt(918, 322, "Ask first", size=14, weight="600", fill=BLUE))
    for j, ln in enumerate([
        "What is each row one of?",
        "What evidence stands behind it?",
        "How well is 'where' known?",
        "Who made the determination,",
        "and when?",
        "What can it be joined to?",
    ]):
        s.append(txt(918, 350 + j * 19, ln, size=13, fill=MUTED))

    s.append(txt(40, 540,
                 "Aggregation across thousands of publishers is possible only because "
                 "they all use these names. That is the whole argument for "
                 "vocabularies.",
                 size=15, fill=AMBER))
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- figure 6
def sampling_bias():
    W, H = 1240, 580
    s = [header(W, H)]
    s.append(txt(40, 52, "A map of where people looked", size=24, weight="600"))
    s.append(txt(40, 78,
                 "Aggregated occurrence data are two maps multiplied together. Only "
                 "one of them is about the organisms.",
                 size=15, fill=MUTED))

    pw, ph, py = 340, 300, 140
    xs = [40, 450, 860]

    def lcg(seed, n):
        vals, v = [], seed
        for _ in range(n * 2):
            v = (1103515245 * v + 12345) % (2 ** 31)
            vals.append(v / (2 ** 31))
        return vals

    def bez(x, y, t):
        p0 = (x + 20, y + 250)
        p1 = (x + 110, y + 215)
        p2 = (x + 150, y + 120)
        p3 = (x + 300, y + 60)
        u = 1 - t
        bx = (u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0]
              + t ** 3 * p3[0])
        by = (u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1]
              + t ** 3 * p3[1])
        return bx, by

    def coast(x, y):
        p0 = (x + 20, y + 250)
        return path(f"M {p0[0]} {p0[1]} C {x + 110} {y + 215}, {x + 150} {y + 120}, "
                    f"{x + 300} {y + 60}", stroke="#9FC3D4", sw=6)

    def dist_coast(px_, py_, ox, oy):
        return min(math.hypot(px_ - bx, py_ - by)
                   for bx, by in (bez(ox, oy, i / 40) for i in range(41)))

    r = lcg(7, 110)
    pts = [(r[i * 2], r[i * 2 + 1]) for i in range(110)]

    def panel(x, title, col):
        return [box(x, py, pw, ph, fill=PAPER, stroke=RULE),
                txt(x, py - 12, title, size=15, weight="600", fill=col)]

    # panel 1: where the organisms are
    s += panel(xs[0], "Where the organisms are", GREEN)
    s.append(coast(xs[0], py))
    for u, v in pts:
        cx_ = xs[0] + 16 + u * (pw - 32)
        cy_ = py + 16 + v * (ph - 32)
        s.append(f'<circle cx="{cx_:.1f}" cy="{cy_:.1f}" r="3.1" fill="{GREEN}" '
                 f'fill-opacity="0.55"/>')

    # panel 2: where people looked
    s += panel(xs[1], "Where people looked", "#246F85")
    s.append(coast(xs[1], py))
    road_y0, road_dy = py + 92, 52
    s.append(line(xs[1] + 16, road_y0, xs[1] + pw - 16, road_y0 + road_dy,
                  stroke="#D9C9AC", sw=5))
    tx_, ty_ = xs[1] + 104, road_y0 + 14
    s.append(f'<circle cx="{tx_}" cy="{ty_}" r="17" fill="#E9DFCB"/>')
    s.append(txt(tx_, ty_ + 32, "town", size=11, fill=MUTED, anchor="middle"))
    effort = []
    for i, (u, v) in enumerate(pts):
        x_ = xs[1] + 16 + u * (pw - 32)
        y_ = py + 16 + v * (ph - 32)
        on_road = abs((y_ - road_y0) - (x_ - (xs[1] + 16)) * road_dy / (pw - 32)) < 22
        in_town = math.hypot(x_ - tx_, y_ - ty_) < 52
        on_coast = dist_coast(x_, y_, xs[1], py) < 26
        if on_road or in_town or on_coast or i % 19 == 0:
            effort.append((u, v))
            s.append(f'<circle cx="{x_:.1f}" cy="{y_:.1f}" r="3.1" fill="#246F85" '
                     f'fill-opacity="0.8"/>')

    # panel 3: what the data show
    s += panel(xs[2], "What the data show", BLUE)
    s.append(coast(xs[2], py))
    for u, v in effort:
        x_ = xs[2] + 16 + u * (pw - 32)
        y_ = py + 16 + v * (ph - 32)
        s.append(f'<circle cx="{x_:.1f}" cy="{y_:.1f}" r="3.1" fill="{BLUE}" '
                 f'fill-opacity="0.8"/>')

    s.append(box(xs[2], py + ph + 26, pw, 76, fill="none", stroke=AMBER, sw=1.5))
    s.append(txt(xs[2] + 18, py + ph + 54, "An empty quarter of this panel",
                 size=13, fill=AMBER))
    s.append(txt(xs[2] + 18, py + ph + 76, "means nobody went there.",
                 size=13, fill=AMBER, weight="600"))

    s.append(txt(40, py + ph + 54,
                 "Effort, taxonomic, temporal and digitisation biases do not make "
                 "the data unusable.",
                 size=15, fill=MUTED))
    s.append(txt(40, py + ph + 76,
                 "They make the data usable for some questions and not others.",
                 size=15, fill=MUTED))
    s.append("</svg>")
    return "".join(s)


# ---------------------------------------------------------------- figure 7
def go_subgraph():
    W, H = 1240, 620
    s = [header(W, H)]
    s.append(txt(40, 52, "The Gene Ontology is a graph, not a list",
                 size=24, weight="600"))
    s.append(txt(40, 78,
                 "Terms have stable identifiers, written definitions, and explicit "
                 "relations to each other. Annotation is inherited upwards.",
                 size=15, fill=MUTED))

    def term(x, y, w, gid, l1, l2, col=GREEN, hi=False):
        h = 64
        out = [box(x, y, w, h, fill=PAPER if hi else "#FFFFFF",
                   stroke=AMBER if hi else RULE, sw=2 if hi else 1.2)]
        out.append(f'<rect x="{x}" y="{y}" width="4" height="{h}" '
                   f'fill="{AMBER if hi else col}"/>')
        out.append(txt(x + 14, y + 24, l1, size=13, weight="600",
                       fill=AMBER if hi else INK))
        if l2:
            out.append(txt(x + 14, y + 41, l2, size=13, weight="600",
                           fill=AMBER if hi else INK))
        out.append(txt(x + 14, y + 57, gid, size=11.5, family=MONO, fill=MUTED))
        return out

    root_x, root_y, root_w = 380, 118, 300
    s += term(root_x, root_y, root_w, "GO:0003006",
              "developmental process", "involved in reproduction", "#2A7568")

    kids = [
        (40, "GO:0048438", "floral whorl", "development", False),
        (250, "GO:0010431", "seed maturation", "", False),
        (460, "GO:0010228", "vegetative to reproductive", "phase transition of meristem", True),
        (790, "GO:0048439", "flower morphogenesis", "", False),
    ]
    ky = 272
    for kx, gid, l1, l2, hi in kids:
        w = 300 if hi else 190
        s += term(kx, ky, w, gid, l1, l2, GREEN, hi)
        s.append(path(f"M {root_x + root_w / 2} {root_y + 64} "
                      f"C {root_x + root_w / 2} {ky - 40}, {kx + w / 2} {root_y + 110}, "
                      f"{kx + w / 2} {ky}",
                      stroke=AMBER if hi else MUTED, sw=1.6 if hi else 1.2,
                      marker=True))

    gkids = [(40, "GO:0048465", "corolla development", ""),
             (250, "GO:0048441", "petal development", "")]
    gy = 410
    for gx, gid, l1, l2 in gkids:
        s += term(gx, gy, 190, gid, l1, l2, GREEN)
        s.append(path(f"M {135} {ky + 64} C 135 {gy - 30}, {gx + 95} {ky + 110}, "
                      f"{gx + 95} {gy}", stroke=MUTED, sw=1.2, marker=True))

    s.append(box(830, 372, 370, 176, fill=PAPER, stroke=RULE))
    s.append(txt(850, 402, "Two consequences", size=15, weight="600", fill=BLUE))
    for j, ln in enumerate([
        "A gene annotated to a term is implicitly",
        "annotated to every ancestor of that term.",
        "So terms at different depths are not",
        "independent evidence in an enrichment test.",
        "",
        "Every annotation carries an evidence code.",
        "One without it is a rumour.",
    ]):
        s.append(txt(850, 430 + j * 19, ln, size=13,
                     fill=AMBER if j > 4 else MUTED))

    s.append(txt(40, 578,
                 "Edges are typed relations (is_a, part_of, regulates). Traversing and "
                 "pruning a subgraph is a graph operation, not a keyword lookup.",
                 size=14, fill=MUTED))
    s.append("</svg>")
    return "".join(s)


if __name__ == "__main__":
    write("lifecycle-arc", lifecycle_arc(), OUT1)
    write("sample-vs-feature", sample_vs_feature(), OUT1)
    write("data-life-cycle", data_life_cycle(), OUT1)
    write("serialisations", serialisations(), OUT1)
    write("occurrence-record", occurrence_record(), OUT2)
    write("sampling-bias", sampling_bias(), OUT2)
    write("go-subgraph", go_subgraph(), OUT2)
