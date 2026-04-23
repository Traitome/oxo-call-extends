---
name: sawfish
category: variant-calling
description: Joint structural variant and copy number variant caller for HiFi sequencing data
tags: ["sawfish", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/sawfish"
---

## Concepts

- **Tool Overview**: Joint structural variant and copy number variant caller for HiFi sequencing data (version 2.2.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sawfish`

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

