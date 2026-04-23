---
name: dbcanlight
category: annotation
description: A lightweight CAZyme annotation tool
tags: [dbcanlight, annotation, SAM]
author: oxo-call-community
source_url: "https://github.com/chtsai0105/dbcanlight/blob/v1.1.1/README.md"
---

## Concepts

- **Tool Overview**: dbcanlight (v1.1.1) - A lightweight CAZyme annotation tool
- **Core Function**: Dbcanlight is a lightweight rewrite of a widely used CAZyme annotation tool run_dbcan. It uses pyhmmer, a Cython binding to HMMER3, in place of the HMMER3 CLI suite as the backend for search processes...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda dbcanlight`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o annotation.gff`
**Explanation:** Annotate genomic features
