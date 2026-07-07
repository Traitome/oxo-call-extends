---
name: orthofinder
category: utility
description: OrthoFinder accurately infers orthogroups, orthologues, gene trees and rooted species trees.
tags: [orthofinder, utility, orthology, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/OrthoFinder/OrthoFinder"
---

## Concepts

- **Tool Overview**: OrthoFinder analyzes orthology relationships across species.
- **Core Function**: Infers orthogroups, orthologs, and gene/species trees.
- **Algorithm**: Uses reciprocal best hits and tree-based methods.
- **Input Format**: Accepts FASTA files of protein sequences.
- **Output**: Produces orthogroups, orthologs, and phylogenetic trees.
- **Use Case**: Comparative genomics, phylogenetics, and evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Sequence Quality**: Results depend on input sequence quality.
- **Taxon Sampling**: Affects tree inference accuracy.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orthofinder --help`
**Explanation:** Shows available options and usage instructions.

### Run OrthoFinder
**Args:** `orthofinder -f fastas/ -o results/`
**Explanation:** Runs orthology analysis on FASTA files.

### With pre-computed alignments
**Args:** `orthofinder -f fastas/ -a alignments/ -o results/`
**Explanation:** Uses pre-computed alignments.

### Specify species tree
**Args:** `orthofinder -f fastas/ -s species_tree.nwk -o results/`
**Explanation:** Uses user-provided species tree.

### Verbose mode
**Args:** `orthofinder -f fastas/ -v -o results/`
**Explanation:** Runs with verbose output.

### Quick mode
**Args:** `orthofinder -f fastas/ -q -o results/`
**Explanation:** Runs in quick mode.

### Number of threads
**Args:** `orthofinder -f fastas/ -t 8 -o results/`
**Explanation:** Uses 8 threads for parallel processing.