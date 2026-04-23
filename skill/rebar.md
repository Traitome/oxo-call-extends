---
name: rebar
category: variant-calling
description: Genomic recombination detection using mutational barcodes.
tags: ["rebar", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/phac-nml/rebar"
---

## Concepts

- **Tool Overview**: Genomic recombination detection using mutational barcodes. (version 0.2.1)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rebar`

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

