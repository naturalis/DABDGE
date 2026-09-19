TP2.3 Annotation with standard vocabularies
===========================================

**Thursday 14:00-15:30, roughly 1.5 h.** No separate submission; the table you build here is
material for Q3 tomorrow.

This morning you found out what is missing from records other people made. This afternoon you
annotate a table yourself, and discover that the hard part is not filling fields in. It is deciding
what the fields mean.

Part A: a real table into Darwin Core
-------------------------------------

### 1. Read the table

In `data/` you will find a sample metadata table taken from a published study: collection sites,
dates, coordinates, and per-sample sequencing yields.

```r
library(dplyr); library(readr)

samples <- read_csv("data/sample-metadata.csv")
glimpse(samples)
```

> Before mapping anything: what is each row one of? A site, a sample, a sequencing run, or a
> specimen? The answer determines every mapping decision that follows, and the original table does
> not state it.

### 2. Map the easy columns

Open the [Darwin Core quick reference](https://dwc.tdwg.org/terms/) alongside your table and write
the mapping down explicitly, as a table rather than in your head.

| Source column | Darwin Core term | Notes |
| ------------- | ---------------- | ----- |
| `site` | `locality` | |
| `lat` | `decimalLatitude` | check the datum |
| `date` | `eventDate` | ISO 8601 |
| ... | | |

Two rules worth following now and for the rest of your career:

- If you are unsure which term applies, read the **definition**, not the label. Terms that sound
  interchangeable often are not.
- If no term applies, do not force one. Record it as a custom field and say so.

### 3. Map the hard columns

Some columns will have no obvious home. Work out what to do with each.

> The oiling status of a beach. The number of reads passing quality filters. The preservation method.
> Which of these is a property of the event, which of the sample, and which of the data product? Does
> Darwin Core have a place for all three?

The honest answer is that Darwin Core is a vocabulary for occurrences and specimens, not for
sequencing runs, and that environmental context belongs in
[MIxS](https://www.gensc.org/pages/standards-intro.html) fields backed by ENVO. Mixed tables are
normal. Knowing which standard owns which column is the skill.

### 4. Where a term comes from

Take one environmental descriptor from your table and find an ENVO term for it:

```r
library(jsonlite)
res <- fromJSON(paste0(
  "https://www.ebi.ac.uk/ols4/api/search?q=coastal%20sediment&ontology=envo"))
res$response$docs |> as_tibble() |> select(label, obo_id, description)
```

> Read the definitions of the top three hits. Are they the same concept at different granularities,
> or different concepts with similar labels? Which would you use, and what would you lose?

### 5. Produce the annotated table

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

> You just wrote `NA` into `coordinateUncertaintyInMeters`. That is the right thing to do and it is
> also an admission. What is the difference between a field that is absent and a field that is
> explicitly empty? Which is more useful to a reuser?

Part B: reading an ontology
---------------------------

### 6. A term is a defined class

```r
term <- fromJSON(paste0(
  "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0010228/complete"))

term$results$name
term$results$definition$text
term$results$aspect
```

> Read the definition. Now imagine a gene annotated to this term. What exactly is being claimed about
> it, and what is not?

### 7. A term has ancestors

```r
anc <- fromJSON(paste0(
  "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/",
  "GO%3A0010228/ancestors?relations=is_a,part_of"))

anc$results$ancestors
```

> A gene annotated to `GO:0010228` is implicitly annotated to every one of those. So if you run an
> enrichment test and both a term and its parent come out significant, how many independent findings
> do you have?

### 8. An annotation has an evidence code

Look up any gene product annotated to the term and inspect the evidence codes attached.

> Which of the annotations were made by a curator reading a paper, and which were inferred
> electronically from sequence similarity? If most are `IEA`, what is the enrichment test actually
> testing?

This is the same structure as this morning's BLAST exercise and as next week's SILVA-based taxonomy
assignment: similarity to a known thing, used to assign a label, inherited by everything downstream.

### 9. AI exercise (25 min)

Two rounds, both short.

**Round one, metadata.** Give an LLM three rows of your raw table and ask it to produce a full Darwin
Core mapping with values.

> Check every field it invented. Look in particular for: terms that do not exist in Darwin Core,
> values supplied for fields your table cannot support, a `basisOfRecord` chosen without being told
> what the rows are, and coordinate precision it has no basis for.

**Round two, ontology.** Give it a short list of GO terms and ask it to write the biological story.

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

Next: [TP2.4 Cross-database integration](../tp4) and the **Q3** submission.
