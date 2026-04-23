---
name: mvicuna
category: assembly
description: M-Vicuna is a modularized version of VICUNA, a de novo assembly program targeting populations with high mutation rates
tags: [mvicuna, assembly, de-novo, viral, mutation]
author: oxo-call-community
source_url: "https://www.broadinstitute.org/scientific-community/science/projects/viral-genomics/vicuna"
---

## Concepts

- **Tool Overview**: M-Vicuna v1.0 - modularized de novo assembler for populations with high mutation rates.
- **Core Function**: Assembles viral quasispecies from sequencing data where high mutation rates complicate standard assembly.
- **Input/Output**: Takes FASTQ reads; outputs consensus contigs/assemblies.
- **Installation**: `conda install -c bioconda mvicuna`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct FASTQ input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o output_dir`
**Explanation:** Runs de novo assembly on input reads targeting highly variable populations.
