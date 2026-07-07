---
name: transcriptm
category: analysis
description: TranscriptM - Tool for analyzing transcriptome complexity.
tags: [transcriptm, transcriptome, complexity, rna-seq, gene-expression]
author: oxo-call-community
source_url: "https://github.com/compbio/transcriptm"
---

## Concepts

- **Tool Overview**: TranscriptM - A tool for analyzing transcriptome complexity and diversity.
- **Core Function**: Measures transcriptome complexity metrics including isoform diversity and expression entropy.
- **Input**: RNA-seq data (FASTQ/BAM), gene annotations.
- **Output**: Complexity metrics, isoform diversity scores, expression profiles.
- **Installation**: `pip install transcriptm` or `conda install -c bioconda transcriptm`
- **Use Case**: Transcriptome analysis, alternative splicing, gene regulation.

## Pitfalls

- **Isoform Resolution**: Requires sufficient sequencing depth for isoform detection.
- **Annotation Quality**: Results depend on annotation completeness.

## Examples

### Analyze complexity
**Args:** `transcriptm -i rnaseq.bam -a genes.gtf -o complexity/`
**Explanation:** Analyze transcriptome complexity from RNA-seq data.

### Isoform diversity
**Args:** `transcriptm isoform -i bam_file.bam -o isoform_diversity/`
**Explanation:** Calculate isoform diversity metrics.
