---
name: smaca
category: population-genomics
description: smaca is a Python tool to detect putative SMA carriers and estimate the absolute SMN1 copy-number in a population
tags: [smaca, population-genomics, smn1, carrier-detection, copy-number]
author: oxo-call-community
source_url: "https://github.com/babelomics/SMAca"
---

## Concepts

- **Tool Overview**: smaca (v1.2.4rc11) - A Python tool for SMA carrier detection and SMN1 copy-number estimation
- **Core Function**: Detects SMA carriers by analyzing SMN1 gene copy-number variation
- **Input/Output**: Accepts VCF files; outputs carrier status and copy-number estimates
- **Algorithm**: Uses statistical methods to estimate SMN1 copy-number from sequencing data
- **Installation**: `conda install -c bioconda smaca`
- **Key Features**: Population-scale analysis, supports multiple sequencing platforms

## Pitfalls

- **VCF Quality**: Requires high-quality VCF with accurate genotype calls
- **Reference Genome**: Must use compatible reference genome (GRCh37/GRCh38)
- **Copy-Number Limits**: May not accurately detect extreme copy-number states
- **Sample Quality**: Low coverage samples may produce unreliable results
- **Platform Specificity**: Performance varies across sequencing platforms
- **Population Differences**: Reference panel should match target population

## Examples

### Display help
**Args:** `smaca --help`
**Explanation:** Shows available options and usage information.

### Basic carrier detection
**Args:** `smaca -i input.vcf -o output_dir/`
**Explanation:** Detect SMA carriers from VCF file.

### With custom reference panel
**Args:** `smaca -i input.vcf -r reference_panel.txt -o output_dir/`
**Explanation:** Use custom reference panel for copy-number estimation.

### Batch processing
**Args:** `smaca -b vcf_list.txt -o output_dir/`
**Explanation:** Process multiple VCF files in batch.

### Generate report
**Args:** `smaca -i input.vcf -o output_dir/ --report`
**Explanation:** Generate comprehensive analysis report.

### Set confidence threshold
**Args:** `smaca -i input.vcf -o output_dir/ -c 0.95`
**Explanation:** Set confidence threshold for carrier calling.

### Extract SMN1 regions
**Args:** `smaca extract -i input.vcf -o smn1_regions.vcf`
**Explanation:** Extract only SMN1-related variants from VCF.