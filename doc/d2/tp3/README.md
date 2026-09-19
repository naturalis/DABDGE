TP2.3 Annotation with standard vocabularies
===========================================

**Thursday 14:00-15:15, roughly 1 h 15 min.** No separate submission; the table you build here is
material for Q3 tomorrow.

This morning you found out what is missing from records other people made. This afternoon you
annotate a table yourself, and discover that the hard part is not filling fields in. It is deciding
what the fields mean.

> **If you are behind:** Start from `data/checkpoints/sample-metadata.csv`. Using this checkpoint is
> expected.

Part A: a real table into Darwin Core
-------------------------------------

### 1. Core: Read the table

In `data/` you will find a sample metadata table taken from a published study: collection sites,
dates, coordinates, and per-sample sequencing yields.

```r
library(dplyr); library(readr)

samples <- read_csv("data/sample-metadata.csv")
glimpse(samples)
```
<!-- TODO: RV to verify --> you should see roughly 10^1 to 10^2 records, most of them one row per
sample with mixed metadata fields.

> Before mapping anything: what is each row one of? A site, a sample, a sequencing run, or a
> specimen? The answer determines every mapping decision that follows, and the original table does
> not state it.

### 2. Core: Map the easy columns

Open the [Darwin Core quick reference](https://dwc.tdwg.org/terms/) alongside your table and write
the mapping down explicitly, as a table rather than in your head.

| Source column | Darwin Core term | Notes |
| ------------- | ---------------- | ----- |
| `site` | `locality` | |
| `lat` | `decimalLatitude` | check the datum |
| `date` | `eventDate` | ISO 8601 |
| ... | | |

<!-- TODO: RV to verify --> you should see roughly 10^0 to 10^1 mapped records, most of them direct
column-to-term matches.

Two rules worth following now and for the rest of your career:

- If you are unsure which term applies, read the **definition**, not the label. Terms that sound
  interchangeable often are not.
- If no term applies, do not force one. Record it as a custom field and say so.

### 3. Core: Map the hard columns

Some columns will have no obvious home. Work out what to do with each.

> The oiling status of a beach. The number of reads passing quality filters. The preservation method.
> Which of these is a property of the event, which of the sample, and which of the data product? Does
> Darwin Core have a place for all three?

The honest answer is that Darwin Core is a vocabulary for occurrences and specimens, not for
sequencing runs, and that environmental context belongs in
[MIxS](https://www.gensc.org/pages/standards-intro.html) fields backed by ENVO. Mixed tables are
normal. Knowing which standard owns which column is the skill.

### 4. Core: Where a term comes from

Take one environmental descriptor from your table and find an ENVO term for it:

```r
library(jsonlite)
res <- fromJSON(paste0(
  "https://www.ebi.ac.uk/ols4/api/search?q=coastal%20sediment&ontology=envo"))
res$response$docs |> as_tibble() |> select(label, obo_id, description)
```
<!-- TODO: RV to verify --> you should see roughly 10^1 records, most of them candidate ENVO terms
that need definition-level checking.

> Read the definitions of the top three hits. Are they the same concept at different granularities,
> or different concepts with similar labels? Which would you use, and what would you lose?

### 5. Core: Produce the annotated table

```r
annotated <- samples |>
  rename(locality = site,
         decimalLatitude = lat,
         decimalLongitude = lon,
         eventDate = date) |>
  mutate(basisOfRecord = "MaterialSample",
         coordinateUncertaintyInMeters = NA_real_)

write_csv(annotated, "out/samples-dwc.csv")
```
<!-- TODO: RV to verify --> you should see roughly 10^1 to 10^2 records, most of them mapped Darwin
Core rows with selected empty fields left explicit.

> You just wrote `NA` into `coordinateUncertaintyInMeters`. That is the right thing to do and it is
> also an admission. What is the difference between a field that is absent and a field that is
> explicitly empty? Which is more useful to a reuser?

Part B: reading an ontology
---------------------------

### 6. Core: A term is a defined class

```r
term <- fromJSON(paste0(
  "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0010228/complete"))

term$results$name
term$results$definition$text
term$results$aspect
```
<!-- TODO: RV to verify --> you should see roughly 10^0 records, most of them one GO term with a
definition and ontology aspect.

> Read the definition. Now imagine a gene annotated to this term. What exactly is being claimed about
> it, and what is not?

### 7. Stretch: A term has ancestors

```r
anc <- fromJSON(paste0(
  "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/",
  "GO%3A0010228/ancestors?relations=is_a,part_of"))

anc$results$ancestors
```

> A gene annotated to `GO:0010228` is implicitly annotated to every one of those. So if you run an
> enrichment test and both a term and its parent come out significant, how many independent findings
> do you have?

Most GO annotations are electronic inference rather than direct experiment. An annotation without
its evidence code is a rumour.

### 8. Stretch: AI exercise (10 min)

Give an LLM a short list of GO terms and ask it to write the biological story.

> Check the GO identifiers against QuickGO. Do they exist? Do the labels match the identifiers? Then
> check the argument: is it treating a term and its ancestor as two pieces of evidence?

Hallucinated GO identifiers are common and take thirty seconds to falsify, which makes this the
cleanest verification exercise of the week. Note what you found; you will need it for the reflection
in week 4.

What to keep
------------

- `out/samples-dwc.csv`, your annotated table
- the mapping table, including the columns you could not map and why
- your AI notes

Next: [TP2.4 Cross-database integration](../tp4) and the **Q3** draft.
