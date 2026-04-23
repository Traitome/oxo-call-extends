---
name: mwga-utils
category: alignment
description: Collection of utilities for processing Multispecies Whole Genome Alignments
tags: [mwga-utils, alignment, whole-genome, multispecies, utilities]
author: oxo-call-community
source_url: "https://github.com/RomainFeron/mgwa_utils"
---

## Concepts

- **Tool Overview**: MWGA-utils v0.1.6 - utilities for processing multispecies whole genome alignments.
- **Core Function**: Provides tools for manipulating and analyzing whole genome alignments across multiple species.
- **Input/Output**: Takes whole genome alignment files (MAF, etc.); outputs processed alignment data.
- **Installation**: `conda install -c bioconda mwga-utils`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct whole genome alignment format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i alignment.maf -o output_dir`
**Explanation:** Processes multispecies whole genome alignment files.
