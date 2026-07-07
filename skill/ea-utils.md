---
name: ea-utils
category: utility
description: "Command-line tools for processing biological sequencing data."
tags: [ea-utils, utility, sequencing-data, FASTQ, quality-control]
author: oxo-call-community
source_url: "https://expressionanalysis.github.io/ea-utils/"
---

## Concepts

- **Tool Overview**: ea-utils is a collection of command-line tools for processing and quality control of biological sequencing data.
- **Core Function**: Provides utilities for FASTQ manipulation, quality filtering, adapter trimming, and sequence conversion.
- **Input/Output**: Input: FASTQ files. Output: Filtered/processed FASTQ, FASTA, or other sequence formats.
- **Algorithm**: Implements efficient sequence parsing and filtering algorithms for high-throughput sequencing data.
- **Key Features**: FASTQ quality filtering, adapter trimming, sequence conversion, duplicate removal, barcode demultiplexing.
- **Installation**: `conda install -c bioconda ea-utils`

## Pitfalls

- **Memory Usage**: Processing large FASTQ files requires significant RAM.
- **Quality Thresholds**: Default quality thresholds may need adjustment for specific datasets.
- **Adapter Sequences**: Requires correct adapter sequences for trimming.
- **Compression**: Input/output compression may affect performance.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Fastq quality filter
**Args:** `fastq-mcf adapters.fa input.fastq -o output.fastq`
**Explanation:** Filters and trims FASTQ reads using adapter sequences.

### Convert FASTQ to FASTA
**Args:** `fastq-to-fasta input.fastq output.fasta`
**Explanation:** Converts FASTQ format to FASTA format.

### Quality filtering
**Args:** `fastq-mcf -q 20 -l 30 input.fastq -o output.fastq`
**Explanation:** Filters reads with quality score < 20 and length < 30.

### Remove duplicates
**Args:** `fastq-dedup input.fastq output.fastq`
**Explanation:** Removes duplicate sequences from FASTQ file.

### Merge paired-end reads
**Args:** `fastq-join read1.fastq read2.fastq -o merged.fastq`
**Explanation:** Merges overlapping paired-end reads.