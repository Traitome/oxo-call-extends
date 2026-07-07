---
name: imctools
category: formatting
description: An Image Mass Cytometry (IMC) file conversion tool that aims to convert IMC rawfiles (.mcd, .txt) into an intermediary ome.tiff, containing all the relevant metadata.
tags: [imctools, formatting, imaging, mass-cytometry]
author: oxo-call-community
source_url: "https://github.com/BodenmillerGroup/imctools/blob/master/README.md"
---

## Concepts

- **Tool Overview**: imctools (v2.1.8) - A Python library for converting and processing Imaging Mass Cytometry (IMC) raw data files
- **Core Function**: Converts IMC raw files (.mcd, .txt) to OME-TIFF format with complete metadata preservation
- **Input/Output**: Accepts .mcd or .txt raw files, outputs OME-TIFF files suitable for downstream analysis
- **Installation**: `conda install -c bioconda imctools` or `pip install imctools`
- **Key Features**: Metadata extraction, channel organization, compatibility with CellProfiler/Ilastik

## Pitfalls

- **File Compatibility**: Requires specific file formats from IMC instruments
- **Memory Usage**: Large IMC files may require significant memory
- **Metadata Integrity**: Incomplete metadata can cause conversion failures
- **Channel Naming**: Strict naming conventions required for proper channel identification
- **Output Formats**: Different downstream tools require different output formats

## Examples

### Convert MCD folder to OME-TIFF
**Args:** `imc-convert-mcd -i raw_data/ -o ome_tiffs/`
**Explanation:** Converts all .mcd files in input folder to OME-TIFF format.

### Extract metadata from MCD file
**Args:** `imc-extract-metadata -i sample.mcd -o metadata.csv`
**Explanation:** Extracts acquisition metadata from MCD file into CSV.

### Create analysis folder for Ilastik
**Args:** `imc-ome2analysis -i image.ome.tiff -o analysis_folder/ -p panel.csv`
**Explanation:** Converts OME-TIFF to analysis-ready format for Ilastik segmentation.

### Batch process multiple files
**Args:** `imc-batch-convert -i raw_data/ -o processed/ --format ome`
**Explanation:** Batch converts all IMC files in input directory.

### Export acquisition summary
**Args:** `imc-export-summary -i ome_tiffs/ -o summary.csv`
**Explanation:** Generates summary CSV with acquisition statistics.

### Convert to BigTIFF format
**Args:** `imc-convert-mcd -i raw.mcd -o output.ome.tiff --bigtiff`
**Explanation:** Outputs in BigTIFF format for large images.