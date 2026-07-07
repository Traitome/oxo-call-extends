---
name: fur
category: utility
description: Find unique genomic regions from target and neighbor genomes.
tags: [fur, comparative genomics, unique regions, genome analysis]
author: oxo-call-community
source_url: "https://github.com/evolbioinf/fur"
---

## Concepts
- **Unique Region Detection**: Identifies regions unique to a target genome.
- **Comparative Genomics**: Compares target genome with related genomes.
- **Genomic Islands**: Detects genomic islands and unique sequences.
- **Sequence Comparison**: Compares sequences across multiple genomes.
- **Targeted Analysis**: Focuses on finding species-specific regions.

## Pitfalls
- **Memory Requirements**: High memory usage for large genome comparisons.
- **Computational Time**: Comparisons can be time-consuming.
- **Genome Quality**: Requires high-quality genome assemblies.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **Output Interpretation**: Results require careful interpretation.

## Examples
### Find unique regions
**Args:** `fur -t target.fasta -n neighbor1.fasta neighbor2.fasta -o unique.bed`
**Explanation:** Finds regions unique to target genome.

### With multiple neighbors
**Args:** `fur -t target.fasta -n *.fasta -o unique.bed`
**Explanation:** Compares target with multiple neighbor genomes.

### Output sequence
**Args:** `fur -t target.fasta -n neighbor.fasta --seq -o unique.fasta`
**Explanation:** Outputs sequences of unique regions.

### Filter by size
**Args:** `fur -t target.fasta -n neighbor.fasta -m 1000 -o unique.bed`
**Explanation:** Only outputs regions >= 1000bp.

### Verbose mode
**Args:** `fur -t target.fasta -n neighbor.fasta -v -o unique.bed`
**Explanation:** Runs in verbose mode with detailed output.