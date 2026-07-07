---
name: sherpas
category: population-genomics
description: sherpas - Recombination detection in phylogenies
tags: ["sherpas", "population-genomics", "phylogeny", "recombination"]
author: oxo-call-community
source_url: "https://github.com/phylo42/sherpas"
---

## Concepts

- **Tool Overview**: sherpas (v1.0.2) screens historical recombination events in phylogenies.
- **Core Function**: Identifies recombination events using ancestral sequences.
- **Algorithm**: Uses phylogenetic methods for recombination detection.
- **Input/Output**: Accepts sequence alignments and produces recombination predictions.
- **Phylogenetics**: Focuses on evolutionary analysis and recombination detection.
- **Applications**: Population genetics, evolutionary biology, and comparative genomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequence alignment quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Run analysis
**Args:** `sherpas -i alignment.fasta -o results/`
**Explanation:** `-i` input alignment; `-o` output directory.

### With tree
**Args:** `sherpas -i alignment.fasta -t tree.newick -o results/`
**Explanation:** `-t` phylogenetic tree file.

### Verbose logging
**Args:** `sherpas -v -i alignment.fasta -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `sherpas --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sherpas --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `sherpas -t 8 -i alignment.fasta -o results/`
**Explanation:** `-t 8` uses 8 threads.

### Ancestral sequences
**Args:** `sherpas -i alignment.fasta -a ancestral.fasta -o results/`
**Explanation:** `-a` ancestral sequences file.