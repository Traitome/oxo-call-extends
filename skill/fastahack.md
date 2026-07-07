---
name: fastahack
category: formatting
description: "fastahack --- *fast* FASTA file indexing, subsequence and sequence extraction"
tags: [fastahack, formatting, FASTA, sequence-extraction, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ekg/fastahack"
---

## Concepts

- **Tool Overview**: fastahack is a fast FASTA file indexing tool for rapid subsequence and sequence extraction.
- **Core Function**: Creates index for FASTA files and enables fast random access to sequences and subsequences.
- **Input/Output**: Input: FASTA file. Output: Index file, extracted sequences.
- **Algorithm**: Uses indexing algorithm for fast sequence lookup.
- **Key Features**: Fast indexing, random access, subsequence extraction, lightweight, efficient memory usage.
- **Installation**: `conda install -c bioconda fastahack`

## Pitfalls

- **Index File**: Requires index file for fast access.
- **Memory Usage**: Indexing large files may require significant memory.
- **Format Compatibility**: Requires standard FASTA format.
- **File Size**: Very large FASTA files may affect performance.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Create index
**Args:** `fastahack -i genome.fasta -f genome.fasta.fai`
**Explanation:** Creates index for FASTA file.

### Extract sequence
**Args:** `fastahack -i genome.fasta -s chr1`
**Explanation:** Extracts entire sequence by name.

### Extract subsequence
**Args:** `fastahack -i genome.fasta -s chr1:1000-2000`
**Explanation:** Extracts subsequence by coordinates.

### List sequences
**Args:** `fastahack -i genome.fasta -l`
**Explanation:** Lists all sequence names.

### Batch extraction
**Args:** `fastahack -i genome.fasta -b regions.bed -o extracted.fasta`
**Explanation:** Extracts multiple regions from BED file.