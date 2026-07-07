---
name: lja
category: assembly
description: LJA (La Jolla Assembler) - Genome assembly from PacBio HiFI reads using de Bruijn graphs
tags: [lja, assembly, de-novo, PacBio, HiFI, de-Bruijn-graph]
author: oxo-call-community
source_url: "https://github.com/AntonBankevich/LJA"
---

## Concepts

- **De Novo Assembly**: De novo genome assembly from sequencing reads
- **De Bruijn Graph**: Uses de Bruijn graph assembly algorithm
- **PacBio HiFI**: Optimized for PacBio HiFi sequencing data
- **Long Reads**: Handles long-read sequencing data
- **Error Correction**: Built-in error correction for reads
- **Scaffolding**: Scaffolds contigs into larger sequences

## Pitfalls

- **K-mer Selection**: K-mer size affects assembly quality
- **Read Quality**: Poor quality reads affect assembly
- **Memory Usage**: Memory-intensive for large genomes
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Complex Regions**: Repeat regions may cause assembly issues

## Examples

### Assemble genome
**Args:** `lja -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles genome from PacBio HiFi reads.

### Specify k-mer size
**Args:** `lja -i reads.fastq -o assembly.fasta -k 31`
**Explanation:** Uses k-mer size 31 for assembly.

### Paired-end reads
**Args:** `lja -1 reads_1.fastq -2 reads_2.fastq -o assembly.fasta`
**Explanation:** Assembles using paired-end reads.

### Threads
**Args:** `lja -i reads.fastq -o assembly.fasta -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Memory limit
**Args:** `lja -i reads.fastq -o assembly.fasta -m 32G`
**Explanation:** Limits memory usage to 32GB.

### Output contigs only
**Args:** `lja -i reads.fastq -o contigs.fasta --contigs-only`
**Explanation:** Outputs only contigs without scaffolding.