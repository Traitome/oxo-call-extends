---
name: hippunfold
category: neuroimaging
description: HippUnfold automatically models the topological folding structure of the human hippocampus and computationally unfolds it.
tags: [hippunfold, hippocampus, neuroimaging, morphometry, subfield-segmentation]
author: oxo-call-community
source_url: "https://github.com/khanlab/hippunfold"
---

## Concepts

- **Hippocampal Unfolding**: Transforms the folded hippocampus into a flattened representation.

- **Laplace Coordinates**: Uses solutions to Laplace's equation to create smooth coordinate systems.

- **Template-based Shape Injection**: Employs fluid diffeomorphic registration to enforce template topology.

- **U-Net Segmentation**: Uses nnUNet for hippocampal tissue segmentation.

- **Multi-modal Support**: Supports T1w and T2w MRI modalities.

- **BIDS App**: Implemented as a BIDS App for easy integration into neuroimaging workflows.

## Pitfalls

- **Input Format**: Requires BIDS-formatted input data.

- **Computational Resources**: May require significant computational resources for large datasets.

- **Memory Usage**: Processing high-resolution images may require substantial memory.

- **Template Compatibility**: Ensure using compatible template files.

- **Modality Selection**: Choose appropriate modality based on input data characteristics.

## Examples

### Run HippUnfold on participant data
**Args:** `hippunfold /input/dir /output/dir participant --participant-label sub-01`
**Explanation:** Runs hippocampal unfolding on a single participant.

### With T1w modality
**Args:** `hippunfold /input/dir /output/dir participant --participant-label sub-01 --modality T1w`
**Explanation:** Uses T1-weighted MRI data for analysis.

### With T2w modality
**Args:** `hippunfold /input/dir /output/dir participant --participant-label sub-01 --modality T2w`
**Explanation:** Uses T2-weighted MRI data for analysis.

### Group level analysis
**Args:** `hippunfold /input/dir /output/dir group`
**Explanation:** Performs group-level analysis across multiple participants.

### Multiple participants
**Args:** `hippunfold /input/dir /output/dir participant --participant-label sub-01 sub-02 sub-03`
**Explanation:** Processes multiple participants in a single run.

### With custom template
**Args:** `hippunfold /input/dir /output/dir participant --participant-label sub-01 --template custom_template`
**Explanation:** Uses a custom template for segmentation.

### Help command
**Args:** `hippunfold --help`
**Explanation:** Shows available options and usage information.