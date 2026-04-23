---
name: mydbfinder
category: annotation
description: MyDbFinder identifies genes from your own database in total or partial sequenced isolates of bacteria.
tags: [mydbfinder, annotation, gene-detection, database, bacteria]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/mydbfinder"
---

## Concepts

- **Tool Overview**: MyDbFinder v1.0.5 - identifies genes from custom databases in bacterial isolates.
- **Core Function**: Screens bacterial genomes against user-provided databases to detect specific genes.
- **Input/Output**: Takes bacterial genome assemblies and custom database; outputs detected genes with matches.
- **Installation**: `conda install -c bioconda mydbfinder`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly formatted custom database.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i genome.fasta -d custom_db -o results.tsv`
**Explanation:** Screens genome against custom database for gene detection.
