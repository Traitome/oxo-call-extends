---
name: igphyml
category: utility
description: IgPhyML is a program designed to build phylogenetic trees and test evolutionary hypotheses regarding B cell affinity maturation
tags: [igphyml, phylogenetics, B cell, affinity maturation]
author: oxo-call-community
source_url: "https://igphyml.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Tool Overview**: IgPhyML is a specialized phylogenetic tool for analyzing B cell receptor sequence evolution and affinity maturation
- **Core Function**: Constructs phylogenetic trees from immunoglobulin sequences and tests evolutionary hypotheses
- **Input/Output**: Accepts aligned Ig sequences in FASTA/PHYLIP format; outputs phylogenetic trees and statistical tests
- **Installation**: `conda install -c bioconda igphyml`
- **Key Features**: Integrates SHM-aware substitution models, supports clonal lineage analysis

## Pitfalls

- **Sequence Alignment**: Poorly aligned sequences can produce incorrect phylogenetic relationships
- **Model Selection**: Choosing inappropriate substitution models can affect tree topology
- **Recombination Detection**: IgPhyML may misinterpret recombination events as point mutations
- **Computational Time**: Large datasets can require significant computational resources
- **Memory Requirements**: May need substantial RAM for complex phylogenetic analyses

## Examples

### Build phylogenetic tree from Ig sequences
**Args:** `igphyml -i aligned_sequences.fasta -o tree.nwk`
**Explanation:** Constructs a phylogenetic tree from aligned immunoglobulin sequences.

### Run with SHM-aware model
**Args:** `igphyml -i sequences.fasta -o tree.nwk --shm-model`
**Explanation:** Uses a somatic hypermutation-aware substitution model for improved accuracy.

### Perform bootstrap analysis
**Args:** `igphyml -i sequences.fasta -o tree_bootstrap.nwk --bootstrap 100`
**Explanation:** Generates 100 bootstrap replicates to assess branch support.

### Test evolutionary hypotheses
**Args:** `igphyml -i sequences.fasta -o hypothesis_test.txt --test-likelihood`
**Explanation:** Performs likelihood ratio tests for comparing evolutionary models.

### Output in Newick and Nexus formats
**Args:** `igphyml -i sequences.fasta -o tree --format newick nexus`
**Explanation:** Generates tree files in multiple formats for compatibility with visualization tools.
