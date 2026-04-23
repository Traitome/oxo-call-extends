---
name: disco
category: assembly
description: DISCO - De novo assembly of circular genomes.
tags: [disco, assembly, circular-genome, prokaryote]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DISCO - De novo assembly tool for circular genomes like bacterial chromosomes and plasmids.
- **Core Function**: Assembles circular genomes from sequencing data with special handling for circular structures.
- **Input/Output**: Expects paired-end reads; outputs circular genome assemblies.
- **Installation**: `conda install -c bioconda disco`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires paired-end sequencing reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `disco --reads R1.fq R2.fq --output assembly/`
**Explanation:** Assembles circular genome from paired-end reads.
