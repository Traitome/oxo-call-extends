---
name: chap
category: structural-biology
description: Functional annotation of ion channel structures
tags: [chap, ion-channels, structural-biology, annotation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/channotation/chap"
---

## Concepts

- **Tool Overview**: CHAP is a tool for the functional annotation of ion channel structures based on structural features.
- **Core Function**: Annotates ion channel structures with functional properties and classification.
- **Features**: Structural analysis, pore region identification, gating mechanism prediction, and functional classification.
- **Input**: Ion channel structure files (PDB format) or sequence data.
- **Output**: Annotation reports with functional predictions and classifications.
- **Application**: Ion channel research, drug discovery, and structural biology.
- **Installation**: Install via bioconda: `conda install -c bioconda chap`

## Pitfalls

- **Structure Quality**: Requires high-resolution structural data.
- **Sequence Homology**: Works best with known ion channel sequences.
- **Annotation Confidence**: Predictions may have varying confidence levels.
- **Complex Structures**: Multi-subunit channels may require special handling.

## Examples

### Annotate ion channel structure
**Args:** `chap -i channel.pdb -o annotation.txt`
**Explanation:** Annotates ion channel structure from PDB file.

### Predict pore properties
**Args:** `chap --pore-analysis -i channel.pdb -o pore_properties.txt`
**Explanation:** Analyzes and reports pore region properties.

### Classify channel type
**Args:** `chap --classify -i channel.fasta -o classification.txt`
**Explanation:** Classifies ion channel based on sequence.

### Display help
**Args:** `chap --help`
**Explanation:** Shows all available options and usage information.