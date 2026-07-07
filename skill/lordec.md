---
name: lordec
category: assembly
description: LoRDEC - Hybrid error correction for long PacBio reads
tags: [lordec, assembly, error-correction, PacBio, bioinformatics]
author: oxo-call-community
source_url: "http://www.atgc-montpellier.fr/lordec/"
---

## Concepts

- **Error Correction**: Correcting sequencing errors in reads
- **Hybrid Correction**: Combining short and long reads
- **PacBio Reads**: Analysis of PacBio sequencing data
- **Long-read Data**: Handling long-read sequencing data
- **Sequence Correction**: Improving sequence accuracy
- **Assembly Preparation**: Preparing reads for assembly

## Pitfalls

- **Read Quality**: Poor quality reads affect correction
- **Short Read Requirement**: Requires short read data for hybrid correction
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Over-correction**: May over-correct valid variations

## Examples

### Error correction
**Args:** `lordec-correct -i long_reads.fastq -s short_reads.fastq -o corrected.fastq`
**Explanation:** Corrects long reads using short reads.

### K-mer size
**Args:** `lordec-correct -i long_reads.fastq -s short_reads.fastq -o corrected.fastq -k 21`
**Explanation:** Uses k-mer size 21 for correction.

### Threads
**Args:** `lordec-correct -i long_reads.fastq -s short_reads.fastq -o corrected.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Error rate
**Args:** `lordec-correct -i long_reads.fastq -s short_reads.fastq -o corrected.fastq -e 0.15`
**Explanation:** Sets expected error rate to 15%.

### Output format
**Args:** `lordec-correct -i long_reads.fastq -s short_reads.fastq -o corrected.fasta -f fasta`
**Explanation:** Outputs in FASTA format.

### Verbose output
**Args:** `lordec-correct -i long_reads.fastq -s short_reads.fastq -o corrected.fastq -v`
**Explanation:** Provides detailed output.