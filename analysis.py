from Bio import SeqIO

# Load your DNA sequence file
record = SeqIO.read("sequence.fasta", "fasta")

# Print basic info
print("ID:", record.id)
print("Length:", len(record.seq))
gc = 100 * float(record.seq.count("G") + record.seq.count("C")) / len(record.seq)
print("GC Content: {:.2f}%".format(gc))
