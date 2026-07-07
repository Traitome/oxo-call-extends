---
name: somatem
category: metagenomics
description: Somatem - Best practices pipeline for long-read metagenomics analysis
tags: [somatem, metagenomics, long-reads, pipeline, microbiome]
author: oxo-call-community
source_url: "https://github.com/treangenlab/Somatem"
---

## Concepts

- **Tool Overview**: somatem (v0.7.1) - A long-read metagenomics pipeline
- **Core Function**: Provides best practices for metagenomics analysis
- **Input/Output**: Accepts long-read FASTQ; outputs taxonomic profiles
- **Algorithm**: Integrates multiple tools for metagenomics workflow
- **Installation**: `conda install -c bioconda somatem`
- **Key Features**: Long-read support, taxonomic profiling, pipeline integration

## Pitfalls

- **Input Requirements**: Requires properly formatted long-read FASTQ
- **Database**: Requires taxonomic database for classification
- **Read Quality**: Read quality affects classification accuracy
- **Pipeline Steps**: Multiple pipeline steps require proper configuration
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on pipeline configuration

## Examples

### Display help
**Args:** `somatem --help`
**Explanation:** Shows available options and usage information.

### Basic pipeline run
**Args:** `somatem --input reads.fastq --database kraken_db --output results/`
**Explanation:** Run complete metagenomics pipeline.

### With quality filtering
**Args:** `somatem --input reads.fastq --database kraken_db --output results/ --filter-quality 10`
**Explanation:** Filter reads by quality.

### With read length filter
**Args:** `somatem --input reads.fastq --database kraken_db --output results/ --min-length 1000`
**Explanation:** Filter reads by minimum length.

### Taxonomic profiling
**Args:** `somatem --input reads.fastq --database kraken_db --output results/ --profile`
**Explanation:** Generate taxonomic profile.

### With abundance estimation
**Args:** `somatem --input reads.fastq --database kraken_db --output results/ --abundance`
**Explanation:** Estimate taxonomic abundance.

### Generate report
**Args:** `somatem --input reads.fastq --database kraken_db --output results/ --report`
**Explanation:** Generate pipeline report.

### With threads
**Args:** `somatem --input reads.fastq --database kraken_db --output results/ --threads 8`
**Explanation:** Use multiple threads for pipeline.