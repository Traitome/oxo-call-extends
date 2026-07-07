---
name: deepsvr
category: variant-calling
description: DeepSVR - deep somatic variant refinement using deep learning to classify real somatic and anomalous variants.
tags: [deepsvr, variant-calling, somatic, deep-learning, filtering]
author: oxo-call-community
source_url: "https://github.com/griffithlab/deepsvr"
---

## Concepts

- **Tool Overview**: deepsvr (v0.1.0+) is a deep learning-based tool for classifying and refining somatic variants in paired tumor-normal sequencing data. It distinguishes true somatic variants from artifacts and germline variants.
- **Core Function**: Uses deep learning to classify somatic variants as real or artifacts, improving the accuracy of somatic variant calling pipelines.
- **Input/Output**: Input: VCF files with somatic calls, optionally with tumor-normal BAM files. Output: Refined VCF with confidence scores, filtered variants.
- **Algorithm**: Uses deep neural networks trained on features derived from variant calls, read alignments, and quality metrics to classify variants.
- **Key Features**: Somatic variant filtering, confidence scoring, integrates with existing pipelines, supports multiple variant callers, batch processing.
- **Installation**: `conda install -c bioconda deepsvr`

## Pitfalls

- **Input Requirements**: Requires paired tumor-normal data for best results.
- **Variant Caller Compatibility**: Works best with specific variant callers.
- **Computational Resources**: Requires significant computational resources.
- **Training Data**: Performance depends on training dataset diversity.
- **Confidence Threshold**: Requires appropriate threshold setting.

## Examples

### Classify somatic variants
**Args:** `deepsvr classify --vcf somatic.vcf --output refined.vcf`
**Explanation:** Classifies and filters somatic variants using deep learning.

### With BAM files
**Args:** `deepsvr classify --vcf somatic.vcf --tumor_bam tumor.bam --normal_bam normal.bam --output refined.vcf`
**Explanation:** Use BAM files for additional feature extraction.

### Filter by confidence
**Args:** `deepsvr classify --vcf somatic.vcf --output refined.vcf --confidence 0.9`
**Explanation:** Filter variants with 90% confidence threshold.