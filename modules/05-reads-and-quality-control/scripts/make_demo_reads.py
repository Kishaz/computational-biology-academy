#!/usr/bin/env python3
"""Build a small, illustrative FASTQ of short reads simulated from a genome.

Teaching purposes only: reads have (1) a realistic 3' quality drop-off and
(2) 3' adapter contamination on short fragments, so FastQC shows something to
see and fastp has something to fix. NOT real sequencing data.
"""
import random

random.seed(42)

READLEN = 150
NREADS = 20000
# A real, commonly seen Illumina adapter prefix (what FastQC flags as the
# "Illumina Universal Adapter" and fastp auto-detects).
ADAPTER = "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"

# --- load the genome (single-sequence FASTA) ---
seq = []
with open("sars2.fasta") as fh:
    for line in fh:
        if not line.startswith(">"):
            seq.append(line.strip())
genome = "".join(seq)
G = len(genome)

def mutate(base, p):
    if random.random() < p:
        return random.choice([b for b in "ACGT" if b != base])
    return base

def qual_char(pos):
    # High quality (~Q37) at the 5' end, sloping down to ~Q12 at the 3' end,
    # plus a little noise — the classic Illumina profile.
    q = 37 - (pos / READLEN) * 25 + random.gauss(0, 2)
    q = max(2, min(40, int(round(q))))
    return chr(q + 33)  # Phred+33 encoding

with open("reads.fastq", "w") as out:
    for i in range(NREADS):
        start = random.randint(0, G - READLEN - 1)
        # Half the fragments are shorter than the read -> read runs into adapter.
        if random.random() < 0.5:
            insert = random.randint(30, READLEN)
        else:
            insert = READLEN
        bases = list(genome[start:start + insert])
        # sequencing errors, more likely toward the 3' end
        bases = [mutate(b, 0.001 + 0.02 * (j / READLEN)) for j, b in enumerate(bases)]
        read = "".join(bases)
        if insert < READLEN:                      # fill the rest with adapter
            need = READLEN - insert
            tail = (ADAPTER * 5)[:need]
            read = read + tail
        read = read[:READLEN]
        quals = "".join(qual_char(j) for j in range(len(read)))
        out.write(f"@read_{i+1}\n{read}\n+\n{quals}\n")

print(f"Wrote reads.fastq: {NREADS} reads x {READLEN} bp (genome length {G})")
