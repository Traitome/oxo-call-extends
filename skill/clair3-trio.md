---
name: clair3-trio
category: variant-calling
description: Clair3-Trio is a variants caller tailored for family trios from nanopore long-reads. Clair3-Trio employs a Trio-to-Trio deep neural network model that allows it to input all trio’s sequencing information and output all trio’s predicted variants within a single model, to perform far better variant calling. We also present MCVLoss, the first loss function that can improve variants calling in trios by leveraging the explicitly encoding of the priors of the Mendelian inheritance in trios. Clair3-Trio showed comprehensive improvement in experiments. It predicted much fewer Mendelian inheritance violation variations than current state-of-the-art methods.
tags: [clair3-trio, variant-calling]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/Clair3-Trio"
---

## Concepts

- **Tool Overview**: clair3-trio (v0.7) - Clair3-Trio is a variants caller tailored for family trios from nanopore long-reads. Clair3-Trio employs a Trio-to-Trio deep neural network model that allows it to input all trio’s sequencing information and output all trio’s predicted variants within a single model, to perform far better variant calling. We also present MCVLoss, the first loss function that can improve variants calling in trios by leveraging the explicitly encoding of the priors of the Mendelian inheritance in trios. Clair3-Trio showed comprehensive improvement in experiments. It predicted much fewer Mendelian inheritance violation variations than current state-of-the-art methods.
- **Core Function**: Clair3-Trio is a variants caller tailored for family trios from nanopore long-reads. Clair3-Trio employs a Trio-to-Trio deep neural network model that allows it to input all trio’s sequencing information and output all trio’s predicted variants within a single model, to perform far better variant calling. We also present MCVLoss, the first loss function that can improve variants calling in trios by leveraging the explicitly encoding of the priors of the Mendelian inheritance in trios. Clair3-Trio showed comprehensive improvement in experiments. It predicted much fewer Mendelian inheritance violation variations than current state-of-the-art methods.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda clair3-trio`

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
