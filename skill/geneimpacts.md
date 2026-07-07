---
name: geneimpacts
category: variant-annotation
description: GeneImpacts - Prioritizes effects of variant annotations from VEP, SnpEff, and other variant callers.
tags: [geneimpacts, variant-annotation, vep, snpeff, variant-prioritization]
author: oxo-call-community
source_url: "https://github.com/brentp/geneimpacts"
---

## Concepts
- **Variant Prioritization**: Prioritizes variants by their functional impact.
- **Annotation Parsing**: Parses annotations from VEP and SnpEff.
- **Impact Classification**: Classifies variants by predicted impact.
- **Effect Ranking**: Ranks variants by severity.
- **Filtering**: Filters variants based on impact criteria.

## Pitfalls
- **Annotation Quality**: Depends on high-quality variant annotations.
- **Tool Compatibility**: Requires specific annotation formats.
- **Threshold Selection**: Impact thresholds require careful selection.
- **False Positives**: May incorrectly classify variant impacts.
- **Interpretation**: Impact predictions require biological interpretation.

## Examples
### Prioritize variants
**Args:** `geneimpacts variants.vcf -o prioritized.txt`
**Explanation:** Prioritizes variants by their functional impact.

### Filter by impact
**Args:** `geneimpacts variants.vcf -i HIGH,MODERATE -o filtered.txt`
**Explanation:** Filters variants to include only HIGH and MODERATE impact.

### Parse VEP output
**Args:** `geneimpacts --vep vep_output.txt -o prioritized.txt`
**Explanation:** Processes VEP annotation output.

### Parse SnpEff output
**Args:** `geneimpacts --snpeff snpeff_output.vcf -o prioritized.txt`
**Explanation:** Processes SnpEff annotation output.

### Generate report
**Args:** `geneimpacts variants.vcf -r report.txt`
**Explanation:** Generates detailed impact report.