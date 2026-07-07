---
name: smashbenchmarking
category: variant-analysis
description: Tool for checking the accuracy of one VCF callset against another for benchmarking purposes
tags: [smashbenchmarking, variant-analysis, vcf, benchmarking, validation]
author: oxo-call-community
source_url: "http://github.com/amplab/smash/"
---

## Concepts

- **Tool Overview**: smashbenchmarking (v1.0.1) - A variant callset comparison tool for benchmarking
- **Core Function**: Compares VCF files to assess variant calling accuracy
- **Input/Output**: Accepts VCF files; outputs comparison statistics and metrics
- **Algorithm**: Uses precision-recall analysis to evaluate variant calls
- **Installation**: `conda install -c bioconda smashbenchmarking`
- **Key Features**: Comprehensive benchmarking metrics, supports large VCF files

## Pitfalls

- **VCF Format**: VCF files must be properly formatted and sorted
- **Reference Genome**: Both VCFs must use the same reference genome
- **Variant Types**: Handles SNVs and indels; structural variants may require special handling
- **Performance**: Large VCF files can be slow to process
- **Memory Usage**: May require significant memory for large datasets
- **Output Interpretation**: Requires understanding of benchmarking metrics

## Examples

### Display help
**Args:** `smashbenchmarking --help`
**Explanation:** Shows available options and usage information.

### Basic comparison
**Args:** `smashbenchmarking -i query.vcf -t truth.vcf -o results.txt`
**Explanation:** Compare query VCF against truth VCF.

### With bed regions
**Args:** `smashbenchmarking -i query.vcf -t truth.vcf -b regions.bed -o results.txt`
**Explanation:** Restrict comparison to specific genomic regions.

### Generate detailed report
**Args:** `smashbenchmarking -i query.vcf -t truth.vcf -o results.txt -d`
**Explanation:** Generate detailed comparison report.

### Filter by quality
**Args:** `smashbenchmarking -i query.vcf -t truth.vcf -o results.txt -q 30`
**Explanation:** Filter variants by quality >= 30.

### Output VCF with annotations
**Args:** `smashbenchmarking -i query.vcf -t truth.vcf -o annotated.vcf -a`
**Explanation:** Output annotated VCF with comparison results.

### Calculate precision-recall
**Args:** `smashbenchmarking -i query.vcf -t truth.vcf -o pr_curve.txt -p`
**Explanation:** Generate precision-recall curve data.

### Batch comparison
**Args:** `smashbenchmarking -b vcf_list.txt -t truth.vcf -o results_dir/`
**Explanation:** Compare multiple query VCFs against truth set.