---
name: snpgenie
category: variant-analysis
description: SNPGenie - Estimate πN/πS, dN/dS and diversity measures from NGS data
tags: [snpgenie, variant-analysis, diversity, dnds, selection]
author: oxo-call-community
source_url: "https://github.com/chasewnelson/SNPGenie"
---

## Concepts

- **Tool Overview**: snpgenie (v1.0) - A tool for estimating selection and diversity measures
- **Core Function**: Calculates πN/πS, dN/dS and other diversity metrics from NGS data
- **Input/Output**: Accepts VCF/BAM files; outputs diversity statistics
- **Algorithm**: Estimates nucleotide diversity and selection coefficients
- **Installation**: `conda install -c bioconda snpgenie`
- **Key Features**: Diversity estimation, selection analysis, NGS support

## Pitfalls

- **Input Requirements**: Requires properly formatted VCF/BAM files
- **Annotation Files**: Requires gene annotation files for analysis
- **Reference Genome**: Must use compatible reference genome
- **Coverage Requirements**: Requires sufficient read coverage
- **Interpretation**: Results require biological interpretation
- **Multiple Testing**: Requires proper statistical correction

## Examples

### Display help
**Args:** `snpgenie --help`
**Explanation:** Shows available options and usage information.

### Basic diversity analysis
**Args:** `snpgenie -i variants.vcf -g genes.gff -o diversity_results.txt`
**Explanation:** Calculate diversity measures from VCF.

### With BAM input
**Args:** `snpgenie -i aligned.bam -r reference.fasta -g genes.gff -o results.txt`
**Explanation:** Calculate diversity from BAM alignment.

### πN/πS analysis
**Args:** `snpgenie -i variants.vcf -g genes.gff -o results.txt --pi`
**Explanation:** Calculate πN/πS ratios.

### dN/dS analysis
**Args:** `snpgenie -i variants.vcf -g genes.gff -o results.txt --dnds`
**Explanation:** Calculate dN/dS ratios.

### With sliding window
**Args:** `snpgenie -i variants.vcf -g genes.gff -o results.txt --window 1000`
**Explanation:** Use sliding window analysis.

### Generate report
**Args:** `snpgenie -i variants.vcf -g genes.gff -o results.txt --report`
**Explanation:** Generate comprehensive report.

### Export statistics
**Args:** `snpgenie -i variants.vcf -g genes.gff -o results.txt --export stats.csv`
**Explanation:** Export statistics to CSV.