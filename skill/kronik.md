---
name: kronik
category: proteomics
description: Processing Hardklor features for peptide candidate identification by chromatographic profiling
tags: [kronik, proteomics, mass-spectrometry, peptide, chromatographic-profiling]
author: oxo-call-community
source_url: "https://github.com/mhoopmann/kronik"
---

## Concepts

- **Chromatographic Profiling**: Processes chromatographic data for peptide detection
- **Hardklor Integration**: Works with Hardklor feature detection output
- **Peptide Candidates**: Identifies candidate peptides from features
- **Mass Spectrometry**: Designed for LC-MS/MS proteomics data
- **Feature Processing**: Processes spectral features for analysis
- **Candidate Filtering**: Filters and ranks peptide candidates

## Pitfalls

- **Hardklor Dependency**: Requires Hardklor output as input
- **Feature Quality**: Poor quality features affect identification
- **Parameter Tuning**: Parameters need optimization for different data
- **False Positives**: May produce false positive candidates
- **Threshold Selection**: Cutoff values affect result quality
- **Data Format**: Requires correct input format compatibility

## Examples

### Process Hardklor features
**Args:** `kronik -i features.txt -o candidates.txt`
**Explanation:** Processes Hardklor features to find peptide candidates.

### Specify confidence
**Args:** `kronik -i features.txt -c 0.95 -o high_conf.txt`
**Explanation:** Only reports candidates with 95% confidence.

### Filter by intensity
**Args:** `kronik -i features.txt --min-intensity 10000 -o filtered.txt`
**Explanation:** Filters candidates by minimum intensity.

### Generate report
**Args:** `kronik -i features.txt -o results.txt --report`
**Explanation:** Creates detailed candidate report.

### Batch processing
**Args:** `kronik batch -d features/ -o results/`
**Explanation:** Processes multiple feature files.

### Export to CSV
**Args:** `kronik -i features.txt -o candidates.csv --csv`
**Explanation:** Exports results in CSV format.