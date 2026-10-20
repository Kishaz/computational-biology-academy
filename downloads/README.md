# Practice pack

Small, safe starter files for practising the Academy modules.

| File | What it is | Honest note |
| --- | --- | --- |
| `metadata_template.csv` | A study-design table (sample, group, replicate, condition, FASTQ names) | A template to copy and adapt, not data from any real study. |
| `toy_reads_R1.fastq`, `toy_reads_R2.fastq` | Six tiny paired reads | **Synthetic**. Made-up sequences for format practice only, not real biology. |
| `get_reference.sh` | A reproducible script that downloads a real reference genome (SARS-CoV-2, RefSeq `NC_045512.2`) from NCBI | Pinned accession. Verify it is current against NCBI if the download fails. |

Real sequencing datasets are deliberately kept out of this repository. The honest,
reproducible way to get them is a small download script like `get_reference.sh`,
so anyone can recreate the exact inputs. The single-cell and spatial modules use
their own datasets suited to those methods, not the bulk FASTQ data above.
