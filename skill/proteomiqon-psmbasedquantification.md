---
name: proteomiqon-psmbasedquantification
category: expression
description: proteomiqon-psmbasedquantification performs label-free and labeled quantification using PSM data.
tags: [proteomiqon-psmbasedquantification, expression, proteomics, quantification]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/PSMBasedQuantification.html"
---

## Concepts

- **Tool Overview**: proteomiqon-psmbasedquantification quantifies proteins.
- **Core Function**: PSM-based quantification.
- **Algorithm**: Uses intensity-based methods.
- **Input Format**: Accepts PSM and MS data.
- **Output**: Produces quantification results.
- **Use Case**: Proteomics quantification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Label Consistency**: May affect quantification.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proteomiqon-psmbasedquantification --help`
**Explanation:** Shows available options and usage instructions.

### Quantify proteins
**Args:** `proteomiqon-psmbasedquantification -i psm_results.txt -m ms_data.mzML -o quant_results.txt`
**Explanation:** Performs PSM-based quantification.

### With parameters
**Args:** `proteomiqon-psmbasedquantification -i psm_results.txt -m ms_data.mzML --params params.yaml -o quant_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proteomiqon-psmbasedquantification -v -i psm_results.txt -m ms_data.mzML -o quant_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proteomiqon-psmbasedquantification -t 4 -i psm_results.txt -m ms_data.mzML -o quant_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proteomiqon-psmbasedquantification -i psm_results.txt -m ms_data.mzML -o quant_results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `proteomiqon-psmbasedquantification -i psm_results.txt -m ms_data.mzML -o quant_results.txt --report report.html`
**Explanation:** Generates HTML report.