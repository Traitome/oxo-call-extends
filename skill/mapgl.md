---
name: mapgl
category: population-genomics
description: Prediction of lineage-specific gain and loss of sequence elements using phylogenetic maximum parsimony.
tags: [mapgl, population-genomics, phylogenetics, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/adadiehl/mapGL"
---

## Concepts

- **Tool Overview**: mapgl v1.3.1 - Predicts lineage-specific gain and loss of sequence elements using phylogenetic maximum parsimony.
- **Core Function**: Identifies lineage-specific gain and loss events of sequence elements across phylogenetic trees.
- **Input/Output**: Input: Sequence alignments, phylogenetic tree; Output: Gain/loss predictions, ancestral reconstructions.
- **Installation**: `conda install -c bioconda mapgl`
- **Maximum Parsimony**: Uses maximum parsimony for ancestral state reconstruction.
- **Lineage-specific Analysis**: Identifies events specific to particular lineages.

## Pitfalls

- **Tree Quality**: Poor quality phylogenetic trees affect predictions.
- **Alignment Quality**: Poor alignments affect gain/loss detection.
- **Missing Data**: Missing sequences may affect reconstruction.
- **Parameter Tuning**: Incorrect parameters affect prediction accuracy.
- **Computational Resources**: Large trees require significant memory.
- **Model Assumptions**: Maximum parsimony assumptions may not always hold.

## Examples

### Run mapGL analysis
**Args:** `mapgl -i alignment.fasta -t tree.newick -o results/`
**Explanation:** Performs lineage-specific gain/loss analysis.

### With confidence estimation
**Args:** `mapgl -i alignment.fasta -t tree.newick -o results/ --confidence`
**Explanation:** Estimates confidence for predictions.

### Ancestral reconstruction
**Args:** `mapgl -i alignment.fasta -t tree.newick -o results/ --reconstruct`
**Explanation:** Performs ancestral sequence reconstruction.

### Verbose mode
**Args:** `mapgl -i alignment.fasta -t tree.newick -o results/ -v`
**Explanation:** Provides detailed logging during analysis.

### Filter by significance
**Args:** `mapgl -i alignment.fasta -t tree.newick -o results/ -p 0.05`
**Explanation:** Filters results by significance level.

### Generate visualization
**Args:** `mapgl -i alignment.fasta -t tree.newick -o results/ --plot`
**Explanation:** Generates visualization of results.