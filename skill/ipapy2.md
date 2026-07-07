---
name: ipapy2
category: annotation
description: Integrated Probabilistic Annotation (IPA) 2.0 - Bayesian-based annotation method for LC-MS/MS metabolomics data.
tags: [ipapy2, metabolomics, annotation, Bayesian, LC-MS/MS]
author: oxo-call-community
source_url: "https://github.com/francescodc87/ipaPy2"
---

## Concepts

- **Tool Overview**: ipaPy2 (v1.3.0) - An improved Bayesian-based annotation method for LC-MS/MS untargeted metabolomics data.
- **Core Function**: Provides statistically rigorous estimates of annotation probabilities for metabolomics features.
- **Bayesian Framework**: Uses Bayesian inference to integrate multiple sources of evidence for metabolite identification.
- **Tandem MS Integration**: Incorporates MS/MS fragmentation data to improve annotation accuracy.
- **Isotope Fingerprints**: Treats isotope peaks as integrated fingerprints rather than individual features.
- **mzMatch Integration**: Fully integrated with the mzMatch pipeline for comprehensive metabolomics analysis.

## Pitfalls

- **Database Dependencies**: Annotation quality depends heavily on database completeness and quality.
- **Computational Resources**: Large datasets may require significant computational resources and memory.
- **Parameter Tuning**: Optimal performance requires careful parameter tuning based on specific experimental conditions.
- **Isotope Pattern Matching**: Requires accurate isotope pattern prediction for confident annotations.
- **Retention Time Alignment**: Inconsistent retention times across runs can affect annotation confidence.
- **Adduct Identification**: Accurate adduct identification is crucial for correct metabolite annotation.

## Examples

### Basic annotation workflow
**Args:** `ipaPy2 annotate -i features.csv -d database.sqlite -o annotations.csv`
**Explanation:** Performs probabilistic annotation of LC-MS/MS features using the specified database.

### With tandem MS data
**Args:** `ipaPy2 annotate -i features.csv -d database.sqlite -m msms_spectra.mgf -o annotations.csv`
**Explanation:** Integrates tandem MS fragmentation data for improved annotation accuracy.

### Custom database building
**Args:** `ipaPy2 build_db -i compound_list.csv -o custom_db.sqlite --add-adducts`
**Explanation:** Builds a custom annotation database with adduct information from compound list.

### Annotation confidence filtering
**Args:** `ipaPy2 filter -i annotations.csv -o filtered.csv --min-confidence 0.8`
**Explanation:** Filters annotations to retain only those with confidence score >= 80%.

### Batch processing mode
**Args:** `ipaPy2 batch -i batch_config.json -o results/ --threads 8`
**Explanation:** Processes multiple datasets in batch mode with parallel processing.

### Visualize annotation results
**Args:** `ipaPy2 visualize -i annotations.csv -o visualization.html`
**Explanation:** Generates an interactive visualization of annotation results for exploration.