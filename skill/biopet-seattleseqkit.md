---
name: biopet-seattleseqkit
category: variant-calling
description: #### Tool - Filter  This tool can filter a seattle seq file.
tags: [biopet-seattleseqkit, variant-calling, BED]
author: oxo-call-community
source_url: "https://github.com/biopet/seattleseqkit"
---

## Concepts

- **Tool Overview**: biopet-seattleseqkit (v0.2) - #### Tool - Filter  This tool can filter a seattle seq file.
- **Core Function**: #### Tool - Filter  This tool can filter a seattle seq file. A given bed file will only select variants inside this regions. Filtering on specific fields is also possible.                #### Tool - M...
- **Input/Output**: BED interval input/output
- **Installation**: `conda install -c bioconda biopet-seattleseqkit`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
