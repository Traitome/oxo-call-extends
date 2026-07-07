---
name: nii2dcm
category: imaging
description: nii2dcm converts NIfTI files to DICOM format using Python.
tags: [nii2dcm, imaging, nifti, dicom]
author: oxo-call-community
source_url: "https://github.com/tomaroberts/nii2dcm"
---

## Concepts

- **Tool Overview**: nii2dcm converts medical imaging data from NIfTI to DICOM format.
- **Core Function**: Transforms volumetric imaging data between formats.
- **Algorithm**: Handles NIfTI header parsing and DICOM metadata generation.
- **Input Format**: Accepts NIfTI files (.nii or .nii.gz).
- **Output**: Produces DICOM files.
- **Use Case**: Medical imaging processing, data conversion, and archive preparation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **File Compatibility**: Requires valid NIfTI files.
- **Metadata**: Requires proper DICOM metadata configuration.
- **Memory Usage**: Large images require memory.
- **Dependency**: Requires Python and related libraries.
- **Output Size**: DICOM files can be large.

## Examples

### Display help
**Args:** `nii2dcm --help`
**Explanation:** Shows available options and usage instructions.

### Basic conversion
**Args:** `nii2dcm -i input.nii -o output/`
**Explanation:** Converts NIfTI to DICOM series.

### With metadata
**Args:** `nii2dcm -i input.nii -o output/ -m metadata.json`
**Explanation:** Uses custom metadata for DICOM files.

### Compressed input
**Args:** `nii2dcm -i input.nii.gz -o output/`
**Explanation:** Handles gzipped NIfTI files.

### Series description
**Args:** `nii2dcm -i input.nii -o output/ -d "MRI Brain"`
**Explanation:** Sets DICOM series description.

### Patient info
**Args:** `nii2dcm -i input.nii -o output/ -p "John Doe"`
**Explanation:** Sets patient name in DICOM metadata.

### Verbose mode
**Args:** `nii2dcm -i input.nii -o output/ -v`
**Explanation:** Runs with verbose output.