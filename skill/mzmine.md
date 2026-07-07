---
name: mzmine
category: utility
description: MZmine - Integrative analysis of mass spectrometry data
tags: [mzmine, utility, mass-spectrometry, metabolomics, lipidomics, lc-ms]
author: oxo-call-community
source_url: "https://github.com/mzmine/mzmine"
---

## Concepts

- **Tool Overview**: MZmine v4.7.29 is a comprehensive, open-source mass spectrometry data processing framework for metabolomics and lipidomics research. It provides modular tools for the entire LC-MS data processing pipeline.
- **Core Function**: Offers spectral preprocessing, feature detection, alignment, gap filling, compound identification, and statistical analysis for mass spectrometry data from various instruments and acquisition modes.
- **Modules**: Key processing modules include raw data filtering, peak detection, chromatogram building, alignment, gap filling, duplicate finding, isotope pattern filtering, and identification against databases.
- **Input Format**: Supports numerous raw MS data formats including mzML, mzXML, netCDF, and vendor-specific formats (Agilent, Waters, Thermo, SCIEX). Can also import processed peak lists.
- **Output**: Generates feature tables (CSV, Excel), identified compounds with annotations, spectral matches, and visualization outputs including chromatograms, spectra, and PCA plots.
- **Use Case**: Untargeted metabolomics, lipidomics, environmental metabolomics, food science, clinical metabolomics, and comparative MS studies.

## Pitfalls

- **Parameter Optimization**: Different instruments and sample types require different parameters. No universal settings work for all data.
- **Memory Usage**: Large LC-MS datasets can consume substantial memory. Process in batches or increase available RAM for large studies.
- **Peak Detection Thresholds**: Incorrect noise thresholds lead to either too many false positives or missed features. Manual validation recommended.
- **Alignment Artifacts**: Poor alignment across samples creates false differences. Visual inspection of alignment results is essential.
- **Database Matching**: Identification confidence depends on database completeness and search parameters. Always report identification criteria.
- **File Format Compatibility**: Some vendor formats require conversion to open formats (mzML) before processing.

## Examples

### Batch processing with parameters
**Args:** `-i raw_data/ -o processed/ -p parameters.xml`
**Explanation:** Runs MZmine in batch mode with predefined parameters. Processes all files in raw_data directory.

### Feature detection only
**Args:** `-i sample.mzML -o features.csv --detect`
**Explanation:** Runs only peak detection module and exports detected features.

### Export feature table
**Args:** `-i processed/*.csv -o combined.csv --merge`
**Explanation:** Combines multiple peak list files into a single feature table.

### Display help
**Args:** `--help`
**Explanation:** Shows command-line options and module information.

### GUI mode (interactive)
**Args:** `mzmine`
**Explanation:** Launches graphical user interface for interactive data processing and parameter optimization.
