---
name: lightassembler
category: assembly
description: LightAssembler - Lightweight de novo assembly algorithm for desktop machines
tags: [lightassembler, assembly, de-novo, bloom-filter, k-mer, lightweight]
author: oxo-call-community
source_url: "https://github.com/SaraEl-Metwally/LightAssembler"
---

## Concepts

- **De Novo Assembly**: De novo genome assembly from sequencing reads
- **Bloom Filter**: Cache-oblivious Bloom filters for efficient k-mer storage
- **K-mer Sampling**: Uniform sampling of g-spaced sequenced k-mers
- **Error Correction**: Statistical testing for k-mer correctness
- **Desktop-friendly**: Designed for execution on desktop machines
- **Memory Efficiency**: Memory-efficient assembly algorithm

## Pitfalls

- **K-mer Selection**: K-mer size selection affects assembly quality
- **Read Quality**: Poor quality reads affect assembly accuracy
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Complex Regions**: Repeat regions may cause assembly issues
- **Memory Usage**: Still memory-intensive for very large genomes

## Examples

### Assemble genome
**Args:** `lightassembler -i reads.fastq -o assembly.fasta -k 31`
**Explanation:** Assembles genome from reads using k-mer size 31.

### Paired-end assembly
**Args:** `lightassembler -i reads_1.fastq -j reads_2.fastq -o assembly.fasta`
**Explanation:** Assembles using paired-end reads.

### Specify k-mer size
**Args:** `lightassembler -i reads.fastq -o assembly.fasta -k 55`
**Explanation:** Uses k-mer size 55 for assembly.

### Output contigs
**Args:** `lightassembler -i reads.fastq -o contigs.fasta -c`
**Explanation:** Outputs only contigs without scaffolding.

### Threads
**Args:** `lightassembler -i reads.fastq -o assembly.fasta -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### Memory limit
**Args:** `lightassembler -i reads.fastq -o assembly.fasta -m 16G`
**Explanation:** Limits memory usage to 16GB.