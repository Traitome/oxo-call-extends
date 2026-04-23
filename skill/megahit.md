---
name: megahit
category: assembly
description: MEGAHIT: An ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph.
tags: [megahit, assembly]
author: oxo-call-community
source_url: "https://github.com/voutcn/megahit"
---

## Concepts

- **Tool Overview**: megahit v1.2.9 - MEGAHIT: An ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph..
- **Core Function**: MEGAHIT: An ultra-fast single-node solution for large and complex metagenomics assembly via succinct de Bruijn graph.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda megahit`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Assemble reads
**Args:** `megahit -1 R1.fq.gz -2 R2.fq.gz -o output_dir`
**Explanation:** Assembles metagenomic reads into contigs.

