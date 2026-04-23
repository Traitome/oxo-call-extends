---
name: bcftools-snvphyl-plugin
category: variant-calling
description: The SNVPhyl (Single Nucleotide Variant PHYLogenomics) pipeline is a pipeline for identifying Single Nucleotide Variants (SNV) within a collection\ of microbial genomes and constructing a phylogenetic tree. This package is the bcftools C plugin
tags: [bcftools-snvphyl-plugin, variant-calling]
author: oxo-call-community
source_url: "https://github.com/phac-nml/snvphyl-tools"
---

## Concepts

- **Tool Overview**: bcftools-snvphyl-plugin (v1.9) - The SNVPhyl (Single Nucleotide Variant PHYLogenomics) pipeline is a pipeline for identifying Single Nucleotide Variants (SNV) within a collection\ of microbial genomes and constructing a phylogenetic tree. This package is the bcftools C plugin
- **Core Function**: The SNVPhyl (Single Nucleotide Variant PHYLogenomics) pipeline is a pipeline for identifying Single Nucleotide Variants (SNV) within a collection\ of microbial genomes and constructing a phylogenetic tree. This package is the bcftools C plugin
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda bcftools-snvphyl-plugin`

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
