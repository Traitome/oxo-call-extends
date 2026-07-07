---
name: biopet-vcfstats
category: variant-calling
description: Generate statistics and metrics from VCF files
tags: [vcf, statistics, variant-calling, quality-control]
author: oxo-call-community
source_url: "https://github.com/biopet/vcfstats"
---

## Concepts

- **Tool Overview**: VcfStats generates comprehensive statistics from VCF files including general variant stats, genotype stats, sample comparisons, and annotation statistics.
- **Statistical Categories**: General stats (variant counts, types), genotype stats (homozygous/heterozygous ratios), sample comparisons (concordance), and annotation-based stats.
- **Output Formats**: JSON and text output for easy integration with downstream analysis.
- **Applications**: Variant calling quality assessment, sample comparison, batch processing statistics.

## Pitfalls

- **Annotation Requirements**: Some statistics require VCF annotation fields to be present.
- **Large Files**: Processing large VCF files can be memory-intensive.

## Examples

### Generate VCF statistics
**Args:** `java -jar VcfStats.jar -i variants.vcf -o stats.json`
**Explanation:** Generates comprehensive statistics from VCF file.

### Disable specific stats
**Args:** `java -jar VcfStats.jar -i variants.vcf -o stats.json --no-genotype-stats`
**Explanation:** Generates stats excluding genotype statistics.

### Compare samples
**Args:** `java -jar VcfStats.jar -i variants.vcf -o stats.json --sample-compare`
**Explanation:** Generates sample comparison statistics including concordance rates.