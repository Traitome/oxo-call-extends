---
name: dawg
category: variant-calling
description: DNA Assembly with Gaps (Dawg) is an application designed to simulate the evolution of recombinant DNA sequences in continuous time based on the robust general time reversible model with gamma and invariant rate heterogeneity and a novel length-dependent model of gap formation.
tags: [dawg, variant-calling]
author: oxo-call-community
source_url: "https://github.com/reedacartwright/dawg"
---

## Concepts

- **Tool Overview**: dawg (v2.0.beta1) - DNA Assembly with Gaps (Dawg) is an application designed to simulate the evolution of recombinant DNA sequences in continuous time based on the robust general time reversible model with gamma and invariant rate heterogeneity and a novel length-dependent model of gap formation.
- **Core Function**: DNA Assembly with Gaps (Dawg) is an application designed to simulate the evolution of recombinant DNA sequences in continuous time based on the robust general time reversible model with gamma and invariant rate heterogeneity and a novel length-dependent model of gap formation.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda dawg`

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
