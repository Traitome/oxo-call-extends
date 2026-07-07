---
name: terminus
category: utility
description: Terminus - Tool for finding terminators in bacterial genomes.
tags: [terminus, terminator, rho-dependent, rho-independent, bacterial, gene-prediction]
author: oxo-call-community
source_url: "https://github.com/tseeman/terminus"
---

## Concepts

- **Tool Overview**: Terminus - A tool for identifying transcription terminators in bacterial genomes, both rho-dependent and rho-independent types.
- **Core Function**: Predicts bacterial transcription terminators by analyzing sequence patterns and structural features.
- **Input**: Bacterial genome sequence in FASTA format.
- **Output**: Predicted terminator locations in GFF3 or BED format, terminator classification.
- **Installation**: `pip install terminus` or `conda install -c bioconda terminus`
- **Use Case**: Bacterial genome annotation, operon prediction, transcriptional regulation studies.

## Pitfalls

- **Bacteria Only**: Designed for bacterial genomes - not suitable for eukaryotes.
- **Rho-dependent**: Rho-dependent terminators are harder to predict from sequence alone.

## Examples

### Find terminators
**Args:** `terminus -i genome.fasta -o terminators.gff3`
**Explanation:** Identify transcription terminators in bacterial genome.

### Include rho-dependent prediction
**Args:** `terminus -i genome.fasta --include-rho -o results/`
**Explanation:** Include rho-dependent terminator prediction in analysis.
