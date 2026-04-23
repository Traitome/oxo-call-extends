---
name: kmcp
category: metagenomics
description: accurate metagenomic profiling of both prokaryotic and viral populations by pseudo-mapping
tags: [kmcp, metagenomics]
author: oxo-call-community
source_url: "https://github.com/shenwei356/kmcp"
---

## Concepts

- **Tool Overview**: kmcp v0.9.4 - accurate metagenomic profiling of both prokaryotic and viral populations by pseudo-mapping.
- **Core Function**: accurate metagenomic profiling of both prokaryotic and viral populations by pseudo-mapping
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kmcp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Index genomes
**Args:** `kmcp index -I genomes.fasta -O index_dir`
**Explanation:** Indexes genome sequences for KMCP search.

### Search reads
**Args:** `kmcp search -d index_dir -1 reads_R1.fq.gz -2 reads_R2.fq.gz -o results.tsv`
**Explanation:** Searches metagenomic reads against indexed genomes.

