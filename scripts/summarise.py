import sys
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} <input.fasta>")

lengths = []
for record in SeqIO.parse(sys.argv[1], "fasta"):
    lengths.append(len(record.seq))
    print(f"{record.id}\t{len(record.seq)}\t{gc_fraction(record.seq):.3f}")

if not lengths:
    print("\n# 0 records", file=sys.stderr)
    raise SystemExit(0)

print(f"\n# {len(lengths)} records, "
      f"min {min(lengths)}, max {max(lengths)}, "
      f"mean {sum(lengths) / len(lengths):.1f}", file=sys.stderr)
