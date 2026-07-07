---
name: confindr
category: qc
description: Detect bacterial contamination in NGS reads
tags: [confindr, contamination, quality-control, ngs, bacterial-genomics]
author: oxo-call-community
source_url: "https://OLC-Bioinformatics.github.io/ConFindr"
---

## Concepts

- **Tool Overview**: ConFindr is a tool for detecting both intra- and inter-species bacterial contamination in next-generation sequencing reads, ensuring data quality for downstream analysis.
- **Core Function**: Identifies contamination by analyzing sequence composition, coverage patterns, and taxonomic signatures in bacterial NGS data.
- **Algorithm**: Uses k-mer based approaches and reference database comparisons to detect foreign sequences.
- **Input**: Bacterial sequencing reads in FASTQ format (Illumina, Nanopore, or PacBio).
- **Output**: Contamination report with identified contaminants and confidence scores.
- **Application**: Bacterial genome sequencing QC, isolate purity verification, and metagenomic sample validation.
- **Installation**: Install via bioconda: `conda install -c bioconda confindr`

## Pitfalls

- **Reference Database**: Detection accuracy depends on completeness of reference databases.
- **Contamination Level**: Low-level contamination may be difficult to detect.
- **Closely Related Strains**: Intra-species contamination harder to distinguish than inter-species.
- **Sequencing Errors**: High error rates may produce false positives.
- **Mixed Cultures**: Intentional mixed cultures will be flagged as contaminated.

## Examples

### Detect contamination in reads
**Args:** `confindr -i reads.fastq -o contamination_report/`
**Explanation:** Analyzes sequencing reads for bacterial contamination.

### With custom database
**Args:** `confindr -i reads.fastq -d custom_db/ -o contamination_report/`
**Explanation:** Uses custom reference database for contamination detection.

### Set detection threshold
**Args:** `confindr -i reads.fastq -t 0.05 -o contamination_report/`
**Explanation:** Sets contamination detection threshold to 5%.

### Display help
**Args:** `confindr --help`
**Explanation:** Shows all available options and usage information.