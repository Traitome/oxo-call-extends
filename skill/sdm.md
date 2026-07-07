---
name: sdm
category: sequence-analysis
description: sdm - Simple demultiplex tool for FASTQ demultiplexing and dereplication
tags: ["sdm", "sequence-analysis", "demultiplexing", "FASTQ"]
author: oxo-call-community
source_url: "https://github.com/hildebra/sdm"
---

## Concepts

- **Tool Overview**: sdm (v3.27) is a simple demultiplex tool for FASTQ demultiplexing and dereplication.
- **Core Function**: Demultiplexes and dereplicates FASTQ sequencing data.
- **Algorithm**: Uses barcode matching for demultiplexing and sequence comparison for dereplication.
- **Input/Output**: Accepts FASTQ files and produces demultiplexed/dereplicated outputs.
- **Multi-Purpose**: Combines demultiplexing and dereplication in one tool.
- **Applications**: Sequencing data processing, quality control, and data reduction.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Barcode Quality**: Results depend on barcode quality and diversity.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **False Positives**: May incorrectly assign reads to samples.
- **Computational Resources**: May require significant compute resources.
- **Barcode Collision**: May struggle with barcode collisions.

## Examples

### Basic demultiplexing
**Args:** `sdm demux -i reads.fastq -b barcodes.txt -o demux/`
**Explanation:** `-i` input FASTQ; `-b` barcode file; `-o` output directory.

### Dereplication
**Args:** `sdm derep -i reads.fastq -o dereplicated.fastq`
**Explanation:** Dereplicates sequences to unique reads.

### Combined operation
**Args:** `sdm process -i reads.fastq -b barcodes.txt -o output/`
**Explanation:** Performs both demultiplexing and dereplication.

### Quality filtering
**Args:** `sdm demux -i reads.fastq -b barcodes.txt -q 20 -o demux/`
**Explanation:** `-q 20` filters reads with quality below 20.

### Verbose logging
**Args:** `sdm demux -i reads.fastq -b barcodes.txt -v -o demux/`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `sdm demux -i reads.fastq -b barcodes.txt -t 8 -o demux/`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `sdm --help`
**Explanation:** Shows available commands and options.