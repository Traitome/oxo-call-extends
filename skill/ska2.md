---
name: ska2
category: sequence-analysis
description: SKA2 - Split Kmer Analysis version 2
tags: ["ska2", "sequence-analysis", "k-mer", "comparative"]
author: oxo-call-community
source_url: "https://github.com/bacpop/ska.rust"
---

## Concepts

- **Tool Overview**: SKA2 (v0.5.1) performs split k-mer analysis for comparative genomics.
- **Core Function**: Analyzes k-mer profiles across multiple genomes.
- **Algorithm**: Uses split k-mer approach for efficient comparison.
- **Input/Output**: Accepts FASTA sequences and produces k-mer profiles.
- **K-mer Analysis**: Specialized for bacterial genome comparison.
- **Applications**: Phylogenetics, population genomics, outbreak analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Input Quality**: Results depend on sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Build k-mer profile
**Args:** `ska2 build -i genome.fasta -o profile.ska`
**Explanation:** `-i` input genome; `-o` output profile.

### Compare profiles
**Args:** `ska2 compare -i profiles/ -o distances.txt`
**Explanation:** Compares multiple k-mer profiles.

### Build tree
**Args:** `ska2 tree -i distances.txt -o tree.nwk`
**Explanation:** Builds phylogenetic tree from distances.

### Help command
**Args:** `ska2 --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `ska2 --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `ska2 -v build -i genome.fasta -o profile.ska`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `ska2 -t 8 build -i genome.fasta -o profile.ska`
**Explanation:** `-t 8` uses 8 threads.
