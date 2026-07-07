---
name: ucsc-bedgeneparts
category: utility
description: UCSC bedGeneParts - Tool for extracting gene parts from BED12 files.
tags: [ucsc-bedgeneparts, ucsc, gene-analysis, bed12, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedGeneParts - A tool for extracting specific parts of genes from BED12 format.
- **Core Function**: Extracts exons, introns, promoters, and other gene features.
- **Input**: BED12 format gene annotation file.
- **Output**: BED file with specific gene parts.
- **Installation**: Part of UCSC utilities
- **Use Case**: Gene structure analysis, feature extraction, annotation.

## Pitfalls

- **Format Requirements**: Requires BED12 format.
- **Annotation Quality**: Results depend on input annotation quality.

## Examples

### Extract exons
**Args:** `bedGeneParts -exons genes.bed12 > exons.bed`
**Explanation:** Extract exon regions from gene annotations.

### Extract promoters
**Args:** `bedGeneParts -promoters=1000 genes.bed12 > promoters.bed`
**Explanation:** Extract 1000bp promoter regions.
