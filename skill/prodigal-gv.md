---
name: prodigal-gv
category: variant-calling
description: A fork of Prodigal meant to improve gene calling for giant viruses
tags: ["prodigal-gv", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/apcamargo/prodigal-gv"
---

## Concepts

- **Tool Overview**: A fork of Prodigal meant to improve gene calling for giant viruses (version 2.11.0)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda prodigal-gv`

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

