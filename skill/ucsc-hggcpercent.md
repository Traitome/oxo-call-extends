---
name: ucsc-hggcpercent
category: utility
description: UCSC hgGcPercent - Tool for calculating GC percentage.
tags: [ucsc-hggcpercent, ucsc, sequence-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgGcPercent - A tool for calculating GC percentage in sequences.
- **Core Function**: Computes GC content across sequences.
- **Input**: FASTA file or genome database.
- **Output**: GC percentage statistics.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence analysis, genome characterization, quality control.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **Window Size**: Requires appropriate window size.

## Examples

### Calculate GC percentage
**Args:** `hgGcPercent genome.fa > gc_stats.txt`
**Explanation:** Calculate GC content.

### With window
**Args:** `hgGcPercent -window=1000 genome.fa > gc_stats.txt`
**Explanation:** Window size for calculation.
