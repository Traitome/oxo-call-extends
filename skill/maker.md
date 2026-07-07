---
name: maker
category: annotation
description: MAKER is a portable and easily configurable genome annotation pipeline.
tags: [maker, annotation, genome-annotation, pipeline]
author: oxo-call-community
source_url: "https://www.yandell-lab.org/software/maker.html"
---

## Concepts

- **Tool Overview**: maker v3.01.04 - MAKER is a comprehensive, portable genome annotation pipeline that integrates multiple evidence sources.
- **Core Function**: Automates gene prediction and annotation using ab initio predictors, EST alignments, and protein homologies.
- **Input/Output**: Input: Genome sequence, ESTs, proteins, repeat libraries; Output: Annotated genes in GFF3/GTF format.
- **Installation**: `conda install -c bioconda maker`
- **Evidence Integration**: Combines multiple evidence types for improved annotation accuracy.
- **Repeat Masking**: Built-in repeat masking using RepeatMasker and RepeatRunner.

## Pitfalls

- **Computational Resources**: Requires significant CPU and memory for large genomes.
- **Configuration Complexity**: Numerous configuration options require careful setup.
- **Evidence Quality**: Poor quality EST/protein data affects annotation quality.
- **Repeat Libraries**: Outdated repeat libraries miss novel repeats.
- **Gene Models**: Over-prediction or under-prediction depending on parameters.
- **Time Requirements**: Full annotation runs can take days for large genomes.

## Examples

### Basic annotation
**Args:** `maker -genome genome.fasta -est ests.fasta -protein proteins.fasta -o annotation/`
**Explanation:** Runs MAKER with EST and protein evidence.

### With repeat masking
**Args:** `maker -genome genome.fasta -est ests.fasta -rm -o annotation/`
**Explanation:** Enables repeat masking during annotation.

### Resuming interrupted run
**Args:** `maker -genome genome.fasta -est ests.fasta -o annotation/ -resume`
**Explanation:** Resumes from previous checkpoint.

### Parallel execution
**Args:** `maker -genome genome.fasta -est ests.fasta -o annotation/ -cpu 16`
**Explanation:** Uses 16 CPU cores for parallel processing.

### Generate final annotations
**Args:** `maker -genome genome.fasta -est ests.fasta -o annotation/ -final`
**Explanation:** Generates final filtered annotations.

### Configuration file
**Args:** `maker -c maker_opts.ctl -o annotation/`
**Explanation:** Uses custom configuration file.