---
name: discovar
category: assembly
description: DISCOVAR - De novo genome assembly and variant discovery.
tags: [discovar, assembly, variant-calling, genome]
author: oxo-call-community
source_url: "https://www.broadinstitute.org/software/discovar/"
---

## Concepts

- **Tool Overview**: DISCOVAR - Genome assembly and variant discovery tool from Broad Institute.
- **Core Function**: Assembles genomes and discovers variants from high-coverage PCR-free data.
- **Input/Output**: Expects paired-end reads; outputs assemblies and variant calls.
- **Installation**: `conda install -c bioconda discovar`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires high-coverage PCR-free paired-end data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `discovar --reads R1.fq R2.fq --output assembly/`
**Explanation:** Assembles genome and discovers variants.
