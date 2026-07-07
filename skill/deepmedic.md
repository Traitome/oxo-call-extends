---
name: deepmedic
category: annotation
description: DeepMedic - efficient multi-scale 3D CNN for brain lesion segmentation.
tags: [deepmedic, annotation, deep-learning, segmentation, medical-imaging]
author: oxo-call-community
source_url: "https://github.com/Kamnitsask/deepmedic"
---

## Concepts

- **Tool Overview**: deepmedic (v0.6.1+) is an efficient multi-scale 3D convolutional neural network for brain lesion segmentation from medical images. It provides accurate segmentation of various brain lesions.
- **Core Function**: Segments brain lesions from MRI scans using a dual-pathway 3D convolutional neural network that captures both local and global context.
- **Input/Output**: Input: NIfTI format medical images (T1, T2, FLAIR sequences). Output: Segmentation masks in NIfTI format, lesion volume statistics.
- **Algorithm**: Uses a dual-pathway architecture with multi-scale context aggregation for robust lesion detection and segmentation.
- **Key Features**: Multi-scale analysis, dual-pathway design, high accuracy, supports multiple MRI modalities, GPU acceleration.
- **Installation**: `conda install -c bioconda deepmedic`

## Pitfalls

- **Input Format**: Requires correct NIfTI format with proper preprocessing.
- **Image Quality**: Poor image quality affects segmentation accuracy.
- **GPU Resources**: Requires GPU for efficient inference.
- **Model Size**: Large models may require significant memory.
- **Training Data**: Performance depends on training dataset diversity.

## Examples

### Run brain lesion segmentation
**Args:** `deepmedic --model model.pkl --input image.nii.gz --output segmentation.nii.gz`
**Explanation:** Runs brain lesion segmentation on input MRI image.

### With multiple modalities
**Args:** `deepmedic --model model.pkl --input t1.nii.gz t2.nii.gz flair.nii.gz --output segmentation.nii.gz`
**Explanation:** Use multiple MRI modalities for improved segmentation.

### Evaluate model
**Args:** `deepmedic --evaluate --model model.pkl --input test_images/ --output metrics.txt`
**Explanation:** Evaluate model performance on test dataset.