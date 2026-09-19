from Bio import SeqIO

record = next(SeqIO.parse("out/Danaus.COI-5P.fas", "fasta"))
for frame in range(3):
    protein = record.seq[frame:].translate(table=5)   # invertebrate mitochondrial
    print(frame, protein.count("*"), protein[:40])
