TP2.4 Cross-database integration
================================

**Thursday 15:30-17:10, roughly 1 h 40 min. Q3 drafted in class, submitted end of day Friday.**

One specimen, or one sample, described in several resources at once. Your job is to 
establish that they are the same thing, and then to write down every way in which the 
resources disagree about it. The disagreements are the result. Nobody is being careless.

### 1. Core: Pick your starting point

Use the prepared specimen chain for this block: start from a BOLD record for 
*Danaus plexippus*, follow the sequence to GenBank, then follow the taxon into GBIF and 
WoRMS.

Write down your starting identifier before you do anything else. The identifier is the
hook that everything else hangs off.

### 2. Core: Follow the links that exist

```r
library(BOLDconnectR); library(dplyr)

# BOLD v5 (public ids, no key needed)
bold_ids <- bold.public.search(taxonomy = list("Danaus plexippus"))
head(bold_ids)

# BCDM records for those ids (requires a BOLD API key configured via bold.apikey())
# bold.apikey("your_actual_api_key_here")  <- workbench > Edit User Preferences
bold <- bold.fetch(
  get_by = "processid",
  identifiers = head(bold_ids$processid, 200)
)
```
You should see at most 200 records, most of them BOLD entries linked
to a smaller set of cross-resource identifiers.

> BOLD v5 is a tokenised API under `portal.boldsystems.org`; `bold.public.search()` wraps 
> the first query stages and `bold.fetch()` wraps retrieval. If `bold.fetch()` fails 
> because your account has no key, ask for the front-led copy of the prepared chain and 
> continue from that.

Follow the outbound links. A BOLD record often carries a GenBank accession (under `insdc_acs`); 
a GenBank record often carries a specimen voucher; a GBIF occurrence carries a dataset key 
and sometimes an `associatedSequences` field.

> Build the chain explicitly. Which links were machine-readable, and which did you have to
> reconstruct by hand from a free-text field?

### 3. Core: Reconcile the name

This is where most of the disagreement lives.

```r
# GBIF backbone
gbif <- fromJSON(paste0("https://api.gbif.org/v1/species/match",
                        "?name=Danaus%20plexippus"))
gbif$usageKey; gbif$status; gbif$matchType; gbif$confidence

# WoRMS
worms <- fromJSON(paste0(
  "https://www.marinespecies.org/rest/AphiaRecordsByName/",
  "Danaus%20plexippus?like=false&marine_only=false"))

# GlobalNames verifier, across many sources at once
gn <- fromJSON(paste0("https://verifier.globalnames.org/api/v1/verifications/",
                      "Danaus%20plexippus"))
gn$names$bestResult |> as_tibble()
```

**Intentional failure.** The WoRMS lookup in this example can return HTTP 204 (no content), and then
`fromJSON()` throws because there is nothing to parse. That failure is the answer. It looks like an
empty response and a parse error, not like a broken script.

You should see one or only a few records, most of them one name-matching result per 
service when content is available.

> Four resources, four identifiers for one organism: a GBIF usage key, an AphiaID, an NCBI taxid and
> a BOLD taxon id. Reconciliation is mapping between identifier spaces. It is not correcting anyone.

Now try a taxon that does not belong in one of them.

> Look up a terrestrial fungus in WoRMS, or a strictly marine invertebrate in a plant-focused
> checklist. What do you get, and what would a script that assumed a single authority have done with
> that answer?

### 4. Core: Tabulate the disagreements

Build this table for your chosen entity. One row per point of comparison, one column per resource.
Four well-checked rows beat eight guessed ones.

| Attribute | Resource A | Resource B | Resource C | Agree? |
| --------- | ---------- | ---------- | ---------- | ------ |
| identifier | | | | n/a |
| accepted name | | | | |
| coordinates | | | | |
| last modified | | | | |

Typical findings, none of which is anybody's fault:

- the same name with different authorities, because the resources follow different nomenclators
- coordinates that differ in the last decimals, because one was georeferenced from a locality string
- a date recorded as a year in one place and a full date in another
- a record updated in one resource in 2019 and mirrored from a 2014 snapshot in another
<!-- TODO: RV to verify --> you should see roughly 10^0 to 10^1 records, most of them disagreements
across identifiers, names, coordinates or dates.

### 5. Core: Draw the integration

Make one figure or one table that shows the entity, the resources, the identifiers, and the links
between them. Mark each link as machine-readable or reconstructed by hand.

This is the deliverable for Q3, and it is worth doing properly: it is the first time in this master's
that you will have drawn a data architecture rather than read one.
<!-- TODO: RV to verify --> you should see roughly 10^0 records, most of them one integration figure
or table with machine-readable versus reconstructed links.

### 6. Core: Judge it against FAIR

Pick your linked record as a whole and name:

- **one FAIR principle it satisfies**, with the evidence
- **one it fails**, with the consequence for somebody trying to reuse it

Be specific. "Not very interoperable" is not an answer. "The BOLD record carries the GenBank
accession as free text inside a notes field, so no machine can follow the link" is.

### 7. Stretch: Front-led demonstration (10 min)

From the front, compare an LLM reconciliation of the two conflicting versions of your record with
the sources it had to choose from.

> Then ask the question it did not ask itself: on what evidence did it choose? A reconciliation is a
> claim about which source is right, and the sources do not say. Look for silent averaging of
> coordinates, a preference for the most recent-looking record, or a taxonomy asserted with an
> authority that appears in none of your sources.

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
