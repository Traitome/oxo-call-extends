---
name: nanometa-live
category: metagenomics
description: Workflow and GUI for real-time species classification and pathogen characterization of nanopore sequence reads.
tags: [nanometa-live, metagenomics, nanopore, real-time, pathogen]
author: oxo-call-community
source_url: "https://github.com/FOI-Bioinformatics/nanometa_live"
---

## Concepts

- **Tool Overview**: NanoMeta-Live v0.4.3 - real-time species classification and pathogen characterization.
- **Core Function**: Provides GUI and workflow for real-time metagenomic analysis of Nanopore reads.
- **Input/Output**: Takes streaming Nanopore reads; outputs species classification and pathogen reports.
- **Installation**: `conda install -c bioconda nanometa-live`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Real-time Setup**: Requires proper configuration for real-time analysis.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads_directory -o output_dir`
**Explanation:** Runs real-time species classification on incoming Nanopore reads.
