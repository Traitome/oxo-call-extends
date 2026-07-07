---
name: mgf-formatter
category: epigenomics
description: Tools for converting peak lists into MGF files formatted for particular downstream applications
tags: [mgf-formatter, epigenomics, mass-spectrometry]
author: oxo-call-community
source_url: "https://bitbucket.org/galaxyp-applications/mgf-formatter"
---

## Concepts

- **Tool Overview**: mgf-formatter v1.0.0 converts peak lists into MGF (Mascot Generic Format) files.
- **Core Function**: Formats peak lists into MGF format for mass spectrometry analysis.
- **MGF Format**: Standard format for mass spectrometry data.
- **Peak List Conversion**: Converts various peak list formats to MGF.
- **Input/Output**: Accepts peak lists; outputs MGF files.
- **Downstream Compatibility**: Prepares data for downstream analysis tools.

## Pitfalls

- **Format Requirements**: Requires specific input format.
- **Data Quality**: Output quality depends on input peak list quality.
- **Parameter Tuning**: May require parameter adjustment for specific tools.
- **File Size**: Large peak lists may require significant memory.
- **Format Compatibility**: May not support all peak list formats.
- **Runtime**: Processing large files can be time-consuming.

## Examples

### Convert peak list to MGF
**Args:** `mgf-formatter -i peaks.txt -o output.mgf`
**Explanation:** Converts peak list to MGF format.

### With custom parameters
**Args:** `mgf-formatter -i peaks.txt -o output.mgf -p params.conf`
**Explanation:** Uses custom formatting parameters.

### Batch conversion
**Args:** `mgf-formatter -i peaks/ -o mgf/`
**Explanation:** Converts multiple peak lists in batch mode.

### Filter peaks
**Args:** `mgf-formatter -i peaks.txt -o output.mgf -f 100`
**Explanation:** Filters peaks by intensity threshold.

### Merge MGF files
**Args:** `mgf-formatter merge -i mgf/ -o merged.mgf`
**Explanation:** Merges multiple MGF files.