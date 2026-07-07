---
name: ncrf
category: utility
description: Noise-Cancelling Repeat Finder (NCRF) uncovers tandem repeats in error-prone long-read sequencing data.
tags: [ncrf, utility, tandem-repeats, long-reads, sequencing]
author: oxo-call-community
source_url: "https://github.com/makovalab-psu/NoiseCancellingRepeatFinder"
---

## Concepts

- **Tool Overview**: NCRF is a tool for detecting tandem repeats in noisy long-read sequencing data.
- **Core Function**: Identifies tandem repeat regions while accounting for high error rates in long reads.
- **Algorithm**: Uses a hidden Markov model approach to distinguish repeat patterns from sequencing errors.
- **Input Format**: Accepts FASTA files containing long-read sequences.
- **Output**: Produces annotations of tandem repeat regions with repeat unit information.
- **Use Case**: Analyzing repeat-rich genomic regions, microsatellite analysis, and structural variation detection.

## Pitfalls

- **High Error Data**: Performance depends on input read quality.
- **Computational Cost**: Can be slow for large genomes.
- **Memory Usage**: Processing large datasets requires significant memory.
- **Version Differences**: Options may vary between versions.
- **Repeat Complexity**: May struggle with complex nested repeats.
- **False Positives**: Can report false positives in low-complexity regions.

## Examples

### Display help
**Args:** `ncrf --help`
**Explanation:** Shows available options and usage instructions.

### Basic repeat finding
**Args:** `ncrf input.fasta -o repeats.gff`
**Explanation:** Detects tandem repeats in input sequences.

### Custom repeat unit
**Args:** `ncrf input.fasta -u ATG -o repeats.gff`
**Explanation:** Searches for specific repeat unit pattern.

### Minimum repeat length
**Args:** `ncrf input.fasta -m 5 -o repeats.gff`
**Explanation:** Sets minimum repeat unit length to 5bp.

### Verbose output
**Args:** `ncrf input.fasta -v -o repeats.gff`
**Explanation:** Produces verbose output with detailed information.

### Threads
**Args:** `ncrf input.fasta -t 4 -o repeats.gff`
**Explanation:** Uses 4 threads for parallel processing.