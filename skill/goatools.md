---
name: goatools
category: programming
description: GOATOOLS is a Python library for Gene Ontology (GO) enrichment analysis and visualization.
tags: [goatools, GO, enrichment, gene-ontology, Python]
author: oxo-call-community
source_url: "https://github.com/tanghaibao/goatools"
---

## Concepts

- **GO Enrichment Analysis**: GOATOOLS performs Gene Ontology enrichment analysis using Fisher's exact test with multiple correction methods including Bonferroni, Sidak, Holm, and FDR variants.

- **GO DAG Structure**: The library parses and processes the Gene Ontology directed acyclic graph (DAG), enabling traversal and analysis of GO term hierarchies.

- **Multiple Testing Correction**: Supports 11 different multiple hypothesis correction methods from statsmodels and custom implementations.

- **Annotation Sources**: Works with NCBI gene2go annotations and supports multiple species through taxon-specific filtering.

- **Visualization**: Provides tools for drawing GO term lineages, generating GO DAG visualizations, and producing publication-quality figures.

- **GO Grouping**: Facilitates visualization of major findings by grouping related GO terms to simplify interpretation of enrichment results.

## Pitfalls

- **GO File Requirements**: Requires the go-basic.obo file for GO term definitions. Outdated OBO files may cause parsing errors or missing terms.

- **Gene ID Compatibility**: Gene identifiers must match those in the annotation file. Mismatched ID formats (e.g., Entrez vs Ensembl) will produce incorrect results.

- **Background Gene Set**: The background gene list significantly impacts enrichment results. Use appropriate background sets matching your study design.

- **Multiple Testing Correction**: Choose correction method carefully. FDR methods (fdr_bh) are generally recommended over Bonferroni for most genomic studies.

- **Memory Usage**: Processing large gene sets or comprehensive GO annotations may require significant memory. Consider subsetting or using more focused GO term subsets.

## Examples

### Run GO enrichment analysis from command line
**Args:** `python -m goatools.find_enrichment --study study_genes.txt --population background_genes.txt --association gene2go --outfile results.txt`
**Explanation:** Performs GO enrichment analysis comparing a study gene list against a population background using gene2go annotations. Outputs results to results.txt.

### Download GO basic OBO file
**Args:** `python -m goatools.obo wget --obo go-basic.obo`
**Explanation:** Downloads the latest go-basic.obo file from the Gene Ontology website, which is required for GO term analysis.

### Perform GO enrichment with specific correction method
**Args:** `python -m goatools.find_enrichment --study genes.txt --population bg.txt --association gene2go --method fdr_bh`
**Explanation:** Runs enrichment analysis using Benjamini-Hochberg FDR correction. Other available methods include bonferroni, sidak, holm, and fdr_by.

### Draw GO term lineage
**Args:** `python -c "from goatools.graph.draw import draw_lineage; draw_lineage(godag, ['GO:0008150'], filename='go_dag.png')"`
**Explanation:** Generates a visualization of the GO term hierarchy for biological_process (GO:0008150) and saves it as an image file.

### Compare multiple GO lists
**Args:** `goatools compare_gos go_list1.txt go_list2.txt --outfile comparison.txt`
**Explanation:** Compares two lists of GO terms to identify common and unique terms between different enrichment results.

### Run enrichment with GO grouping
**Args:** `python -m goatools.find_enrichment --study genes.txt --population bg.txt --association gene2go --go_grouping`
**Explanation:** Groups related GO terms in the output to simplify interpretation of large enrichment results.

### Load GO DAG programmatically
**Args:** `from goatools.base import get_godag; godag = get_godag("go-basic.obo")`
**Explanation:** Loads the GO DAG from the go-basic.obo file into a GODag object for programmatic access to GO term information.
