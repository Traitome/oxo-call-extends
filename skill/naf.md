---
name: naf
category: formatting
description: Compressed binary file format for DNA/RNA/protein sequence data
tags: [naf, formatting, compression, sequence, binary]
author: oxo-call-community
source_url: "https://github.com/KirillKryukov/naf"
---

## Concepts

- **Tool Overview**: NAF v1.3.0 - compressed binary file format for DNA/RNA/protein sequence data.
- **Core Function**: Provides high-compression binary format for sequence data with fast random access.
- **Input/Output**: Takes FASTA/FASTQ; outputs compressed NAF format, and vice versa.
- **Installation**: `conda install -c bioconda naf`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Format Compatibility**: NAF is a specialized format; convert back for tools requiring FASTA/FASTQ.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Compress FASTA
**Args:** `-c input.fasta -o output.naf`
**Explanation:** Compresses FASTA file to NAF format.

### Decompress NAF
**Args:** `-d input.naf -o output.fasta`
**Explanation:** Decompresses NAF file back to FASTA format.
