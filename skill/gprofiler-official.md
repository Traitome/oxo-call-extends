---
name: gprofiler-official
category: bioinformatics
description: g:Profiler provides functional enrichment analysis and gene list analysis tools for biological data interpretation.
tags: [gprofiler, functional-enrichment, GO-analysis, bioinformatics]
author: oxo-call-community
source_url: "http://biit.cs.ut.ee/gprofiler"
---

## Concepts

- **Functional Enrichment**: g:Profiler performs functional enrichment analysis to identify overrepresented biological functions in gene lists.

- **Multiple Databases**: Supports multiple annotation databases including GO, KEGG, Reactome, and more.

- **Orthology Support**: Provides orthology-based analysis across multiple species.

- **Gene Conversion**: Converts gene identifiers between different naming systems.

- **Interactive Results**: Generates interactive results with visualization capabilities.

- **API Access**: Provides programmatic access through REST API for integration with bioinformatics pipelines.

## Pitfalls

- **Gene ID Format**: Ensure gene identifiers match the expected format. Mixed ID types can cause errors.

- **Species Selection**: Choose the correct species for analysis. Incorrect species will produce irrelevant results.

- **Multiple Testing**: Apply appropriate multiple testing correction to avoid false positives.

- **Database Currency**: Results depend on database version. Use the latest databases for up-to-date annotations.

- **Input Size**: Very large gene lists may exceed API limits. Consider splitting large queries.

## Examples

### Basic enrichment analysis
**Args:** `gprofiler -i gene_list.txt -o results.txt`
**Explanation:** Performs functional enrichment analysis on a gene list and saves results.

### Specify species
**Args:** `gprofiler -i gene_list.txt -s hsapiens -o results.txt`
**Explanation:** Specifies human as the target species for enrichment analysis.

### Include specific databases
**Args:** `gprofiler -i gene_list.txt -d GO:BP,KEGG -o results.txt`
**Explanation:** Limits analysis to Biological Process (GO:BP) and KEGG pathways.

### Gene ID conversion
**Args:** `gprofiler convert -i gene_list.txt -f ensembl -t symbol -o converted.txt`
**Explanation:** Converts Ensembl IDs to gene symbols.

### Interactive HTML output
**Args:** `gprofiler -i gene_list.txt -o results.html`
**Explanation:** Generates an interactive HTML report with visualization.

### Batch analysis
**Args:** `gprofiler batch -d gene_lists/ -o results/`
**Explanation:** Processes multiple gene lists in a directory.

### REST API query
**Args:** `curl "https://biit.cs.ut.ee/gprofiler/api/gost/profile?organism=hsapiens&query=APOE,APP,PSEN1"`
**Explanation:** Queries the g:Profiler REST API directly for enrichment analysis.