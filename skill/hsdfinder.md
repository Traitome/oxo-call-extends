---
name: hsdfinder
category: gene_prediction
description: A tool to predict highly similar duplicates (HSDs) in eukaryotes using BLAST-based strategy
tags: [hsdfinder, gene_duplication, HSD, paralogs, eukaryotes]
author: oxo-call-community
source_url: "https://github.com/zx0223winner/HSDFinder"
---

## Concepts

- **HSD Prediction**: Identifies highly similar duplicated genes in eukaryotic genomes
- **BLAST-Based Strategy**: Uses all-against-all BLAST searches for duplicate detection
- **Pfam Domain Annotation**: Integrates protein domain information from Pfam
- **KEGG Pathway Analysis**: Categorizes HSDs by KEGG pathway functional categories
- **Heatmap Visualization**: Generates heatmaps for cross-species comparison
- **Amino Acid Identity Thresholds**: Supports customizable similarity thresholds

## Pitfalls

- **BLAST Parameters**: E-value cutoff significantly affects prediction sensitivity
- **Computational Time**: All-against-all BLAST can be computationally intensive
- **Database Dependencies**: Requires InterProScan and KEGG annotations
- **Threshold Selection**: Balancing sensitivity and specificity requires careful tuning
- **Partial Genes**: May incorrectly identify partial gene duplicates
- **Pseudogenes**: Pseudogenes may be incorrectly classified as functional duplicates

## Examples

### Basic HSD prediction
**Args:** `hsdfinder -b blast_results.tsv -i interproscan.tsv -o hsd_results.txt`
**Explanation:** Predicts HSDs using BLAST and InterProScan results.

### With custom thresholds
**Args:** `hsdfinder -b blast.tsv -i interpro.tsv -o results.txt -id 90 -len 10`
**Explanation:** Sets 90% identity threshold and 10aa length variance.

### Generate heatmap
**Args:** `hsdfinder -b blast.tsv -i interpro.tsv -o results/ --heatmap kegg_annotations.txt`
**Explanation:** Generates heatmap visualization linked to KEGG pathways.

### Cross-species comparison
**Args:** `hsdfinder -b species1_blast.tsv -i species1_interpro.tsv -o comparison/ --compare species2/`
**Explanation:** Compares HSDs between two species.

### Batch mode
**Args:** `hsdfinder --batch species_list.txt -o batch_results/`
**Explanation:** Processes multiple species in batch mode.