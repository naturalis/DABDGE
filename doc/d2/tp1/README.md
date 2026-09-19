TP2.1 Sequence handling with Biopython
======================================

**Thursday 09:00-10:30, roughly 1.5 h.** No submission. The habits you build here are used in every
block that follows.

Yesterday we said that FASTA has nowhere to put metadata, so people put it in the definition line,
and that every downstream script therefore has to parse that line. This morning you write those
scripts.

Set up your working directory
-----------------------------

Everything you make today goes in one place, because on Friday afternoon you will package it.

```bash
mkdir -p ~/dabdge-w2/{data,scripts,out}
cd ~/dabdge-w2
```

Check that Biopython is available:

```bash
python3 -c "import Bio; print(Bio.__version__)"
```

If that fails, either `pip install biopython` or start the container described in
[the repository README](../../../README.md).

### 1. Get some sequences

We will use barcode sequences for a genus with plenty of records, so that the exercises have
something to bite on. Use the anchor-site taxon if one has been assigned to you; otherwise use
*Danaus*.

```bash
curl -o data/Danaus.fas "https://www.boldsystems.org/index.php/API_Public/sequence?taxon=Danaus"
```

> The BOLD API changed between versions 4 and 5. If the call above returns nothing useful, use the
> copy in `data/` in this repository and note the failure: an API that moves is a reproducibility
> problem, and you have just met one.

Look at what you have before you write any code:

```bash
head -2 data/Danaus.fas
grep -c '>' data/Danaus.fas
```

### 2. Read the definition line with shell tools

The definition line is structured as `>ID|Scientific binomial|marker|accession`. That structure is a
convention, not a standard, but it is enough for a first pass:

```bash
grep '>' data/Danaus.fas | cut -f 3 -d '|' | sort | uniq -c | sort -rn
```

> How many markers are in the file? Did you expect more than one? What would have told you in
> advance?

### 3. Hit the wall

Now try to pull out only the COI-5P sequences with the same tools.

> Write the command. Then explain why it does not work.

The answer is that a FASTA record spans an unpredictable number of lines, so a line-oriented tool
cannot keep the definition line and its sequence together. This is the moment to reach for a parser.

### 4. Filter with Biopython

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

> Older versions of this script opened files with `open(path, "rU")`. That mode was removed in
> Python 3.11. Code rots; this is the mild version of the problem you will see again in TP2.5.

### 5. Describe what you have

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

> COI-5P is a protein-coding fragment of a fixed expected length. How many of your records have it?
> What are the short ones, and should they be in the file at all?

### 6. Translate, and find out what the reading frame is

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

### 7. Similarity, and what it does not tell you

Build a small reference database from a handful of named sequences and search your set against it.

```bash
makeblastdb -in data/toy-reference.fas -dbtype nucl
blastn -query out/Danaus.COI-5P.fas -db data/toy-reference.fas \
       -outfmt "6 qseqid sseqid pident length evalue bitscore" \
       -max_target_seqs 1 > out/hits.tsv
head out/hits.tsv
```

Sort the hits by percentage identity and look at both ends of the range.

> A query matches its best hit at 87% identity. What can you conclude about its identity? Now the
> harder question: the reference database contains fifty species and the world contains rather more.
> What does the best hit mean when the right answer is not in the database at all?

That question is the whole of reference-database-dependent identification, and you will meet it again
in week 3 with SILVA and in week 4 with BOLD. Today it is enough to have felt it.

### 8. Convert, so that others can read it

```python
import sys
from Bio import SeqIO, AlignIO
from Bio.Align import MultipleSeqAlignment

records = {}
for seq in SeqIO.parse(sys.argv[1], "fasta"):
    seq.seq = seq.seq.upper()
    records[seq.description.split('|')[0]] = seq

aln = MultipleSeqAlignment([records[k] for k in sorted(records)])
AlignIO.write(aln, sys.argv[2], sys.argv[3])
```

Sorting the records and normalising the case makes two files comparable with `diff`. Without it, two
alignments of the same data differ in bytes while being identical in content, and you cannot tell
which kind of difference you are looking at.

What to keep
------------

Leave `scripts/` and `out/` where they are. You will retrieve records into the same tree this
morning, annotate them this afternoon, and package the lot at the end of the day.

Next: [TP2.2 Retrieval](../tp2) and the **Q2** submission.
