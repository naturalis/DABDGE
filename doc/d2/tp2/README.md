TP2.2 Retrieval, and the metadata audit
=======================================

**Thursday 10:45-13:00, roughly 2 h. Submit Q2 by end of day.**

Yesterday you were shown records. Today you go and get them, from three resources that were built by
different communities for different purposes, and you find out how much of what you need is actually
there.

From here on we work in R, because that is the environment you will use for the rest of the master's
and because your submission is an R Markdown or Quarto document. Python stays where it belongs, in
sequence handling.

```r
library(jsonlite)
library(dplyr)
library(readr)
```

### 1. A nucleotide record, from two places at once

GenBank, ENA and DDBJ mirror each other under the INSDC agreement, so the same accession resolves in
all three. Fetch it from both and compare what you are given.

```r
acc <- "GU706282"

gb <- readLines(paste0(
  "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
  "?db=nuccore&id=", acc, "&rettype=gb&retmode=text"))

ena <- readLines(paste0("https://www.ebi.ac.uk/ena/browser/api/embl/", acc))

writeLines(head(gb, 25))
writeLines(head(ena, 25))
```

> The sequence is the same. Is the metadata? List two fields that appear in one rendering and not
> the other. Which rendering would you cite, and does it matter?

Record the **versioned** accession, not the bare one. `GU706282` is a moving target;
`GU706282.1` is not.

### 2. A protein record

```r
p <- fromJSON("https://rest.uniprot.org/uniprotkb/P00395.json")

p$primaryAccession
p$entryType                       # reviewed or unreviewed
p$proteinDescription$recommendedName$fullName$value
length(p$references)
```

> UniProtKB has two halves: Swiss-Prot, curated by hand, and TrEMBL, annotated automatically. The
> accession does not tell you which you have. `entryType` does. Why does that distinction matter
> more than the accession itself?

Look at the evidence attached to one annotation:

```r
p$comments[[1]]
```

> Find one statement in this entry that is supported by an experiment, and one that is inferred. How
> is the difference recorded?

### 3. An occurrence record

```r
occ <- fromJSON(paste0(
  "https://api.gbif.org/v1/occurrence/search",
  "?scientificName=Cladosporium%20cladosporioides&limit=20"))

occ$results |>
  select(any_of(c("key", "scientificName", "eventDate",
                  "decimalLatitude", "decimalLongitude",
                  "coordinateUncertaintyInMeters",
                  "basisOfRecord", "datasetKey", "recordedBy"))) |>
  as_tibble()
```

Now go up one level, to the dataset the record belongs to:

```r
ds <- fromJSON(paste0("https://api.gbif.org/v1/dataset/", occ$results$datasetKey[1]))
ds$title
ds$license
ds$publishingOrganizationKey
```

> An occurrence has two kinds of provenance: who observed it, and who published it. Both matter, for
> different reasons. Which of the two would you need in order to decide whether you may reuse the
> record?

### 4. Choose your record

Pick **one** record to audit properly. Use the anchor site if one has been assigned; otherwise pick
any record from the three resources above that interests you. Prefer one with a physical specimen
behind it: those have more metadata to be missing.

### 5. Audit it

Work through this checklist and write the answers down as you go. You are not looking for a verdict,
you are looking for specifics.

| Question | Where you looked | What you found |
| -------- | ---------------- | -------------- |
| What identifies this record, and is the identifier versioned? | | |
| What kind of evidence stands behind it? | | |
| Who made the determination, and when? | | |
| Where was it collected, and how well is that known? | | |
| What is missing that a reuser would need? | | |
| What licence applies? | | |

Two of the rows usually bite. `coordinateUncertaintyInMeters` is empty far more often than it is
populated, and the licence is frequently stated at the dataset level and nowhere on the record
itself.

### 6. A deposit, rather than a record

Yesterday we left a question open: a study deposited its data in three places under three identifier
schemes. Look at what a machine can see of one of them.

```r
dc <- fromJSON("https://api.datacite.org/dois/10.5061/dryad.4sd51d4b")

dc$data$attributes$titles
dc$data$attributes$rightsList          # is there a licence?
dc$data$attributes$relatedIdentifiers  # does it point at the other deposits?
dc$data$attributes$descriptions |> substr(1, 300)
```

> A DOI that resolves makes a deposit findable. What would have to be in `relatedIdentifiers` for the
> three deposits to be findable *as one study*? Is it there?

### 7. AI exercise (20 min)

Give an LLM the accession or identifier of your chosen record and ask it to describe the record:
where it was collected, what the organism is, who deposited it, what the sequence encodes.

Then check every claim against the record you actually retrieved.

> Find at least one statement that is wrong, unsupported, or more confident than the underlying
> record allows. Common failure modes: coordinates invented to a precision the record does not have,
> a collector or a date filled in plausibly, a taxonomic authority attached to the wrong name, and an
> accession that does not exist at all.

Write down which tool you used, what you asked it, and what you caught. This goes in your submission
and feeds into the cross-module reflection in week 4.

Q2: metadata-quality mini-report
--------------------------------

**Due end of day today.** Half a page plus a brief annotated record, as R Markdown or Quarto.

1. Retrieve one biological record from a named public database. Report its identifiers, its
   provenance, and the fields that are missing.
2. Identify two metadata-quality issues and propose one fix for each. A fix is something somebody
   could actually do: a field to populate, a vocabulary to use, a link to add.
3. Include your AI-use note: which tool, for what task, and one output you had to correct or reject.

Scoring is correct / partial / incorrect per question, plus the record itself on clarity of
annotation. Feedback comes back tomorrow morning.

> Keep it to 30-45 minutes. This is a diagnostic, not an essay.

Next: [TP2.3 Annotation](../tp3).
