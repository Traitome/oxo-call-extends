---
name: das_tool
category: assembly
description: Recovery of genomes from metagenomes via a dereplication, aggregation and scoring strategy.
tags: [das_tool, assembly]
author: oxo-call-community
source_url: "https://github.com/cmks/DAS_Tool"
---

## Concepts

- **Tool Overview**: das_tool (v1.1.7) - Recovery of genomes from metagenomes via a dereplication, aggregation and scoring strategy.
- **Core Function**: DAS Tool is an automated method that integrates the results of a flexible number of binning algorithms to calculate an optimized, non-redundant set of bins from a single assembly.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda das_tool`

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
