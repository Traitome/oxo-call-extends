---
name: pyhoward
category: variant-calling
description: HOWARD - Highly Open Workflow for Annotation & Ranking toward genomic variant Discovery
tags: ["pyhoward", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/bioinfo-chru-strasbourg/howard"
---

## Concepts

- **Tool Overview**: HOWARD - Highly Open Workflow for Annotation & Ranking toward genomic variant Discovery (version 0.13.0)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pyhoward`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Call variants
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Identifies variants from aligned reads.

