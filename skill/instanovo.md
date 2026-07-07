---
name: instanovo
category: proteomics
description: InstaNovo enables diffusion-powered de novo peptide sequencing in large scale proteomics experiments using deep learning models.
tags: [instanovo, proteomics, de-novo-sequencing, deep-learning, diffusion]
author: oxo-call-community
source_url: "https://instadeepai.github.io/InstaNovo/"
---

## Concepts

- **Diffusion-based Peptide Sequencing**: InstaNovo uses diffusion models for accurate de novo peptide sequencing from mass spectrometry data.
- **Deep Learning Architecture**: Leverages transformer-based neural networks and diffusion processes to predict peptide sequences.
- **Large-scale Processing**: Designed for processing large-scale proteomics datasets efficiently.
- **Mass Spectrometry Integration**: Works with raw mass spectrometry data in various formats (mzML, mzXML).
- **Post-translational Modifications**: Supports identification of post-translational modifications (PTMs) in peptides.

## Pitfalls

- **Computational Requirements**: Requires significant computational resources for model training and inference.
- **Model Selection**: Different models may be needed for different mass spectrometry platforms.
- **Data Quality**: Performance depends on input mass spectrometry data quality; noisy data reduces accuracy.
- **PTM Handling**: Complex PTMs may require additional configuration or custom models.
- **Memory Usage**: Processing large datasets may require careful memory management.

## Examples

### Basic de novo sequencing
**Args:** `instanovo predict --input spectra.mzML --output peptides.fasta --model instanovo_base`
**Explanation:** Predicts peptide sequences from mass spectrometry data using the base model.

### Use large model for higher accuracy
**Args:** `instanovo predict --input spectra.mzML --output peptides.fasta --model instanovo_large`
**Explanation:** Uses the larger model for improved prediction accuracy at the cost of increased computation.

### Enable PTM detection
**Args:** `instanovo predict --input spectra.mzML --output peptides.fasta --model instanovo_base --enable_ptm`
**Explanation:** Enables post-translational modification detection during peptide sequencing.

### Batch processing
**Args:** `instanovo predict --input_dir spectra/ --output_dir results/ --model instanovo_base`
**Explanation:** Processes multiple mass spectrometry files in batch mode.

### Fine-tune model on custom data
**Args:** `instanovo fine_tune --train_data train_spectra.mzML --model instanovo_base --output_model custom_model`
**Explanation:** Fine-tunes the base model on custom training data for improved performance on specific datasets.

### Generate confidence scores
**Args:** `instanovo predict --input spectra.mzML --output peptides.fasta --model instanovo_base --confidence_threshold 0.8`
**Explanation:** Filters predictions to include only peptides with confidence score ≥ 0.8.