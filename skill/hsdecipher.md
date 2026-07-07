---
name: hsdecipher
category: comparative_genomics
description: Pipeline for the downstream analysis of highly similar duplicate genes (HSDs)
tags: [hsdecipher, duplicate_genes, HSD, evolution, comparative_genomics]
author: oxo-call-community
source_url: "https://github.com/zx0223winner/HSDecipher"
---

## Concepts

- **HSD Analysis**: Downstream analysis of highly similar duplicate genes
- **Statistical Analysis**: Comprehensive statistics on HSD characteristics
- **Gene Set Expansion**: Expands HSD gene sets through comparative analysis
- **Visualization**: Generates visualizations of HSD distribution and characteristics
- **Comparative Genomics**: Supports cross-species comparison of HSD patterns
- **Evolutionary Insights**: Provides insights into gene duplication mechanisms and adaptation

## Pitfalls

- **Input Data Quality**: Requires high-quality gene annotations and alignments
- **Computational Resources**: Large datasets may require significant computational resources
- **Orthology Assignment**: Accurate orthology calls are critical for cross-species comparison
- **Threshold Selection**: HSD definition thresholds can significantly affect results
- **Visualization Complexity**: Complex datasets may produce cluttered visualizations
- **Annotation Dependencies**: Relies on functional annotations (Pfam, KEGG)

## Examples

### Basic HSD analysis
**Args:** `hsdecipher -i hsd_candidates.txt -o analysis_results/`
**Explanation:** Runs downstream analysis on HSD candidates.

### With statistical report
**Args:** `hsdecipher -i hsd_candidates.txt -o results/ --statistics`
**Explanation:** Generates comprehensive statistical report.

### Gene set expansion
**Args:** `hsdecipher -i hsd_candidates.txt -o results/ --expand`
**Explanation:** Expands HSD gene set through additional analysis.

### Cross-species comparison
**Args:** `hsdecipher -i hsd_list.txt -o comparison/ --compare species1.txt species2.txt`
**Explanation:** Compares HSD patterns across multiple species.

### Generate visualizations
**Args:** `hsdecipher -i hsd_candidates.txt -o results/ --visualize`
**Explanation:** Generates visualizations of HSD distribution.