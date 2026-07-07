---
name: domino
category: variant-calling
description: DOMINO - Variant calling with low false positive rates using AMI algorithm.
tags: [domino, variant-calling, AMI-algorithm, false-discovery, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Shamir-Lab/DOMINO"
---

## Concepts

- **Tool Overview**: DOMINO is a variant calling tool using the AMI (Approximate Median Interval) algorithm.
- **Core Function**: Calls variants with high accuracy and low false positive rates.
- **Input/Output**: Input: BAM alignment files, reference genome. Output: VCF with variant calls.
- **Algorithm**: Uses Approximate Median Interval method for robust variant detection.
- **Key Features**: Low false discovery rate, robust to sequencing errors, batch processing, parallel execution.
- **Installation**: `conda install -c bioconda domino`

## Pitfalls

- **Input Requirements**: Requires sorted and indexed BAM files; unsorted BAMs will fail.
- **Reference Genome**: BAM and reference must be from the same genome build.
- **Alignment Quality**: Poor quality alignments affect variant calling accuracy.
- **Memory Usage**: Processing large BAM files requires significant RAM.
- **Computation Time**: Comprehensive variant calling can be time-consuming.
- **Output Size**: VCF files can be large; consider compression options.

## Examples

### Call variants
**Args:** `domino --bam sample.bam --fasta ref.fa --output variants.vcf`
**Explanation:** Calls variants from aligned sequencing data.

### Multiple samples
**Args:** `domino --bam sample1.bam sample2.bam --fasta ref.fa --output variants.vcf`
**Explanation:** Calls variants from multiple BAM files simultaneously.

### With quality filtering
**Args:** `domino --bam sample.bam --fasta ref.fa --output variants.vcf --min-quality 20`
**Explanation:** Filters variants by minimum quality score.

### Parallel processing
**Args:** `domino --bam sample.bam --fasta ref.fa --output variants.vcf --threads 8`
**Explanation:** Uses 8 threads for faster variant calling.

### Output confidence scores
**Args:** `domino --bam sample.bam --fasta ref.fa --output variants.vcf --confidence`
**Explanation:** Includes confidence scores for each variant call.

### Targeted sequencing
**Args:** `domino --bam sample.bam --fasta ref.fa --output variants.vcf --targets regions.bed`
**Explanation:** Only calls variants in specified genomic regions.