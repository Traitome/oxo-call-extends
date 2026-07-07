---
name: dechat
category: qc
description: Repeat and haplotype aware error correction for nanopore sequencing reads.
tags: [dechat, qc, nanopore, error-correction, long-reads]
author: oxo-call-community
source_url: "https://github.com/LuoGroup2023/DeChat"
---

## Concepts

- **Tool Overview**: dechat (v1.0.1+) is an error correction tool for nanopore sequencing reads that considers repeat regions and haplotype information. It improves base-calling accuracy by leveraging these features.
- **Core Function**: Corrects errors in nanopore sequencing reads by using repeat-aware and haplotype-aware algorithms that better handle complex genomic regions.
- **Input/Output**: Input: Raw nanopore FASTQ reads, reference genome (optional). Output: Error-corrected FASTQ reads, correction statistics.
- **Algorithm**: Uses multiple sequence alignment and consensus calling with special handling for repeat regions and haplotype-specific variants.
- **Key Features**: Repeat region handling, haplotype awareness, supports both reference-guided and de novo correction, improved accuracy in complex regions.
- **Installation**: `conda install -c bioconda dechat`

## Pitfalls

- **Read Quality**: Requires reasonable base quality for effective correction.
- **Repeat Complexity**: Very complex repeats may still pose challenges.
- **Computational Resources**: Large datasets may require significant resources.
- **Haplotype Diversity**: High heterozygosity may affect correction accuracy.
- **Reference Bias**: Reference-guided mode may introduce reference bias.

## Examples

### Correct nanopore reads
**Args:** `dechat -i raw_reads.fastq -o corrected_reads.fastq`
**Explanation:** Perform error correction on nanopore reads.

### Reference-guided correction
**Args:** `dechat -i raw_reads.fastq -r reference.fasta -o corrected_reads.fastq`
**Explanation:** Use reference genome for guided error correction.

### Repeat-aware correction
**Args:** `dechat -i raw_reads.fastq -o corrected_reads.fastq --repeat-aware`
**Explanation:** Enable special handling for repeat regions.