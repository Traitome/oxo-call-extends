---
name: ebfilter
category: qc
description: "EBFilter (Empirical Bayesian Mutation Filtering)"
tags: [ebfilter, qc, variant-filtering, mutation-detection, Bayesian]
author: oxo-call-community
source_url: "https://github.com/Genomon-Project/EBFilter"
---

## Concepts

- **Tool Overview**: EBFilter is an empirical Bayesian mutation filtering tool for detecting somatic mutations from sequencing data.
- **Core Function**: Filters false-positive mutations using empirical Bayesian methods based on sequence context and quality.
- **Input/Output**: Input: VCF files with variant calls. Output: Filtered VCF with high-confidence mutations.
- **Algorithm**: Uses empirical Bayesian approach to calculate posterior probabilities of true mutations.
- **Key Features**: Somatic mutation filtering, strand bias detection, quality-based filtering, context-aware filtering.
- **Installation**: `conda install -c bioconda ebfilter`

## Pitfalls

- **Reference Genome**: Requires matching reference genome for context analysis.
- **Tumor-Normal Pairs**: Designed for tumor-normal paired analysis.
- **Quality Scores**: Depends on accurate base quality scores.
- **Variant Caller Compatibility**: May need adjustment for different variant callers.
- **Memory Usage**: Large VCF files require significant RAM.

## Examples

### Basic mutation filtering
**Args:** `EBFilter -i input.vcf -o filtered.vcf -r ref.fasta`
**Explanation:** Filters mutations using empirical Bayesian approach.

### With tumor-normal pair
**Args:** `EBFilter -i tumor.vcf -n normal.vcf -o filtered.vcf -r ref.fasta`
**Explanation:** Filters somatic mutations using tumor-normal paired data.

### Adjust confidence threshold
**Args:** `EBFilter -i input.vcf -o filtered.vcf -r ref.fasta -c 0.95`
**Explanation:** Sets confidence threshold to 95%.

### Output statistics
**Args:** `EBFilter -i input.vcf -o filtered.vcf -r ref.fasta -s stats.txt`
**Explanation:** Generates filtering statistics.

### Strand bias filtering
**Args:** `EBFilter -i input.vcf -o filtered.vcf -r ref.fasta --strand-bias`
**Explanation:** Enables strand bias filtering.