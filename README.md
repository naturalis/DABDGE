DABDGE - Data Analysis from Genes to Ecosystems
===============================================

### Introduction

This repository contains the teaching materials for the two-day block **Data architecture, FAIR,
ontologies and retrieval**, taught by Rutger Vos
([Naturalis Biodiversity Center](https://naturalis.nl)) within the curricular unit *Analysis of
Biological Data from the Gene to the Ecosystem* (DABDGE). DABDGE is the first CU of the MSc
programme in [Molecular and Environmental Computational Biology](https://ecum.uminho.pt) (MBCMA)
at the University of Minho, hosted by the Department of Biology (ECUM) and the Centre of Molecular
and Environmental Biology (CBMA), Campus de Gualtar, Braga.

DABDGE runs as an intensive four-week block in September and October 2026 and is organised around a
lifecycle arc:

**Generation and deposit** (W1, Pedro) → **Architecture and FAIR** (W2, this repository) →
**Analysis and inference** (W3, Pedro) → **Application and integration** (W4, Filipe).

This block is week 2 of that arc. Its anchor question is:

> **How is a biological record structured, made interoperable, and used?**

The week takes students from the inside of a single record (identifiers, formats, provenance) to the
joins between records held in different databases by different communities under different curation
regimes. It assumes the R and RStudio bootstrap delivered in week 1 and hands off to the
phyloseq, diversity and phylogeny work of week 3 and to the BOLD curation work of week 4.

The design follows the pedagogical principles set out for the CU as a whole: map-making over
mastery, a shared vocabulary defined once and used consistently, critical data literacy, tool
tasting rather than tool mastery, and reproducible work from day one. Where a topic is kept light,
the downstream CU that consolidates it is named explicitly (see *Hand-offs* below).

### Preparations

The block consists of lectures and hands-on computer practicals that require you to have the
following:

- a working laptop, any major operating system is fine
- [R](https://cran.r-project.org/) and [RStudio](https://posit.co/products/open-source/rstudio/)
  (open source edition), already installed during week 1
- [Python 3](https://www.python.org/) with [Biopython](https://biopython.org/) and
  [Jupyter](https://jupyter.org/), provided in the conda environment for this repository
- a plain text editor you are comfortable with

Get the course materials by opening this repository on GitHub, clicking the green **Code** button,
and downloading the ZIP. Unpack it somewhere you can find again, for example in your home folder,
and work from that unpacked folder.

Install a conda distribution first (for example
[Miniforge](https://conda-forge.org/download/) or
[Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main)). Then, from the
repository root, create and activate the teaching environment:

```bash
conda env create -f environment.yml
conda activate dabdge
```

No accounts are needed for the public databases used here. All retrieval is done over public APIs.

### Schedule

#### Day 1 - How a biological record is built (Wed 23 September 2026, 6 h T)

- **09:00-12:00** Lecture I: [The anatomy of a biological record](doc/d1/lecture1.md)
  - data architecture: rows, columns, identifiers; sample sheets versus feature tables
  - the central dogma as a data pipeline, and the formats that carry each step (FASTA, FASTQ,
    GenBank, GFF)
  - identifiers and accessions: what an accession promises, record versioning, submission
  - one record, many serialisations: why interoperability is a format problem and an identifier
    problem at the same time
- **14:00-17:00** Lecture II: [From record to network](doc/d1/lecture2.md)
  - public database structure: NCBI/ENA, UniProt, GBIF, BOLD
  - metadata, ontologies and controlled vocabularies: Darwin Core, GO, ENVO, taxonomy identifiers
  - why annotation quality bounds inference, worked through three cases
  - FAIR in depth, provenance, versioning and curation/QA-QC concepts
  - multi-source integration: what cross-scale interpretation can and cannot claim

Protect a 10-15 minute break in the middle of each block.

#### Day 2 - Retrieval, annotation and integration (Thu 24 September 2026, 8 h TP)

| | Block | Time | Minutes |
| --- | --- | --- | --- |
| | Setup and orientation | 09:00-09:15 | 15 |
| TP2.1 | [Sequence handling with Biopython](doc/d2/tp1) | 09:15-10:30 | 75 |
| | Break | 10:30-10:45 | |
| TP2.2 | [Retrieval and the metadata audit](doc/d2/tp2) | 10:45-12:35 | 110 |
| | Q2 written in class | 12:35-13:00 | 25 |
| | Lunch | 13:00-14:00 | |
| TP2.3 | [Annotation with standard vocabularies](doc/d2/tp3) | 14:00-15:15 | 75 |
| | Break | 15:15-15:30 | |
| TP2.4 | [Cross-database integration](doc/d2/tp4) | 15:30-17:10 | 100 |
| | Break | 17:10-17:20 | |
| TP2.5 | [Packaging](doc/d2/tp5) | 17:20-18:00 | 40 |

- **TP2.1** FASTA in and out, basic statistics, translation, marker filtering, then similarity
  reading from a supplied hits table.
- **TP2.2** pull a gene record and an occurrence record from public databases, inspect provenance and
  metadata, and complete the audit that feeds **Q2**. The **12:35-13:00** writing period is
  protected time for Q2, not an extension of the practical.
- **TP2.3** map a real sample table onto Darwin Core, then read a GO term as a defined class and
  walk its subgraph, ending with a short GO identifier check.
- **TP2.4** link one specimen across resources, reconcile the names, list the discrepancies, and
  draft **Q3** in class.
- **TP2.5** package the day's work as a deposit that would pass the morning audit, then submit a
  zip through `{{SUBMISSION_CHANNEL}}`.

### Assessment

This block contributes two of the six continuous assessment items for the CU (10% each). Both are
short: two to four targeted questions plus the figure or table you produced. Expect 30 to 45 minutes
to finalise, not a full evening. Submit reproducible documents (R Markdown or Quarto) where code is
involved, or a single page where only interpretation is required.

| ID | Submit by | Content |
| -- | --------- | ------- |
| Q2 | EOD Thu 24 Sep | Metadata-quality mini-report. Retrieve one biological record from a named public database and report its identifiers, provenance and missing fields. Identify two metadata-quality issues and propose one fix per issue. Half a page plus a brief annotated record. |
| Q3 | EOD Fri 25 Sep | Cross-database integration mini-report. Link one sample or specimen across two or more public resources and list the discrepancies. Describe one FAIR principle the linked record satisfies and one it fails. Half a page plus one integration diagram or table. Drafted in class on Thursday, finalised over the weekend. |

**AI-use policy.** You may use AI-guided tools for either submission, provided that you disclose the
use in a brief note at the end (which tool, for what task), and that where the use was substantive
you include at least one explicit observation of an output you had to correct, reject or refine. The
point is transparent and responsible use, not abstinence. Observations from this block feed into the
cross-module AI reflection submitted with Q6 in week 4.

### Teaching datasets

Practicals run on the recurring case-study anchor for the CU where possible, so that the same system
is seen through a different lens each week. Where an exercise needs a dataset with a specific
property that the anchor does not have, the substitute is named in the practical and the reason is
given.

- `data/anchor/` - records from the CU's recurring coastal and marine anchor site
- `data/worked-example/` - the multi-deposit worked example used in the day 1 lectures and in TP2.2
- `data/toy-db/` - notes and provenance for the small TP2.1 similarity reference database (`data/toy-reference.fas`)
- `data/checkpoints/` - checkpoint files and folders used to rejoin each Day 2 practical block

All datasets in this repository are subsets, prepared for teaching, of openly licensed published
data. Provenance and licence for each are recorded in the README of its directory, which is itself
an instance of the practice the block teaches.

### Databases and tools used

- **Sequences and genomes**: [NCBI](https://www.ncbi.nlm.nih.gov/) / [ENA](https://www.ebi.ac.uk/ena/),
  GenBank
- **Proteins**: [UniProt](https://www.uniprot.org/)
- **Biodiversity records**: [GBIF](https://www.gbif.org/), [OBIS](https://obis.org/)
- **Barcoding**: [BOLD](https://www.boldsystems.org/) (structure and API here; content, BINs and
  curation in week 4), [WoRMS](https://www.marinespecies.org/) as taxonomic cross-reference
- **Vocabularies**: [Darwin Core](https://dwc.tdwg.org/), [Gene Ontology](https://geneontology.org/)
  and [QuickGO](https://www.ebi.ac.uk/QuickGO/), [ENVO](https://sites.google.com/view/environmentontology/)
- **Software**: R with the tidyverse, Python with Biopython, Git and GitHub, R Markdown or Quarto

### Continuing threads

These run through the whole CU and are reinforced here:

- **From observation to evidence.** Every dataset is the product of choices about what to measure,
  how to sample and how to record. Read those choices first.
- **Reference frames matter.** Whether the reference is a database, a model organism, a phylogeny or
  a baseline period, the choice constrains the conclusions.
- **Reproducibility is a competence, not a virtue.** Practised from week 1, demanded in every
  deliverable thereafter.
- **AI is an instrument with calibration drift.** Useful, often impressive, occasionally wrong in
  confident ways. Treat its output as you would any instrument output, with documented verification.
- **Scale-linking as the master skill.** DABDGE is the only CU in the master's that explicitly works
  the molecular to community to ecosystem connection.

### Hand-offs

This block orients and exposes; the named CU goes deep.

| Kept light here | Consolidating CU |
| --------------- | ---------------- |
| Alignment algorithms, scoring matrices | CU2 Fundamentals of Computational Biology |
| Phylogenetic inference methods | CU2 / Project |
| Metabarcoding analysis, diversity, ordination | DABDGE week 3, then CU5 Ecoinformatics |
| RNA-seq and full omics workflows | CU4 Omics and Genetic Approaches in Model Organisms |
| BOLD content, BINs, BAGS, curation practice | DABDGE week 4 |
| Graph databases and semantic query languages | downstream / Project |

### Provenance and reuse

Parts of these materials are adapted from
`naturalis/mebioda`, the repository for the MSc course
*Methods in Biodiversity Analysis* taught at Leiden University, in particular the material on
sequence data formats, database APIs, phylogenetic data representation, semantics and version
control. Adaptations, cuts and additions are documented per file.

Content is released under the [MIT licence](LICENSE) unless a dataset directory states otherwise.
Corrections are welcome by email or through `{{SUBMISSION_CHANNEL}}`.
