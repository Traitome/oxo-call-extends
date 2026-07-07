---
name: simpleaf
category: single-cell
description: simpleaf - Simplified interface for alevin-fry
tags: ["simpleaf", "single-cell", "rnaseq", "rust"]
author: oxo-call-community
source_url: "https://simpleaf.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: simpleaf (v0.24.0) provides a simplified interface for alevin-fry.
- **Core Function**: Runs alevin-fry for single-cell RNA-seq quantification.
- **Algorithm**: Wraps alevin-fry with simplified workflows.
- **Input/Output**: Accepts FASTQ reads and produces gene counts.
- **RNA-seq Quantification**: Specialized for single-cell RNA-seq analysis.
- **Applications**: Single-cell transcriptomics, gene expression analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Dependency Issues**: Requires alevin-fry installation.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Run quantification
**Args:** `simpleaf quant -i reads.fastq -x index/ -o counts/`
**Explanation:** `-i` input FASTQ; `-x` index; `-o` output counts.

### Build index
**Args:** `simpleaf index -t transcripts.fasta -o index/`
**Explanation:** `-t` transcriptome FASTA.

### With sample sheet
**Args:** `simpleaf quant -s samples.csv -o counts/`
**Explanation:** `-s` sample sheet with multiple samples.

### Help command
**Args:** `simpleaf --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simpleaf --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simpleaf -v quant -i reads.fastq -x index/ -o counts/`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `simpleaf quant -t 8 -i reads.fastq -x index/ -o counts/`
**Explanation:** `-t 8` uses 8 threads.
