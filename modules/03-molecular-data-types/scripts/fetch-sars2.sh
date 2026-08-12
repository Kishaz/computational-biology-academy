#!/usr/bin/env bash
# fetch-sars2.sh — download a tiny public reference genome (SARS-CoV-2, ~30 KB)
# from NCBI's E-utilities, using only curl. From Module 03.
#
# Run with:  bash fetch-sars2.sh

set -euo pipefail

URL="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_045512.2&rettype=fasta&retmode=text"

curl -s "$URL" -o sars2.fasta

echo "First two lines:"
head -2 sars2.fasta
echo "Number of sequences (FASTA headers):"
grep -c "^>" sars2.fasta

# NOTE: for real (large) sequencing data, use the proper tools instead — e.g.
# the SRA Toolkit (prefetch / fasterq-dump), Entrez Direct (efetch / esearch),
# or NCBI 'datasets'. Verify their current usage in the official docs.
