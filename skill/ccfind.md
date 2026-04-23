---
name: ccfind
category: assembly
description: Circular Complete genome FINDer for detecting circular complete genomes
tags: [ccfind, circular-genome, virus, metagenomics]
author: oxo-call-community
source_url: "https://github.com/yosuken/ccfind"
---

## Concepts

- **Tool Overview**: ccfind detects circular complete genomes from metagenome assemblies.
- **Core Function**: Identifies circular contigs with terminal redundancy indicating completeness.
- **Algorithm**: Detects terminal redundancy patterns suggesting circular genomes.
- **Input**: Assembled contigs in FASTA format.
- **Output**: List of circular complete genomes with evidence.
- **Application**: Virus discovery and plasmid detection in metagenomes.
- **Installation**: Install via bioconda: `conda install -c bioconda ccfind`

## Pitfalls

- **Assembly Quality**: Requires good quality assembly with contig coverage.
- **Terminal Redundancy**: Relies on detecting terminal redundancy patterns.
- **False Positives**: Repetitive regions may cause false circular calls.
- **Minimum Length**: Set appropriate minimum contig length.

## Examples

### Find circular genomes
**Args:** `ccfind -i contigs.fa -o circular_genomes.tsv`
**Explanation:** Identifies circular complete genomes from metagenome assembly.

### Set minimum length
**Args:** `ccfind -i contigs.fa -l 1000 -o circular.tsv`
**Explanation:** Only reports circular genomes at least 1kb in length.

### Display help
**Args:** `ccfind --help`
**Explanation:** Shows all available options and usage information.
