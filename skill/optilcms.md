---
name: optilcms
category: utility
description: OptiLCMS is a pipeline for processing LC-MS raw data with optimized parameters.
tags: [optilcms, utility, lc-ms, metabolomics]
author: oxo-call-community
source_url: "https://github.com/xia-lab/OptiLCMS"
---

## Concepts

- **Tool Overview**: OptiLCMS processes LC-MS data with optimized parameters.
- **Core Function**: Performs peak detection and quantification.
- **Algorithm**: Uses optimized signal processing algorithms.
- **Input Format**: Accepts mzML, mzXML, and raw LC-MS formats.
- **Output**: Produces peak tables and quantification results.
- **Use Case**: Metabolomics, LC-MS analysis, and biomarker discovery.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Tuning**: Requires proper parameter configuration.
- **Data Quality**: Results depend on input data quality.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `optilcms --help`
**Explanation:** Shows available options and usage instructions.

### Process LC-MS data
**Args:** `optilcms -i raw.mzML -o peaks.csv`
**Explanation:** Processes LC-MS raw data.

### With parameters
**Args:** `optilcms -i raw.mzML -p params.json -o peaks.csv`
**Explanation:** Uses custom parameters.

### Quality control
**Args:** `optilcms -i raw.mzML -q -o peaks.csv`
**Explanation:** Runs quality control checks.

### Batch processing
**Args:** `optilcms batch -d raw/ -o results/`
**Explanation:** Processes multiple LC-MS files.

### Verbose mode
**Args:** `optilcms -i raw.mzML -v -o peaks.csv`
**Explanation:** Runs with verbose output.

### Export format
**Args:** `optilcms -i raw.mzML -o peaks.txt --txt`
**Explanation:** Outputs in text format.