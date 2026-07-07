---
name: kobas
category: annotation
description: KEGG Orthology Based Annotation System - gene set enrichment analysis
tags: [kobas, annotation, pathway-enrichment, KEGG, GO, gene-set-analysis]
author: oxo-call-community
source_url: "http://kobas.cbi.pku.edu.cn"
---

## Concepts

- **KEGG Annotation**: Annotates genes using KEGG Orthology
- **Pathway Enrichment**: Performs pathway enrichment analysis
- **GO Analysis**: Supports Gene Ontology enrichment analysis
- **Gene Set Analysis**: Identifies enriched gene sets from experiments
- **Multiple Species**: Supports analysis across many species
- **Statistical Analysis**: Provides statistical significance of enrichments

## Pitfalls

- **Database Updates**: Gene annotations require regular database updates
- **Multiple Testing**: Requires correction for multiple hypothesis testing
- **Species Coverage**: Some species have incomplete annotations
- **Gene ID Mapping**: Proper ID mapping is critical for analysis
- **Background Selection**: Background gene set affects enrichment results
- **Interpretation**: Statistical significance doesn't guarantee biological relevance

## Examples

### Annotate gene list
**Args:** `kobas annotate -i genes.txt -s hsapiens -t gene -o annotations.txt`
**Explanation:** Annotates gene list with KEGG pathways and GO terms.

### Run enrichment analysis
**Args:** `kobas enrich -i genes.txt -s hsapiens -t gene -o enrichment.txt`
**Explanation:** Performs gene set enrichment analysis.

### Specify gene set database
**Args:** `kobas enrich -i genes.txt -s hsapiens -d KEGG_PATHWAY -o results.txt`
**Explanation:** Enrichment analysis against KEGG pathways only.

### Compare conditions
**Args:** `kobas compare -i genes1.txt -i genes2.txt -s hsapiens -o comparison.txt`
**Explanation:** Compares enrichment between two gene sets.

### Visualize results
**Args:** `kobas visualize -i enrichment.txt -o plot.pdf`
**Explanation:** Generates visualization of enrichment results.

### Batch processing
**Args:** `kobas batch -d gene_lists/ -s hsapiens -o results/`
**Explanation:** Processes multiple gene lists in batch mode.