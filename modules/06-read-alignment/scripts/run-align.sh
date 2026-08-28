#!/usr/bin/env bash
# run-align.sh: the Module 06 alignment pipeline.
#   index the reference -> map reads (bwa mem) -> sort -> BAM -> CRAM.
# Assumes a Conda env with bwa and samtools:
#   conda create -n align -c conda-forge -c bioconda bwa samtools
#   conda activate align
#
# Inputs:  sars2.fasta (reference), reads.fastq (clean reads from Module 05)
set -euo pipefail

REF="${1:-sars2.fasta}"
READS="${2:-reads.fastq}"

echo "1) Index the reference (one-time)"
bwa index "$REF"

echo "2) Map the reads to the reference"
bwa mem "$REF" "$READS" > aln.sam

echo "3) Sort into a compressed BAM, then index it"
samtools sort -O bam -o aln.sorted.bam aln.sam
samtools index aln.sorted.bam

echo "4) How did the mapping go?"
samtools flagstat aln.sorted.bam

echo "5) Convert to CRAM (needs the SAME reference), then index it"
samtools view -C -T "$REF" -o aln.cram aln.sorted.bam
samtools index aln.cram

echo "Done. Compare sizes:"
ls -lh aln.sam aln.sorted.bam aln.cram
