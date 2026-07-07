---
name: motifraptor
category: utility
description: Motif-centric analysis on GWAS data
tags: [motifraptor, utility, gwas]
author: oxo-call-community
source_url: "https://github.com/pinellolab/MotifRaptor"
---

## Concepts

- **Tool Overview**: MotifRaptor v0.3.0 performs motif-centric analysis on GWAS data.
- **Core Function**: Identifies motif enrichment in GWAS-associated regions.
- **GWAS Integration**: Analyzes GWAS summary statistics with motif data.
- **Motif Enrichment**: Detects enriched transcription factor binding motifs.
- **Statistical Analysis**: Uses statistical methods for enrichment testing.
- **Input/Output**: Accepts GWAS data and motifs; outputs enrichment results.

## Pitfalls

- **GWAS Specific**: Designed for GWAS data analysis.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for enrichment.
- **Data Quality**: Results depend on GWAS and motif quality.
- **Multiple Testing**: Requires careful correction for multiple comparisons.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Run motif enrichment
**Args:** `motifraptor -i gwas_results.txt -m motifs.pwm -o enrichment.txt`
**Explanation:** Performs motif enrichment analysis on GWAS data.

### With background regions
**Args:** `motifraptor -i gwas_results.txt -m motifs.pwm -b background.bed -o enrichment.txt`
**Explanation:** Uses custom background regions.

### With FDR correction
**Args:** `motifraptor -i gwas_results.txt -m motifs.pwm --fdr -o enrichment.txt`
**Explanation:** Applies FDR correction.

### Verbose output
**Args:** `motifraptor -i gwas_results.txt -m motifs.pwm -v -o enrichment.txt`
**Explanation:** Shows detailed analysis results.

### Generate plot
**Args:** `motifraptor -i gwas_results.txt -m motifs.pwm -p plot.png -o enrichment.txt`
**Explanation:** Generates enrichment plot.