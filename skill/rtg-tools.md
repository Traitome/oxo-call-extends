---
name: rtg-tools
category: variant_analysis
description: RealTimeGenomics Tools - Utilities for accurate VCF comparison and manipulation.
tags: ["rtg-tools", "vcf", "variant_analysis", "comparison", "RealTimeGenomics"]
author: oxo-call-community
source_url: "https://realtimegenomics.github.io/rtg-tools/index.html"
---

## Concepts

- **Tool Overview**: rtg-tools (v3.13) is a comprehensive toolkit for variant call format (VCF) manipulation, comparison, and validation. It provides specialized utilities for benchmarking variant callers and analyzing VCF files.
- **Core Function**: Performs sophisticated VCF comparisons with configurable sensitivity and specificity metrics. Supports VCF normalization, filtering, and merging operations.
- **Algorithm**: Uses advanced comparison algorithms that account for variant representation differences, supporting both exact matching and fuzzy comparison of variants.
- **Input Format**: VCF/BCF files, optionally compressed with gzip. Supports both single-sample and multi-sample VCFs.
- **Output Format**: Filtered/merged VCF files, comparison reports in HTML/JSON/TSV formats, ROC curves for benchmarking.
- **Use Case**: Benchmarking variant callers, validating variant pipelines, comparing VCF files from different sources, quality control of variant calls.

## Pitfalls

- **Memory intensive**: Large VCF files require significant memory; consider chunked processing.
- **Reference requirements**: Comparison tools require a reference genome for normalization.
- **Format compatibility**: Strict VCF format requirements; malformed VCFs cause errors.
- **Performance impact**: Complex comparisons can be computationally expensive.
- **Filter configuration**: Default filters may not suit all use cases; review and adjust thresholds.
- **Phased data**: Special handling required for phased variants in comparison.

## Examples

### Compare two VCF files
**Args:** `rtg vcfcompare -b truth.vcf -c call.vcf -o comparison`
**Explanation:** `-b` baseline/truth VCF; `-c` call VCF to evaluate; `-o` output directory. Generates detailed comparison report.

### Normalize VCF variants
**Args:** `rtg vcfnormalize -i input.vcf -r reference.fasta -o normalized.vcf`
**Explanation:** Normalizes variant representations (left-aligned, decomposed multi-allelics) for consistent comparison.

### Filter VCF by quality
**Args:** `rtg vcffilter -i input.vcf -o filtered.vcf --min-quality 30`
**Explanation:** Filters variants with quality score below 30.

### Merge multiple VCFs
**Args:** `rtg vcfmerge -o merged.vcf input1.vcf input2.vcf input3.vcf`
**Explanation:** Merges multiple VCF files into a single multi-sample VCF.

### Generate ROC curve
**Args:** `rtg rocplot -i comparison/summary.tsv -o roc.pdf`
**Explanation:** Generates ROC curve visualization from comparison results.

### Validate VCF format
**Args:** `rtg vcfvalidate -i input.vcf`
**Explanation:** Validates VCF file format and reports any errors or warnings.

### Subset VCF by region
**Args:** `rtg vcfslicer -i input.vcf -o subset.vcf --region chr1:100000-200000`
**Explanation:** Extracts variants from a specific genomic region.
