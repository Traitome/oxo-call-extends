---
name: arb-bio-devel
category: alignment
description: ARB 6 Sequence Analysis Suite
tags: [arb-bio-devel, alignment, SAM]
author: oxo-call-community
source_url: "http://www.arb-home.de/documentation.html"
---

## Concepts

- **Tool Overview**: arb-bio-devel (v6.0.6) - ARB 6 Sequence Analysis Suite
- **Core Function**: "ARB (ARBor, Latin: tree): A software environment for maintaining databases of molecular sequences and additional information, and for analyzing the sequence data, with emphasis on phylogeny reconstru...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda arb-bio-devel`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
