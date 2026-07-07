---
name: meta-neuro
category: utility
description: Medial Tractography Analysis (MeTA)
tags: [meta-neuro, utility, neuroimaging, tractography]
author: oxo-call-community
source_url: "https://github.com/USC-LoBeS/meta"
---

## Concepts

- **Tool Overview**: MeTA v2.0.1 is a workflow for Medial Tractography Analysis, designed to minimize microstructural heterogeneity in diffusion MRI (dMRI) metrics.
- **Core Function**: Extracts and parcels the core volume along bundle length in voxel-space while preserving bundle shape.
- **Diffusion MRI Analysis**: Processes diffusion MRI data to analyze white matter tractography.
- **Bundle Analysis**: Captures regional variation within and along white matter bundles.
- **Input/Output**: Accepts diffusion MRI data in NIfTI format; outputs analyzed tracts and metrics.
- **Microstructural Analysis**: Provides detailed microstructural information about white matter tracts.

## Pitfalls

- **Data Quality**: Analysis quality depends on input diffusion MRI data quality.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Image Registration**: Requires accurate image registration for reliable results.
- **Artifact Handling**: Susceptibility artifacts can affect analysis results.
- **Expertise Required**: Requires expertise in diffusion MRI analysis for proper interpretation.

## Examples

### Run tractography analysis
**Args:** `meta-neuro -i dwi.nii.gz -o results/`
**Explanation:** Runs tractography analysis on diffusion MRI data.

### With mask
**Args:** `meta-neuro -i dwi.nii.gz -m mask.nii.gz -o results/`
**Explanation:** Uses a region of interest mask for analysis.

### Specify tracts
**Args:** `meta-neuro -i dwi.nii.gz -t tracts.txt -o results/`
**Explanation:** Analyzes specific white matter tracts.

### Generate visualization
**Args:** `meta-neuro -i dwi.nii.gz -o results/ -v`
**Explanation:** Generates visualizations of tractography results.

### Batch processing
**Args:** `meta-neuro -i subjects/ -o results/`
**Explanation:** Processes multiple subjects in batch mode.