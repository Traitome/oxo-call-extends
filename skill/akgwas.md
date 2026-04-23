---
name: akgwas
category: assembly
description: AKmerGWAS -- All input format (shor_read; assembly; genomes) k-mer GWAS.
tags: [akgwas, assembly]
author: oxo-call-community
source_url: "https://github.com/suzkami/Aseembly_GWAS"
---

## Concepts

- **Tool Overview**: akgwas (v0.1.0) - AKmerGWAS -- All input format (shor_read; assembly; genomes) k-mer GWAS.
- **Core Function**: AKmerGWAS is a pipeline for k-mer based genome-wide association studies with any input format (shor_read; assembly; genomes).
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda akgwas`

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
