---
name: biotradis
category: annotation
description: Tools to analyse TraDIS transposon insertion sequencing data
tags: [tradis, transposon, insertion-sequencing, essentiality]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/Bio-Tradis"
---

## Concepts
- **Tool Overview**: Bio-Tradis provides tools for analyzing TraDIS (Transposon Directed Insertion-site Sequencing) data to identify essential genes and conditionally essential regions.
- **TraDIS Analysis**: Maps transposon insertion sites, calculates insertion density, and identifies essential genes.
- **Essentiality**: Genes with few insertions are essential; genes with many insertions are non-essential.
- **Applications**: Gene essentiality studies, conditional essentiality, pathway analysis.

## Pitfalls
- **Insertion Bias**: Transposon insertion may have sequence bias affecting results.
- **Coverage Requirements**: Requires sufficient sequencing depth for accurate essentiality calls.

## Examples
### Process TraDIS data
**Args:** `tradis --input reads.fq --reference genome.fa --output tradis_analysis/`
**Explanation:** Processes TraDIS sequencing data to identify insertion sites.

### Identify essential genes
**Args:** `tradis_essentiality --insertions insertions.bed --genes genes.gff --output essentiality.tsv`
**Explanation:** Identifies essential genes based on insertion density.
