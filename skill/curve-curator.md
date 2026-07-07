---
name: curve-curator
category: utility
description: CurveCurator - analysis platform for dose-dependent data with 4-parameter curve fitting
tags: [curve-curator, utility, dose-response, curve-fitting, high-throughput]
author: oxo-call-community
source_url: "https://github.com/kusterlab/curve_curator"
---

## Concepts

- **Tool Overview**: curve-curator (v0.6.0+) is an open-source analysis platform for dose-dependent data, performing 4-parameter curve fitting to estimate potency and effect size.
- **Core Function**: Fits classical 4-parameter logistic equations to dose-response data, providing statistical significance measures and automated hit selection.
- **Input/Output**: Input: CSV/TSV files with dose and response values. Output: Fitted parameters, significance scores, interactive dashboard.
- **Key Features**: 2D-thresholding for false positive reduction, interactive visualization dashboard, automated hit selection.
- **Installation**: `conda install -c bioconda curve-curator`

## Pitfalls

- **Data Format**: Requires specific column naming for dose and response variables.
- **Convergence**: Some datasets may require parameter tuning for curve fitting convergence.
- **Baseline Correction**: Ensure proper baseline subtraction before analysis.
- **High-Throughput**: Large datasets may require batch processing.
- **Interpretation**: IC50/EC50 values should be validated with appropriate controls.

## Examples

### Analyze dose-response data
**Args:** `curve-curator -i dose_response.csv -o results/`
**Explanation:** Perform curve fitting on dose-response data and generate analysis reports.

### Run with 2D-thresholding
**Args:** `curve-curator -i data.csv -o results/ --threshold`
**Explanation:** Apply 2D-thresholding to reduce false positives in high-throughput data.

### Launch interactive dashboard
**Args:** `curve-curator -i data.csv --dashboard`
**Explanation:** Launch interactive dashboard for data exploration.
