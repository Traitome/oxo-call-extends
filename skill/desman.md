---
name: desman
category: metagenomics
description: De novo Extraction of Strains from MetAgeNomes.
tags: [desman, metagenomics, strain, deconvolution, binning]
author: oxo-call-community
source_url: "https://github.com/chrisquince/DESMAN"
---

## Concepts

- **Tool Overview**: DESMAN v2.1 - Tool for de novo extraction of individual strain genomes from metagenomic data.
- **Core Function**: Resolves strain-level variation within metagenomic bins using SNP patterns and abundance information.
- **Input/Output**: Expects BAM files and MAG bins; outputs strain-resolved genomes and variant profiles.
- **Installation**: `conda install -c bioconda desman`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires mapped reads and genome bins from metagenomic assembly.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `desman --bam mapping.bam --bins bins/ --output strains/`
**Explanation:** Extracts strain genomes from metagenomic bins.
