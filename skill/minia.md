---
name: minia
category: assembly
description: Minia is a short-read assembler based on a de Bruijn graph, capable of assembling a human genome on a desktop computer in a day.
tags: [minia, assembly, de-bruijn]
author: oxo-call-community
source_url: "https://github.com/GATB/minia"
---

## Concepts

- **Tool Overview**: Minia v3.2.6 is a short-read assembler based on de Bruijn graph.
- **Core Function**: Assembles short-read sequencing data into contiguous sequences.
- **de Bruijn Graph**: Uses de Bruijn graph algorithm for assembly.
- **Memory Efficient**: Designed to assemble large genomes with limited memory.
- **Input/Output**: Accepts short-read sequences; outputs assembled contigs.
- **Genome Assembly**: Supports de novo genome assembly workflows.

## Pitfalls

- **Short-read Specific**: Designed for short sequencing reads.
- **Computational Resources**: Assembly may require significant computational resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal assembly.
- **Data Quality**: Assembly quality depends on input read quality.
- **Contig N50**: May produce fragmented assemblies for complex genomes.

## Examples

### Assemble short reads
**Args:** `minia -in reads.fastq -out assembly`
**Explanation:** Assembles short reads into contigs.

### With custom k-mer size
**Args:** `minia -in reads.fastq -out assembly -k 31`
**Explanation:** Uses k-mer size of 31 for assembly.

### Paired-end assembly
**Args:** `minia -in reads_1.fastq -in2 reads_2.fastq -out assembly`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `minia -in fastq/ -out assemblies/`
**Explanation:** Processes multiple read files in batch mode.

### Generate statistics
**Args:** `minia -in reads.fastq -out assembly -stats`
**Explanation:** Generates assembly statistics.