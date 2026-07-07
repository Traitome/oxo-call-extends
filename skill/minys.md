---
name: minys
category: assembly
description: MinYS allows targeted assembly of bacterial genomes using a reference-guided pipeline.
tags: [minys, assembly, bacterial]
author: oxo-call-community
source_url: "https://github.com/cguyomar/MinYS"
---

## Concepts

- **Tool Overview**: MinYS v1.1 performs targeted bacterial genome assembly.
- **Core Function**: Assembles bacterial genomes using reference-guided approach.
- **Targeted Assembly**: Focuses assembly on specific genomic regions.
- **Reference-Guided**: Uses reference sequences for assembly guidance.
- **Input/Output**: Accepts sequencing reads; outputs assembled contigs.
- **Bacterial Genomics**: Supports bacterial genome analysis workflows.

## Pitfalls

- **Bacteria Specific**: Designed for bacterial genome assembly.
- **Computational Resources**: Assembly may require significant resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal assembly.
- **Data Quality**: Assembly quality depends on input data quality.
- **Reference Genome**: Requires appropriate reference sequences.

## Examples

### Assemble bacterial genome
**Args:** `minys -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Performs targeted assembly using reference.

### With custom k-mer size
**Args:** `minys -i reads.fastq -r reference.fasta -o assembly.fasta -k 31`
**Explanation:** Uses k-mer size of 31.

### Paired-end assembly
**Args:** `minys -i reads_1.fastq -I reads_2.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** Processes paired-end reads.

### Batch processing
**Args:** `minys -i fastq/ -r reference.fasta -o assemblies/`
**Explanation:** Processes multiple read files.

### Generate statistics
**Args:** `minys -i reads.fastq -r reference.fasta -o assembly.fasta -s stats.txt`
**Explanation:** Generates assembly statistics.