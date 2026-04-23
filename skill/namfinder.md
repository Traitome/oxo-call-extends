---
name: namfinder
category: alignment
description: Finds Non-overlapping Approximate Matches (NAMs) between query and reference sequences using strobemers
tags: [namfinder, alignment, strobemers, approximate-matching, sequence]
author: oxo-call-community
source_url: "https://github.com/ksahlin/namfinder"
---

## Concepts

- **Tool Overview**: NAMfinder v0.1.3 - finds non-overlapping approximate matches using strobemers.
- **Core Function**: Identifies approximate sequence matches between query and reference using strobemer technology.
- **Input/Output**: Takes query and reference FASTA files; outputs NAMs in tabular format.
- **Installation**: `conda install -c bioconda namfinder`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FASTA format for query and reference.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-q query.fasta -r reference.fasta -o nams.tsv`
**Explanation:** Finds non-overlapping approximate matches between sequences.
