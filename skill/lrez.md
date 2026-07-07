---
name: lrez
category: programming
description: Standalone tool and library allowing to work with barcoded linked-reads
tags: [lrez, programming, linked-reads, barcodes]
author: oxo-call-community
source_url: "https://github.com/morispi/LRez"
---

## Concepts

- **Tool Overview**: lrez v2.2.4 is a standalone tool and library for working with barcoded linked-reads data from technologies like 10X Genomics.
- **Core Function**: Processes and analyzes barcoded linked-reads to extract barcode information, phase reads, and perform haplotype-aware analysis.
- **Barcode Extraction**: Extracts and decodes barcodes from linked-read sequences for downstream analysis.
- **Input/Output**: Input: FASTQ/BAM files with barcoded reads; Output: Processed reads, barcode files, phased variants.
- **Installation**: `conda install -c bioconda lrez` or build from source.
- **Key Features**: Supports read processing, barcode extraction, haplotype phasing, and integration with variant callers.

## Pitfalls

- **Barcode Quality**: Low-quality barcodes can lead to incorrect read grouping and phasing errors.
- **Input Format**: Requires specific FASTQ format with barcode information in read headers.
- **Memory Usage**: Processing large datasets may require significant memory resources.
- **Version Compatibility**: Options and output formats may change between versions.
- **Reference Genome**: Phasing accuracy depends on the quality and completeness of the reference genome.
- **Read Length**: Performance may degrade with very short or very long reads.

## Examples

### Process linked-reads
**Args:** `lrez process -i reads.fastq -o processed_reads/`
**Explanation:** Processes barcoded linked-reads and outputs processed data.

### Extract barcodes
**Args:** `lrez extract -i reads.fastq -o barcodes.txt`
**Explanation:** Extracts barcodes from linked-read sequences into a separate file.

### Phase reads
**Args:** `lrez phase -i aligned.bam -v variants.vcf -o phased.bam`
**Explanation:** Phases aligned reads using known variant information.

### Barcode statistics
**Args:** `lrez stats -i reads.fastq -o stats.txt`
**Explanation:** Generates statistics about barcode distribution and quality.

### Filter low-quality barcodes
**Args:** `lrez filter -i reads.fastq -o filtered.fastq -q 20`
**Explanation:** Filters out reads with low-quality barcodes (Phred quality < 20).

### Help documentation
**Args:** `lrez --help`
**Explanation:** Displays all available commands and options.