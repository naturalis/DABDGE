import sys
from Bio import SeqIO
from Bio.Data.CodonTable import TranslationError

print("id\tframe\tstops")
for record in SeqIO.parse(sys.argv[1], "fasta"):
    counts = []
    for frame in range(3):
        seq = record.seq[frame:]
        stops = 0
        for i in range(0, len(seq) - len(seq) % 3, 3):
            try:
                if seq[i:i + 3].translate(table=5) == "*":
                    stops += 1
            except TranslationError:
                pass
        counts.append((stops, frame))
    stops, frame = min(counts)
    print(f"{record.id}\t{frame}\t{stops}")