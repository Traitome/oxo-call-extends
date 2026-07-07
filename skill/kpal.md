---
name: kpal
category: kmer
description: Analysis toolkit and programming library for k-mer profiles
tags: [kpal, kmer, k-mer, profiling, library]
author: oxo-call-community
source_url: "https://kpal.readthedocs.org"
---

## Concepts

- **K-mer Profiling**: Analyzes and profiles k-mer distributions
- **Programming Library**: Provides library functions for k-mer analysis
- **Profile Comparison**: Compares k-mer profiles between samples
- **Statistics**: Calculates k-mer frequency statistics
- **Data Structures**: Implements efficient k-mer data structures
- **Scripting Support**: Supports integration with analysis pipelines

## Pitfalls

- **K-mer Size**: Different k-mer sizes give different perspectives
- **Memory Usage**: Large k-mer datasets require significant memory
- **Hash Collisions**: Hash collisions affect counting accuracy
- **Profile Normalization**: Proper normalization is needed for comparison
- **Error Rates**: Sequencing errors create spurious k-mers
- **Duplicate k-mers**: Identical k-mers from different origins

## Examples

### Analyze k-mer profile
**Args:** `kpal profile -i reads.fastq -k 21 -o profile.txt`
**Explanation:** Analyzes k-mer profile from sequencing reads.

### Compare profiles
**Args:** `kpal compare -p profile1.txt -p profile2.txt -o comparison.txt`
**Explanation:** Compares two k-mer profiles.

### Filter k-mers
**Args:** `kpal filter -i profile.txt --min-count 5 -o filtered.txt`
**Explanation:** Filters k-mers by minimum count.

### Calculate statistics
**Args:** `kpal stats -i profile.txt -o statistics.txt`
**Explanation:** Calculates statistical metrics for profile.

### Export histogram
**Args:** `kpal histogram -i profile.txt -o hist.txt`
**Explanation:** Exports k-mer frequency histogram.

### Batch processing
**Args:** `kpal batch -d profiles/ -o results/`
**Explanation:** Processes multiple k-mer profiles.