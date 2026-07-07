---
name: seqcomplexity
category: sequence-analysis
description: seqcomplexity - Calculates sequence complexity from FastQ files
tags: ["seqcomplexity", "sequence-analysis", "complexity", "FASTQ"]
author: oxo-call-community
source_url: "https://github.com/stevenweaver/seqcomplexity"
---

## Concepts

- **Tool Overview**: seqcomplexity (v0.1.2) calculates per-read and total sequence complexity from FastQ files.
- **Core Function**: Measures sequence complexity to identify low-complexity regions.
- **Algorithm**: Implements various complexity metrics for sequence analysis.
- **Input/Output**: Accepts FASTQ files and produces complexity scores.
- **Complexity Analysis**: Focuses on measuring sequence complexity.
- **Applications**: Quality control, filtering low-complexity reads, and sequence analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large FASTQ files.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Format**: Requires correct FASTQ format.
- **Performance**: May be slow for very large files.
- **Documentation**: Some features have limited documentation.

## Examples

### Calculate complexity
**Args:** `seqcomplexity -i reads.fastq -o complexity.txt`
**Explanation:** `-i` input FASTQ; `-o` output file.

### Per-read complexity
**Args:** `seqcomplexity -i reads.fastq -p -o per_read.txt`
**Explanation:** `-p` outputs per-read complexity.

### Threshold filtering
**Args:** `seqcomplexity -i reads.fastq -t 0.5 -o filtered.txt`
**Explanation:** `-t 0.5` filters reads below complexity threshold.

### Verbose logging
**Args:** `seqcomplexity -i reads.fastq -v -o complexity.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqcomplexity --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqcomplexity --version`
**Explanation:** Shows current version.

### Summary statistics
**Args:** `seqcomplexity -i reads.fastq -s -o summary.txt`
**Explanation:** `-s` outputs summary statistics only.