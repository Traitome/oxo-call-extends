---
name: tciaclient
category: utility
description: TCIA Client - Client tool for accessing The Cancer Imaging Archive (TCIA) programmatic API.
tags: [tciaclient, cancer-imaging, tcga, radiology, medical-imaging, api-client]
author: oxo-call-community
source_url: "https://github.com/kirbyju/TCIA_Client_Scripts"
---

## Concepts

- **Tool Overview**: tciaclient - Command-line client for accessing The Cancer Imaging Archive (TCIA) API to download medical imaging data.
- **Core Function**: Provides programmatic access to TCIA's collection of cancer imaging datasets, allowing automated download of DICOM images.
- **Input**: Collection name, patient ID, or query parameters specifying desired imaging data.
- **Output**: Downloads medical imaging data (DICOM files) to local storage.
- **Installation**: `pip install tciaclient` or download from GitHub
- **Use Case**: Researchers downloading radiology images for cancer imaging analytics, ML model training, or radiomics analysis.

## Pitfalls

- **API Access**: Requires TCIA account and API key for access.
- **Data Size**: Medical imaging datasets can be extremely large - ensure adequate storage.
- **Network**: Stable internet connection required for large downloads.
- **DICOM Format**: Downloads are DICOM files - requires DICOM viewers or converters for analysis.

## Examples

### List collections
**Args:** `tciaclient --key YOUR_API_KEY list-collections`
**Explanation:** Display all available TCIA collections/datasets.

### Get patient IDs
**Args:** `tciaclient --key YOUR_API_KEY get-patient-ids --collection "TCGA-BRCA"`
**Explanation:** List patient IDs for a specific TCIA collection.

### Download images
**Args:** `tciaclient --key YOUR_API_KEY download-images --patient-id TCGA-AR-A0AR --output-dir ./dicom/`
**Explanation:** Download all imaging studies for a specific patient.
