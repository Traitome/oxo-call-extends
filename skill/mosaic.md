---
name: mosaic
category: expression
description: Counts Strand-seq reads and classifies strand states using Hidden Markov Model.
tags: [mosaic, expression, single-cell]
author: oxo-call-community
source_url: "https://github.com/friendsofstrandseq/mosaicatcher/"
---

## Concepts

- **Tool Overview**: mosaic v0.3.1 analyzes Strand-seq data using Hidden Markov Model.
- **Core Function**: Classifies strand states of chromosomes in single cells.
- **Strand-seq**: Designed for Strand-sequencing data analysis.
- **Hidden Markov Model**: Uses HMM for state classification.
- **Single-Cell Analysis**: Supports single-cell sequencing data.
- **Input/Output**: Accepts aligned reads; outputs strand state classifications.

## Pitfalls

- **Strand-seq Specific**: Designed for Strand-sequencing data.
- **Memory Requirements**: Memory usage depends on cell count.
- **Parameter Tuning**: May require parameter adjustment for HMM.
- **Data Quality**: Results depend on sequencing quality.
- **Chromosome Coverage**: Requires sufficient coverage per chromosome.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Run strand state classification
**Args:** `mosaic -i alignments.bam -o strand_states.txt`
**Explanation:** Classifies strand states using HMM.

### With custom parameters
**Args:** `mosaic -i alignments.bam -p params.yaml -o strand_states.txt`
**Explanation:** Uses custom HMM parameters.

### Generate visualization
**Args:** `mosaic -i alignments.bam -v -o strand_states.txt`
**Explanation:** Generates strand state visualization.

### Batch processing
**Args:** `mosaic -i bam/ -o results/`
**Explanation:** Processes multiple samples.

### Generate report
**Args:** `mosaic -i alignments.bam -r report.html -o strand_states.txt`
**Explanation:** Generates analysis report.