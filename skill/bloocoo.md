---
name: bloocoo
category: qc
description: K-mer spectrum-based read error corrector for large datasets with low memory footprint
tags: [bloocoo, error-correction, qc, kmer, reads]
author: oxo-call-community
source_url: "https://github.com/GATB/bloocoo"
---

## Concepts

- **Tool Overview**: Bloocoo is a k-mer spectrum-based read error correction tool with low memory usage.
- **Core Function**: Corrects sequencing errors using k-mer frequency analysis.
- **Memory Efficiency**: Can correct human genome resequencing at 70x coverage with <4GB memory.
- **Input**: FASTQ files with raw sequencing reads.
- **Output**: Corrected FASTQ files with reduced error rates.
- **Installation**: Install via bioconda: `conda install -c bioconda bloocoo`

## Pitfalls

- **K-mer Size**: Choose appropriate k-mer size based on read length and coverage.
- **Coverage**: Very low coverage may reduce correction effectiveness.
- **Heterozygosity**: May incorrectly correct true variants at low frequency.
- **Output Quality**: Check quality metrics after correction.

## Examples

### Correct read errors
**Args:** `bloocoo -i reads.fq -o corrected.fq`
**Explanation:** Corrects sequencing errors using default k-mer spectrum parameters.

### Set k-mer size
**Args:** `bloocoo -i reads.fq -k 31 -o corrected.fq`
**Explanation:** Uses 31-mer size for error correction.

### Multi-threaded correction
**Args:** `bloocoo -i reads.fq -t 8 -o corrected.fq`
**Explanation:** Uses 8 threads for faster error correction.

### Set coverage threshold
**Args:** `bloocoo -i reads.fq -c 3 -o corrected.fq`
**Explanation:** Uses minimum k-mer coverage of 3 for solid k-mers.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
