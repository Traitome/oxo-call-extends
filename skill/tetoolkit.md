---
name: tetoolkit
category: analysis
description: TEToolkit - Transposable Element Toolkit for analyzing TE expression and epigenomics.
tags: [tetoolkit, transposable-element, te-expression, chip-seq, rna-seq, epigenomics]
author: oxo-call-community
source_url: "https://github.com/compbio/tetoolkit"
---

## Concepts

- **Tool Overview**: TEToolkit - A comprehensive toolkit for transposable element analysis combining expression and epigenetic data.
- **Core Function**: Analyzes TE expression from RNA-seq and TE chromatin accessibility from ChIP-seq/ATAC-seq data.
- **Input**: RNA-seq, ChIP-seq, or ATAC-seq data in BAM/FASTQ format, TE annotation.
- **Output**: TE expression matrices, differential expression results, chromatin enrichment profiles.
- **Installation**: `pip install tetoolkit` or `conda install -c bioconda tetoolkit`
- **Use Case**: Studying TE regulation through epigenetics, TE activation in disease.

## Pitfalls

- **Multi-mapping**: TE reads often map to multiple loci - handle with appropriate parameters.
- **TE Annotation**: Quality of analysis depends on TE annotation completeness.

## Examples

### TE expression from RNA-seq
**Args:** `tetoolkit rnaseq -i rnaseq.bam -a te_annotation.gtf -o te_expression/`
**Explanation:** Quantify TE expression from RNA-seq data.

### Chromatin accessibility
**Args:** `tetoolkit chipseq -i atacseq.bam -o chromatin_analysis/`
**Explanation:** Analyze TE chromatin accessibility from ATAC-seq data.
