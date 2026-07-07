---
name: cats-rf
category: transcriptomics
description: Reference-free transcriptome assembly quality assessment tool
tags: [cats-rf, transcriptome, assembly, quality-control, rna-seq, reference-free]
author: oxo-call-community
source_url: "https://github.com/bodulic/CATS-rf/blob/main/README.md"
---

## Concepts

- **Tool Overview**: CATS-rf evaluates transcriptome assembly quality without requiring a reference genome.
- **Core Function**: Assesses assembly quality directly from RNA-seq reads.
- **Algorithm**: Uses read mapping statistics and assembly metrics for evaluation.
- **Input**: Assembled transcriptome FASTA and original RNA-seq reads.
- **Output**: Quality metrics including read mapping rates and assembly completeness.
- **Application**: Evaluating de novo transcriptome assemblies when reference genome is unavailable.
- **Installation**: Install via bioconda: `conda install -c bioconda cats-rf`

## Pitfalls

- **Read Quality**: Results depend on input RNA-seq read quality.
- **Assembly Format**: Requires properly formatted FASTA assembly.
- **Memory Usage**: Large datasets may require significant memory.
- **Computational Time**: Read mapping can be computationally intensive.

## Examples

### Assess assembly quality
**Args:** `cats-rf -a assembly.fasta -1 reads_1.fastq -2 reads_2.fastq -o results/`
**Explanation:** Evaluates transcriptome assembly quality using RNA-seq reads.

### Generate report
**Args:** `cats-rf -a assembly.fasta -1 reads_1.fastq -2 reads_2.fastq -o report.txt --report`
**Explanation:** Generates detailed quality assessment report.

### Display help
**Args:** `cats-rf --help`
**Explanation:** Shows all available options and usage information.