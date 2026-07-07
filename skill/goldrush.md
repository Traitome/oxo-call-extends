---
name: goldrush
category: assembly
description: GoldRush is a linear-time de novo long read assembler for genome assembly from long sequencing reads.
tags: [goldrush, genome-assembly, long-reads, de-novo, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BirolLab/goldrush"
---

## Concepts

- **Linear-Time Assembly**: GoldRush achieves linear time complexity for genome assembly by leveraging efficient k-mer counting and graph traversal algorithms.

- **Long Read Support**: Optimized for long sequencing reads from technologies like PacBio and Oxford Nanopore.

- **De Novo Assembly**: Performs de novo assembly without requiring a reference genome.

- **Graph-Based Assembly**: Uses de Bruijn graph or overlap-layout-consensus (OLC) approaches depending on read characteristics.

- **Error Correction**: Includes built-in error correction for improving read quality before assembly.

- **Contig Scaffolding**: Supports scaffolding of contigs using paired-end reads or mate-pair libraries.

## Pitfalls

- **Memory Requirements**: Assembly of large genomes requires significant memory. Consider using machines with sufficient RAM.

- **Read Quality**: Low-quality reads can introduce errors in the assembly. Preprocess reads with quality filtering.

- **k-mer Selection**: Choosing the appropriate k-mer size is critical. Too small k-mers increase noise, too large k-mers reduce sensitivity.

- **Computational Time**: Assembling very large genomes can be computationally intensive. Consider parallel processing options.

- **Repeat Regions**: Highly repetitive regions can cause misassembly. Use additional scaffolding data when available.

## Examples

### Basic genome assembly
**Args:** `goldrush -i reads.fastq -o assembly.fasta`
**Explanation:** Assembles long reads into contigs and saves the result to assembly.fasta.

### Specify k-mer size
**Args:** `goldrush -i reads.fastq -k 51 -o assembly.fasta`
**Explanation:** Uses k-mer size 51 for assembly, suitable for longer reads with higher accuracy.

### Enable error correction
**Args:** `goldrush -i reads.fastq --correct -o assembly.fasta`
**Explanation:** Performs error correction on reads before assembly to improve accuracy.

### Use multiple threads
**Args:** `goldrush -i reads.fastq -t 8 -o assembly.fasta`
**Explanation:** Uses 8 threads for parallel processing to accelerate assembly.

### Scaffold contigs
**Args:** `goldrush -i reads.fastq -p paired_reads.fastq -o scaffolded.fasta`
**Explanation:** Uses paired-end reads to scaffold contigs into larger sequences.

### Generate assembly graph
**Args:** `goldrush -i reads.fastq --graph -o assembly.gfa`
**Explanation:** Generates the assembly graph in GFA format for visualization and analysis.

### Set minimum contig length
**Args:** `goldrush -i reads.fastq -m 1000 -o assembly.fasta`
**Explanation:** Filters out contigs shorter than 1000 base pairs from the output.