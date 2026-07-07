---
name: sepp
category: phylogenetics
description: sepp - SATe-enabled phylogenetic placement
tags: ["sepp", "phylogenetics", "phylogenetic-placement", "evolution"]
author: oxo-call-community
source_url: "https://github.com/smirarab/sepp"
---

## Concepts

- **Tool Overview**: sepp (v4.5.6) performs SATe-enabled phylogenetic placement.
- **Core Function**: Places sequences into existing phylogenetic trees.
- **Algorithm**: Uses SATé (Simultaneous Alignment and Tree Estimation) approach.
- **Input/Output**: Accepts query sequences and reference trees; produces placement results.
- **Phylogenetic Placement**: Focuses on placing query sequences into reference trees.
- **Applications**: Metagenomics, evolutionary biology, and sequence classification.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Reference Tree**: Requires appropriate reference tree for placement.
- **Sequence Quality**: Results depend on input sequence quality.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Place sequences
**Args:** `run_sepp.py -a query.fasta -o output/`
**Explanation:** `-a` query sequences; `-o` output directory.

### With reference tree
**Args:** `run_sepp.py -a query.fasta -t reference.tree -o output/`
**Explanation:** `-t` specifies reference tree.

### Verbose logging
**Args:** `run_sepp.py -a query.fasta -v -o output/`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `run_sepp.py -a query.fasta -t 8 -o output/`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `run_sepp.py --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `run_sepp.py --version`
**Explanation:** Shows current version.

### Evaluate placement
**Args:** `evaluate_placement.py -i output/placement.json -o evaluation.txt`
**Explanation:** Evaluates placement quality.