---
name: intemap
category: assembly
description: Integrated metagenomic assembly pipeline for short reads that combines multiple assembly strategies for improved contig reconstruction.
tags: [intemap, assembly, metagenomics, short-reads]
author: oxo-call-community
source_url: "http://cqb.pku.edu.cn/ZhuLab/InteMAP/index.html"
---

## Concepts

- **Integrated Assembly Pipeline**: InteMAP combines multiple assembly strategies for metagenomic short-read data.
- **Hybrid Assembly Approach**: Integrates de Bruijn graph and overlap-layout-consensus methods.
- **Contig Extension**: Extends short contigs using paired-end read information.
- **Quality Improvement**: Polishes assembled contigs to improve accuracy.
- **MetaSPAdes Integration**: Incorporates MetaSPAdes for initial assembly.

## Pitfalls

- **Memory Requirements**: Metagenomic assembly can be memory-intensive for complex communities.
- **Computational Time**: Comprehensive assembly may require significant processing time.
- **Input Quality**: Performance depends on input read quality and coverage.
- **Community Complexity**: Highly diverse microbial communities may affect assembly quality.
- **Parameter Tuning**: Assembly parameters may need adjustment for specific datasets.

## Examples

### Basic metagenomic assembly
**Args:** `intemap -1 reads_1.fastq -2 reads_2.fastq -o assembly_output`
**Explanation:** Performs integrated metagenomic assembly from paired-end reads.

### With custom k-mer sizes
**Args:** `intemap -1 reads_1.fastq -2 reads_2.fastq -o custom_assembly -k 21,33,55`
**Explanation:** Uses multiple k-mer sizes for assembly (21, 33, 55).

### Specify coverage cutoff
**Args:** `intemap -1 reads_1.fastq -2 reads_2.fastq -o filtered_assembly -c 5`
**Explanation:** Filters out contigs with coverage below 5x.

### Enable contig extension
**Args:** `intemap -1 reads_1.fastq -2 reads_2.fastq -o extended_assembly --extend`
**Explanation:** Enables contig extension using paired-end information.

### Polishing assembly
**Args:** `intemap -1 reads_1.fastq -2 reads_2.fastq -o polished_assembly --polish`
**Explanation:** Polishes assembled contigs to improve base accuracy.

### With reference-guided assembly
**Args:** `intemap -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o guided_assembly`
**Explanation:** Uses reference genome to guide assembly process.