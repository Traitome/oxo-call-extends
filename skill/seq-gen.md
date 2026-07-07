---
name: seq-gen
category: simulation
description: seq-gen - Simulate sequence evolution along phylogenies
tags: ["seq-gen", "simulation", "phylogenetics", "evolution"]
author: oxo-call-community
source_url: "http://tree.bio.ed.ac.uk/software/Seq-Gen/"
---

## Concepts

- **Tool Overview**: seq-gen (v1.3.5) simulates the evolution of nucleotide or amino acid sequences along phylogenies.
- **Core Function**: Generates simulated sequence data using common substitution models.
- **Algorithm**: Implements various substitution models (JC69, K80, HKY85, GTR, etc.).
- **Input/Output**: Accepts Newick tree files and produces FASTA sequence files.
- **Sequence Simulation**: Focuses on simulating molecular evolution.
- **Applications**: Phylogenetics research, method testing, and benchmarking.

## Pitfalls

- **Memory Usage**: High memory requirements for large trees.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for realistic simulations.
- **Tree Format**: Requires correct Newick tree format.
- **Substitution Model**: Results depend on model choice.
- **Documentation**: Some features have limited documentation.

## Examples

### Simulate sequences
**Args:** `seq-gen -m HKY -l 1000 -t 0.5 tree.nw > output.fasta`
**Explanation:** `-m HKY` HKY85 model; `-l 1000` sequence length; `-t 0.5` transition/transversion ratio.

### Amino acid simulation
**Args:** `seq-gen -m JTT -l 500 tree.nw > output.fasta`
**Explanation:** `-m JTT` JTT amino acid model.

### Variable rates
**Args:** `seq-gen -m GTR -a 0.5 -l 1000 tree.nw > output.fasta`
**Explanation:** `-a 0.5` gamma distribution shape parameter.

### Verbose logging
**Args:** `seq-gen -v -m HKY -l 1000 tree.nw > output.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seq-gen --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seq-gen -V`
**Explanation:** Shows current version.

### Output format
**Args:** `seq-gen -m HKY -l 1000 -f phylip tree.nw > output.phy`
**Explanation:** `-f phylip` outputs in PHYLIP format.