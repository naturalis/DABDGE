import sys
from Bio import SeqIO, AlignIO
from Bio.Align import MultipleSeqAlignment

records = {}
for seq in SeqIO.parse(sys.argv[1], "fasta"):
    seq.seq = seq.seq.upper()
    records[seq.description.split('|')[0]] = seq

aln = MultipleSeqAlignment([records[k] for k in sorted(records)])
AlignIO.write(aln, sys.argv[2], sys.argv[3])
