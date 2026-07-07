---
name: geco2
category: formatting
description: Fast DNA sequence compression tool using context-based compression algorithms.
tags: [geco2, dna-compression, bioinformatics, data-compression]
author: oxo-call-community
source_url: "https://github.com/cobilab/geco2"
---

## Concepts
- **DNA Compression**: Specialized compression for DNA sequence data.
- **Context-based Compression**: Uses context models for efficient compression.
- **Fast Compression**: Optimized for high-speed compression and decompression.
- **Reference-free**: Does not require a reference genome for compression.
- **Multiple Formats**: Supports FASTA, FASTQ, and other sequence formats.

## Pitfalls
- **Sequence Type**: Optimized for DNA sequences, not general text.
- **Memory Usage**: Large sequences require significant memory.
- **Compression Ratio**: May not achieve optimal ratio for highly repetitive sequences.
- **Format Support**: Limited to specific sequence formats.
- **Parallel Processing**: May not fully utilize multi-core processors.

## Examples
### Compress FASTA file
**Args:** `geco2 compress -i genome.fasta -o genome.geco2`
**Explanation:** Compresses a FASTA file using Geco2 algorithm.

### Decompress file
**Args:** `geco2 decompress -i genome.geco2 -o genome.fasta`
**Explanation:** Decompresses a Geco2 compressed file.

### Compress with maximum compression
**Args:** `geco2 compress -i genome.fasta -o genome.geco2 -c 9`
**Explanation:** Compresses with maximum compression level (level 9).

### Compress FASTQ file
**Args:** `geco2 compress -i reads.fastq -o reads.geco2 -f fastq`
**Explanation:** Compresses a FASTQ file specifying input format.

### Benchmark compression
**Args:** `geco2 benchmark -i genome.fasta -o benchmark_results.txt`
**Explanation:** Runs benchmark tests on compression performance.