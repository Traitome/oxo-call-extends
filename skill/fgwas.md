---
name: fgwas
category: annotation
description: "fgwas is a command line tool for integrating functional genomic information into a genome-wide association study (GWAS)."
tags: [fgwas, annotation, GWAS, functional-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/joepickrell/fgwas"
---

## Concepts

- **Tool Overview**: fgwas is a tool for integrating functional genomic information into GWAS analysis to improve variant association detection.
- **Core Function**: Combines functional annotations with GWAS summary statistics for improved variant prioritization.
- **Input/Output**: Input: GWAS data, functional annotations. Output: Annotated association results.
- **Algorithm**: Uses Bayesian methods to integrate functional annotations with association signals.
- **Key Features**: Functional integration, Bayesian inference, annotation enrichment, variant prioritization, genome-wide analysis.
- **Installation**: `conda install -c bioconda fgwas`

## Pitfalls

- **Annotation Quality**: Results depend on annotation quality.
- **GWAS Data**: Requires well-powered GWAS data.
- **Computational Complexity**: Large datasets may require significant resources.
- **Model Assumptions**: Bayesian assumptions may affect results.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic analysis
**Args:** `fgwas -i gwas_summary.txt -o results/`
**Explanation:** Integrates functional annotations with GWAS data.

### With annotations
**Args:** `fgwas -i gwas_summary.txt -annot annotation.bed -o results/`
**Explanation:** Uses specific functional annotations.

### Enrichment analysis
**Args:** `fgwas -i gwas_summary.txt -annot annotation.bed -o results/ --enrichment`
**Explanation:** Performs annotation enrichment analysis.

### Fine-mapping
**Args:** `fgwas -i gwas_summary.txt -annot annotation.bed -o results/ --fine-map`
**Explanation:** Performs fine-mapping with annotations.

### Visualization
**Args:** `fgwas -i gwas_summary.txt -annot annotation.bed -o results/ --plot`
**Explanation:** Generates visualization of results.