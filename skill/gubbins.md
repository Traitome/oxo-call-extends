---
name: gubbins
category: bioinformatics
description: Gubbins performs rapid phylogenetic analysis of large samples of recombinant bacterial whole genome sequences.
tags: [gubbins, phylogenetics, recombination-detection, bioinformatics]
author: oxo-call-community
source_url: "https://nickjcroucher.github.io/gubbins"
---

## Concepts

- **Phylogenetic Analysis**: Gubbins analyzes bacterial genome sequences for phylogenetic relationships.

- **Recombination Detection**: Identifies recombination events in bacterial genomes.

- **Whole Genome Sequences**: Processes complete bacterial genome sequences.

- **Large Sample Handling**: Designed for analyzing large sample sets.

- **Rapid Analysis**: Optimized for fast processing of genomic data.

- **Visualization**: Generates phylogenetic trees and recombination maps.

## Pitfalls

- **Genome Quality**: Results depend on input genome assembly quality.

- **Recombination Rate**: High recombination rates may complicate analysis.

- **Computational Resources**: Large datasets require significant memory and CPU.

- **Alignment Quality**: Poor alignments affect tree accuracy.

- **Parameter Tuning**: Adjust parameters based on dataset characteristics.

## Examples

### Run recombination analysis
**Args:** `run_gubbins.py -i alignment.fasta -o results/`
**Explanation:** Runs recombination detection on sequence alignment.

### Generate phylogenetic tree
**Args:** `run_gubbins.py -i alignment.fasta -t -o results/`
**Explanation:** Generates phylogenetic tree with recombination events.

### Custom window size
**Args:** `run_gubbins.py -i alignment.fasta -w 1000 -o results/`
**Explanation:** Sets custom window size for analysis.

### Batch processing
**Args:** `for f in *.fasta; do run_gubbins.py -i $f -o ${f%.fasta}_results/; done`
**Explanation:** Processes multiple alignments.

### Visualize results
**Args:** `gubbins_draw -i results/ -o tree.png`
**Explanation:** Generates visualization of recombination events.

### Check convergence
**Args:** `run_gubbins.py -i alignment.fasta -c -o results/`
**Explanation:** Checks convergence of recombination detection.

### Help command
**Args:** `run_gubbins.py --help`
**Explanation:** Shows available options and usage information.