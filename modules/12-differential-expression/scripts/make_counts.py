#!/usr/bin/env python3
"""Generate a realistic RNA-seq counts matrix with a KNOWN answer, for teaching
differential expression. ~1000 genes, 3 control + 3 treated samples, counts from
a negative-binomial model (what DESeq2 assumes). Samples have different library
depths so normalisation matters. 40 genes are truly changed (20 up, 20 down);
the rest are not. Teaching only, not real data.

Outputs:
  counts_full.tsv   gene x sample integer counts (the matrix DESeq2 reads)
  coldata.tsv       sample -> condition
  truth.tsv         which genes were designed to change, and by how much
"""
import random, math
random.seed(12)

NGENES = 1000
CTRL = ["ctrl_1", "ctrl_2", "ctrl_3"]
TREAT = ["treat_1", "treat_2", "treat_3"]
SAMPLES = CTRL + TREAT
# different library depths (size factors) -> raw counts are NOT comparable
SIZE = {"ctrl_1": 1.0, "ctrl_2": 1.3, "ctrl_3": 0.8,
        "treat_1": 1.5, "treat_2": 0.9, "treat_3": 1.15}
DISP = 0.12  # NB dispersion

def poisson(lam):
    if lam < 30:
        L = math.exp(-lam); k = 0; p = 1.0
        while True:
            k += 1; p *= random.random()
            if p <= L:
                return k - 1
    return max(0, int(round(random.gauss(lam, math.sqrt(lam)))))

def nb(mean, disp=DISP):
    if mean <= 0:
        return 0
    r = 1.0 / disp
    lam = random.gammavariate(r, mean / r)
    return poisson(lam)

genes = [f"gene{n:04d}" for n in range(1, NGENES + 1)]
# baseline mean expression per gene: log-normal spread (a few to thousands)
base = {g: math.exp(random.gauss(4.0, 1.8)) for g in genes}

# choose DE genes
de_up = random.sample(genes, 20)
remaining = [g for g in genes if g not in de_up]
de_down = random.sample(remaining, 20)
log2fc = {}
for g in genes:
    log2fc[g] = 0.0
for g in de_up:
    log2fc[g] = random.uniform(1.5, 3.0)
for g in de_down:
    log2fc[g] = -random.uniform(1.5, 3.0)

def is_treat(s):
    return s in TREAT

# build the matrix
mat = {}
for g in genes:
    row = {}
    for s in SAMPLES:
        fold = 2 ** log2fc[g] if is_treat(s) else 1.0
        mean = base[g] * fold * SIZE[s]
        row[s] = nb(mean)
    mat[g] = row

with open("counts_full.tsv", "w") as f:
    f.write("gene\t" + "\t".join(SAMPLES) + "\n")
    for g in genes:
        f.write(g + "\t" + "\t".join(str(mat[g][s]) for s in SAMPLES) + "\n")

with open("coldata.tsv", "w") as f:
    f.write("sample\tcondition\n")
    for s in SAMPLES:
        f.write(f"{s}\t{'treated' if is_treat(s) else 'control'}\n")

with open("truth.tsv", "w") as f:
    f.write("gene\ttrue_log2fc\tdirection\n")
    for g in genes:
        d = "up" if g in de_up else ("down" if g in de_down else "none")
        f.write(f"{g}\t{log2fc[g]:.3f}\t{d}\n")

print(f"Wrote counts_full.tsv ({NGENES} genes x {len(SAMPLES)} samples), coldata.tsv, truth.tsv")
print(f"Designed DE: {len(de_up)} up, {len(de_down)} down, {NGENES-40} unchanged")
