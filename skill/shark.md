---
name: shark
category: alignment
description: shark - Mapping-free filtering of useless RNA-Seq reads
tags: ["shark", "alignment", "RNA-seq", "filtering"]
author: oxo-call-community
source_url: "https://algolab.github.io/shark/"
---

## Concepts

- **Tool Overview**: shark (v1.2.0) performs mapping-free filtering of RNA-Seq reads.
- **Core Function**: Filters useless reads without mapping to reference.
- **Algorithm**: Uses k-mer based approach for read filtering.
- **Input/Output**: Accepts FASTQ reads and produces filtered reads.
- **Read Filtering**: Focuses on removing low-quality or uninformative reads.
- **Applications**: RNA-seq analysis, preprocessing, and NGS data cleaning.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.
- **k-mer Size**: Choosing appropriate k-mer size is critical.

## Examples

### Filter reads
**Args:** `shark -i reads.fastq -o filtered.fastq`
**Explanation:** `-i` input reads; `-o` output filtered reads.

### With k-mer size
**Args:** `shark -i reads.fastq -k 25 -o filtered.fastq`
**Explanation:** `-k 25` k-mer size.

### Paired-end
**Args:** `shark -1 reads_1.fastq -2 reads_2.fastq -o filtered/`
**Explanation:** `-1/-2` paired-end reads.

### Verbose logging
**Args:** `shark -v -i reads.fastq -o filtered.fastq`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shark --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shark --version`
**Explanation:** Shows current version.

### Stats output
**Args:** `shark -i reads.fastq -o filtered.fastq -s stats.txt`
**Explanation:** `-s` output statistics file.