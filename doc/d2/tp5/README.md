TP2.5 Packaging, and the deposit you wish you had found
=======================================================

**Thursday 17:20-18:00, roughly 40 min.** Submit a zip of this folder through
`{{SUBMISSION_CHANNEL}}`. The result is the container your Q3 goes in, and the habit you carry into
the project and the dissertation.

This morning you audited somebody's deposit and found it wanting. It would be poor form to end the
day with a folder that would fail the same audit. So spend the last forty minutes making one that
passes.

### 1. Look at what you have

```bash
cd ~/dabdge-w2
find . -type f | sort
```

Most likely: a few scripts, several downloaded files, some intermediate output, and at least one
thing called `final2.csv`.

> Hand that folder to the person sitting next to you. Can they tell which file is input, which is
> output, and which was a mistake? That is the audit, and it takes ten seconds.

### 2. Give it a shape

One layout, used consistently, beats a clever one. Use this structure for the folder you hand in:

```
dabdge-w2/
├── README.md          what this is, who made it, when
├── LICENSE            what others may do with it
├── data/              inputs, never edited by hand
│   └── README.md      where each file came from, and when it was retrieved
├── scripts/           code, in the order it runs
├── out/               everything derived; deletable and regenerable
└── report.qmd         the Q3 document
```

```bash
mkdir -p data scripts out
```

Two rules that do most of the work:

- **`data/` is read-only.** If you need to change an input, write the changed version to `out/`. An
  input you have edited in place has lost its provenance and cannot be re-downloaded to check.
- **`out/` is disposable.** If deleting it loses something, that something belongs elsewhere.

### 3. Write the README you wanted this morning

Not a description of the project. A description of the files.

```markdown
# DABDGE week 2, [your name]

Work from the practicals of 24 September 2026.

## Data

| File | Source | Retrieved | Licence |
| ---- | ------ | --------- | ------- |
| `data/Danaus.fas` | archived BOLD v3 teaching artefact from `naturalis/DABDGE` | 2026-09-24 | see BOLD terms |
| `data/sample-metadata.csv` | supplied in the course repository | 2026-09-24 | CC0 |

## Scripts

Run in this order:

1. `scripts/filter_marker.py` - selects one marker from a multi-marker FASTA
2. `scripts/summarise.py` - per-record length and GC, to `out/`

## Outputs

`out/samples-dwc.csv` - sample table mapped to Darwin Core. Columns not in Darwin Core are
prefixed `x_` and defined in `data/README.md`.
```

> The retrieval date is the field people forget and the one that matters most, because the resource
> has moved on since. Write it down for every file.

### 4. Say what the licence is

An unlicensed deposit is legally unusable however open it looks. For teaching material and derived
tables, CC0 or CC-BY is normal; for code, MIT or Apache-2.0. Copy the licence text from the
`LICENSE` file in the downloaded course materials into a file called `LICENSE` in your folder.

> Your outputs are derived from sources with their own terms. Does your licence conflict with any of
> them? This is not a rhetorical question and the answer is occasionally yes.

### 5. Submit the folder

Zip `dabdge-w2/` when you are done. Submit the zip file through `{{SUBMISSION_CHANNEL}}`, with your
name on it if that system does not add your name for you.

### 6. Audit your neighbour

Swap folders with the person next to you, by USB stick, AirDrop, shared drive or whatever the room
allows, and score theirs the way you scored the Dryad
deposit this morning.

| | Evidence | Pass, partial or fail |
| - | -------- | --------------------- |
| Findable | | |
| Accessible | | |
| Interoperable | | |
| Reusable | | |

> You have five minutes and they are in the room, which is a considerable advantage over every
> other dataset you will ever audit. Ask them the questions you could not ask the authors this
> morning.

### 7. One thing to take with you

The deposit you audited this morning was made by competent people meeting the standards of their
time. Yours will be audited by somebody in 2038 under standards that do not exist yet.

The defence is not perfection. It is writing down what you did, what the files are, where they came
from, and what somebody may do with them. Everything else is recoverable from that; nothing is
recoverable without it.

Where this goes next
--------------------

- **Q3** is due end of day Friday. Submit it through `{{SUBMISSION_CHANNEL}}`, not in a separate
  folder.
- **Week 3** (Pedro) computes on records of exactly this kind, in phyloseq. The identifiers you have
  been fussing over are the ones that have to line up.
- **Week 4** (Filipe) curates barcode records against the same principles, under the name QA/QC, and
  asks you to build an integrative argument across all four weeks in **Q6**. The AI notes you have
  been keeping since Monday feed the reflection that goes with it.

Back to [the day 2 overview](..) or [the repository README](../../../README.md).
