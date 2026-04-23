---
name: gpatch
category: alignment
description: Starting with alignments of contigs to a reference genome, produce a chromosome-scale pseudoassembly by patching gaps between mapped contigs with sequences from the reference. Download the github repository for helper scripts to automate GPatch workflows, identify and correct misjoins in the contig assembly, produce dot-plots of patched pseudoassemblies to a reference assembly, and generate chrom.sizes and liftover chains for patched pseudoassemblies."
tags: [gpatch, alignment]
author: oxo-call-community
source_url: "https://github.com/adadiehl/GPatch.git"
---

## Concepts

- **Tool Overview**: gpatch (v0.4.0) - Starting with alignments of contigs to a reference genome, produce a chromosome-scale pseudoassembly by patching gaps between mapped contigs with sequences from the reference. Download the github repository for helper scripts to automate GPatch workflows, identify and correct misjoins in the contig assembly, produce dot-plots of patched pseudoassemblies to a reference assembly, and generate chrom.sizes and liftover chains for patched pseudoassemblies."
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda gpatch`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
