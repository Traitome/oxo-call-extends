---
name: hicberg
category: bioinformatics
description: HiCBerg is a statistical profiling tool for Hi-C, ChIA-PET, Capture-C contact data and genomic data reconstruction.
tags: [hicberg, Hi-C, ChIA-PET, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/sebgra/hicberg"
---

## Concepts

- **Contact Data Analysis**: HiCBerg analyzes Hi-C and related contact data.

- **Statistical Profiling**: Uses statistical methods for data analysis.

- **Genomic Reconstruction**: Reconstructs genomic data from contact maps.

- **3D Genome**: Analyzes three-dimensional genome organization.

- **Chromatin Interactions**: Identifies chromatin interactions.

- **Data Integration**: Integrates multiple data types.

## Pitfalls

- **Data Quality**: Results depend on input data quality.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Normalization**: Proper normalization is critical.

## Examples

### Analyze Hi-C data
**Args:** `hicberg --input contacts.txt --output results/`
**Explanation:** Analyzes Hi-C contact data.

### With ChIA-PET data
**Args:** `hicberg --input chiapet.bedpe --output results/`
**Explanation:** Processes ChIA-PET data.

### Batch processing
**Args:** `for f in *.txt; do hicberg --input $f --output ${f%.txt}_results/; done`
**Explanation:** Processes multiple contact files.

### Generate report
**Args:** `hicberg --input contacts.txt --output results/ --report`
**Explanation:** Generates comprehensive analysis report.

### Help command
**Args:** `hicberg --help`
**Explanation:** Shows available options and usage information.