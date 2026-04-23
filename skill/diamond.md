---
name: diamond
category: alignment
description: Accelerated BLAST compatible local sequence aligner.
tags: [diamond, alignment, blast, sequence-search, protein]
author: oxo-call-community
source_url: "https://github.com/bbuchfink/diamond"
---

## Concepts

- **Tool Overview**: DIAMOND v2.1.24 - High-performance BLAST-compatible sequence aligner for protein and translated DNA searches.
- **Core Function**: Performs fast sequence alignment similar to BLAST but 20,000x faster for protein searches using optimized algorithms.
- **Input/Output**: Expects FASTA query sequences and DIAMOND database; outputs alignments in BLAST-compatible formats.
- **Installation**: `conda install -c bioconda diamond`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires database creation with `diamond makedb` before searching.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available commands and options.

### Create database
**Args:** `diamond makedb --in proteins.fa -d mydb`
**Explanation:** Creates DIAMOND database from protein sequences.

### Run search
**Args:** `diamond blastp -d mydb -q queries.fa -o matches.m8`
**Explanation:** Runs BLASTP-like protein search against database.
