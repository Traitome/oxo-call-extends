---
name: goenrichment
category: bioinformatics
description: GOEnrichment performs Gene Ontology term enrichment analysis on gene sets to identify overrepresented biological functions.
tags: [goenrichment, GO, gene-ontology, enrichment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/DanFaria/GOEnrichment"
---

## Concepts

- **GO Term Enrichment**: GOEnrichment identifies Gene Ontology terms that are significantly overrepresented in a given gene set compared to a background set.

- **Statistical Testing**: Uses Fisher's exact test to calculate enrichment significance, with options for multiple testing correction.

- **GO Categories**: Analyzes all three GO categories: biological process (BP), cellular component (CC), and molecular function (MF).

- **Annotation Databases**: Supports multiple annotation databases including GeneDB, Ensembl, and custom annotation files.

- **Visualization**: Generates visualizations of enrichment results including bar charts, dot plots, and GO term hierarchies.

- **Batch Processing**: Supports processing multiple gene sets in a single run for comparative analysis.

## Pitfalls

- **Background Set Selection**: The choice of background gene set significantly affects results. Use appropriate background sets matching your experimental design.

- **Annotation Quality**: Results depend on the quality and completeness of GO annotations. Outdated annotations may miss recent discoveries.

- **Multiple Testing**: Multiple hypothesis testing can inflate false positives. Always apply appropriate correction methods (e.g., FDR).

- **Gene ID Format**: Ensure gene identifiers match those in the annotation database. ID mismatches will produce incorrect results.

- **Threshold Sensitivity**: Adjust significance thresholds based on your study design. Stringent thresholds may miss biologically relevant terms.

## Examples

### Basic enrichment analysis
**Args:** `goenrichment -i genes.txt -b background.txt -o results.txt`
**Explanation:** Performs GO enrichment analysis comparing genes.txt against background.txt and saves results.

### Specify GO category
**Args:** `goenrichment -i genes.txt -b background.txt -c BP -o results.txt`
**Explanation:** Focuses enrichment analysis on biological process (BP) category. Use CC for cellular component or MF for molecular function.

### Adjust significance threshold
**Args:** `goenrichment -i genes.txt -b background.txt -p 0.01 -o results.txt`
**Explanation:** Sets p-value threshold to 0.01 for identifying significant GO terms.

### Generate visualization
**Args:** `goenrichment -i genes.txt -b background.txt --plot -o plot.png`
**Explanation:** Generates a bar plot visualization of the top enriched GO terms.

### Batch process multiple gene sets
**Args:** `goenrichment -d gene_sets/ -b background.txt -o output_dir/`
**Explanation:** Processes all gene sets in the gene_sets directory and saves individual results.

### Use custom annotations
**Args:** `goenrichment -i genes.txt -b background.txt -a custom_annotations.txt -o results.txt`
**Explanation:** Uses a custom annotation file instead of the default database.

### Output GO hierarchy
**Args:** `goenrichment -i genes.txt -b background.txt --hierarchy -o hierarchy.txt`
**Explanation:** Outputs the hierarchical relationships between enriched GO terms.