---
name: agg
category: formatting
description: gVCF aggregation tool for combining single-sample gVCFs into multi-sample VCFs
tags: [agg, gvcf, aggregation, vcf, population-genomics, joint-calling]
author: oxo-call-community
source_url: "https://github.com/Illumina/agg"
---

## Concepts

- **Tool Overview**: agg is Illumina's gVCF aggregation tool that combines multiple single-sample gVCF files into multi-sample VCFs for population-scale genomic analysis.
- **Core Function**: Performs joint genotyping and aggregation of gVCF files, handling multiallelic variants, normalization, and cohort-level quality metrics.
- **Input/Output**: Input: Single-sample gVCF files. Output: Multi-sample VCF with cohort-wide variant statistics and quality metrics.
- **Variant Processing**: Decomposes MNPs (multiallelic nucleotide polymorphisms), performs left-shifting/trimming of indels, and handles complex substitutions.
- **Quality Metrics**: Calculates per-variant metrics including missingness, mean depth, mean GQ, allelic imbalance, inbreeding coefficient, and Mendelian error ratios.
- **Installation**: Install via bioconda: `conda install -c bioconda agg`
- **Use Cases**: Large-scale population studies, biobanks, cohort-level variant analysis, joint genotyping pipelines.

## Pitfalls

- **Batch Size**: Large cohorts should be processed in batches (e.g., 1000 samples per batch) to manage memory and computational resources.
- **Genome Chunks**: For very large datasets, split genome into chunks/regions to avoid unworkably large output files.
- **MNP Decomposition**: Multiallelic variants are written as one allele per line - ensure downstream tools can handle this format.
- **Filtering**: No variant QC filters are applied by default - use FILTER=PASS variants for analysis.
- **Reference**: Ensure all input gVCFs use the same reference genome build.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available command-line options and parameters.

### Aggregate multiple gVCFs
**Args:** `agg -i sample1.gvcf.gz -i sample2.gvcf.gz -i sample3.gvcf.gz -o cohort.vcf.gz`
**Explanation:** Combines three single-sample gVCFs into a multi-sample VCF.

### Use file list for many samples
**Args:** `agg --variant-list gvcf_list.txt -o cohort.vcf.gz`
**Explanation:** Aggregates gVCFs listed in a text file (one path per line) for large cohorts.

### Specify output directory
**Args:** `agg -i *.gvcf.gz -o cohort.vcf.gz --output-dir /path/to/output/`
**Explanation:** Sets custom output directory for aggregated VCF and intermediate files.

### Enable verbose logging
**Args:** `agg -i sample1.gvcf.gz -i sample2.gvcf.gz -o cohort.vcf.gz -v`
**Explanation:** Enables verbose mode for detailed progress information.

### Process specific genomic region
**Args:** `agg -i sample1.gvcf.gz -i sample2.gvcf.gz -o chr1_region.vcf.gz --region chr1:1000000-2000000`
**Explanation:** Aggregates only variants within specified genomic region.

### Set intermediate results directory
**Args:** `agg -i *.gvcf.gz -o cohort.vcf.gz --intermediate-results-dir /tmp/agg_temp/`
**Explanation:** Specifies separate directory for intermediate files to manage disk space.

### Process with custom reference
**Args:** `agg -i sample1.gvcf.gz -i sample2.gvcf.gz -o cohort.vcf.gz --reference GRCh38.fa`
**Explanation:** Specifies reference genome for validation and normalization.

### Batch processing for large cohort
**Args:** `agg --variant-list batch1.txt -o batch1.vcf.gz && agg --variant-list batch2.txt -o batch2.vcf.gz`
**Explanation:** Processes large cohort in batches to manage computational resources.