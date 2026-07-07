---
name: kipoi_veff
category: variant-calling
description: "kipoi_veff: variant effect prediction plugin for Kipoi"
tags: [kipoi_veff, variant-calling, variant-effect, kipoi, deep-learning]
author: oxo-call-community
source_url: "https://kipoi.org/veff-docs/"
---
## Concepts

- **Variant Effect Prediction**: Predicts the functional impact of genetic variants
- **Deep Learning Integration**: Uses deep learning models for variant effect prediction
- **Annotation Pipeline**: Integrates with Kipoi model zoo for variant annotation
- **Multi-allelic Support**: Handles multi-allelic variants and complex genotypes
- **Effect Classification**: Classifies variants into functional categories (missense, nonsense, silent)
- **Batch Processing**: Processes large variant datasets efficiently

## Pitfalls

- **Model Availability**: Requires appropriate Kipoi models to be installed
- **Input Data Quality**: Poor quality VCF files can cause prediction errors
- **Computational Resources**: GPU acceleration recommended for large datasets
- **Reference Genome**: Must match the reference used for model training
- **Variant Representation**: Proper variant normalization is critical
- **Effect Prediction Limits**: Models may not capture all types of variant effects

## Examples

### Predict variant effects
**Args:** `kipoi_veff predict -i variants.vcf -m model_name -o effects.csv`
**Explanation:** Predicts functional effects of variants using a specified Kipoi model.

### Annotate VCF file
**Args:** `kipoi_veff annotate -i input.vcf -o annotated.vcf -m model_name`
**Explanation:** Annotates a VCF file with predicted variant effects.

### Batch processing mode
**Args:** `kipoi_veff batch -d vcf_files/ -o results/ -m model_name`
**Explanation:** Processes multiple VCF files in batch mode.

### Filter by effect type
**Args:** `kipoi_veff filter -i variants.vcf -o filtered.vcf --effect missense`
**Explanation:** Filters variants by predicted effect type.

### Generate summary statistics
**Args:** `kipoi_veff stats -i effects.csv -o summary.txt`
**Explanation:** Generates summary statistics of variant effect predictions.

### Compare model predictions
**Args:** `kipoi_veff compare -m model1 model2 -i variants.vcf -o comparison.csv`
**Explanation:** Compares predictions from multiple models.