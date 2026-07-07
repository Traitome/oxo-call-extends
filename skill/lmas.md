---
name: lmas
category: assembly
description: LMAS - Last (Meta)Genomic Assembler Standing
tags: [lmas, assembly, metagenomics, de-novo, genome-assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/B-UMMI/LMAS"
---

## Concepts

- **Metagenomic Assembly**: Metagenomic sequence assembly
- **De Novo Assembly**: De novo assembly from metagenomic reads
- **Mixed Reads**: Handles mixed microbial community data
- **Contig Assembly**: Assembles reads into contigs
- **Binning Support**: Supports metagenomic binning
- **Long Reads**: Optimized for long-read sequencing data

## Pitfalls

- **Community Complexity**: Complex microbial communities may affect assembly
- **Read Quality**: Poor quality reads affect assembly accuracy
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Contamination**: Contaminating sequences may affect results

## Examples

### Assemble metagenome
**Args:** `lmas -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles metagenomic reads into contigs.

### Long-read mode
**Args:** `lmas -i reads.fastq -o assembly.fasta -l`
**Explanation:** Optimized for long-read sequencing data.

### Threads
**Args:** `lmas -i reads.fastq -o assembly.fasta -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum contig length
**Args:** `lmas -i reads.fastq -o assembly.fasta -m 500`
**Explanation:** Sets minimum contig length to 500bp.

### Binning
**Args:** `lmas -i reads.fastq -o assembly/ -b`
**Explanation:** Performs metagenomic binning.

### Verbose output
**Args:** `lmas -i reads.fastq -o assembly.fasta -v`
**Explanation:** Provides detailed output.