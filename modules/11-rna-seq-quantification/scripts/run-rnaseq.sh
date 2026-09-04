#!/usr/bin/env bash
# run-rnaseq.sh: the Module 11 RNA-seq quantification pipeline.
#   align RNA reads (splice-aware) -> count reads per gene -> counts matrix.
# Assumes a Conda env with hisat2, samtools and subread (featureCounts):
#   conda create -n align -c conda-forge -c bioconda hisat2 samtools subread
#   conda activate align
#
# Inputs:  genome.fasta, genes.gtf, and reads/<sample>.fastq for each sample.
set -euo pipefail

GENOME="${1:-genome.fasta}"
GTF="${2:-genes.gtf}"
SAMPLES="ctrl_1 ctrl_2 ctrl_3 treat_1 treat_2 treat_3"

mkdir -p aligned

echo "1) Index the reference (one-time)"
hisat2-build "$GENOME" genome_index

echo "2) Align each sample's RNA reads with the splice-aware aligner"
for s in $SAMPLES; do
    hisat2 -x genome_index -U "reads/$s.fastq" | samtools sort -o "aligned/$s.bam" -
done

echo "3) Count reads per gene across all samples"
featureCounts -a "$GTF" -t exon -g gene_id -o counts.txt aligned/*.bam

echo "Done. The counts matrix is counts.txt"
echo "(Geneid + one column per sample; featureCounts also writes counts.txt.summary)."
