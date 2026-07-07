---
name: mitgard
category: expression
description: Mitochondrial Genome Assembly from RNA-seq Data.
tags: [mitgard, expression, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/pedronachtigall/MITGARD"
---

## Concepts

- **Tool Overview**: MITGARD v1.1 assembles mitochondrial genomes from RNA-seq data.
- **Core Function**: Recovers mitochondrial sequences from RNA sequencing data.
- **Mitochondrial Assembly**: Specifically designed for mtDNA assembly.
- **RNA-seq Data**: Uses RNA sequencing reads for assembly.
- **Input/Output**: Accepts RNA-seq data; outputs mitochondrial genome sequences.
- **Organellar Genomics**: Supports mitochondrial genome analysis workflows.

## Pitfalls

- **RNA-seq Specific**: Designed for RNA sequencing data.
- **Computational Resources**: Assembly may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal assembly.
- **Data Quality**: Results depend on input data quality.
- **Reference Mitochondria**: Requires appropriate reference sequences.

## Examples

### Assemble mitochondrial genome
**Args:** `mitgard -i reads.fastq -o mito_genome.fasta`
**Explanation:** Assembles mitochondrial genome from RNA-seq data.

### With reference
**Args:** `mitgard -i reads.fastq -r ref_mito.fasta -o mito_genome.fasta`
**Explanation:** Uses reference mitochondrial genome.

### Detailed output
**Args:** `mitgard -i reads.fastq -o mito_genome.fasta -v`
**Explanation:** Generates detailed assembly report.

### Batch processing
**Args:** `mitgard -i fastq/ -o genomes/`
**Explanation:** Processes multiple FASTQ files.

### Generate statistics
**Args:** `mitgard -i reads.fastq -o mito_genome.fasta -s stats.txt`
**Explanation:** Generates assembly statistics.