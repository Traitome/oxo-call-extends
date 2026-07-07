---
name: clove
category: metagenomics
description: Classification of genomic fusions into structural variation events
tags: [clove, structural-variation, fusion-genes, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/PapenfussLab/clove"
---

## Concepts

- **Tool Overview**: CLOVE is a tool for classifying genomic fusions into structural variation events, enabling systematic analysis of complex genomic rearrangements.
- **Core Function**: Identifies and categorizes different types of structural variations including gene fusions, translocations, and rearrangements.
- **Algorithm**: Uses breakpoint analysis and sequence alignment to classify fusion events into predefined structural variation categories.
- **Input**: Fusion predictions from various tools or breakpoint coordinates.
- **Output**: Classified structural variation events with annotations.
- **Application**: Cancer genomics, structural variation analysis, and genome rearrangement studies.
- **Installation**: Install via bioconda: `conda install -c bioconda clove`

## Pitfalls

- **Data Quality**: Requires high-quality fusion predictions for accurate classification.
- **Reference Genome**: Must use appropriate reference genome for breakpoint analysis.
- **Computational Resources**: May require significant resources for large datasets.
- **Parameter Tuning**: May require adjustment of classification parameters.
- **False Positives**: May classify false fusion predictions.

## Examples

### Classify fusion events
**Args:** `clove -i fusions.bed -r reference.fasta -o classified_sv.txt`
**Explanation:** Classifies genomic fusion events from BED file.

### From multiple tools
**Args:** `clove -i jaffa.txt tophat.txt -o combined_sv.txt`
**Explanation:** Integrates and classifies fusions from multiple prediction tools.

### With annotation
**Args:** `clove -i fusions.bed -a annotation.gtf -o annotated_sv.txt`
**Explanation:** Adds gene annotation to classified structural variations.

### Display help
**Args:** `clove --help`
**Explanation:** Shows all available options and usage information.