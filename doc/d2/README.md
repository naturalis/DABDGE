Day 2: Retrieval, annotation and integration
============================================

**Thursday 24 September 2026, 8 h of practicals.** Two submissions come out of today:
**Q2 by end of day** and **Q3 drafted in class and submitted by end of day Friday**.

Yesterday you were shown records. Today you go and get them, find out how much of what you need is
actually in them, annotate a table yourself, establish that a specimen described in four resources
is the same specimen, and then leave behind a folder that somebody else could use.

It is a long day, so it is broken into four blocks with breaks between them.

Each block marks steps as Core or Stretch. Stretch steps are optional. If you complete the Core
steps, you have completed the day. All material stays available afterwards if you want to come back
to the Stretch parts.

Practicals
----------

| | Block | Time | Minutes |
| --- | --- | --- | --- |
| | Setup and orientation | 09:00-09:15 | 15 |
| TP2.1 | [Sequence handling with Biopython](tp1/README.md) | 09:15-10:30 | 75 |
| | Break | 10:30-10:45 | |
| TP2.2 | [Retrieval and the metadata audit](tp2/README.md) | 10:45-12:35 | 110 |
| | Q2 written in class | 12:35-13:00 | 25 |
| | Lunch | 13:00-14:00 | |
| TP2.3 | [Annotation with standard vocabularies](tp3/README.md) | 14:00-15:15 | 75 |
| | Break | 15:15-15:30 | |
| TP2.4 | [Cross-database integration](tp4/README.md) | 15:30-17:10 | 100 |

### [TP2.1 Sequence handling with Biopython](tp1/README.md)

FASTA in and out, basic statistics, translation and marker filtering, then similarity reading from
a supplied hits table. This is the one Python block of the week; from TP2.2 onwards the work is in
R.

### [TP2.2 Retrieval and the metadata audit](tp2/README.md)

Pull a nucleotide record from NCBI and ENA at once and compare what each gives you, then an
occurrence record, and audit the metadata against what an analysis would actually need. The
**12:35-13:00** slot is protected writing time for **Q2**, not an extension of the practical.

### [TP2.3 Annotation with standard vocabularies](tp3/README.md)

Map a real sample table onto Darwin Core and find out that the difficulty is not filling fields in
but deciding what the fields mean, then read a GO term as a defined class and walk its subgraph.
Finish with a short GO identifier check against QuickGO.

### [TP2.4 Cross-database integration](tp4/README.md)

One specimen, described in several resources at once. Establish that they are the same thing, then
write down every way in which the resources disagree. The disagreements are the result. **Q3 is
drafted here**, finalised over the weekend.

Before you start
----------------

- R and RStudio, with `jsonlite`, `dplyr`, `readr` and `ggplot2` available
- the conda environment from the repository root, which provides Python, Biopython, Jupyter and BLAST
  (`conda env create -f environment.yml` and `conda activate dabdge`)
- the day 1 lecture notes to hand ([Lecture I](../d1/lecture1.md), [Lecture II](../d1/lecture2.md)),
  since the vocabulary is assumed rather than repeated

All retrieval today is over public APIs and no accounts are needed. If a service is slow or down,
say so early: there are cached copies of every record used here, and it is better to work from those
than to spend the block watching a spinner.
