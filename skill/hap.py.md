---
name: hap.py
category: bioinformatics
description: hap.py is a tool for haplotype-aware VCF comparison and benchmarking of variant callers.
tags: [hap.py, VCF-comparison, variant-calling, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Illumina/hap.py"
---

## Concepts

- **VCF Comparison**: hap.py compares VCF files at haplotype level.

- **Variant Benchmarking**: Benchmarks variant callers performance.

- **Haplotype-Aware**: Considers haplotype phase in comparison.

- **Truth Sets**: Works with reference truth sets.

- **Performance Metrics**: Generates comprehensive performance metrics.

- **Variant Evaluation**: Evaluates variant calling accuracy.

## Pitfalls

- **Phasing Quality**: Results depend on phasing quality.

- **Reference Genome**: Ensure using correct reference genome.

- **VCF Format**: Ensure correct VCF format.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Compare VCF files
**Args:** `hap.py -r reference.fasta -f regions.bed -b truth.vcf -c call.vcf -o comparison`
**Explanation:** Compares called variants against truth set.

### Haplotype-aware comparison
**Args:** `hap.py -r reference.fasta -b truth.vcf -c call.vcf -o comparison --haploid`
**Explanation:** Performs haplotype-aware comparison.

### Generate report
**Args:** `hap.py -r reference.fasta -b truth.vcf -c call.vcf -o comparison --roc`
**Explanation:** Generates ROC curve and performance report.

### Batch processing
**Args:** `for chr in {1..22}; do hap.py -r reference.fasta -b chr${chr}_truth.vcf -c chr${chr}_call.vcf -o chr${chr}_comp; done`
**Explanation:** Processes multiple chromosome files.

### Quality filtering
**Args:** `hap.py -r reference.fasta -b truth.vcf -c call.vcf -o comparison -Q 30`
**Explanation:** Filters variants by quality score.

### Summary statistics
**Args:** `hap.py -r reference.fasta -b truth.vcf -c call.vcf -o comparison --summary`
**Explanation:** Generates summary statistics.

### Help command
**Args:** `hap.py --help`
**Explanation:** Shows available options and usage information.