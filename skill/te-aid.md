---
name: te-aid
category: annotation
description: TE-AID - Transposable Element annotation and analysis tool for eukaryotic genomes.
tags: [te-aid, transposable-element, te-annotation, repeat-masking, genomics, eukaryotes]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/TE-AID"
---

## Concepts

- **Tool Overview**: TE-AID (Transposable Element Annotation and Integration Database) - A pipeline for annotating transposable elements and integrating TE annotations with other genomic features.
- **Core Function**: Identifies, classifies, and annotates transposable elements in eukaryotic genome sequences.
- **Input**: Genomic sequences in FASTA format, optional RepeatMaster library.
- **Output**: TE annotations in GFF3 format, summary statistics, and optional database for integration.
- **Installation**: `conda install -c bioconda te-aid`
- **Use Case**: Genome annotation projects, repeat analysis, studying TE impact on gene expression.

## Pitfalls

- **Eukaryotic Genomes**: Designed for eukaryotic genomes - not suitable for prokaryotes.
- **Library Quality**: Accuracy depends on quality of repeat library used for annotation.
- **Computational Time**: Full genome TE annotation can be time-consuming for large genomes.

## Examples

### Basic TE annotation
**Args:** `te-aid -g genome.fasta -o te_annotation/`
**Explanation:** Run full TE annotation pipeline on genome sequence.

### With custom library
**Args:** `te-aid -g genome.fasta -l repeat_library.fasta -o output/`
**Explanation:** Use custom repeat library instead of default.

### Generate summary report
**Args:** `te-aid -g genome.fasta --summary -o results/`
**Explanation:** Generate summary statistics of TE content in genome.
