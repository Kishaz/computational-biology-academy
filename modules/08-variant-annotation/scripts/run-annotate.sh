#!/usr/bin/env bash
# run-annotate.sh: the Module 08 variant-annotation step.
#   take a called VCF and add functional effects with SnpEff.
# Assumes a Conda env with bcftools and snpeff:
#   conda create -n align -c conda-forge -c bioconda bwa samtools bcftools snpeff
#   conda activate align
#
# Input:  calls.filtered.vcf.gz (confident variants from Module 07)
set -euo pipefail

VCF="${1:-calls.filtered.vcf.gz}"
GENOME="${2:-NC_045512.2}"   # SnpEff database name for the reference

echo "1) SnpEff wants plain VCF; decompress if needed"
bcftools view "$VCF" -Ov -o calls.for_snpeff.vcf

echo "2) Annotate (first run downloads the $GENOME gene map)"
snpEff "$GENOME" calls.for_snpeff.vcf > annotated.vcf

echo "3) Read the primary effect of each variant"
grep -v '^#' annotated.vcf | while IFS=$'\t' read -r chrom pos id ref alt qual filter info rest; do
  ann=$(printf '%s' "$info" | grep -o 'ANN=[^;]*' | sed 's/ANN=//' | cut -d',' -f1)
  IFS='|' read -r allele effect impact gene _ <<< "$ann"
  printf '%s\t%s>%s\t%s\t%s\t%s\n' "$pos" "$ref" "$alt" "$gene" "$effect" "$impact"
done

echo "Done. Full annotations are in the INFO/ANN field of annotated.vcf"
echo "(SnpEff also writes snpEff_summary.html and snpEff_genes.txt)."
