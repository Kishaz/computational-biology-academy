#!/usr/bin/env python3
"""Build a small RNA-seq experiment with a KNOWN answer.

A synthetic mini-genome of 8 genes, each given a designed expression level in
two conditions (control vs treated), 3 replicates each. Reads are simulated in
numbers proportional to each gene's designed expression, so featureCounts should
recover the design. Teaching purposes only, not real data.

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

# gene -> (control_reads, treated_reads). Housekeeping = steady; UP/DOWN = differential.
DESIGN = {
    "HKA": (1000, 1000),   # housekeeping, high, steady
    "HKB": (800,  800),    # housekeeping, steady
    "HKC": (600,  600),    # housekeeping, steady
    "MID": (200,  200),    # moderate, steady
    "LOWa": (40,   40),    # low, steady
    "LOWb": (30,   30),    # low, steady
    "UP":  (50,   800),    # switched ON by treatment
    "DOWN":(600,   60),    # switched OFF by treatment
}
GENES = list(DESIGN.keys())

def randseq(n):
    return "".join(random.choice("ACGT") for _ in range(n))

# --- build reference genome: genes separated by spacers, on one contig ---
os.makedirs("ref", exist_ok=True)
os.makedirs("reads", exist_ok=True)
genome_parts = []
coords = {}   # gene -> (start, end) 1-based inclusive
pos = 1
genome = ""
genome += randseq(SPACER); pos = len(genome) + 1
gene_seq = {}
for g in GENES:
    s = randseq(GENE_LEN)
    gene_seq[g] = s
    start = len(genome) + 1
    genome += s
    end = len(genome)
    coords[g] = (start, end)
    genome += randseq(SPACER)   # intergenic spacer after each gene

with open("ref/mini_genome.fasta", "w") as f:
    f.write(">chr1 synthetic mini genome\n")
    for i in range(0, len(genome), 70):
        f.write(genome[i:i+70] + "\n")

# --- GTF annotation (single exon per gene) ---
with open("ref/genes.gtf", "w") as f:
    for g in GENES:
        s, e = coords[g]
        attr = f'gene_id "{g}"; transcript_id "{g}.t1";'
        f.write(f"chr1\tsynthetic\texon\t{s}\t{e}\t.\t+\t.\t{attr}\n")

# --- simulate reads per sample, counts ~ designed expression (Poisson noise) ---
def emit_reads(fh, gene, n, rid_start):
    seq = gene_seq[gene]
    rid = rid_start
    for _ in range(n):
        start = random.randint(0, GENE_LEN - READLEN)
        read = list(seq[start:start+READLEN])
        # light sequencing error
        for j in range(READLEN):
            if random.random() < 0.002:
                read[j] = random.choice([b for b in "ACGT" if b != read[j]])
        qual = "I" * READLEN     # high quality (Phred ~40) for a clean teaching demo
        fh.write(f"@{gene}_read{rid}\n{''.join(read)}\n+\n{qual}\n")
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
            # ~7% replicate-to-replicate variation, so counts differ slightly
            # between replicates like real data, centred on the designed level.
            n = max(0, int(round(base * random.gauss(1.0, 0.07))))
            rid = emit_reads(fh, g, n, rid)

# --- record the design for later checking ---
with open("truth.tsv", "w") as f:
    f.write("gene\tcontrol\ttreated\trole\n")
    roles = {"HKA":"housekeeping","HKB":"housekeeping","HKC":"housekeeping",
             "MID":"moderate","LOWa":"low","LOWb":"low",
             "UP":"up in treated","DOWN":"down in treated"}
    for g in GENES:
        c, t = DESIGN[g]
        f.write(f"{g}\t{c}\t{t}\t{roles[g]}\n")

print("Wrote ref/mini_genome.fasta,", len(genome), "bp,", len(GENES), "genes")
print("Wrote ref/genes.gtf, reads/ (6 samples), truth.tsv")
