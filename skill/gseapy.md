---
name: gseapy
category: bioinformatics
description: gseapy provides a Python interface for Gene Set Enrichment Analysis, enabling programmatic access to enrichment analysis workflows.
tags: [gseapy, python, gene-set-enrichment, bioinformatics]
author: oxo-call-community
source_url: "https://gseapy.readthedocs.io"
---

## Concepts

- **Python Interface**: gseapy provides Python bindings for GSEA analysis.

- **Programmatic Access**: Enables integration of GSEA into Python workflows.

- **Multiple Databases**: Supports various gene set databases including MSigDB.

- **Enrichment Methods**: Implements multiple enrichment methods.

- **Visualization**: Generates publication-quality visualizations.

- **Batch Processing**: Supports batch processing of multiple gene lists.

## Pitfalls

- **Memory Usage**: Processing large datasets may require significant memory.

- **Database Compatibility**: Ensure compatibility with gene set database versions.

- **Python Environment**: Requires proper Python environment setup.

- **Dependency Management**: Manage dependencies carefully.

- **Result Interpretation**: Interpret enrichment results with caution.

## Examples

### Basic GSEA analysis
**Args:** `import gseapy as gp`
**Explanation:** Imports the gseapy module.

### Run enrichment analysis
**Args:** `enr = gp.enrichr(gene_list=genes, gene_sets='GO_Biological_Process_2023', outdir='results')`
**Explanation:** Performs enrichment analysis using Enrichr.

### Plot results
**Args:** `gp.dotplot(enr.res2d, title='Enrichment Results')`
**Explanation:** Generates a dot plot of enrichment results.

### Compare gene sets
**Args:** `comparison = gp.compare_reports('pathways/', outdir='comparison')`
**Explanation:** Compares multiple enrichment reports.

### Load gene sets
**Args:** `gene_sets = gp.get_library('KEGG_2021_Human')`
**Explanation:** Loads KEGG gene sets from Enrichr.

### Custom gene sets
**Args:** `enr = gp.enrichr(gene_list=genes, gene_sets='custom.gmt', outdir='results')`
**Explanation:** Uses custom gene set file.

### Batch analysis
**Args:** `for genes in gene_lists: gp.enrichr(gene_list=genes, gene_sets='GO', outdir=f'results_{i}')`
**Explanation:** Processes multiple gene lists in a loop.