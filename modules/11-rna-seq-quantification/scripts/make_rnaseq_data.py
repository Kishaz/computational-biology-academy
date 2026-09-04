#!/usr/bin/env python3
"""Build a small RNA-seq experiment with a KNOWN answer.

A synthetic mini-genome of 8 genes (named neutrally, gene A..H, as a real
counts matrix would be: the names say nothing about how the gene behaves).
Each gene has a designed expression level in two conditions (control vs
treated), 3 replicates each. Reads are simulated in numbers proportional to
each gene's designed expression, so featureCounts should recover the design.
Teaching purposes only, not real data.

Two genes change with treatment (geneB up, geneD down); the rest hold steady.
You are meant to DISCOVER which two from the counts, not read it off a label.

Outputs:
  ref/mini_genome.fasta   the reference
  ref/genes.gtf           gene annotation (one exon per gene)
  reads/<sample>.fastq    6 samples: ctrl_1..3, treat_1..3
  truth.tsv               the designed expression, for checking
"""
import random, os
random.seed(11)

READLEN = 100
GENE_LEN = 1500
SPACER = 500

# gene -> (control_reads, treated_reads). Order is "genomic", not sorted by
# behaviour, so the two changing genes sit scattered among the steady ones.
DESIGN = {
    "geneA": (1000, 1000),   # steady, high
    "geneB": (50,   800),    # UP with treatment
    "geneC": (800,  800),    # steady
    "geneD": (600,   60),    # DOWN with treatment
    "geneE": (600,  600),    # steady
    "geneF": (40,    40),    # steady, low
    "geneG": (200,  200),    # steady, moderate
    "geneH": (30,    30),    # steady, low
}
GENES = list(DESIGN.keys())

def randseq(n):
    return "".join(random.choice("ACGT") for _ in range(n))

os.makedirs("ref", exist_ok=True)
os.makedirs("reads", exist_ok=True)
coords = {}
genome = randseq(SPACER)
gene_seq = {}
for g in GENES:
    s = randseq(GENE_LEN)
    gene_seq[g] = s
    start = len(genome) + 1
    genome += s
    coords[g] = (start, len(genome))
    genome += randseq(SPACER)

with open("ref/mini_genome.fasta", "w") as f:
    f.write(">chr1 synthetic mini genome\n")
    for i in range(0, len(genome), 70):
        f.write(genome[i:i+70] + "\n")

with open("ref/genes.gtf", "w") as f:
    for g in GENES:
        s, e = coords[g]
        f.write(f'chr1\tsynthetic\texon\t{s}\t{e}\t.\t+\t.\tgene_id "{g}"; transcript_id "{g}.t1";\n')

def emit_reads(fh, gene, n, rid):
    seq = gene_seq[gene]
    for _ in range(n):
        start = random.randint(0, GENE_LEN - READLEN)
        read = list(seq[start:start+READLEN])
        for j in range(READLEN):
            if random.random() < 0.002:
                read[j] = random.choice([b for b in "ACGT" if b != read[j]])
        fh.write(f"@{gene}_read{rid}\n{''.join(read)}\n+\n{'I'*READLEN}\n")
        rid += 1
    return rid

samples = {
    "ctrl_1": "control", "ctrl_2": "control", "ctrl_3": "control",
    "treat_1": "treated", "treat_2": "treated", "treat_3": "treated",
}
for sample, cond in samples.items():
    rid = 1
    with open(f"reads/{sample}.fastq", "w") as fh:
        for g in GENES:
            base = DESIGN[g][0 if cond == "control" else 1]
            n = max(0, int(round(base * random.gauss(1.0, 0.07))))
            rid = emit_reads(fh, g, n, rid)

roles = {"geneA":"steady","geneB":"up in treated","geneC":"steady","geneD":"down in treated",
         "geneE":"steady","geneF":"steady","geneG":"steady","geneH":"steady"}
with open("truth.tsv", "w") as f:
    f.write("gene\tcontrol\ttreated\trole\n")
    for g in GENES:
        c, t = DESIGN[g]
        f.write(f"{g}\t{c}\t{t}\t{roles[g]}\n")

print(f"Wrote reference ({len(genome)} bp), GTF ({len(GENES)} genes), reads (6 samples), truth.tsv")
