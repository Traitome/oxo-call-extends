---
name: cryptogenotyper
category: variant-calling
description: This package crypto_typer: tool to subtype the parasite, Cryptosporidium, based on the 18S and gp60 markers.
tags: [cryptogenotyper, variant-calling]
author: oxo-call-community
source_url: "https://github.com/phac-nml/CryptoGenotyper"
---

## Concepts

- **Tool Overview**: cryptogenotyper (v1.5.0) - This package crypto_typer: tool to subtype the parasite, Cryptosporidium, based on the 18S and gp60 markers.
- **Core Function**: A comprehensive tool for subtyping the parasite Cryptosporidium based on two key genetic markers: 18S and gp60. The tool provides a streamlined workflow for analyzing sequencing data and assigning spe...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cryptogenotyper`

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
