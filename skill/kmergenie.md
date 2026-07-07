---
name: kmergenie
category: assembly
description: KmerGenie estimates the best k-mer length for genome de novo assembly
tags: [kmergenie, assembly, k-mer, genome-assembly, optimization]
author: oxo-call-community
source_url: "http://kmergenie.bx.psu.edu"
---

## Concepts

- **K-mer Length Optimization**: Estimates optimal k-mer length for assembly
- **De Novo Assembly**: Supports reference-free genome assembly
- **Read Analysis**: Analyzes read characteristics to recommend k-mer size
- **Quality Assessment**: Evaluates assembly quality at different k-mer lengths
- **Parameter Selection**: Automates the often trial-and-error process of k-mer selection
- **Multiple Assemblers**: Can work with various de Bruijn graph assemblers

## Pitfalls

- **Computational Time**: Testing multiple k-mer lengths is time-consuming
- **Memory Usage**: Large k-mer lengths require significant memory
- **Read Length**: Requires sufficient read length for accurate estimation
- **Genome Complexity**: Complex genomes may need different k-mer strategies
- **Heterozygosity**: High heterozygosity affects optimal k-mer selection
- **Assembly Software**: Recommendations may be specific to certain assemblers

## Examples

### Estimate best k-mer size
**Args:** `kmergenie reads.fastq -o output`
**Explanation:** Estimates optimal k-mer length from sequencing reads.

### Specify k-mer range
**Args:** `kmergenie reads.fastq -k 21-121 -o output`
**Explanation:** Tests k-mer sizes from 21 to 121.

### Paired-end reads
**Args:** `kmergenie -l reads.lst -o output`
**Explanation:** Uses file list for paired-end reads.

### Set output directory
**Args:** `kmergenie reads.fastq -o kmer_analysis/`
**Explanation:** Specifies output directory for results.

### Quick estimation
**Args:** `kmergenie reads.fastq --quick -o output`
**Explanation:** Runs faster estimation with fewer k-mer values.

### Custom k-mer list
**Args:** `kmergenie reads.fastq -k 21,31,41,51,61,71 -o output`
**Explanation:** Tests specific k-mer sizes only.