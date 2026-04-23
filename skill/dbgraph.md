---
name: dbgraph
category: assembly
description: A graph-centric approach for metagenome-guided peptide identification in metaproteomics.
tags: [dbgraph, assembly]
author: oxo-call-community
source_url: "https://github.com/jj-umn/graph2pro-var"
---

## Concepts

- **Tool Overview**: dbgraph (v1.0.0) - A graph-centric approach for metagenome-guided peptide identification in metaproteomics.
- **Core Function**: Includes program DBGraph2Pro and DBGraphPep2Pro. Creates a peptide and protein database from graph generated from nucleotide sequencing data using MEGAHIT or MetaSpades. A graph-centric approach for m...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda dbgraph`

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
