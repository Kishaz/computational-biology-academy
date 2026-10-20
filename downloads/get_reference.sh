#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# get_reference.sh
# Download a small, REAL reference genome for practice: the SARS-CoV-2
# reference (RefSeq NC_045512.2, about 30 kb). This is the reference used in
# the alignment and variant modules.
#
# Reproducible on purpose: the accession is pinned. Accessions and endpoints
# can change over time, so if the download fails, confirm the current accession
# and NCBI E-utilities URL against the official NCBI documentation.
# ---------------------------------------------------------------------------
set -euo pipefail

ACC="NC_045512.2"          # SARS-CoV-2 reference genome (RefSeq)
OUT="sars2.fasta"
URL="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=${ACC}&rettype=fasta&retmode=text"

echo "Fetching ${ACC} from NCBI..."
curl -fL -o "${OUT}" "${URL}"

echo "Saved ${OUT}"
echo "First line:"
head -n 1 "${OUT}"

# Expected (yours may differ slightly if NCBI updates the header):
#   >NC_045512.2 Severe acute respiratory syndrome coronavirus 2 ...
