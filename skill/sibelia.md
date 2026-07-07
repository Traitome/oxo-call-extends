---
name: sibelia
category: utility
description: Sibelia - Genome comparison via de Bruijn graph
tags: ["sibelia", "utility", "genome-comparison", "de-bruijn"]
author: oxo-call-community
source_url: "https://github.com/bioinf/Sibelia"
---

## Concepts

- **Tool Overview**: Sibelia (v3.0.7) performs whole-genome comparison using de Bruijn graphs.
- **Core Function**: Aligns multiple genomes and identifies syntenic regions.
- **Algorithm**: Uses de Bruijn graph construction for efficient comparison.
- **Input/Output**: Accepts multiple FASTA files and produces alignment results.
- **Genome Comparison**: Focuses on identifying conserved and variable regions.
- **Applications**: Comparative genomics, evolutionary analysis, and pan-genomics.

## Pitfalls

- **Memory Usage**: Very high memory requirements for large genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment of k-mer size.
- **Input Size**: Performance degrades with many large genomes.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Compare genomes
**Args:** `sibelia -o output/ genome1.fasta genome2.fasta genome3.fasta`
**Explanation:** `-o` output directory; input genomes.

### With k-mer size
**Args:** `sibelia -k 25 -o output/ genome1.fasta genome2.fasta`
**Explanation:** `-k 25` k-mer size.

### With reference
**Args:** `sibelia -r reference.fasta -o output/ genomes.fasta`
**Explanation:** `-r` reference genome.

### Help command
**Args:** `sibelia --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sibelia --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sibelia -v -o output/ genomes.fasta`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sibelia -t 8 -o output/ genomes.fasta`
**Explanation:** `-t 8` uses 8 threads.
