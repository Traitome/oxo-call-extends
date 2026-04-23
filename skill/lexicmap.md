---
name: lexicmap
category: alignment
description: efficient sequence alignment against millions of prokaryotic genomes
tags: [lexicmap, alignment]
author: oxo-call-community
source_url: "https://github.com/shenwei356/LexicMap"
---

## Concepts

- **Tool Overview**: lexicmap v0.9.0 - efficient sequence alignment against millions of prokaryotic genomes.
- **Core Function**: efficient sequence alignment against millions of prokaryotic genomes
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda lexicmap`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Index references
**Args:** `lexicmap index -k 31 -s reference.fasta -o index_dir`
**Explanation:** Builds LexicMap index from reference sequences.

### Search queries
**Args:** `lexicmap search -i index_dir -q queries.fasta -o results.tsv`
**Explanation:** Searches query sequences against indexed references.

