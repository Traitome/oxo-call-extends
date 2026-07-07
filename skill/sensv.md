---
name: sensv
category: variant-analysis
description: sensv - Structural variation detection from NGS data
tags: ["sensv", "variant-analysis", "structural-variation", "NGS"]
author: oxo-call-community
source_url: "https://github.com/HKU-BAL/SENSV"
---

## Concepts

- **Tool Overview**: sensv (v1.0.4) detects structural variations from NGS data.
- **Core Function**: Identifies structural variants (SVs) from sequencing reads.
- **Algorithm**: Uses split-read and read-pair approaches for SV detection.
- **Input/Output**: Accepts BAM files and produces SV calls in VCF format.
- **Structural Variation**: Focuses on detecting deletions, duplications, inversions, and translocations.
- **Applications**: Genomics, variant analysis, and disease research.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **False Positives**: May produce false positive calls.
- **Reference Genome**: Requires proper reference genome setup.

## Examples

### Detect SVs
**Args:** `sensv -i reads.bam -r reference.fasta -o svs.vcf`
**Explanation:** `-i` input BAM; `-r` reference genome; `-o` output VCF.

### With breakpoints
**Args:** `sensv -i reads.bam -r reference.fasta -b -o svs.vcf`
**Explanation:** `-b` outputs breakpoint information.

### Verbose logging
**Args:** `sensv -i reads.bam -r reference.fasta -v -o svs.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `sensv -i reads.bam -r reference.fasta -t 8 -o svs.vcf`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `sensv --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sensv --version`
**Explanation:** Shows current version.

### Filter SVs
**Args:** `sensv filter -i svs.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters SVs by quality score.