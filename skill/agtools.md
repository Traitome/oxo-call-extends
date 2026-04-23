---
name: agtools
category: assembly
description: agtools: A Software Framework to Manipulate Assembly Graphs
tags: [agtools, assembly]
author: oxo-call-community
source_url: "https://agtools.readthedocs.io/"
---

## Concepts

- **Tool Overview**: agtools (v1.1.0) - agtools: A Software Framework to Manipulate Assembly Graphs
- **Core Function**: agtools is a Python framework for manipulating assembly graphs for downstream metagenomic applications, with a focus on the Graphical Fragment Assembly (GFA) format.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda agtools`

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
