---
name: biopet-vcffilter
category: qc
description: Filter VCF files based on various quality metrics and criteria
tags: [vcf, filtering, variant-calling, quality-control]
author: oxo-call-community
source_url: "https://github.com/biopet/vcffilter"
---

## Concepts

- **Tool Overview**: VcfFilter filters VCF files based on quality metrics including depth, quality scores, genotype quality, and other variant attributes.
- **Filtering Criteria**: Supports filtering by total depth (DP), sample depth (AD), quality score (QUAL), genotype quality (GQ), and reference/alternate allele counts.
- **Sample-level Filtering**: Can filter based on individual sample genotypes and quality metrics.
- **Flexible Configuration**: Supports multiple filtering criteria combined with AND/OR logic.
- **Applications**: Variant quality filtering, hard filtering, quality control.

## Pitfalls

- **Filter String Syntax**: Requires proper syntax for filter expressions.
- **Missing Fields**: Some fields may not be present in all VCF files.

## Examples

### Filter by depth
**Args:** `java -jar VcfFilter.jar -i variants.vcf -o filtered.vcf -f "DP>10"`
**Explanation:** Filters variants with total depth greater than 10.

### Filter by quality and depth
**Args:** `java -jar VcfFilter.jar -i variants.vcf -o filtered.vcf -f "QUAL>30 && DP>20"`
**Explanation:** Filters variants with QUAL > 30 AND DP > 20.

### Remove reference calls
**Args:** `java -jar VcfFilter.jar -i variants.vcf -o filtered.vcf --remove-reference`
**Explanation:** Removes variants that are reference calls across all samples.