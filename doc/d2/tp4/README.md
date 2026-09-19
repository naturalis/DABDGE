TP2.4 Cross-database integration
================================

**Thursday 15:45-17:45, roughly 2 h. Q3 drafted in class, submitted end of day Friday.**

One specimen, or one sample, described in several resources at once. Your job is to establish that
they are the same thing, and then to write down every way in which the resources disagree about it.

The disagreements are the result. Nobody is being careless.

### 1. Pick your starting point

Choose one of these, and use the anchor site if one has been assigned to you.

- a **specimen** with a barcode record: start from BOLD, follow the sequence to GenBank, the taxon to
  GBIF and WoRMS
- a **sample** from a published study: start from the deposit, follow to the sequence archive and to
  the taxa it reports
- a **taxon** you met this morning: start from the name and see how many resources hold something
  about it

Write down your starting identifier before you do anything else. Everything hangs off it.

### 2. Follow the links that exist

```r
library(jsonlite); library(dplyr)

# BOLD, if your starting point is a specimen
bold <- fromJSON(paste0(
  "https://www.boldsystems.org/index.php/API_Public/combined",
  "?taxon=Danaus%20plexippus&format=json"))
```

> If the BOLD call fails, the API version has moved. Use the cached copy in `data/` and record the
> failure. An identifier that resolves and an API that answers are two different promises, and only
> one of them was made to you.

Follow the outbound links. A BOLD record often carries a GenBank accession; a GenBank record often
carries a specimen voucher; a GBIF occurrence carries a dataset key and sometimes an
`associatedSequences` field.

> Build the chain explicitly. Which links were machine-readable, and which did you have to
> reconstruct by hand from a free-text field?

### 3. Reconcile the name

This is where most of the disagreement lives.

```r
# GBIF backbone
gbif <- fromJSON(paste0("https://api.gbif.org/v1/species/match",
                        "?name=Cladosporium%20cladosporioides"))
gbif$usageKey; gbif$status; gbif$matchType; gbif$confidence

# WoRMS
worms <- fromJSON(paste0(
  "https://www.marinespecies.org/rest/AphiaRecordsByName/",
  "Cladosporium%20cladosporioides?like=false&marine_only=false"))

# GlobalNames verifier, across many sources at once
gn <- fromJSON(paste0("https://verifier.globalnames.org/api/v1/verifications/",
                      "Cladosporium%20cladosporioides"))
gn$names$bestResult |> as_tibble()
```

> Four resources, four identifiers for one organism: a GBIF usage key, an AphiaID, an NCBI taxid and
> a BOLD taxon id. Reconciliation is mapping between identifier spaces. It is not correcting anyone.

Now try a taxon that does not belong in one of them.

> Look up a terrestrial fungus in WoRMS, or a strictly marine invertebrate in a plant-focused
> checklist. What do you get, and what would a script that assumed a single authority have done with
> that answer?

### 4. Tabulate the disagreements

Build this table for your chosen entity. One row per point of comparison, one column per resource.

| Attribute | Resource A | Resource B | Resource C | Agree? |
| --------- | ---------- | ---------- | ---------- | ------ |
| identifier | | | | n/a |
| accepted name | | | | |
| authority | | | | |
| rank | | | | |
| coordinates | | | | |
| collection date | | | | |
| determiner | | | | |
| last modified | | | | |

Typical findings, none of which is anybody's fault:

- the same name with different authorities, because the resources follow different nomenclators
- coordinates that differ in the last decimals, because one was georeferenced from a locality string
- a date recorded as a year in one place and a full date in another
- a record updated in one resource in 2019 and mirrored from a 2014 snapshot in another

### 5. Draw the integration

Make one figure or one table that shows the entity, the resources, the identifiers, and the links
between them. Mark each link as machine-readable or reconstructed by hand.

This is the deliverable for Q3, and it is worth doing properly: it is the first time in this master's
that you will have drawn a data architecture rather than read one.

### 6. Judge it against FAIR

Pick your linked record as a whole and name:

- **one FAIR principle it satisfies**, with the evidence
- **one it fails**, with the consequence for somebody trying to reuse it

Be specific. "Not very interoperable" is not an answer. "The BOLD record carries the GenBank
accession as free text inside a notes field, so no machine can follow the link" is.

### 7. AI exercise (20 min)

Give an LLM the two conflicting versions of your record and ask it to reconcile them into a single
authoritative record.

> Then ask the question it did not ask itself: on what evidence did it choose? A reconciliation is a
> claim about which source is right, and the sources do not say. Look for silent averaging of
> coordinates, a preference for the most recent-looking record, or a taxonomy asserted with an
> authority that appears in none of your sources.

Note what you found.

Q3: cross-database integration mini-report
------------------------------------------

**Drafted today, submitted end of day Friday 25 September.** Half a page plus one integration diagram
or table, as R Markdown or Quarto.

1. Link one sample or specimen across two or more public resources. List the discrepancies you found.
2. Describe one FAIR principle the linked record satisfies and one it fails.
3. Include your AI-use note: which tool, for what task, and one output you had to correct or reject.

You have the weekend because the drawing takes longer than the retrieval. Do not let it take longer
than an evening.

> A warning about the trap in this exercise. It is tempting to report that the resources are messy.
> They are, and that observation is worth nothing on its own. The report worth writing says which
> specific link is broken, what a reuser cannot do because of it, and what would fix it.

Next: [TP2.5 FAIR packaging](../tp5).
