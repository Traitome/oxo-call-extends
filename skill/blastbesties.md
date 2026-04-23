---
name: blastbesties
category: alignment
description: Rapid discovery of reciprocal best BLAST pairs from BLAST output files
tags: [blastbesties, blast, orthologs, reciprocal-best-hit]
author: oxo-call-community
source_url: "https://github.com/Adamtaranto/blast-besties"
---

## Concepts

- **Tool Overview**: BlastBesties finds reciprocal best BLAST hits (RBH) from BLAST output files.
- **Core Function**: Identifies orthologous gene pairs using reciprocal best hit approach.
- **Input**: BLAST tabular output files (-outfmt 6).
- **Output**: Reciprocal best hit pairs with match statistics.
- **Application**: Ortholog identification for comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda blastbesties`

## Pitfalls

- **BLAST Format**: Requires tabular BLAST output (-outfmt 6).
- **Bidirectional BLAST**: Both forward and reverse BLAST results needed.
- **E-value Threshold**: Adjust threshold for appropriate stringency.
- **Self-Hits**: Tool automatically excludes self-matches.

## Examples

### Find reciprocal best hits
**Args:** `blastbesties -a speciesA_vs_B.tsv -b speciesB_vs_A.tsv -o rbh_pairs.tsv`
**Explanation:** Identifies reciprocal best BLAST hits between two species.

### With e-value filter
**Args:** `blastbesties -a fwd.tsv -b rev.tsv -e 1e-10 -o rbh_pairs.tsv`
**Explanation:** Applies e-value threshold of 1e-10 for RBH filtering.

### Output with full statistics
**Args:** `blastbesties -a fwd.tsv -b rev.tsv -v -o rbh_pairs.tsv`
**Explanation:** Verbose output includes all match statistics for RBH pairs.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
