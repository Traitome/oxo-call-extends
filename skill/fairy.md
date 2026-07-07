---
name: fairy
category: metagenomics
description: "fairy calculates all-to-all approximate coverage for multi-sample metagenomic binning > 100x faster than alignment."
tags: [fairy, metagenomics, coverage-calculation, binning, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/fairy"
---

## Concepts

- **Tool Overview**: fairy is a tool for calculating all-to-all approximate coverage for multi-sample metagenomic binning, designed to be over 100x faster than traditional alignment-based methods.
- **Core Function**: Estimates coverage relationships between samples for metagenomic binning without full alignment.
- **Input/Output**: Input: Metagenomic reads (FASTQ), contigs/scaffolds (FASTA). Output: Coverage matrix, binning suggestions.
- **Algorithm**: Uses k-mer based approaches to estimate coverage relationships efficiently.
- **Key Features**: Ultra-fast coverage calculation, multi-sample support, metagenomic binning aid, memory efficient, parallel processing.
- **Installation**: `conda install -c bioconda fairy`

## Pitfalls

- **k-mer Size**: Requires appropriate k-mer size selection.
- **Memory Usage**: May require substantial RAM for large datasets.
- **Accuracy Trade-off**: Approximate method may have lower accuracy than full alignment.
- **Data Quality**: Results depend on input data quality.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic coverage calculation
**Args:** `fairy -r reads.fastq -c contigs.fasta -o coverage_matrix.txt`
**Explanation:** Calculates coverage matrix for metagenomic binning.

### Multi-sample analysis
**Args:** `fairy -r samples/ -c contigs.fasta -o coverage_matrix.txt`
**Explanation:** Processes multiple samples for coverage analysis.

### Custom k-mer size
**Args:** `fairy -r reads.fastq -c contigs.fasta -o coverage_matrix.txt -k 31`
**Explanation:** Uses custom k-mer size for coverage estimation.

### Parallel processing
**Args:** `fairy -r reads.fastq -c contigs.fasta -o coverage_matrix.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Bin coverage
**Args:** `fairy -r reads.fastq -c contigs.fasta -o bin_coverage.txt --bins bins.txt`
**Explanation:** Calculates coverage for predefined bins.