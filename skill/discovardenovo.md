---
name: discovardenovo
category: assembly
description: DISCOVAR de novo - De novo assembly of large and small genomes.
tags: [discovardenovo, assembly, de-novo, genome, broad-institute]
author: oxo-call-community
source_url: "https://www.broadinstitute.org/software/discovar/"
---

## Concepts

- **Tool Overview**: DISCOVAR de novo (v52488+) is a de novo assembly tool for both large and small genomes.
- **Core Function**: Assembles genomes de novo from high-quality paired-end sequencing data.
- **Input/Output**: Input: Paired-end reads (FASTQ). Output: Genome assemblies in FASTA format, assembly statistics.
- **Algorithm**: Uses de Bruijn graph assembly optimized for high-coverage data.
- **Key Features**: De novo assembly, handles large genomes, high accuracy, gap closure, quality assessment.
- **Installation**: `conda install -c bioconda discovardenovo`

## Pitfalls

- **Input Requirements**: Requires high-coverage PCR-free paired-end reads.
- **Computational Resources**: Requires significant computational resources for large genomes.
- **Memory Usage**: High memory requirements for large datasets.
- **Read Quality**: Poor quality reads affect assembly quality.
- **Contamination**: Contaminating sequences affect assembly.

## Examples

### De novo genome assembly
**Args:** `discovardenovo --reads R1.fq R2.fq --output assembly.fa`
**Explanation:** Performs de novo genome assembly from paired-end reads.

### With quality trimming
**Args:** `discovardenovo --reads R1.fq R2.fq --output assembly.fa --trim-quality 20`
**Explanation:** Trim low quality bases before assembly.

### Gap closure mode
**Args:** `discovardenovo --reads R1.fq R2.fq --output assembly.fa --close-gaps`
**Explanation:** Attempt gap closure in assembly.

### Generate statistics
**Args:** `discovardenovo --reads R1.fq R2.fq --output assembly.fa --stats stats.tsv`
**Explanation:** Generate assembly quality statistics.

### Large genome mode
**Args:** `discovardenovo --reads R1.fq R2.fq --output assembly.fa --large-genome`
**Explanation:** Optimize for large genome assembly.