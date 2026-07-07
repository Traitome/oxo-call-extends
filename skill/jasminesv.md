---
name: jasminesv
category: variant-calling
description: Software for merging structural variants between individuals and samples.
tags: [jasminesv, variant-calling, structural-variants, SV, merging]
author: oxo-call-community
source_url: "https://github.com/mkirsche/Jasmine"
---

## Concepts

- **Tool Overview**: jasminesv (v1.1.5) - A tool for merging and consolidating structural variant calls from multiple individuals.
- **SV Merging**: Merges overlapping or adjacent structural variants across samples.
- **Multi-sample Calling**: Integrates SV calls from multiple individuals into a unified callset.
- **Genotype Merging**: Consolidates genotypes across samples for each variant.
- **Quality Filtering**: Filters variants based on quality scores and support across samples.
- **Standardized Output**: Generates VCF output compatible with downstream analysis tools.

## Pitfalls

- **Variant Resolution**: Different callers may report variants at slightly different positions.
- **False Positives**: Merging can propagate false positives across samples.
- **Complex Rearrangements**: Complex structural variants may be incorrectly merged.
- **Genotype Conflicts**: Inconsistent genotypes across samples require resolution.
- **Memory Usage**: Processing large cohorts requires significant memory.
- **Caller Compatibility**: Different SV callers may produce incompatible formats.

## Examples

### Merge SV calls
**Args:** `Jasmine -i sample1.vcf sample2.vcf sample3.vcf -o merged.vcf`
**Explanation:** Merges SV calls from multiple VCF files.

### Set merging distance
**Args:** `Jasmine -i *.vcf -o merged.vcf -d 500`
**Explanation:** Merges variants within 500 bp of each other.

### Filter by quality
**Args:** `Jasmine -i *.vcf -o merged.vcf -q 30`
**Explanation:** Filters variants with quality score ≥30.

### Keep private variants
**Args:** `Jasmine -i *.vcf -o merged.vcf --keep-private`
**Explanation:** Retains variants present in only one sample.

### Output genotype statistics
**Args:** `Jasmine -i *.vcf -o merged.vcf --stats stats.txt`
**Explanation:** Generates statistics about merged variants and genotypes.

### Use reference genome
**Args:** `Jasmine -i *.vcf -o merged.vcf -r reference.fasta`
**Explanation:** Uses reference genome for variant normalization.