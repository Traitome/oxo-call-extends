---
name: tefinder
category: annotation
description: TE-Finder - Tool for identifying and classifying transposable elements in genomic sequences.
tags: [tefinder, transposable-element, te-annotation, classification, genomics]
author: oxo-call-community
source_url: "https://github.com/compbio/tefinder"
---

## Concepts

- **Tool Overview**: TE-Finder - A tool for identifying and classifying transposable elements in genomic sequences.
- **Core Function**: Detects TE sequences and classifies them by family, order, and evolutionary age.
- **Input**: Genomic sequences in FASTA format.
- **Output**: TE coordinates and classifications in GFF3 or BED format.
- **Installation**: `pip install tefinder` or `conda install -c bioconda tefinder`
- **Use Case**: Annotating TE content in newly sequenced genomes.

## Pitfalls

- **Reference Libraries**: Uses reference TE databases - results depend on library completeness.
- **Genome Size**: Large eukaryotic genomes require significant processing time.

## Examples

### Find TEs in genome
**Args:** `tefinder -i genome.fasta -o te_annotation.gff3`
**Explanation:** Identify and classify transposable elements in genome sequence.

### With repeat library
**Args:** `tefinder -i genome.fasta -l repeats.fasta -o results/`
**Explanation:** Use custom repeat library for TE identification.

### Summary report
**Args:** `tefinder -i genome.fasta --summary -o report.txt`
**Explanation:** Generate summary of TE content by family and order.
