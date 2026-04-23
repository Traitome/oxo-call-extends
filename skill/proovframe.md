---
name: proovframe
category: variant-calling
description: frame-shift correction for long read (meta)genomics
tags: ["proovframe", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/thackl/proovframe"
---

## Concepts

- **Tool Overview**: frame-shift correction for long read (meta)genomics (version 0.9.7)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda proovframe`

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

