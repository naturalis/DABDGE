Day 2: Retrieval, annotation and integration
============================================

**Thursday 24 September 2026, 8 h of practicals.** Two submissions come out of today: **Q2 by end of
day**, and **Q3 drafted in class and submitted by end of day Friday**.

Yesterday you were shown records. Today you go and get them, find out how much of what you need is
actually in them, annotate a table yourself, establish that a specimen described in four resources
is the same specimen, and then leave behind a folder that somebody else could use.

It is a long day, so it is broken into five blocks with breaks between them. Everything you make
goes into one working directory, `~/dabdge-w2`, because the last hour packages it.

Practicals
----------

| | Practical | When | Submission |
| --- | --------- | ---- | ---------- |
| TP2.1 | [Sequence handling with Biopython](tp1/README.md) | 09:00-10:30 | none |
| TP2.2 | [Retrieval, and the metadata audit](tp2/README.md) | 10:45-13:00 | **Q2, end of day** |
| TP2.3 | [Annotation with standard vocabularies](tp3/README.md) | 14:00-15:30 | none |
| TP2.4 | [Cross-database integration](tp4/README.md) | 15:45-17:45 | **Q3 drafted** |
| TP2.5 | [Packaging](tp5/README.md) | 17:45-18:45 | none |

### [TP2.1 Sequence handling with Biopython](tp1/README.md)

FASTA in and out, basic statistics, translation and marker filtering, then BLAST-style similarity
intuition against a toy reference database. This is the one Python block of the week; from TP2.2
onwards the work is in R.

### [TP2.2 Retrieval, and the metadata audit](tp2/README.md)

Pull a nucleotide record from NCBI and ENA at once and compare what each gives you, then an
occurrence record and a barcode record, and audit the metadata against what an analysis would
actually need. **Submit Q2 by end of day.**

### [TP2.3 Annotation with standard vocabularies](tp3/README.md)

Map a real sample table onto Darwin Core and find out that the difficulty is not filling fields in
but deciding what the fields mean, then read a GO term as a defined class and walk its subgraph.
*AI exercise: critique LLM-generated metadata fields.*

### [TP2.4 Cross-database integration](tp4/README.md)

One specimen or sample, described in several resources at once. Establish that they are the same
thing, then write down every way in which the resources disagree. The disagreements are the result.
**Q3 is drafted here**, finalised over the weekend. *AI exercise: LLM cross-source disambiguation.*

### [TP2.5 Packaging](tp5/README.md)

Turn the day's folder into a deposit that would pass the audit you performed this morning: a
structure, a README, recorded provenance, and a commit. This is the container your Q3 goes in, and
the habit that carries into the project and the dissertation.

Before you start
----------------

- R and RStudio, with `jsonlite`, `dplyr`, `readr` and `ggplot2` available
- Python 3 with Biopython, or the provided container
- a GitHub account, for the packaging block at the end of the day
- the day 1 lecture notes to hand ([Lecture I](../d1/lecture1.md), [Lecture II](../d1/lecture2.md)),
  since the vocabulary is assumed rather than repeated

All retrieval today is over public APIs and no accounts are needed. If a service is slow or down,
say so early: there are cached copies of every record used here, and it is better to work from those
than to spend the block watching a spinner.
