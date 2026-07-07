---
name: short-read-connector
category: utility
description: short-read-connector - Comparison of two read sets
tags: ["short-read-connector", "utility", "read-comparison", "GATB"]
author: oxo-call-community
source_url: "https://github.com/GATB/short_read_connector"
---

## Concepts

- **Tool Overview**: short-read-connector (v1.2.0) enables comparison of two read sets.
- **Core Function**: Identifies common sequences between read datasets.
- **Algorithm**: Uses k-mer based comparison approach.
- **Input/Output**: Accepts FASTQ files and produces comparison results.
- **Read Comparison**: Focuses on identifying shared sequences.
- **Applications**: Metagenomics, read deduplication, and sequence comparison.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Compare read sets
**Args:** `short-read-connector -a reads_a.fastq -b reads_b.fastq -o results.txt`
**Explanation:** `-a/-b` input read sets; `-o` output results.

### With k-mer size
**Args:** `short-read-connector -a reads_a.fastq -b reads_b.fastq -k 31 -o results.txt`
**Explanation:** `-k 31` k-mer size.

### Verbose logging
**Args:** `short-read-connector -v -a reads_a.fastq -b reads_b.fastq -o results.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `short-read-connector --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `short-read-connector --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `short-read-connector -t 8 -a reads_a.fastq -b reads_b.fastq -o results.txt`
**Explanation:** `-t 8` uses 8 threads.

### Output format
**Args:** `short-read-connector -a reads_a.fastq -b reads_b.fastq -f csv -o results.csv`
**Explanation:** `-f csv` CSV output format.