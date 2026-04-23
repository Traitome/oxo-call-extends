---
name: rnasnp
category: variant-calling
description: Efficient detection of local RNA secondary structure changes induced by SNPs.
tags: ["rnasnp", "variant-calling"]
author: oxo-call-community
source_url: "http://rth.dk/resources/rnasnp/software"
---

## Concepts

- **Tool Overview**: Efficient detection of local RNA secondary structure changes induced by SNPs. (version 1.2)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rnasnp`

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

