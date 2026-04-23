---
name: discovardenovo
category: assembly
description: DISCOVAR de novo - De novo assembly of large and small genomes.
tags: [discovardenovo, assembly, de-novo, genome]
author: oxo-call-community
source_url: "https://www.broadinstitute.org/software/discovar/"
---

## Concepts

- **Tool Overview**: DISCOVAR de novo v52488 - De novo assembly tool for both large and small genomes.
- **Core Function**: Assembles genomes de novo from high-quality paired-end sequencing data.
- **Input/Output**: Expects paired-end reads; outputs genome assemblies in FASTA format.
- **Installation**: `conda install -c bioconda discovardenovo`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires high-coverage PCR-free paired-end reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `discovardenovo --reads R1.fq R2.fq --output assembly.fa`
**Explanation:** Performs de novo genome assembly.
