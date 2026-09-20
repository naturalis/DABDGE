Scripts
=======

Two unrelated kinds of code live here: the script that draws the lecture figures, and reference
copies of the small scripts students write in the day 2 practicals.

Figures
-------

[`make_figures.py`](make_figures.py) writes every figure used in the two day 1 lectures, as an SVG
master plus a PNG export at twice nominal size. Run it from the repository root:

```bash
python3 scripts/make_figures.py
```

It needs [cairosvg](https://cairosvg.org/) for the PNG export, which is not in
[`environment.yml`](../environment.yml) because nothing else in the course requires it:

```bash
pip install cairosvg
```

The output directories are set in two constants at the top of the file. Check them before you run
it, then look at [doc/d1/lecture1](../doc/d1/lecture1/README.md) and
[doc/d1/lecture2](../doc/d1/lecture2/README.md) to see what was written and what each figure is for.
Every figure is regenerated on every run, so hand edits to an SVG do not survive. Edit the drawing
code instead.

Practical scripts
-----------------

These are the scripts written during [TP2.1](../doc/d2/tp1/README.md), kept here so that a broken
morning does not block the afternoon, and so that the packaging exercise in
[TP2.5](../doc/d2/tp5/README.md) has something to package.

| Script | What it does |
| ------ | ------------ |
| [`filter_marker.py`](filter_marker.py) | Selects records for one marker out of a multi-marker FASTA, by parsing the definition line. Usage: `filter_marker.py <input.fasta> <marker>`, writes FASTA to stdout. |
| [`summarise.py`](summarise.py) | Per-record length and GC fraction to stdout as TSV, with a count and a length summary to stderr. Usage: `summarise.py <input.fasta>`. |
| [`tp1_convert_alignment.py`](tp1_convert_alignment.py) | Reads an aligned FASTA, checks that the identifiers are unique and the lengths equal, and writes it out in another alignment format. Usage: `tp1_convert_alignment.py <input.fasta> <output> <format>`. |
| [`tp1_translate_frames.py`](tp1_translate_frames.py) | Translates the first record of a COI file in three reading frames under the invertebrate mitochondrial code and counts stop codons in each, which is how you find the frame that is actually coding. Input path is fixed inside the script; run it from your own working directory. |

A word on using these. The point of TP2.1 is the twenty minutes spent working out why the definition
line will not parse, so write your own first and compare afterwards. All of them assume the working
directory laid out at the start of TP2.1, with `data/`, `scripts/` and `out/` alongside each other,
which is also the layout TP2.5 asks you to deposit.

Everything here is released under the [MIT licence](../LICENSE). Pull requests are welcome,
including from students: the definition-line parsing in `filter_marker.py` is deliberately naive and
there is a better version of it waiting to be written.
