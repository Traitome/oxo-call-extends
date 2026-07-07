---
name: lorikeet-genome
category: variant-calling
description: Lorikeet - Metagenomic variant calling and diversity analysis
tags: [lorikeet-genome, variant-calling, metagenomics, diversity, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rhysnewell/Lorikeet"
---

## Concepts

- **Metagenomics**: Analysis of microbial community data
- **Variant Calling**: Detection of genetic variants in metagenomes
- **Diversity Analysis**: Analysis of microbial diversity
- **Local Reassembly**: Local reassembly of haplotypes
- **Haplotype Analysis**: Analysis of microbial haplotypes
- **Population Genetics**: Population genetic analysis

## Pitfalls

- **Read Quality**: Poor quality reads affect variant calling
- **Community Complexity**: Complex communities may affect accuracy
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive calls

## Examples

### Call variants
**Args:** `lorikeet call --bam input.bam --ref reference.fasta --output variants.vcf`
**Explanation:** Calls variants in metagenomic data.

### Diversity analysis
**Args:** `lorikeet diversity --bam input.bam --ref reference.fasta --output diversity.txt`
**Explanation:** Performs diversity analysis.

### Local reassembly
**Args:** `lorikeet reassemble --bam input.bam --ref reference.fasta --output reassembled.fasta`
**Explanation:** Performs local reassembly.

### Threads
**Args:** `lorikeet call --bam input.bam --ref reference.fasta --output variants.vcf --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Quality filtering
**Args:** `lorikeet call --bam input.bam --ref reference.fasta --output variants.vcf --min-qual 30`
**Explanation:** Filters by minimum quality score.

### Verbose output
**Args:** `lorikeet call --bam input.bam --ref reference.fasta --output variants.vcf --verbose`
**Explanation:** Provides detailed output.