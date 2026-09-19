from Bio import SeqIO

record = next(SeqIO.parse("out/Danaus.COI-5P.fas", "fasta"), None)
if record is None:
    raise SystemExit("No FASTA records found in out/Danaus.COI-5P.fas")

for frame in range(3):
    protein = record.seq[frame:].translate(table=5)   # invertebrate mitochondrial
    print(frame, protein.count("*"), protein[:40])
