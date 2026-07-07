---
name: sdust
category: sequence-analysis
description: sdust - Symmetric DUST for finding low-complexity regions in DNA sequences
tags: ["sdust", "sequence-analysis", "low-complexity", "DNA"]
author: oxo-call-community
source_url: "https://github.com/lh3/sdust"
---

## Concepts

- **Tool Overview**: sdust (v0.1) is a tool for finding low-complexity regions in DNA sequences using Symmetric DUST.
- **Core Function**: Identifies low-complexity regions in DNA sequences.
- **Algorithm**: Uses the DUST algorithm for sequence complexity analysis.
- **Input/Output**: Accepts FASTA/FASTQ files and produces annotation of low-complexity regions.
- **Symmetric DUST**: Improved version of the original DUST algorithm.
- **Applications**: Sequence analysis, repeat masking, and quality control.

## Pitfalls

- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Sensitivity**: May miss some low-complexity regions with default parameters.
- **Specificity**: May flag non-repetitive regions as low-complexity.
- **Output Format**: Output may require further processing.
- **Documentation**: Some features have limited documentation.
- **Performance**: May be slow for very large sequences.

## Examples

### Basic analysis
**Args:** `sdust -i input.fasta -o output.bed`
**Explanation:** `-i` input FASTA; `-o` output BED file.

### With threshold
**Args:** `sdust -i input.fasta -t 10 -o output.bed`
**Explanation:** `-t 10` sets complexity threshold.

### Output to stdout
**Args:** `sdust input.fasta`
**Explanation:** Outputs results to standard output.

### Verbose logging
**Args:** `sdust -v -i input.fasta -o output.bed`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sdust --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sdust --version`
**Explanation:** Shows current version.

### Window size
**Args:** `sdust -i input.fasta -w 64 -o output.bed`
**Explanation:** `-w 64` sets window size for analysis.