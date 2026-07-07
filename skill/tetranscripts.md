---
name: tetranscripts
category: analysis
description: TETRANSCRIPTS - Transposable Element transcript analysis from RNA-seq.
tags: [tetranscripts, transposable-element, te-transcripts, rna-seq, expression]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/tetranscripts"
---

## Concepts

- **Tool Overview**: TETRANSCRIPTS - A tool for comprehensive analysis of transposable element transcripts from RNA-seq data.
- **Core Function**: Quantifies TE-derived transcripts, distinguishes between TE gene and TE insertions, and performs differential expression analysis.
- **Input**: RNA-seq alignments (BAM), TE annotation, genome reference.
- **Output**: TE transcript quantification, expression matrices, differential expression results.
- **Installation**: `pip install tetranscripts` or `conda install -c bioconda tetranscripts`
- **Use Case**: Studying TE transcription in development, disease, and stress responses.

## Pitfalls

- **Gene Expression Confusion**: Distinguishing TE gene transcription from TE insertion transcription can be challenging.
- **Annotation Quality**: Requires high-quality TE annotation for accurate quantification.

## Examples

### Quantify TE transcripts
**Args:** `tetranscripts -b rnaseq.bam -t te_annotation.gtf -o te_transcripts/`
**Explanation:** Quantify TE-derived transcripts from RNA-seq.

### Differential expression
**Args:** `tetranscripts diff -c control/ -t treated/ -o differential/`
**Explanation:** Identify differentially expressed TEs between conditions.
