---
name: sctagger
category: single-cell
description: scTagger - Fast and accurate matching of cellular barcodes across short- and long-reads
tags: ["sctagger", "single-cell", "barcode-matching", "RNA-seq"]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/sctagger"
---

## Concepts

- **Tool Overview**: scTagger (v1.1.1) matches cellular barcodes across short- and long-read single-cell RNA-seq experiments.
- **Core Function**: Identifies and matches cellular barcodes from mixed sequencing data.
- **Algorithm**: Uses fuzzy matching for barcode identification across read types.
- **Input/Output**: Accepts FASTQ files and produces barcode-matched reads.
- **Multi-Read Support**: Works with both short-read and long-read sequencing data.
- **Applications**: Single-cell RNA-seq analysis, barcode demultiplexing, and data integration.

## Pitfalls

- **Barcode Quality**: Results depend on barcode quality and diversity.
- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **False Positives**: May incorrectly match barcodes.
- **Barcode Collision**: May struggle with barcode collisions.

## Examples

### Basic barcode matching
**Args:** `sctagger match -i reads.fastq -b barcodes.txt -o matched.fastq`
**Explanation:** `-i` input reads; `-b` barcode list; `-o` matched output.

### With quality filtering
**Args:** `sctagger match -i reads.fastq -b barcodes.txt -q 20 -o matched.fastq`
**Explanation:** `-q 20` filters reads with quality below 20.

### Fuzzy matching
**Args:** `sctagger match -i reads.fastq -b barcodes.txt --fuzzy -o matched.fastq`
**Explanation:** `--fuzzy` enables fuzzy barcode matching.

### Verbose logging
**Args:** `sctagger match -i reads.fastq -b barcodes.txt -v -o matched.fastq`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `sctagger match -i reads.fastq -b barcodes.txt -t 8 -o matched.fastq`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Output statistics
**Args:** `sctagger stats -i matched.fastq -o stats.csv`
**Explanation:** Generates matching statistics.

### Batch processing
**Args:** `sctagger batch -i fastq_dir/ -b barcodes.txt -o output_dir/`
**Explanation:** Processes multiple FASTQ files in batch.