---
name: fings
category: qc
description: "FiNGS (Filters for Next Generation Sequencing) is a tool for filtering somatic variants in cancer genomics, using tumor-normal BAM pairs to identify and remove false positive variant calls."
tags: [fings, qc, ngs, filtering, somatic-variants, cancer, genomics, vcf, bam, variant-filtering]
author: oxo-call-community
source_url: "https://github.com/cpwardell/FiNGS"
---

## Concepts
- **Tool Overview**: FiNGS (Filters for Next Generation Sequencing) is a specialized tool for filtering somatic variant calls in cancer genomics. It applies multiple filters to improve precision of somatic mutation detection by removing false positives from tumor-normal sequencing comparisons.
- **Core Function**: Filters somatic variant calls by evaluating evidence from aligned reads in tumor and normal BAM files. Uses criteria such as variant allele frequency, read depth, mapping quality, and strand bias to distinguish true somatic mutations from sequencing artifacts.
- **Input/Output**: Input: VCF file with variant calls and matched tumor/normal BAM files. Output: Filtered VCF file with additional FILTER field annotations indicating which filters each variant passed or failed.
- **Filtering Strategy**: User-configurable filter parameters via tab-delimited configuration file. Includes default filters optimized for ICGC standards. Each filter evaluates specific quality criteria and contributes to overall variant classification.
- **Filter Categories**: Filters include position-based filters (intronic, exonic, splice site), sequencing artifact filters (strand bias, mapping quality), population frequency filters (dbSNP, ExAC, 1000 Genomes), and custom user-defined thresholds.
- **Somatic Confidence**: Assigns confidence scores to variants based on filter pass/fail patterns. High-confidence somatic variants pass all stringent filters while low-confidence variants may represent subclonal events or borderline cases.
- **Installation**: `conda install -c bioconda fings` or `pip install fings`. Requires Python 2.7+ or 3.x, PyVCF, and samtools. Docker image also available.

## Pitfalls
- **Matched Normal Requirement**: FiNGS requires matched tumor-normal pairs from the same individual. Using unrelated normal samples will produce incorrect results as germline variants will be misclassified as somatic.
- **BAM Synchronization**: Tumor and normal BAM files must be properly coordinate-sorted and indexed. Misaligned or unsynchronized files lead to incorrect allele frequency calculations and filtering decisions.
- **VCF Compatibility**: Only supports VCF v4.0+. Older VCF formats may parse incorrectly or cause errors. Convert older files using bcftools before processing.
- **Filter Parameter Tuning**: Default filter thresholds may be too stringent or lenient for specific sequencing platforms. Optimize parameters based on sequencing depth and platform characteristics.
- **Paired-End Strand Bias**: Some true variants may be filtered due to strand bias in paired-end sequencing. Review strand-biased variants manually before final exclusion.
- **Parallelization Limits**: Memory usage scales with variant count. Very large VCF files (millions of variants) may require chunked processing to avoid memory exhaustion.

## Examples
### Run with default filters
**Args:** `fings -v variants.vcf -t tumor.bam -n normal.bam -o filtered.vcf`
**Explanation:** Applies default FiNGS filters to somatic variant calls. Uses built-in default threshold values for all filter categories.

### Run with custom filter parameters
**Args:** `fings -v variants.vcf -t tumor.bam -n normal.bam -c my_filters.txt -o filtered.vcf`
**Explanation:** Uses user-defined filter configuration file instead of defaults. Filter parameters file is tab-delimited specifying filter names and threshold values.

### Apply ICGC standard filters
**Args:** `fings -v variants.vcf -t tumor.bam -n normal.bam --ICGC -o filtered.vcf`
**Explanation:** Applies filter thresholds conforming to ICGC (International Cancer Genome Consortium) standards. Recommended for international collaborative projects requiring standardized filtering.

### Chunked processing for large files
**Args:** `fings -v variants.vcf -t tumor.bam -n normal.bam -c 1000 -o filtered.vcf`
**Explanation:** Processes variants in chunks of 1000 to manage memory usage for large VCF files. Essential for whole-genome scale variant calling outputs.

### Generate filtering report
**Args:** `fings -v variants.vcf -t tumor.bam -n normal.bam -o filtered.vcf -r report.txt`
**Explanation:** Creates detailed filtering report showing which filters each variant passed/failed. Report includes summary statistics and per-variant filter annotations.

### Filter with minimum depth requirements
**Args:** `fings -v variants.vcf -t tumor.bam -n normal.bam -d 20 -o filtered.vcf`
**Explanation:** Requires minimum 20x read depth in both tumor and normal samples for a variant to pass. Variants below this threshold are marked as low-depth artifacts.

### Review specific filter failures
**Args:** `fings -v variants.vcf -t tumor.bam -n normal.bam --show-failed SB,QD -o filtered.vcf`
**Explanation:** Shows detailed information about variants failing strand bias (SB) and quality by depth (QD) filters. Useful for troubleshooting sequencing artifacts.
