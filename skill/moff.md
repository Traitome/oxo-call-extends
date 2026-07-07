---
name: moff
category: utility
description: moFF extracts apex MS1 intensity using identified MS2 peptides.
tags: [moff, utility, proteomics]
author: oxo-call-community
source_url: "https://github.com/compomics/moFF"
---

## Concepts

- **Tool Overview**: moFF v2.0.3 extracts apex MS1 intensity from proteomics data.
- **Core Function**: Extracts peak intensity from mass spectrometry data.
- **MS1 Extraction**: Uses identified MS2 peptides to extract MS1 intensities.
- **Label-free Quantification**: Supports label-free protein quantification.
- **Input/Output**: Accepts MS data; outputs quantified proteins.
- **Proteomics**: Supports mass spectrometry-based proteomics workflows.

## Pitfalls

- **MS Data Required**: Requires mass spectrometry data.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for optimal extraction.
- **Data Quality**: Results depend on MS data quality.
- **Peptide Identification**: Requires MS2 peptide identifications.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Extract MS1 intensity
**Args:** `moff -i ms_data.mzML -p peptides.txt -o intensities.txt`
**Explanation:** Extracts apex MS1 intensities.

### With calibration
**Args:** `moff -i ms_data.mzML -p peptides.txt -c -o intensities.txt`
**Explanation:** Applies intensity calibration.

### Verbose output
**Args:** `moff -i ms_data.mzML -p peptides.txt -v -o intensities.txt`
**Explanation:** Shows detailed extraction process.

### Batch processing
**Args:** `moff -i mzML/ -p peptides.txt -o results/`
**Explanation:** Processes multiple MS files.

### Generate report
**Args:** `moff -i ms_data.mzML -p peptides.txt -r report.html -o intensities.txt`
**Explanation:** Generates analysis report.