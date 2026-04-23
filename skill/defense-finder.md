---
name: defense-finder
category: annotation
description: Defense Finder - systematic search of all known anti-phage systems.
tags: [defense-finder, annotation, phage, defense-systems, bacteria]
author: oxo-call-community
source_url: "https://github.com/mdmparis/defense-finder"
---

## Concepts

- **Tool Overview**: Defense Finder v2.0.1 - Tool for systematic detection of anti-phage defense systems in bacterial genomes.
- **Core Function**: Identifies known anti-phage defense systems (CRISPR, restriction-modification, etc.) in prokaryotic genomes.
- **Input/Output**: Expects protein FASTA or genome files; outputs list of detected defense systems with annotations.
- **Installation**: `conda install -c bioconda defense-finder`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Works best with complete genomes or predicted proteins.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `defense-finder run --input proteins.fa --output results/`
**Explanation:** Searches for anti-phage defense systems in protein sequences.
