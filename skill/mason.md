---
name: mason
category: utility
description: Collection of tools for simulating biological sequences including DNA, RNA, and sequencing reads.
tags: [mason, simulation, sequencing, reads]
author: oxo-call-community
source_url: "https://www.seqan.de/apps/mason.html"
---

## Concepts

- **Tool Overview**: Mason is a comprehensive suite for simulating biological sequences and sequencing data.
- **Core Function**: Simulates Illumina, PacBio, and Ion Torrent sequencing reads with realistic errors.
- **Simulation Types**: Supports DNA/RNA sequence simulation, variant simulation, and read simulation.
- **Error Models**: Implements realistic sequencing error models for different platforms.
- **Input/Output**: Accepts reference sequences, produces simulated reads and variants.
- **Installation**: `conda install -c bioconda mason`

## Pitfalls

- **Parameter Complexity**: Many parameters require careful adjustment for realistic simulations.
- **Memory Requirements**: Simulating large genomes requires significant memory.
- **Computation Time**: Generating large datasets can be time-consuming.
- **Reference Quality**: Simulation accuracy depends on input reference quality.
- **Error Model Selection**: Choosing the wrong error model can produce unrealistic data.
- **Output Size**: Large simulations can generate massive output files.

## Examples

### Simulate Illumina reads
**Args:** `mason illumina -i reference.fasta -o reads.fastq -c 50`
**Explanation:** Simulates 50x coverage Illumina reads.

### Simulate variants
**Args:** `mason variant -i reference.fasta -v variants.vcf -o mutated.fasta`
**Explanation:** Introduces variants from VCF into reference.

### Paired-end simulation
**Args:** `mason illumina -i reference.fasta -o reads_1.fastq -o2 reads_2.fastq -c 30`
**Explanation:** Generates paired-end reads with 30x coverage.

### With quality scores
**Args:** `mason illumina -i reference.fasta -o reads.fastq -q -c 50`
**Explanation:** Includes quality scores in output.

### Custom error rate
**Args:** `mason illumina -i reference.fasta -o reads.fastq -e 0.01 -c 50`
**Explanation:** Sets custom error rate of 1%.

### PacBio simulation
**Args:** `mason pacbio -i reference.fasta -o reads.fastq -c 20`
**Explanation:** Simulates PacBio sequencing reads.
