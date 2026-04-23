---
name: condiga
category: assembly
description: ConDiGA: Contigs Directed Gene Annotation for accurate protein sequence database construction in metaproteomics
tags: [condiga, assembly]
author: oxo-call-community
source_url: "https://github.com/metagentools/ConDiGA"
---

## Concepts

- **Tool Overview**: condiga (v0.2.2) - ConDiGA: Contigs Directed Gene Annotation for accurate protein sequence database construction in metaproteomics
- **Core Function**: ConDiGA is a taxonomic annotation pipeline for metagenomic data to construct accurate protein sequence databases for deep metaproteomic coverage.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda condiga`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
