---
name: snp-pipeline
category: variant-analysis
description: SNP-Pipeline - Scripts and functions for SNP matrix construction
tags: [snp-pipeline, variant-analysis, snps, matrix, pipeline]
author: oxo-call-community
source_url: "https://github.com/CFSAN-Biostatistics/snp-pipeline"
---

## Concepts

- **Tool Overview**: snp-pipeline (v2.2.1) - A pipeline for SNP matrix construction
- **Core Function**: Builds SNP matrices from multiple samples
- **Input/Output**: Accepts VCF files; outputs SNP matrices
- **Algorithm**: Integrates SNP calling and matrix assembly
- **Installation**: `conda install -c bioconda snp-pipeline`
- **Key Features**: Matrix construction, multi-sample, pipeline integration

## Pitfalls

- **Input Requirements**: Requires properly formatted VCF files
- **Sample Matching**: Samples must be properly matched
- **Matrix Size**: Large matrices require significant memory
- **Missing Data**: Missing SNPs affect matrix quality
- **Filtering**: Requires proper filtering for quality SNPs
- **Output Format**: Multiple output formats available

## Examples

### Display help
**Args:** `snp-pipeline --help`
**Explanation:** Shows available options and usage information.

### Basic matrix construction
**Args:** `snp-pipeline -i vcfs/ -o snp_matrix.csv`
**Explanation:** Build SNP matrix from VCF files.

### With reference
**Args:** `snp-pipeline -i vcfs/ -r reference.fasta -o snp_matrix.csv`
**Explanation:** Use reference for matrix construction.

### Filter by quality
**Args:** `snp-pipeline -i vcfs/ -o snp_matrix.csv --min-quality 20`
**Explanation:** Filter SNPs by minimum quality.

### Filter by coverage
**Args:** `snp-pipeline -i vcfs/ -o snp_matrix.csv --min-coverage 10`
**Explanation:** Filter SNPs by minimum coverage.

### Output format
**Args:** `snp-pipeline -i vcfs/ -o snp_matrix.tsv --format tsv`
**Explanation:** Output matrix in TSV format.

### With phylogeny
**Args:** `snp-pipeline -i vcfs/ -o snp_matrix.csv --phylogeny`
**Explanation:** Generate phylogeny from SNP matrix.

### Generate report
**Args:** `snp-pipeline -i vcfs/ -o snp_matrix.csv --report`
**Explanation:** Generate pipeline report.