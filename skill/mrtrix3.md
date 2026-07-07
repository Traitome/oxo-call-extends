---
name: mrtrix3
category: utility
description: Advanced diffusion MRI analysis tools including CSD, tractography, and fibre density.
tags: [mrtrix3, utility, mri]
author: oxo-call-community
source_url: "https://www.mrtrix.org"
---

## Concepts

- **Tool Overview**: MRtrix3 v3.0.8 performs advanced diffusion MRI analysis.
- **Core Function**: Provides tools for diffusion tensor imaging and tractography.
- **CSD**: Constrained Spherical Deconvolution for fibre orientation estimation.
- **Probabilistic Tractography**: Maps white matter connections probabilistically.
- **Track-Density Imaging**: Visualizes white matter pathways.
- **Input/Output**: Accepts DICOM/NIfTI; outputs processed images and tracks.

## Pitfalls

- **MRI Specific**: Designed for diffusion MRI data.
- **Memory Requirements**: Memory usage depends on image size.
- **Parameter Tuning**: May require parameter adjustment for analysis.
- **Data Quality**: Results depend on MRI acquisition quality.
- **Computational Resources**: Large datasets may require significant resources.
- **Expertise Required**: Requires knowledge of diffusion MRI analysis.

## Examples

### Convert DICOM to NIfTI
**Args:** `mrconvert input.dcm output.nii.gz`
**Explanation:** Converts DICOM to NIfTI format.

### Perform CSD
**Args:** `dwi2fod csd input.nii.gz response.txt output.nii.gz`
**Explanation:** Computes fibre orientation distribution.

### Run tractography
**Args:** `tckgen input.nii.gz tracks.tck`
**Explanation:** Generates tractography streamlines.

### Create track-density image
**Args:** `tckmap tracks.tck output.nii.gz`
**Explanation:** Creates track-density image.

### Visualize tracks
**Args:** `mrview input.nii.gz -tractography.load tracks.tck`
**Explanation:** Visualizes tractography results.