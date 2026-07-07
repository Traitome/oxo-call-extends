---
name: sprinter
category: single-cell
description: SPRINTER - Single-cell Proliferation Rate Inference in Non-homogeneous Tumours
tags: [sprinter, single-cell, proliferation, tumor, evolution]
author: oxo-call-community
source_url: "https://github.com/zaccaria-lab/SPRINTER/blob/v1.0.0/README.md"
---

## Concepts

- **Tool Overview**: sprinter (v1.0.0) - A single-cell proliferation rate inference tool
- **Core Function**: Infers proliferation rates in non-homogeneous tumors through evolutionary routes
- **Input/Output**: Accepts single-cell data; outputs proliferation rate estimates
- **Algorithm**: Evolutionary route-based proliferation inference
- **Installation**: `conda install -c bioconda sprinter`
- **Key Features**: Proliferation inference, tumor heterogeneity, evolutionary analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted single-cell data
- **Data Quality**: Data quality affects proliferation inference accuracy
- **Tumor Heterogeneity**: Heterogeneity affects inference reliability
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Inference Accuracy**: Accuracy depends on data quality and evolutionary model

## Examples

### Display help
**Args:** `sprinter --help`
**Explanation:** Shows available options and usage information.

### Basic proliferation inference
**Args:** `sprinter -i single_cell_data.txt -o proliferation_rates.txt`
**Explanation:** Infer proliferation rates from single-cell data.

### With evolutionary model
**Args:** `sprinter -i single_cell_data.txt -e evolutionary_model.txt -o proliferation_rates.txt`
**Explanation:** Use specific evolutionary model.

### With clustering
**Args:** `sprinter -i single_cell_data.txt -o proliferation_rates.txt --cluster`
**Explanation:** Enable clustering for heterogeneous tumors.

### Multiple datasets
**Args:** `sprinter -i data1.txt data2.txt -o proliferation_rates.txt`
**Explanation:** Infer proliferation from multiple datasets.

### Output detailed results
**Args:** `sprinter -i single_cell_data.txt -o proliferation_rates.txt --detailed`
**Explanation:** Output detailed proliferation information.

### Output evolutionary routes
**Args:** `sprinter -i single_cell_data.txt -o proliferation_rates.txt --routes`
**Explanation:** Output evolutionary routes.

### Output statistics
**Args:** `sprinter -i single_cell_data.txt -o proliferation_rates.txt --stats`
**Explanation:** Output inference statistics.

### Generate report
**Args:** `sprinter -i single_cell_data.txt -o proliferation_rates.txt --report`
**Explanation:** Generate proliferation inference report.

### With threads
**Args:** `sprinter -i single_cell_data.txt -o proliferation_rates.txt -p 8`
**Explanation:** Use multiple threads for inference.