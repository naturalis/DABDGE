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
