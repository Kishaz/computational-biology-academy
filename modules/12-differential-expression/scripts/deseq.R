#!/usr/bin/env Rscript
# Module 12: differential expression with DESeq2.
suppressMessages(library(DESeq2))

counts <- as.matrix(read.delim("counts_full.tsv", row.names = 1))
coldata <- read.delim("coldata.tsv", row.names = 1)
coldata$condition <- factor(coldata$condition, levels = c("control", "treated"))

dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData   = coldata,
                              design    = ~ condition)
dds <- DESeq(dds)

cat("\n=== size factors (DESeq2's normalisation for library depth) ===\n")
print(round(sizeFactors(dds), 3))

res <- results(dds, contrast = c("condition", "treated", "control"))
res <- res[order(res$padj), ]

cat("\n=== summary ===\n")
summary(res)

sig <- subset(as.data.frame(res), padj < 0.05)
cat("\nSignificant genes (padj < 0.05):", nrow(sig), "\n")
cat("  up   (log2FC > 0):", sum(sig$log2FoldChange > 0), "\n")
cat("  down (log2FC < 0):", sum(sig$log2FoldChange < 0), "\n")

out <- data.frame(gene = rownames(res),
                  baseMean = round(res$baseMean, 1),
                  log2FoldChange = round(res$log2FoldChange, 3),
                  pvalue = signif(res$pvalue, 3),
                  padj = signif(res$padj, 3))
write.table(out, "results.tsv", sep = "\t", quote = FALSE, row.names = FALSE)
cat("\nWrote results.tsv\n")
