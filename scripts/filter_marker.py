import sys
from Bio import SeqIO

if len(sys.argv) != 3:
    raise SystemExit(f"Usage: {sys.argv[0]} <input.fasta> <marker>")

infile, marker = sys.argv[1], sys.argv[2]

for record in SeqIO.parse(infile, "fasta"):
    fields = record.description.split('|')
    if len(fields) > 2 and fields[-2] == marker:
        SeqIO.write(record, sys.stdout, "fasta")
