---
name: detonate
category: assembly
description: DETONATE - DE novo TranscriptOme rNa-seq Assembly with or without the Truth Evaluation (RSEM-EVAL and REF-EVAL).
tags: [detonate, assembly, transcriptome, evaluation, quality]
author: oxo-call-community
source_url: "http://deweylab.biostat.wisc.edu/detonate/"
---

## Concepts

- **Tool Overview**: DETONATE v1.11 - Toolkit for evaluating de novo transcriptome assemblies with RSEM-EVAL and REF-EVAL components.
- **Core Function**: Assesses quality of transcriptome assemblies using reference-free (RSEM-EVAL) and reference-based (REF-EVAL) metrics.
- **Input/Output**: Expects transcriptome FASTA and read alignments; outputs assembly quality scores.
- **Installation**: `conda install -c bioconda detonate`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires transcriptome assembly and aligned reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `rsem-eval-calculate-score --paired reads_1.fq reads_2.fq assembly.fa sample_name`
**Explanation:** Evaluates transcriptome assembly quality using RSEM-EVAL.
