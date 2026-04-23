---
name: diamond_add_taxonomy
category: annotation
description: Utility to annotate DIAMOND results with NCBI taxonomy lineage.
tags: [diamond_add_taxonomy, annotation, taxonomy, diamond, ncbi]
author: oxo-call-community
source_url: "https://github.com/pvanheus/diamond_add_taxonomy"
---

## Concepts

- **Tool Overview**: diamond_add_taxonomy v0.1.2 - Utility for adding NCBI taxonomy information to DIAMOND search results.
- **Core Function**: Annotates DIAMOND alignment output with taxonomic lineage information from NCBI taxonomy database.
- **Input/Output**: Expects DIAMOND output (format 6) and NCBI taxonomy files; outputs annotated results with taxonomy.
- **Installation**: `conda install -c bioconda diamond_add_taxonomy`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires DIAMOND tabular output and NCBI taxonomy dump files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `diamond_add_taxonomy --input diamond.out --taxonmap prot.accession2taxid --taxonnodes nodes.dmp --output annotated.out`
**Explanation:** Adds taxonomy lineage to DIAMOND search results.
