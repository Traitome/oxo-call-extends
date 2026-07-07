---
name: metilene
category: expression
description: Fast and sensitive detection of differential DNA methylation.
tags: [metilene, expression, methylation]
author: oxo-call-community
source_url: "http://www.bioinf.uni-leipzig.de/Software/metilene"
---

## Concepts

- **Tool Overview**: Metilene v0.2.9 is a fast and sensitive tool for detecting differential DNA methylation.
- **Core Function**: Detects differentially methylated regions between samples.
- **Speed Optimization**: Optimized for fast analysis of large datasets.
- **Sensitivity**: Highly sensitive detection of methylation differences.
- **Input/Output**: Accepts methylation data; outputs differentially methylated regions.
- **Statistical Analysis**: Uses statistical methods to identify significant differences.

## Pitfalls

- **Data Requirements**: Requires properly formatted methylation data.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal sensitivity.
- **Data Quality**: Analysis quality depends on input data quality.
- **False Positives**: May produce false positive results if parameters are not tuned properly.

## Examples

### Detect differential methylation
**Args:** `metilene -i sample1.txt sample2.txt -o diff.txt`
**Explanation:** Detects differentially methylated regions between samples.

### With custom threshold
**Args:** `metilene -i sample1.txt sample2.txt -o diff.txt -t 0.05`
**Explanation:** Uses significance threshold of 0.05.

### Multiple comparisons
**Args:** `metilene -i sample1.txt sample2.txt sample3.txt -o diff.txt`
**Explanation:** Compares methylation across multiple samples.

### Generate report
**Args:** `metilene -i sample1.txt sample2.txt -o diff.txt -r report.html`
**Explanation:** Generates HTML report of results.

### Batch processing
**Args:** `metilene -i data/ -o results/`
**Explanation:** Processes multiple sample pairs in batch mode.