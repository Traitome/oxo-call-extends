---
name: lorma
category: assembly
description: LoRMA - Error correction tool for long sequencing reads
tags: [lorma, assembly, error-correction, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://www.cs.helsinki.fi/u/lmsalmel/LoRMA/"
---

## Concepts

- **Error Correction**: Correcting sequencing errors in long reads
- **Long-read Data**: Handling long-read sequencing data
- **Self-correction**: Self-correction of reads without external data
- **Sequence Alignment**: Alignment-based error correction
- **Quality Improvement**: Improving sequence quality
- **Assembly Preparation**: Preparing reads for assembly

## Pitfalls

- **Read Quality**: Poor quality reads affect correction
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Over-correction**: May over-correct valid variations
- **Read Length**: Very short reads may be filtered out

## Examples

### Error correction
**Args:** `lorma -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects sequencing errors in long reads.

### K-mer size
**Args:** `lorma -i reads.fastq -o corrected.fastq -k 21`
**Explanation:** Uses k-mer size 21 for correction.

### Threads
**Args:** `lorma -i reads.fastq -o corrected.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum coverage
**Args:** `lorma -i reads.fastq -o corrected.fastq -c 5`
**Explanation:** Sets minimum coverage threshold.

### Output format
**Args:** `lorma -i reads.fastq -o corrected.fasta -f fasta`
**Explanation:** Outputs in FASTA format.

### Verbose output
**Args:** `lorma -i reads.fastq -o corrected.fastq -v`
**Explanation:** Provides detailed output.