---
name: deepmedic
category: annotation
description: Efficient Multi-Scale 3D Convolutional Neural Network for Brain Lesion Segmentation.
tags: [deepmedic, annotation, deep-learning, segmentation, medical-imaging]
author: oxo-call-community
source_url: "https://github.com/Kamnitsask/deepmedic"
---

## Concepts

- **Tool Overview**: DeepMedic v0.6.1 - Efficient multi-scale 3D CNN for brain lesion segmentation from medical images.
- **Core Function**: Segments brain lesions from MRI scans using a dual-pathway 3D convolutional neural network.
- **Input/Output**: Expects NIfTI format medical images; outputs segmentation masks in NIfTI format.
- **Installation**: `conda install -c bioconda deepmedic`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct NIfTI image format and proper preprocessing.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepmedic --model model.pkl --input image.nii.gz --output segmentation.nii.gz`
**Explanation:** Runs brain lesion segmentation on input MRI image.
