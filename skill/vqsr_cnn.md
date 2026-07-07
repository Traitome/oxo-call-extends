---
name: vqsr_cnn
category: bioinformatics
description: VQSR-CNN - Variant quality recalibration.
tags: [vqsr_cnn, variant-analysis, machine-learning, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vqsr-cnn/"
---

## Concepts

- **Tool Overview**: VQSR-CNN - CNN-based variant quality recalibration.
- **Core Function**: Uses CNN to recalibrate variant quality scores.
- **Input**: VCF file.
- **Output**: Recalibrated VCF.
- **Installation**: Install via pip or conda
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Training**: Requires model training.

## Examples

### Recalibrate variants
**Args:** `vqsr_cnn -i input.vcf -o recalibrated.vcf`
**Explanation:** Recalibrate variant quality.

### With options
**Args:** `vqsr_cnn -i input.vcf -o recalibrated.vcf -m model.pt`
**Explanation:** Use custom model.
