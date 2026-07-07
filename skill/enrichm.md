---
name: enrichm
category: population-genomics
description: "EnrichM is a toolbox for comparing the functional composition of population genomes."
tags: [enrichm, population-genomics, functional-analysis, metagenomics, annotation]
author: oxo-call-community
source_url: "https://github.com/geronimp/enrichM"
---

## Concepts

- **Tool Overview**: EnrichM is a bioinformatics toolbox for analyzing and comparing the functional composition of microbial communities and population genomes using functional annotation data.
- **Core Function**: Performs functional enrichment analysis, compares functional profiles across samples, and identifies differentially abundant functions.
- **Input/Output**: Input: Genomic/metagenomic sequences, functional annotations (KO, COG, Pfam). Output: Functional profiles, enrichment statistics, comparative reports.
- **Algorithm**: Uses statistical methods to compare functional abundances between groups and identify significantly enriched functions.
- **Key Features**: Functional profiling, enrichment analysis, differential abundance testing, visualization, batch processing, support for multiple annotation databases.
- **Installation**: `conda install -c bioconda enrichm`

## Pitfalls

- **Annotation Quality**: Results depend on the quality and completeness of functional annotations.
- **Database Selection**: Choice of annotation database (KO, COG, etc.) affects analysis results.
- **Statistical Threshold**: Appropriate statistical thresholds must be chosen to avoid false positives.
- **Sample Size**: Small sample sizes may lead to unreliable statistical results.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic functional profiling
**Args:** `enrichm profile -i genomes/ -o profiles/`
**Explanation:** Generates functional profiles from genomic sequences.

### Enrichment analysis
**Args:** `enrichm enrich -p profiles/ -g groups.txt -o enrichment/`
**Explanation:** Performs functional enrichment analysis between groups.

### Differential abundance
**Args:** `enrichm diff -p profiles/ -g groups.txt -o diff_results/`
**Explanation:** Identifies differentially abundant functions between groups.

### Generate visualization
**Args:** `enrichm plot -i profiles/ -o plot.pdf`
**Explanation:** Generates visualization of functional profiles.

### Batch processing
**Args:** `enrichm batch -i input.txt -o results/`
**Explanation:** Processes multiple datasets in batch mode.