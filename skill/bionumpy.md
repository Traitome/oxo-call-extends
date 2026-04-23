---
name: bionumpy
category: utility
description: Library for working with biological sequence data as numpy arrays
tags: [numpy, sequence-data, high-performance, python]
author: oxo-call-community
source_url: "https://github.com/bionumpy/bionumpy"
---

## Concepts
- **Tool Overview**: bionumpy enables working with biological sequence data (FASTQ, FASTA, BED, VCF, BAM) as numpy arrays for high-performance processing.
- **Numpy Integration**: Represents sequences and genomic data as numpy arrays, enabling vectorized operations and efficient computation.
- **Performance**: Achieves C-like performance through numpy vectorization while maintaining Python readability.
- **Applications**: K-mer counting, sequence filtering, format conversion, quality control.

## Pitfalls
- **Memory Usage**: Large datasets loaded as numpy arrays require substantial memory.
- **Data Types**: Sequence data is encoded as integers; be aware of encoding conventions.

## Examples
### Count k-mers
**Args:** `bionumpy count_kmers -i reads.fq -k 31 -o kmer_counts.tsv`
**Explanation:** Counts 31-mers in FASTQ file using numpy-accelerated operations.

### Filter reads by quality
**Args:** `bionumpy filter -i reads.fq --min-quality 20 -o filtered.fq`
**Explanation:** Filters reads by average quality score.
