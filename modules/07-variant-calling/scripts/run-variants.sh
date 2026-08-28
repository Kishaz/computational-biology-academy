#!/usr/bin/env bash
# run-variants.sh: the Module 07 variant-calling pipeline.
#   map reads -> call variants (bcftools) -> filter the noise.
# Assumes a Conda env with bwa, samtools and bcftools:
#   conda create -n align -c conda-forge -c bioconda bwa samtools bcftools
#   conda activate align
#
# Inputs:  sars2.fasta (reference), reads.fastq (a sample's clean reads)
set -euo pipefail

REF="${1:-sars2.fasta}"
READS="${2:-reads.fastq}"

echo "1) Map the sample's reads to the reference"
bwa index "$REF"
bwa mem "$REF" "$READS" | samtools sort -O bam -o aln.sorted.bam -
samtools index aln.sorted.bam

echo "2) Call variants: tally the pileup, then decide what is real"
bcftools mpileup -f "$REF" aln.sorted.bam \
  | bcftools call -mv -Oz -o calls.vcf.gz
bcftools index calls.vcf.gz

echo "3) What did we find?"
bcftools query -f '%POS\t%REF\t%ALT\t%QUAL\t%INFO/DP\n' calls.vcf.gz

echo "4) Keep only confident calls (drop the sequencing noise)"
bcftools view -i 'QUAL>=20 && INFO/DP>=10' calls.vcf.gz -Oz -o calls.filtered.vcf.gz
bcftools index calls.filtered.vcf.gz

echo "Done. Confident variants:"
bcftools query -f '%POS\t%REF\t%ALT\t%QUAL\n' calls.filtered.vcf.gz
