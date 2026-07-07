---
name: transrate
category: analysis
description: TransRate - Tool for evaluating transcriptome assembly quality.
tags: [transrate, transcriptome-assembly, quality-assessment, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/blahah/transrate"
---

## Concepts

- **Tool Overview**: TransRate - A tool for evaluating the quality of transcriptome assemblies.
- **Core Function**: Assesses assembly quality using multiple metrics including read mapping and contiguity.
- **Input**: Transcriptome assembly (FASTA), RNA-seq reads (FASTQ).
- **Output**: Quality scores, assembly metrics, improvement suggestions.
- **Installation**: `conda install -c bioconda transrate`
- **Use Case**: Transcriptome assembly evaluation, quality control, assembly optimization.

## Pitfalls

- **Memory**: Large assemblies may require significant memory.
- **Computation Time**: Quality assessment may be time-consuming for large datasets.

## Examples

### Evaluate assembly
**Args:** `transrate --assembly transcripts.fasta --left reads_1.fastq --right reads_2.fastq`
**Explanation:** Evaluate transcriptome assembly quality.

### With reference
**Args:** `transrate --assembly assembly.fasta --reference genome.fasta --left reads.fastq`
**Explanation:** Evaluate assembly against reference genome.
