---
name: meryl
category: expression
description: Multi-threaded, multi-process, out-of-core k-mer counter for large sequencing datasets.
tags: [meryl, k-mer-analysis, bioinformatics]
author: oxo-call-community
source_url: "http://kmer.sourceforge.net/wiki/index.php/Getting_Started_with_Meryl"
---

## Concepts

- **Tool Overview**: Meryl efficiently counts k-mers from sequencing data.
- **Core Function**: High-performance k-mer counting.
- **Multi-threaded**: Uses multiple threads for parallel processing.
- **Out-of-core**: Handles datasets larger than memory.
- **Multiple Processes**: Supports multi-process execution.
- **Installation**: `conda install -c bioconda meryl`

## Pitfalls

- **Memory Requirements**: Still significant memory usage.
- **k-mer Size**: Optimal k depends on data type.
- **Computation Time**: Slow for very large datasets.
- **Output Size**: Large output files possible.
- **Parameter Tuning**: Requires careful configuration.
- **File Format**: Limited input format support.

## Examples

### Count k-mers
**Args:** `meryl count k=21 output kmers.meryl reads.fastq`
**Explanation:** Counts 21-mers from FASTQ file.

### Multiple inputs
**Args:** `meryl count k=31 output kmers.meryl R1.fastq R2.fastq`
**Explanation:** Counts k-mers from multiple files.

### Threaded processing
**Args:** `meryl count k=21 threads=16 output kmers.meryl reads.fastq`
**Explanation:** Uses 16 threads for faster counting.

### Merge k-mer databases
**Args:** `meryl union output merged.meryl db1.meryl db2.meryl`
**Explanation:** Merges multiple k-mer databases.

### Help documentation
**Args:** `meryl --help`
**Explanation:** Displays available options.
