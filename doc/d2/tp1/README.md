TP2.1 Sequence handling with Biopython
======================================

**Thursday 09:15-10:30, roughly 1 h 15 min.** No submission. The habits you build here are used in
every block that follows.

Yesterday we said that FASTA has nowhere to put metadata, so people put it in the definition line,
and that every downstream script therefore has to parse that line. This morning you write those
scripts.

> **If you are behind:** From step 5 onwards, start from
> `data/checkpoints/Danaus.COI-5P.fas`. Using this checkpoint is expected.

Set up your working directory
-----------------------------

Everything you do today happens in one place: inside the downloaded repository, with the environment
activated. Consult the repository's root README.md for how to do that.

When all is set up, check that Biopython is available:

```bash
python3 -c "import Bio; print(Bio.__version__)"
```

If that fails, create and activate the conda environment described in
[the repository README](../../../README.md#preparations).

### 1. Core: Get some sequences

We will use a BOLD v3-era FASTA snapshot for a genus with plenty of records, so that the exercises
have something to bite on. Use *Danaus*.

```bash
cp data/Danaus.v3.fas data/Danaus.fas
```

> BOLD v3 was retired in July 2026 and no longer serves this FASTA endpoint. The file in this
> repository is an archived teaching artefact: keep the retrieval note with it, because an API that
> moves is a reproducibility problem and you have just met one.

Look at what you have before you write any code:

```bash
grep '>' data/Danaus.fas
```
You should see four records, with BOLD v3-style definition lines.

### 2. Core: Read the definition line with shell tools

The definition line is structured as `>ID|Scientific binomial|marker|accession`. That structure is a
convention, not a standard, but it is enough for a first pass:

```bash
grep '>' data/Danaus.fas | cut -f 3 -d '|' | sort | uniq -c | sort -rn
```
You should see a couple of marker groups, one group being the dominant marker in BOLD

> How many markers are in the file? Did you expect more than one? What would have told you in
> advance?

### 3. Core: Hit the wall

Now try to pull out only the COI-5P sequences with the same tools.

> Write the command. Then explain why it does not work.

**Intentional failure.** This command cannot work with a line-oriented tool. The failure is the
answer. It looks like headers without their full sequences, or sequences detached from the marker
you filtered on. A FASTA record spans an unpredictable number of lines, so you must use a parser.

### 4. Core: Filter with Biopython

Create `scripts/filter_marker.py`:

```python
import sys
from Bio import SeqIO

infile, marker = sys.argv[1], sys.argv[2]

for record in SeqIO.parse(infile, "fasta"):
    fields = record.description.split('|')
    if len(fields) > 2 and fields[2] == marker:
        print('>' + record.description)
        print(record.seq)
```

Run it:

```bash
python3 scripts/filter_marker.py data/Danaus.fas COI-5P > out/Danaus.COI-5P.fas
grep -c '>' out/Danaus.COI-5P.fas
```
<!-- TODO: RV to verify --> you should see roughly 10^3 records, most of them COI-5P sequences.

> Older versions of this script opened files with `open(path, "rU")`. That mode was removed in
> Python 3.11. Code rots; this is the mild version of the problem you will see again in TP2.5.

### 5. Core: Describe what you have

Create `scripts/summarise.py`:

```python
import sys
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

lengths = []
for record in SeqIO.parse(sys.argv[1], "fasta"):
    lengths.append(len(record.seq))
    print(f"{record.id}\t{len(record.seq)}\t{gc_fraction(record.seq):.3f}")

print(f"\n# {len(lengths)} records, "
      f"min {min(lengths)}, max {max(lengths)}, "
      f"mean {sum(lengths) / len(lengths):.1f}", file=sys.stderr)
```

```bash
python3 scripts/summarise.py out/Danaus.COI-5P.fas > out/Danaus.COI-5P.tsv
```
<!-- TODO: RV to verify --> you should see roughly 10^3 records, most of them near one expected
COI-5P length.

> COI-5P is a protein-coding fragment of a fixed expected length. How many of your records have it?
> What are the short ones, and should they be in the file at all?

### 6. Stretch: Translate, and find out what the reading frame is

```python
from Bio import SeqIO

record = next(SeqIO.parse("out/Danaus.COI-5P.fas", "fasta"))
for frame in range(3):
    protein = record.seq[frame:].translate(table=5)   # invertebrate mitochondrial
    print(frame, protein.count("*"), protein[:40])
```

> Which frame gives the fewest stop codons? Now change `table=5` to the default `table=1`. What
> happens, and why? An annotation that does not travel with the sequence has to be supplied by you,
> correctly, every time.

**Intentional failure.** Changing to `table=1` is expected to fail biologically for this case. The
failure is the answer. It looks like many extra stop codons in otherwise plausible coding sequence.

### 7. Stretch: Similarity, and what it does not tell you

You have been given a BLAST hits table in `data/hits.tsv`. Read that file first.

For reference, this is how the supplied file was produced. You do not need to run these commands.

```bash
makeblastdb -in data/toy-reference.fas -dbtype nucl
blastn -query out/Danaus.COI-5P.fas -db data/toy-reference.fas \
       -outfmt "6 qseqid sseqid pident length evalue bitscore" \
       -max_target_seqs 1 > data/hits.tsv
```

Now inspect the supplied file:

```bash
head data/hits.tsv
sort -k3,3nr data/hits.tsv | head
sort -k3,3n data/hits.tsv | head
```

> A query matches its best hit at 87% identity. What can you conclude about its identity? Now the
> harder question: the reference database contains fifty species and the world contains rather more.
> What does the best hit mean when the right answer is not in the database at all?

That question is the whole of reference-database-dependent identification, and you will meet it again
in week 3 with SILVA and in week 4 with BOLD. Today it is enough to have felt it.

What to keep
------------

Leave `scripts/` and `out/` where they are. You will retrieve records into the same tree this
morning, annotate them this afternoon, and package the lot at the end of the day.

Next: [TP2.2 Retrieval](../tp2), then the protected **Q2** writing period.
