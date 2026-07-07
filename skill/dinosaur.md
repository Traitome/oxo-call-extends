---
name: dinosaur
category: annotation
description: Dinosaur - Peptide feature detection for mass spectrometry data.
tags: [dinosaur, annotation, proteomics, ms, feature-detection]
author: oxo-call-community
source_url: "https://github.com/ficklscherer/dinosaur"
---

## Concepts

- **Tool Overview**: Dinosaur is a peptide feature detection tool for mass spectrometry proteomics data.
- **Core Function**: Detects and quantifies peptide features (chromatographic peaks) from LC-MS data.
- **Input/Output**: Input: mzML mass spectrometry files. Output: Detected features with retention time, m/z, and intensity.
- **Algorithm**: Uses peak detection and clustering algorithms to identify peptide features.
- **Key Features**: Feature detection, retention time alignment, intensity quantification, noise filtering, batch processing.
- **Installation**: `conda install -c bioconda dinosaur`

## Pitfalls

- **Input Requirements**: Requires mzML format mass spectrometry data.
- **Data Quality**: Poor quality MS data affects feature detection accuracy.
- **Retention Time**: Requires proper retention time alignment for accurate matching.
- **Noise Level**: High noise can produce false positive features.
- **Computational Time**: May be slow for large MS datasets.

## Examples

### Detect peptide features
**Args:** `dinosaur --input sample.mzML --output features.tsv`
**Explanation:** Detects peptide features from LC-MS data.

### With retention time alignment
**Args:** `dinosaur --input sample.mzML --output features.tsv --align-rt`
**Explanation:** Perform retention time alignment during feature detection.

### Filter by intensity
**Args:** `dinosaur --input sample.mzML --output features.tsv --min-intensity 1000`
**Explanation:** Filter features by minimum intensity threshold.

### Batch processing
**Args:** `dinosaur --input-dir mzml_files/ --output-dir features/`
**Explanation:** Process multiple mass spectrometry files in batch.

### Generate visualization
**Args:** `dinosaur --input sample.mzML --output features.tsv --plot features.png`
**Explanation:** Generate visualization of detected features.