import sys
from Bio import SeqIO

infile, marker = sys.argv[1], sys.argv[2]

for record in SeqIO.parse(infile, "fasta"):
    fields = record.description.split('|')
    if len(fields) > 2 and fields[2] == marker:
        print('>' + record.description)
        print(record.seq)