---
name: bcbio-variation
category: variant-calling
description: Toolkit to analyze genomic variation data, built on the GATK with Clojure
tags: [bcbio-variation, variant-calling]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbio.variation"
---

## Concepts

- **Tool Overview**: bcbio-variation (v0.2.6) - Toolkit to analyze genomic variation data, built on the GATK with Clojure
- **Core Function**: Toolkit to analyze genomic variation data, built on the GATK with Clojure
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda bcbio-variation`

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
