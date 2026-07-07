---
name: proteomiqon-alignmentbasedquantification
category: alignment
description: proteomiqon-alignmentbasedquantification performs XIC extraction and quantification from MS runs.
tags: [proteomiqon-alignmentbasedquantification, alignment, proteomics, quantification]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/AlignmentBasedQuantification.html"
---

## Concepts

- **Tool Overview**: proteomiqon-alignmentbasedquantification quantifies peptides.
- **Core Function**: Alignment-based quantification.
- **Algorithm**: Uses XIC extraction methods.
- **Input Format**: Accepts mzML/mzLite files.
- **Output**: Produces quantification results.
- **Use Case**: Proteomics quantification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Peptide Alignment**: Affects quantification.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proteomiqon-alignmentbasedquantification --help`
**Explanation:** Shows available options and usage instructions.

### Quantify peptides
**Args:** `proteomiqon-alignmentbasedquantification -i ms_data.mzML -p peptides.txt -o quant_results.txt`
**Explanation:** Performs alignment-based quantification.

### With parameters
**Args:** `proteomiqon-alignmentbasedquantification -i ms_data.mzML -p peptides.txt --params params.yaml -o quant_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proteomiqon-alignmentbasedquantification -v -i ms_data.mzML -p peptides.txt -o quant_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proteomiqon-alignmentbasedquantification -t 4 -i ms_data.mzML -p peptides.txt -o quant_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proteomiqon-alignmentbasedquantification -i ms_data.mzML -p peptides.txt -o quant_results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `proteomiqon-alignmentbasedquantification -i ms_data.mzML -p peptides.txt -o quant_results.txt --report report.html`
**Explanation:** Generates HTML report.