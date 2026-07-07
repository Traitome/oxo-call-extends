---
name: transanno
category: annotation
description: TransAnno - Tool for transcriptome annotation.
tags: [transanno, transcriptome, annotation, gene-prediction, rna-seq]
author: oxo-call-community
source_url: "https://github.com/compbio/transanno"
---

## Concepts

- **Tool Overview**: TransAnno - A tool for annotating transcriptomes and predicting gene structures.
- **Core Function**: Integrates RNA-seq data and homology evidence for gene annotation.
- **Input**: RNA-seq alignments (BAM), genome sequence (FASTA), protein sequences.
- **Output**: Gene annotations (GTF/GFF), transcript models, functional annotations.
- **Installation**: `pip install transanno` or `conda install -c bioconda transanno`
- **Use Case**: Genome annotation, gene prediction, transcriptome analysis.

## Pitfalls

- **Evidence Integration**: Requires multiple evidence types for accurate annotation.
- **Computational Resources**: Large genomes may require significant resources.

## Examples

### Annotate genome
**Args:** `transanno -g genome.fasta -r rnaseq.bam -p proteins.fasta -o annotations/`
**Explanation:** Annotate genome using RNA-seq and protein homology.

### Predict genes
**Args:** `transanno predict -i genome.fasta -o gene_predictions.gtf`
**Explanation:** Predict gene structures from genome sequence.
