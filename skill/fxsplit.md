---
name: fxsplit
category: utility
description: Split FASTX (and 2bit) into N chunks/files/headers.
tags: [fxsplit, FASTX, sequence processing, file splitting]
author: oxo-call-community
source_url: "https://github.com/alejandrogzi/fxsplit"
---

## Concepts
- **FASTX Splitting**: Splits FASTQ/FASTA files into multiple chunks.
- **Multiple Formats**: Supports FASTQ, FASTA, and 2bit formats.
- **Chunking Strategies**: Multiple ways to split files (by size, by number).
- **Efficient Processing**: Optimized for large sequence files.
- **Parallel Processing**: Supports parallel splitting.

## Pitfalls
- **Memory Usage**: Large files require significant memory.
- **Output Management**: Many output files can be difficult to manage.
- **Format Compatibility**: Requires proper input format.
- **Splitting Strategy**: Choosing wrong strategy can affect downstream analysis.
- **Indexing**: Split files may need re-indexing.

## Examples
### Split by number of reads
**Args:** `fxsplit -i reads.fastq -n 10 -o split_`
**Explanation:** Splits FASTQ into 10 equal parts.

### Split by file size
**Args:** `fxsplit -i reads.fastq -s 1G -o split_`
**Explanation:** Splits FASTQ into 1GB chunks.

### Split FASTA by sequences
**Args:** `fxsplit -i genome.fasta -n 5 -o chr_`
**Explanation:** Splits FASTA into 5 files.

### Parallel splitting
**Args:** `fxsplit -i reads.fastq -n 10 -t 4 -o split_`
**Explanation:** Splits using 4 threads.

### Split 2bit file
**Args:** `fxsplit -i genome.2bit -n 10 -o split_`
**Explanation:** Splits 2bit format file.