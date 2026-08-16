#!/usr/bin/env bash
# run-qc.sh — the Module 05 QC pipeline: FastQC -> fastp (trim) -> FastQC.
# Assumes a Conda env with fastqc and fastp (see the module, Part D).
#   conda create -n qc -c conda-forge -c bioconda fastqc fastp multiqc
set -euo pipefail

READS="${1:-reads.fastq}"

echo "1) QC the raw reads"
fastqc "$READS"

echo "2) Trim low-quality tails + remove adapters with fastp"
fastp -i "$READS" -o "${READS%.fastq}.trimmed.fastq" \
      --cut_tail --cut_tail_window_size 4 --cut_tail_mean_quality 20 \
      --length_required 30 \
      -h fastp.html -j fastp.json

echo "3) QC the trimmed reads (confirm the fix)"
fastqc "${READS%.fastq}.trimmed.fastq"

echo "Done. Open the *_fastqc.html and fastp.html reports in a browser."
