---
name: evofold2
category: population-genomics
description: "Identifies functional RNA-structure in multiple sequence alignments."
tags: [evofold2, population-genomics, RNA-structure, comparative-genomics, evolution]
author: oxo-call-community
source_url: "https://github.com/jakob-skou-pedersen/phy"
---

## Concepts

- **Tool Overview**: EvoFold2 is a tool for identifying functional RNA structures in multiple sequence alignments using evolutionary conservation signals.
- **Core Function**: Predicts RNA secondary structures and identifies structurally conserved regions across multiple species.
- **Input/Output**: Input: Multiple sequence alignment (FASTA/Stockholm). Output: Predicted RNA structures, conservation scores, structural annotations.
- **Algorithm**: Uses phylogenetic comparative methods to identify conserved RNA secondary structures based on compensatory mutations.
- **Key Features**: RNA structure prediction, evolutionary conservation analysis, multiple alignment analysis, structural annotation, visualization.
- **Installation**: `conda install -c bioconda evofold2`

## Pitfalls

- **Alignment Quality**: Results depend on high-quality multiple sequence alignments.
- **Sequence Diversity**: Requires sufficient evolutionary diversity in input sequences.
- **Computation Time**: Large alignments may require significant processing time.
- **Memory Usage**: May require substantial RAM for large datasets.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic RNA structure prediction
**Args:** `evofold2 -i alignment.fasta -o structures.txt`
**Explanation:** Predicts RNA structures from multiple sequence alignment.

### With conservation scoring
**Args:** `evofold2 -i alignment.fasta -o structures.txt --conservation`
**Explanation:** Includes conservation scores in output.

### Visualization
**Args:** `evofold2 -i alignment.fasta -o structures.txt --plot`
**Explanation:** Generates visualization of predicted structures.

### Batch processing
**Args:** `evofold2 -i alignments/ -o results/ --batch`
**Explanation:** Processes multiple alignments in batch mode.

### Detailed output
**Args:** `evofold2 -i alignment.fasta -o structures.txt --detailed`
**Explanation:** Outputs detailed structural information.