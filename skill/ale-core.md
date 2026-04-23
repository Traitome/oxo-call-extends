---
name: ale-core
category: assembly
description: ALE: Assembly Likelihood Estimator. Core C implemented  scoring programs only without supplementary plotting scripts.
tags: [ale-core, assembly]
author: oxo-call-community
source_url: "https://github.com/sc932/ALE"
---

## Concepts

- **Tool Overview**: ale-core (v20220503) - ALE: Assembly Likelihood Estimator. Core C implemented  scoring programs only without supplementary plotting scripts.
- **Core Function**: This package is designed to hold the core scoring functionality of ALE without the 10+ year old supplementary python plotting scripts
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ale-core`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
