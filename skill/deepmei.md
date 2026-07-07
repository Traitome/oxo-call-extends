---
name: deepmei
category: variant-calling
description: DeepMEI - deep learning based mobile element insertion detection.
tags: [deepmei, variant-calling, transposon, insertion, deep-learning]
author: oxo-call-community
source_url: "https://github.com/Kanglu123/deepmei/tree/deepmei-v1.6.24"
---

## Concepts

- **Tool Overview**: deepmei (v1.6.24+) is a deep learning-based tool for detecting mobile element insertions (MEI) in genomic sequencing data. It identifies transposon insertions with high accuracy.
- **Core Function**: Detects mobile element insertion events using deep learning from aligned sequencing reads, identifying insertion breakpoints and types.
- **Input/Output**: Input: BAM/CRAM alignment files, reference genome. Output: VCF with MEI calls, insertion types, confidence scores.
- **Algorithm**: Uses convolutional neural networks to identify patterns associated with mobile element insertions from read alignments.
- **Key Features**: High accuracy, supports multiple MEI types, breakpoint precision, confidence scoring, VCF output.
- **Installation**: `conda install -c bioconda deepmei`

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM/CRAM files with index.
- **Reference Genome**: Must use compatible reference genome.
- **Insertion Size**: May miss very small insertions.
- **Computational Resources**: Requires significant computational resources.
- **Training Data**: Performance depends on training dataset diversity.

## Examples

### Detect mobile element insertions
**Args:** `deepmei --bam input.bam --reference ref.fa --output mei_calls.vcf`
**Explanation:** Detects mobile element insertions from aligned reads.

### With increased sensitivity
**Args:** `deepmei --bam input.bam --reference ref.fa --output mei_calls.vcf --sensitive`
**Explanation:** Use sensitive mode for detecting low-confidence insertions.

### Batch processing
**Args:** `deepmei --bam_list bam_files.txt --reference ref.fa --output results/`
**Explanation:** Process multiple BAM files in batch.