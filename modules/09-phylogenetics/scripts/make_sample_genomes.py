#!/usr/bin/env python3
"""Build a small set of SARS-CoV-2-like genomes with a KNOWN family tree, so the
tree-builder has a right answer to recover. Teaching purposes only.

Each genome is the reference (NC_045512.2) plus a set of mutations. The mutations
are nested on purpose:
  - four samples share the D614G set  -> one deep clade
  - two of those also share N501Y     -> the "alpha" sub-clade
  - the other two share L452R          -> the "delta" sub-clade
D614G (A23403G), N501Y (A23063T) and L452R (T22917G) are real, documented mutations;
every ancestral base is checked against the reference before it is changed.

Input:  sars2.fasta (the reference)
Output: samples.fasta (reference + 5 samples)
"""
seq = []
with open("sars2.fasta") as f:
    f.readline()
    for line in f:
        seq.append(line.strip())
REF = "".join(seq)
def base(pos): return REF[pos - 1]           # 1-based

G_CLADE = [(241, 'T'), (3037, 'T'), (14408, 'T'), (23403, 'G')]   # includes D614G
ALPHA   = [(23063, 'T')]                                          # N501Y
DELTA   = [(22917, 'G')]                                          # L452R
TS = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
def priv(pos): return (pos, TS[base(pos)])   # a private, sample-specific change

samples = {
    "early":  [priv(1500)],
    "alpha1": G_CLADE + ALPHA + [priv(5000)],
    "alpha2": G_CLADE + ALPHA + [priv(8200)],
    "delta1": G_CLADE + DELTA + [priv(12500)],
    "delta2": G_CLADE + DELTA + [priv(16800)],
}

# safety: every ancestral base must match the reference
for name, muts in samples.items():
    for pos, alt in muts:
        assert base(pos) != alt, f"{name}: {pos} already {alt} in reference"

def build(muts):
    g = list(REF)
    for pos, alt in muts:
        g[pos - 1] = alt
    return "".join(g)

with open("samples.fasta", "w") as out:
    out.write(">reference\n")
    for i in range(0, len(REF), 70):
        out.write(REF[i:i + 70] + "\n")
    for name, muts in samples.items():
        s = build(muts)
        out.write(f">{name}\n")
        for i in range(0, len(s), 70):
            out.write(s[i:i + 70] + "\n")

print(f"Wrote samples.fasta: reference + {len(samples)} samples")
