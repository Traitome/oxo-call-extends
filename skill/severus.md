---
name: severus
category: variant-calling
description: severus - Somatic structural variant calling using long reads
tags: ["severus", "variant-calling", "structural-variants", "long-reads"]
author: oxo-call-community
source_url: "https://github.com/KolmogorovLab/Severus"
---

## Concepts

- **Tool Overview**: severus (v1.7) detects somatic structural variants using long-read sequencing data.
- **Core Function**: Identifies structural variants from long-read alignments.
- **Algorithm**: Uses signal processing and alignment analysis for variant detection.
- **Input/Output**: Accepts BAM files and produces VCF output.
- **Long-Read Analysis**: Focuses on structural variant detection from long reads.
- **Applications**: Cancer genomics, structural variant analysis, and long-read sequencing.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Call variants
**Args:** `severus -i tumor.bam -n normal.bam -r reference.fasta -o output.vcf`
**Explanation:** `-i` tumor BAM; `-n` normal BAM; `-r` reference.

### From single sample
**Args:** `severus -i sample.bam -r reference.fasta -o output.vcf`
**Explanation:** Single sample mode.

### Verbose logging
**Args:** `severus -v -i tumor.bam -n normal.bam -r reference.fasta -o output.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `severus --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `severus --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `severus -t 8 -i tumor.bam -n normal.bam -r reference.fasta -o output.vcf`
**Explanation:** `-t 8` uses 8 threads.