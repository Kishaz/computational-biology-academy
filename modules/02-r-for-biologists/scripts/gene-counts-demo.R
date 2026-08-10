# gene-counts-demo.R
# A tiny base-R demo on toy gene counts, from Module 02.
# Run with:  Rscript gene-counts-demo.R

counts <- c(GeneA = 120, GeneB = 85, GeneC = 200, GeneD = 40, GeneE = 150)

# In a script, output must be requested explicitly (unlike the interactive console):
print(mean(counts))      # average count (should be 119)
print(summary(counts))   # min, quartiles, median, mean, max

# Save a bar chart to a file
png("gene_counts.png", width = 600, height = 400)
barplot(counts, main = "Toy gene counts", ylab = "Count")
dev.off()

cat("Done — wrote gene_counts.png\n")
