---
name: nonpareil
category: metagenomics
description: Nonpareil estimates average coverage and creates diversity curves for metagenomic datasets.
tags: [nonpareil, metagenomics, coverage, diversity]
author: oxo-call-community
source_url: "https://github.com/lmrodriguezr/nonpareil"
---

## Concepts

- **Tool Overview**: Nonpareil estimates sequencing coverage and diversity in metagenomic data.
- **Core Function**: Computes coverage estimates and generates diversity curves.
- **Algorithm**: Uses k-mer based approach for coverage estimation.
- **Input Format**: Accepts FASTQ/FASTA reads from metagenomic sequencing.
- **Output**: Produces coverage estimates and diversity curves.
- **Use Case**: Metagenomics analysis, sequencing depth assessment, and diversity estimation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Data Quality**: Results depend on input data quality.
- **Interpretation**: Requires understanding of coverage metrics.

## Examples

### Display help
**Args:** `nonpareil --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `nonpareil -i reads.fastq -o output/`
**Explanation:** Runs coverage and diversity analysis.

### Specify k-mer size
**Args:** `nonpareil -i reads.fastq -k 25 -o output/`
**Explanation:** Uses k-mer size of 25.

### Paired-end reads
**Args:** `nonpareil -i reads_1.fastq -i2 reads_2.fastq -o output/`
**Explanation:** Processes paired-end reads.

### Threads
**Args:** `nonpareil -i reads.fastq -t 8 -o output/`
**Explanation:** Uses 8 threads for parallel processing.

### Output plot
**Args:** `nonpareil -i reads.fastq -o output/ --plot`
**Explanation:** Generates coverage curve plot.

### Estimate coverage only
**Args:** `nonpareil -i reads.fastq -o coverage.txt --estimate-only`
**Explanation:** Only estimates coverage without full analysis.