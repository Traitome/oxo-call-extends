---
name: metacortex
category: assembly
description: MetaCortex is an assembler for metagenomic, or environmental sequence data.
tags: [metacortex, assembly, metagenomics, environmental]
author: oxo-call-community
source_url: "https://github.com/SR-Martin/metacortex"
---

## Concepts

- **Tool Overview**: MetaCortex v0.5.1 is a de novo assembler specifically designed for metagenomic and environmental sequence data.
- **Core Function**: Assembles short sequencing reads from complex microbial communities into contiguous sequences (contigs).
- **Graph-based Assembly**: Uses de Bruijn graph assembly approach optimized for metagenomic data.
- **Multi-sample Support**: Capable of handling multiple metagenomic samples simultaneously.
- **Input/Output**: Accepts FASTQ-formatted sequencing reads; outputs assembled contigs in FASTA format.
- **Memory Efficiency**: Optimized for memory usage when dealing with large metagenomic datasets.

## Pitfalls

- **Complexity Limits**: May struggle with highly complex metagenomic communities with many low-abundance species.
- **Computational Resources**: Large datasets may require significant computational resources.
- **Contig Quality**: Assembly quality depends on input read quality and coverage.
- **Parameter Tuning**: May require parameter adjustment for optimal results with different datasets.
- **Repeat Regions**: Difficult-to-assemble repeat regions can affect contiguity.
- **Strain Variation**: Closely related strains may collapse into single contigs.

## Examples

### Assemble metagenomic reads
**Args:** `metacortex -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles metagenomic reads into contigs.

### Paired-end assembly
**Args:** `metacortex -i reads_1.fastq reads_2.fastq -o assembly.fasta`
**Explanation:** Processes paired-end sequencing data for assembly.

### Specify k-mer size
**Args:** `metacortex -i reads.fastq -k 31 -o assembly.fasta`
**Explanation:** Uses k-mer size of 31 for de Bruijn graph construction.

### Multiple samples
**Args:** `metacortex -i sample1.fastq sample2.fastq -o assembly.fasta`
**Explanation:** Assembles multiple metagenomic samples together.

### Output assembly statistics
**Args:** `metacortex -i reads.fastq -o assembly.fasta -s stats.txt`
**Explanation:** Generates assembly statistics file.