---
name: edta
category: annotation
description: "Extensive de-novo TE Annotator."
tags: [edta, annotation, transposable-elements, TE-detection, genome-annotation]
author: oxo-call-community
source_url: "https://github.com/oushujun/EDTA"
---

## Concepts

- **Tool Overview**: EDTA (Extensive de-novo TE Annotator) is a comprehensive pipeline for de novo transposable element (TE) identification and annotation in plant genomes.
- **Core Function**: Detects and classifies TEs using multiple detection tools, generates non-redundant TE libraries, and annotates genome assemblies.
- **Input/Output**: Input: Genome assembly (FASTA). Output: TE annotations (GFF3), TE consensus sequences, classification reports.
- **Algorithm**: Integrates multiple TE detection tools (LTR_FINDER, LTR_harvest, TIR-Learner, HelitronScanner) with post-processing and classification.
- **Key Features**: De novo TE detection, automated classification, non-redundant library generation, comprehensive annotation, plant genome optimization.
- **Installation**: `conda install -c bioconda edta`

## Pitfalls

- **Computation Resources**: Requires significant RAM and CPU time for large genomes.
- **Genome Size**: Very large genomes may require extended processing time.
- **LTR Detection**: LTR retrotransposons require specific parameters for different species.
- **Classification Accuracy**: Some TEs may be misclassified without manual curation.
- **Version Updates**: New versions may change detection algorithms.

## Examples

### Basic TE annotation
**Args:** `EDTA.pl --genome genome.fa --species others --output edta_output`
**Explanation:** Runs complete TE annotation pipeline on genome assembly.

### Specify organism type
**Args:** `EDTA.pl --genome genome.fa --species rice --output edta_output`
**Explanation:** Optimizes parameters for rice genome annotation.

### Generate non-redundant library
**Args:** `EDTA.pl --genome genome.fa --species others --output edta_output --anno 1`
**Explanation:** Generates non-redundant TE library and performs annotation.

### Parallel processing
**Args:** `EDTA.pl --genome genome.fa --species others --output edta_output --threads 16`
**Explanation:** Uses 16 threads for parallel processing.

### LTR-specific analysis
**Args:** `EDTA.pl --genome genome.fa --species others --output edta_output --step LTR`
**Explanation:** Runs only LTR retrotransposon detection step.