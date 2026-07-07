---
name: sizemeup
category: utility
description: sizemeup - Genome size estimation tool
tags: ["sizemeup", "utility", "genome-size", "estimation"]
author: oxo-call-community
source_url: "https://github.com/rpetit3/sizemeup"
---

## Concepts

- **Tool Overview**: sizemeup (v1.3.0) estimates genome size from sequencing data.
- **Core Function**: Calculates genome size using k-mer analysis.
- **Algorithm**: Uses k-mer frequency distribution for estimation.
- **Input/Output**: Accepts FASTQ reads and produces size estimates.
- **Genome Size Estimation**: Specialized for sequencing data analysis.
- **Applications**: Genome sequencing projects, assembly planning.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Estimate genome size
**Args:** `sizemeup -i reads.fastq -o estimate.txt`
**Explanation:** `-i` input FASTQ; `-o` output estimate.

### With k-mer size
**Args:** `sizemeup -i reads.fastq -k 31 -o estimate.txt`
**Explanation:** `-k 31` k-mer size.

### Multiple files
**Args:** `sizemeup -i reads_1.fastq -i reads_2.fastq -o estimate.txt`
**Explanation:** Process paired-end reads.

### Help command
**Args:** `sizemeup --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sizemeup --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sizemeup -v -i reads.fastq -o estimate.txt`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sizemeup -t 8 -i reads.fastq -o estimate.txt`
**Explanation:** `-t 8` uses 8 threads.
