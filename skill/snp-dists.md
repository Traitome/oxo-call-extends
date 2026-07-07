---
name: snp-dists
category: variant-analysis
description: SNP-Dists - Convert FASTA alignment to SNP distance matrix
tags: [snp-dists, variant-analysis, alignment, distance-matrix, snps]
author: oxo-call-community
source_url: "https://github.com/tseemann/snp-dists"
---

## Concepts

- **Tool Overview**: snp-dists (v1.2.0) - A tool for calculating SNP distances from alignments
- **Core Function**: Converts multi-FASTA alignments to pairwise SNP distance matrices
- **Input/Output**: Accepts FASTA alignments; outputs distance matrix in CSV/TSV
- **Algorithm**: Counts SNP differences between aligned sequences
- **Installation**: `conda install -c bioconda snp-dists`
- **Key Features**: SNP distance calculation, matrix output, fast processing

## Pitfalls

- **Input Requirements**: Requires properly aligned FASTA sequences
- **Alignment Quality**: Poor alignments produce inaccurate distances
- **Missing Data**: Gaps and missing data affect distance calculation
- **Reference Choice**: Choice of reference affects SNP counting
- **Output Format**: Multiple output formats available
- **Large Alignments**: Large alignments can be slow to process

## Examples

### Display help
**Args:** `snp-dists --help`
**Explanation:** Shows available options and usage information.

### Basic distance matrix
**Args:** `snp-dists alignment.fasta > distances.csv`
**Explanation:** Calculate SNP distances from alignment.

### With output file
**Args:** `snp-dists alignment.fasta -o distances.tsv`
**Explanation:** Output distances to TSV file.

### With reference
**Args:** `snp-dists alignment.fasta -r reference.fasta > distances.csv`
**Explanation:** Use reference for SNP counting.

### CSV format
**Args:** `snp-dists alignment.fasta -f csv > distances.csv`
**Explanation:** Output in CSV format.

### TSV format
**Args:** `snp-dists alignment.fasta -f tsv > distances.tsv`
**Explanation:** Output in TSV format.

### With labels
**Args:** `snp-dists alignment.fasta --labels > distances.csv`
**Explanation:** Include sequence labels in output.

### Filter by distance
**Args:** `snp-dists alignment.fasta --max-distance 100 > distances.csv`
**Explanation:** Filter distances by maximum threshold.