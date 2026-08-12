# fetch-sars2.R — download a tiny public reference genome (SARS-CoV-2, ~30 KB)
# from NCBI's E-utilities, using only base R. From Module 03.
#
# Run with:  Rscript fetch-sars2.R

url <- "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_045512.2&rettype=fasta&retmode=text"

download.file(url, "sars2.fasta", quiet = TRUE)

cat("Downloaded bytes:", file.info("sars2.fasta")$size, "\n")
cat("Header:", readLines("sars2.fasta", n = 1), "\n")

# NOTE: for real biological datasets, use Bioconductor helpers such as GEOquery,
# or example-data packages like 'airway'. Verify current usage in the Bioconductor
# documentation.
