---
name: msalign2
category: alignment
description: Align CE-MS or LC-MS datasets using accurate mass information.
tags: [msalign2, alignment, mass-spectrometry]
author: oxo-call-community
source_url: "http://www.ms-utils.org/msalign2/index.html"
---

## Concepts

- **Tool Overview**: MSAlign2 v1.0 aligns mass spectrometry datasets.
- **Core Function**: Performs retention time alignment for MS data.
- **CE-MS Support**: Supports Capillary Electrophoresis MS data.
- **LC-MS Support**: Supports Liquid Chromatography MS data.
- **Accurate Mass**: Uses accurate mass information for alignment.
- **Input/Output**: Accepts MS files; outputs aligned datasets.

## Pitfalls

- **MS Data Specific**: Designed for mass spectrometry data.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for alignment.
- **Data Quality**: Results depend on MS data quality.
- **Format Support**: Limited to specific MS file formats.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Align two datasets
**Args:** `msalign2 -i dataset1.csv dataset2.csv -o aligned.csv`
**Explanation:** Aligns two MS datasets.

### With CE-MS data
**Args:** `msalign2 -i ce_ms_data.csv -o aligned.csv`
**Explanation:** Processes CE-MS data.

### Specify alignment parameters
**Args:** `msalign2 -i dataset1.csv dataset2.csv -p params.txt -o aligned.csv`
**Explanation:** Uses custom alignment parameters.

### Generate alignment report
**Args:** `msalign2 -i dataset1.csv dataset2.csv -r report.txt -o aligned.csv`
**Explanation:** Generates detailed alignment report.

### Batch processing
**Args:** `msalign2 -i csv/ -o results/`
**Explanation:** Processes multiple dataset files.