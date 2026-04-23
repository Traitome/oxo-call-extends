---
name: bicseq2-norm
category: variant-calling
description: BICseq2-norm - Normalize potential biases in sequencing data for CNV detection
tags: [cnv, normalization, copy-number, bias-correction]
author: oxo-call-community
source_url: "http://compbio.med.harvard.edu/BIC-seq/"
---

## Concepts
- **Tool Overview**: BICseq2-norm is the normalization module of BICseq2, designed to correct potential biases in sequencing data before copy number variation (CNV) detection. It normalizes read depth for GC content, mappability, and other systematic biases.
- **Bias Correction**: Corrects for GC-content bias, mappability bias, and other technical artifacts that affect read depth uniformity.
- **Workflow**: Part of the BICseq2 pipeline. BICseq2-norm produces normalized read depth, which is then used by BICseq2-seg for CNV segmentation.
- **Statistical Model**: Uses the Bayesian Information Criterion (BIC) for model selection.

## Pitfalls
- **Reference Files**: Requires GC content and mappability tracks for the reference genome.
- **Bin Size**: Choice of bin size affects resolution and noise. Smaller bins give higher resolution but more noise.
- **Paired with BICseq2-seg**: BICseq2-norm output must be processed by BICseq2-seg for CNV calling.

## Examples
### Normalize sequencing data
**Args:** `NBICseq-norm -l 100 -g gc_content.txt -m mappability.txt normal.bam tumor.bam output`
**Explanation:** Normalizes tumor vs normal BAM files with 100bp bins using GC and mappability correction.

### Specify bin size
**Args:** `NBICseq-norm -l 500 -g gc.txt -m map.txt sample.bam output`
**Explanation:** Normalizes with 500bp bins for smoother profile.
