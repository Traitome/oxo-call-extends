---
name: dfam
category: annotation
description: The Dfam database is a collection of repetitive DNA element sequence alignments, HMMs and matches for Eukaryote genomes.
tags: [dfam, annotation, repeat, transposable-element, hmm]
author: oxo-call-community
source_url: "https://dfam.org"
---

## Concepts

- **Tool Overview**: Dfam v3.7 - Database and scanning tool for repetitive DNA elements (transposable elements) in eukaryotic genomes.
- **Core Function**: Identifies and annotates transposable elements and other repetitive sequences using HMM-based profiles.
- **Input/Output**: Expects genome FASTA files; outputs repeat annotations in GFF/FASTA format.
- **Installation**: `conda install -c bioconda dfam`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires genome sequence in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dfamscan.pl --seq genome.fa --output repeats.gff`
**Explanation:** Scans genome for repetitive elements using Dfam HMM profiles.
