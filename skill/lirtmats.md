---
name: lirtmats
category: proteomics
description: LiRTMaTS - Liverpool retention time matching software for mass spectrometry
tags: [lirtmats, proteomics, mass-spectrometry, retention-time, matching, bioinformatics]
author: oxo-call-community
source_url: "https://pypi.org/project/lirtmats/"
---

## Concepts

- **Retention Time Matching**: Matches retention times across mass spectrometry runs
- **Mass Spectrometry**: Analysis of mass spectrometry data
- **Peptide Identification**: Identifies peptides based on retention time
- **Chromatography Alignment**: Aligns chromatographic runs
- **Normalization**: Normalizes retention time data
- **Quality Control**: Quality control for mass spectrometry experiments

## Pitfalls

- **Retention Time Drift**: Chromatographic drift affects matching
- **Peptide Quality**: Poor quality peptides affect matching accuracy
- **Instrument Variation**: Different instruments may produce different results
- **Parameter Tuning**: Requires careful parameter optimization
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets

## Examples

### Match retention times
**Args:** `lirtmats -i runs.txt -o matches.txt`
**Explanation:** Matches retention times across multiple runs.

### Align runs
**Args:** `lirtmats -i runs.txt -o aligned.txt -a`
**Explanation:** Aligns chromatographic runs.

### Normalize data
**Args:** `lirtmats -i runs.txt -o normalized.txt -n`
**Explanation:** Normalizes retention time data.

### Quality control
**Args:** `lirtmats -i runs.txt -o qc_report.txt -q`
**Explanation:** Generates quality control report.

### Threads
**Args:** `lirtmats -i runs.txt -o matches.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output statistics
**Args:** `lirtmats -i runs.txt -o stats.txt -s`
**Explanation:** Outputs matching statistics.