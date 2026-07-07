---
name: illumina-utils
category: programming
description: A library and collection of scripts to work with Illumina paired-end data (for CASAVA 1.8+).
tags: [illumina-utils, programming, paired-end, fastq]
author: oxo-call-community
source_url: "https://github.com/meren/illumina-utils"
---

## Concepts

- **Tool Overview**: illumina-utils (v2.13) - A Python library and set of command-line scripts for processing Illumina paired-end sequencing data
- **Core Function**: Handles demultiplexing, quality filtering, and format conversion for CASAVA 1.8+ data
- **Input/Output**: Processes Illumina FASTQ files, supports various output formats including QIIME-compatible formats
- **Installation**: `conda install -c bioconda illumina-utils` or from GitHub source
- **Key Features**: Dual-index support, quality score conversion, and sample metadata management

## Pitfalls

- **CASAVA Version**: Designed for CASAVA 1.8+; older versions may require preprocessing
- **Paired-End Requirement**: Assumes paired-end data; single-end files need special handling
- **Memory Constraints**: Processing large datasets requires sufficient system memory
- **Barcode Mismatch**: Strict barcode matching may discard valid reads
- **Compression Issues**: Mixed compressed/uncompressed files can cause processing errors

## Examples

### Demultiplex paired-end reads
**Args:** `iu-demultiplex -i input/ -o output/ -b barcodes.txt --paired-end`
**Explanation:** Demultiplexes paired-end reads using specified barcode file.

### Filter by quality score
**Args:** `iu-filter-quality -i reads.fastq -o filtered.fastq -q 20`
**Explanation:** Filters reads keeping only those with average quality score >= 20.

### Convert quality scores
**Args:** `iu-convert-quality -i input.fastq -o output.fastq --phred64-to-33`
**Explanation:** Converts Phred-64 quality scores to Phred-33 format.

### Extract barcode statistics
**Args:** `iu-barcode-stats -i fastq/ -o stats/ --detailed`
**Explanation:** Generates detailed barcode usage statistics across samples.

### Merge paired-end files
**Args:** `iu-merge-pairs -i r1.fastq r2.fastq -o merged.fastq`
**Explanation:** Merges overlapping paired-end reads into single sequences.

### Generate sample summary
**Args:** `iu-sample-summary -i demultiplexed/ -o summary.csv`
**Explanation:** Creates summary CSV with read counts and quality metrics per sample.