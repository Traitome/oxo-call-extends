---
name: tin-score-calculation
category: analysis
description: TIN-score Calculation - Tool for calculating Transcription Integrity Number.
tags: [tin-score, transcription-integrity, rna-seq, gene-expression, quality-control]
author: oxo-call-community
source_url: "https://github.com/compbio/tin-score"
---

## Concepts

- **Tool Overview**: TIN-score Calculation - A tool for calculating the Transcription Integrity Number (TIN) from RNA-seq data.
- **Core Function**: Computes TIN score which measures the integrity of RNA transcripts by analyzing coverage uniformity across gene bodies.
- **Input**: RNA-seq alignments (BAM), gene annotations (GTF).
- **Output**: TIN scores per gene, summary statistics, quality reports.
- **Installation**: `pip install tin-score` or `conda install -c bioconda tin-score`
- **Use Case**: RNA-seq quality control, identifying degraded RNA samples, library preparation assessment.

## Pitfalls

- **Gene Annotation**: TIN calculation depends on accurate gene annotation.
- **Coverage**: Requires sufficient sequencing coverage across gene bodies.

## Examples

### Calculate TIN score
**Args:** `tin-score -b rnaseq.bam -a genes.gtf -o tin_scores.tsv`
**Explanation:** Calculate TIN scores for all genes from RNA-seq data.

### Generate report
**Args:** `tin-score -b sample.bam -a annotation.gtf --report -o tin_report/`
**Explanation:** Calculate TIN scores and generate quality report.
