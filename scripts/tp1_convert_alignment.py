import sys
from Bio import SeqIO, AlignIO
from Bio.Align import MultipleSeqAlignment

if len(sys.argv) != 4:
    raise SystemExit(f"Usage: {sys.argv[0]} <input.fasta> <output> <format>")

records = {}
length = None
for seq in SeqIO.parse(sys.argv[1], "fasta"):
    seq.seq = seq.seq.upper()
    key = seq.description.split('|')[0]
    if key in records:
        raise ValueError(f"Duplicate record identifier: {key}")
    if length is None:
        length = len(seq.seq)
    elif len(seq.seq) != length:
        raise ValueError("All sequences must have the same length to write an alignment")
    records[key] = seq

if not records:
    raise SystemExit(f"No FASTA records found in {sys.argv[1]}")

aln = MultipleSeqAlignment([records[k] for k in sorted(records)])
AlignIO.write(aln, sys.argv[2], sys.argv[3])
