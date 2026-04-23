---
name: bio2zarr
category: utility
description: Convert bioinformatics data to Zarr format
tags: [zarr, format-conversion, genomics-data]
author: oxo-call-community
source_url: "https://github.com/sgkit-dev/bio2zarr"
---

## Concepts
- **Tool Overview**: bio2zarr converts bioinformatics data formats (VCF, BCF, PLINK) to Zarr format for efficient cloud-native access and analysis.
- **Zarr Format**: Zarr is a cloud-optimized format for chunked, compressed, N-dimensional arrays. Ideal for large-scale genomic data in cloud environments.
- **Applications**: Large-scale population genomics, cloud-based analysis, efficient random access to variant data.
- **Integration**: Works with sgkit and other Python genomics libraries.

## Pitfalls
- **Storage**: Zarr format may use more disk space than compressed VCF/BCF.
- **Conversion Time**: Initial conversion can be time-consuming for large datasets.

## Examples
### Convert VCF to Zarr
**Args:** `bio2zarr vcf2zarr input.vcf output.zarr`
**Explanation:** Converts VCF file to Zarr format.

### Convert with specific fields
**Args:** `bio2zarr vcf2zarr input.vcf output.zarr --fields GT,DP,GQ`
**Explanation:** Converts only specified genotype fields to Zarr.
