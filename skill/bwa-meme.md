---
name: bwa-meme
category: alignment
description: Faster BWA-MEM2 using learned-index for accelerated alignment
tags: [bwa-meme, alignment, learned-index, fast]
author: oxo-call-community
source_url: "https://github.com/kaist-ina/BWA-MEME"
---

## Concepts

- **Tool Overview**: BWA-MEME accelerates BWA-MEM2 using learned index structures.
- **Core Function**: Maps reads faster than BWA-MEM2 using machine learning-based indexing.
- **Algorithm**: Replaces FM-index lookup with learned index for faster seed finding.
- **Compatibility**: Produces identical output to BWA-MEM2.
- **Installation**: Install via bioconda: `conda install -c bioconda bwa-meme`

## Pitfalls

- **Linux Only**: Currently only available on Linux-64.
- **Index Training**: Requires training step to build learned index.
- **Memory Usage**: May use more memory than BWA-MEM2.

## Examples

### Build learned index
**Args:** `bwa-meme index reference.fa`
**Explanation:** Builds learned index from reference genome.

### Align reads
**Args:** `bwa-meme mem -t 8 reference.fa reads.fq > aligned.sam`
**Explanation:** Aligns reads using learned index for faster mapping.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
