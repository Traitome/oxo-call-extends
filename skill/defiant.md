---
name: defiant
category: epigenomics
description: Defiant - differential methylation analysis with easy identification and annotation.
tags: [defiant, epigenomics, methylation, differential-analysis]
author: oxo-call-community
source_url: "https://github.com/hhg7/defiant"
---

## Concepts

- **Tool Overview**: defiant (v1.1.4+) is a tool for fast differential methylation analysis with annotation capabilities. It identifies differentially methylated regions (DMRs) between conditions.
- **Core Function**: Identifies DMRs from bisulfite sequencing data and annotates them with genomic features like promoters, exons, and CpG islands.
- **Input/Output**: Input: Methylation calls (BED/Bismark output), sample annotations. Output: DMRs with statistics, genomic annotations, visualization.
- **Algorithm**: Uses statistical tests (t-test, ANOVA) to identify regions with significant methylation differences between groups.
- **Key Features**: Fast analysis, statistical rigor, genomic annotation, visualization tools, supports multiple comparison groups.
- **Installation**: `conda install -c bioconda defiant`

## Pitfalls

- **Input Requirements**: Requires methylation data in compatible format.
- **Sample Size**: Requires sufficient biological replicates for statistical power.
- **Normalization**: Requires proper data normalization.
- **Multiple Testing**: Requires appropriate multiple testing correction.
- **Annotation Quality**: Depends on annotation database completeness.

## Examples

### Find differentially methylated regions
**Args:** `defiant --control control.bed --treatment treatment.bed --output dmrs.tsv`
**Explanation:** Finds differentially methylated regions between conditions.

### With annotation
**Args:** `defiant --control control.bed --treatment treatment.bed --output dmrs.tsv --annotate`
**Explanation:** Annotate DMRs with genomic features.

### Multiple groups
**Args:** `defiant --groups groups.txt --output dmrs.tsv`
**Explanation:** Compare multiple experimental groups.