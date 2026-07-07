---
name: msoma
category: variant-calling
description: Somatic mutation detection using beta-binomial null model for NGS data.
tags: [msoma, variant-calling, oncology]
author: oxo-call-community
source_url: "https://github.com/AkeyLab/mSOMA"
---

## Concepts

- **Tool Overview**: mSOMA v0.1.2 detects somatic mutations using beta-binomial models.
- **Core Function**: Identifies somatic variants from paired tumor-normal sequencing data.
- **Beta-Binomial Model**: Uses statistical model for variant detection.
- **NGS Analysis**: Works with next-generation sequencing data.
- **Somatic Variant Calling**: Distinguishes somatic from germline variants.
- **Input/Output**: Accepts BAM files; outputs variant calls.

## Pitfalls

- **Paired Samples**: Requires tumor-normal sample pairs.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for detection.
- **Data Quality**: Results depend on sequencing quality.
- **Computational Resources**: Large datasets may require significant resources.
- **FDR Control**: Requires appropriate false discovery rate control.

## Examples

### Detect somatic mutations
**Args:** `msoma -t tumor.bam -n normal.bam -r reference.fa -o variants.vcf`
**Explanation:** Identifies somatic variants from paired samples.

### With quality filtering
**Args:** `msoma -t tumor.bam -n normal.bam -r reference.fa -q 20 -o variants.vcf`
**Explanation:** Applies quality threshold of 20.

### Generate report
**Args:** `msoma -t tumor.bam -n normal.bam -r reference.fa -rpt report.txt -o variants.vcf`
**Explanation:** Generates detailed detection report.

### Batch processing
**Args:** `msoma -i samples.txt -r reference.fa -o results/`
**Explanation:** Processes multiple sample pairs.

### Specify regions
**Args:** `msoma -t tumor.bam -n normal.bam -r reference.fa -b regions.bed -o variants.vcf`
**Explanation:** Restricts analysis to specific genomic regions.