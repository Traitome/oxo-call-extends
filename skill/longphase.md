---
name: longphase
category: variant-calling
description: LongPhase - Ultra-fast co-phasing of SNPs, indels, SVs, and 5mC modifications
tags: [longphase, variant-calling, phasing, haplotypes, epigenomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/twolinin/longphase"
---

## Concepts

- **Haplotype Phasing**: Determining haplotype phase from reads
- **SNP Phasing**: Single-nucleotide polymorphism phasing
- **Indel Phasing**: Insertion and deletion phasing
- **SV Phasing**: Structural variant phasing
- **5mC Modifications**: Detection of DNA methylation
- **Multi-platform**: Support for Nanopore and PacBio platforms

## Pitfalls

- **Read Quality**: Poor quality reads affect phasing
- **Mapping Quality**: Requires accurate read mapping
- **Coverage Depth**: Requires sufficient coverage depth
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **False Phasing**: May produce incorrect haplotype calls

## Examples

### Phase haplotypes
**Args:** `longphase haplotype -r reference.fa -b reads.bam -o phased_output`
**Explanation:** Phases haplotypes from long-read data.

### Detect modifications
**Args:** `longphase haplotype -r reference.fa -b reads.bam -o phased_output -m`
**Explanation:** Detects 5mC modifications.

### Threads
**Args:** `longphase haplotype -r reference.fa -b reads.bam -o phased_output -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `longphase haplotype -r reference.fa -b reads.bam -o phased_output -f vcf`
**Explanation:** Outputs results in VCF format.

### Quality filtering
**Args:** `longphase haplotype -r reference.fa -b reads.bam -o phased_output -q 30`
**Explanation:** Filters by minimum quality score.

### Verbose output
**Args:** `longphase haplotype -r reference.fa -b reads.bam -o phased_output -v`
**Explanation:** Provides detailed output.