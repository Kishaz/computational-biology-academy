#!/usr/bin/env bash
# run-tree.sh: the Module 09 phylogenetics pipeline.
#   align many genomes -> infer a tree with support values.
# Assumes a Conda env with mafft and iqtree:
#   conda create -n align -c conda-forge -c bioconda mafft iqtree
#   conda activate align
#
# Input:  samples.fasta (a multi-FASTA of the genomes to compare)
set -euo pipefail

FASTA="${1:-samples.fasta}"
ROOT="${2:-reference}"   # which sequence to root the tree on (outgroup)

echo "1) Multiple sequence alignment (line up homologous positions)"
mafft --auto "$FASTA" > aligned.fasta

echo "2) Infer the tree: GTR+G model, 1000 ultrafast bootstraps, rooted on $ROOT"
iqtree -s aligned.fasta -m GTR+G -B 1000 -o "$ROOT" --redo

echo "Done. The tree is aligned.fasta.treefile (Newick)."
echo "Peek at it in the terminal with:"
echo "  python3 -c \"from Bio import Phylo; Phylo.draw_ascii(Phylo.read('aligned.fasta.treefile','newick'))\""
