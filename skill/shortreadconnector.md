---
name: shortreadconnector
category: utility
description: shortreadconnector - Comparison of two read sets
tags: ["shortreadconnector", "utility", "read-comparison", "GATB"]
author: oxo-call-community
source_url: "https://github.com/GATB/short_read_connector"
---

## Concepts

- **Tool Overview**: shortreadconnector (v1.1.3) enables comparison of two read sets using k-mer analysis.
- **Core Function**: Identifies common sequences and differences between read datasets.
- **Algorithm**: Uses k-mer based comparison approach from the GATB library.
- **Input/Output**: Accepts FASTQ files and produces comparison statistics.
- **Read Comparison**: Focuses on identifying shared sequences between datasets.
- **Applications**: Metagenomics analysis, read deduplication, and sequence comparison.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment of k-mer size.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Compare read sets
**Args:** `shortreadconnector -a reads_a.fastq -b reads_b.fastq -o results.txt`
**Explanation:** `-a/-b` input read sets; `-o` output results.

### With k-mer size
**Args:** `shortreadconnector -a reads_a.fastq -b reads_b.fastq -k 31 -o results.txt`
**Explanation:** `-k 31` k-mer size.

### Verbose logging
**Args:** `shortreadconnector -v -a reads_a.fastq -b reads_b.fastq -o results.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shortreadconnector --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shortreadconnector --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shortreadconnector -t 8 -a reads_a.fastq -b reads_b.fastq -o results.txt`
**Explanation:** `-t 8` uses 8 threads.

### Output format
**Args:** `shortreadconnector -a reads_a.fastq -b reads_b.fastq -f csv -o results.csv`
**Explanation:** `-f csv` CSV output format.
