---
name: mvirs
category: metagenomics
description: mVIRs: Localisation of inducible prophages using NGS data
tags: [mvirs, metagenomics, prophage, localization, ngv]
author: oxo-call-community
source_url: "https://github.com/SushiLab/mVIRs"
---

## Concepts

- **Tool Overview**: mVIRs v1.1.1 - localizes inducible prophages using NGS data.
- **Core Function**: Identifies and localizes inducible prophages within bacterial genomes using next-generation sequencing data.
- **Input/Output**: Takes NGS read data; outputs predicted prophage locations.
- **Installation**: `conda install -c bioconda mvirs`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct NGS input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.bam -o prophage_locations.tsv`
**Explanation:** Identifies inducible prophage locations from NGS data.
