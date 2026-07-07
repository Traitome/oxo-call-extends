---
name: psm-utils
category: utility
description: psm-utils provides utilities for parsing and handling peptide-spectrum matches (PSM) and search engine results.
tags: [psm-utils, utility, mass-spectrometry, PSM-processing]
author: oxo-call-community
source_url: "https://psm_utils.readthedocs.io"
---

## Concepts

- **Tool Overview**: psm-utils handles PSM data.
- **Core Function**: PSM parsing and processing.
- **Algorithm**: Uses standardized parsing.
- **Input Format**: Accepts various search engine outputs.
- **Output**: Produces processed PSM data.
- **Use Case**: Proteomics data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Format Compatibility**: May have issues with some formats.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psm-utils --help`
**Explanation:** Shows available options and usage instructions.

### Parse PSM
**Args:** `psm-utils parse -i search_results.txt -o psm.json`
**Explanation:** Parses search engine results.

### With parameters
**Args:** `psm-utils parse -i search_results.txt -p params.yaml -o psm.json`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psm-utils -v parse -i search_results.txt -o psm.json`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psm-utils -t 4 parse -i search_results.txt -o psm.json`
**Explanation:** Uses 4 threads for parallel processing.

### Convert format
**Args:** `psm-utils convert -i psm.mzid -o psm.csv`
**Explanation:** Converts between PSM formats.

### Generate report
**Args:** `psm-utils parse -i search_results.txt -o psm.json --report report.html`
**Explanation:** Generates HTML report.