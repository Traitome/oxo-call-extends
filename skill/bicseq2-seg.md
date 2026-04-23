---
name: bicseq2-seg
category: variant-calling
description: BICseq2-seg - Detect CNVs based on normalized data
tags: [cnv, segmentation, copy-number, variant-calling]
author: oxo-call-community
source_url: "http://compbio.med.harvard.edu/BIC-seq/"
---

## Concepts
- **Tool Overview**: BICseq2-seg is the segmentation module of BICseq2 for detecting copy number variations (CNVs) from normalized sequencing data. It takes normalized read depth from BICseq2-norm and identifies CNV segments.
- **Segmentation Algorithm**: Uses a statistical segmentation algorithm based on the Bayesian Information Criterion (BIC) to identify regions with consistent copy number.
- **CNV Types**: Detects both copy number gains (amplifications) and losses (deletions).
- **Workflow**: Second step of BICseq2 pipeline, following BICseq2-norm normalization.

## Pitfalls
- **Input Requirement**: Requires pre-normalized data from BICseq2-norm.
- **Threshold Selection**: Sensitivity and specificity depend on segmentation thresholds.
- **Tumor Purity**: For tumor samples, CNV calls may be affected by tumor purity and heterogeneity.

## Examples
### Detect CNVs from normalized data
**Args:** `NBICseq-seg -n normalized.txt -o cnv_segments.txt`
**Explanation:** Performs CNV segmentation on normalized read depth data.

### Specify minimum segment size
**Args:** `NBICseq-seg -n normalized.txt -minSeg 10000 -o cnv_segments.txt`
**Explanation:** Requires CNV segments to be at least 10kb in size.
