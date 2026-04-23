---
name: modifi
category: variant-calling
description: DNA modification detection from PacBio SMRT metagenomic data
tags: [modifi, variant-calling]
author: oxo-call-community
source_url: "https://github.com/sachdevalab/MODIFI"
---

## Concepts

- **Tool Overview**: modifi v0.0.3 - MODIFI detects DNA base modifications and infers host-mobile genetic element (MGE) linkages from PacBio metagenomic sequencing data. It supports modification calling, motif discovery, and host-MGE association for both subreads and HiFi read types. Native motif finding uses pbmotifmaker (from pbtk) on Linux if installed; otherwise use the bundled MultiMotifMaker.jar (OpenJDK). On macOS, install PacBio tools separately or rely on the JAR fallback..
- **Core Function**: DNA modification detection from PacBio SMRT metagenomic data
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda modifi`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
