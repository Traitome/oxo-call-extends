---
name: lighter
category: qc
description: Lighter - K-mer based error correction for whole genome sequencing data
tags: [lighter, qc, error-correction, k-mer, sequencing, genome]
author: oxo-call-community
source_url: "https://github.com/mourisl/Lighter"
---

## Concepts

- **K-mer Error Correction**: K-mer based error correction method
- **Whole Genome Sequencing**: Optimized for WGS data
- **Error Detection**: Detects sequencing errors using k-mer frequencies
- **Quality Improvement**: Improves read quality before assembly
- **Parallel Processing**: Supports parallel error correction
- **Memory Efficiency**: Memory-efficient algorithm design

## Pitfalls

- **K-mer Size**: K-mer size selection is critical
- **Coverage Depth**: Requires sufficient coverage depth
- **Memory Usage**: May require significant memory for large genomes
- **Parameter Tuning**: Requires careful parameter optimization
- **Complex Genomes**: Complex genomes may have more false positives
- **Time Consumption**: Error correction may take significant time

## Examples

### Correct reads
**Args:** `lighter -r reads.fastq -o corrected.fastq -k 23`
**Explanation:** Corrects sequencing errors using k-mer size 23.

### Paired-end correction
**Args:** `lighter -1 reads_1.fastq -2 reads_2.fastq -o corrected/`
**Explanation:** Corrects paired-end reads.

### Coverage threshold
**Args:** `lighter -r reads.fastq -o corrected.fastq -c 30`
**Explanation:** Sets minimum coverage threshold to 30.

### Threads
**Args:** `lighter -r reads.fastq -o corrected.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Memory limit
**Args:** `lighter -r reads.fastq -o corrected.fastq -m 32G`
**Explanation:** Limits memory usage to 32GB.

### Error rate
**Args:** `lighter -r reads.fastq -o corrected.fastq -e 0.01`
**Explanation:** Sets expected error rate to 1%.