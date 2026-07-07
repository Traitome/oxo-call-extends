---
name: skyline2isocor
category: formatting
description: Convert Skyline output to IsoCor input format for natural abundance isotope correction
tags: [skyline2isocor, formatting, metabolomics, isotope-correction]
author: oxo-call-community
source_url: "https://github.com/MetaboHUB-MetaToul-FluxoMet/Skyline2IsoCor"
---

## Concepts

- **Tool Overview**: skyline2isocor (v1.0.0) - A converter tool for preparing Skyline output for IsoCor software
- **Core Function**: Transforms Skyline quantification data into IsoCor-compatible format for isotope correction
- **Input/Output**: Accepts Skyline CSV output; outputs IsoCor-ready CSV files
- **Installation**: `pip install skyline2isocor` or `conda install -c bioconda skyline2isocor`
- **Key Features**: Handles metabolite name mapping; supports various Skyline output formats
- **Use Case**: Metabolomics research requiring accurate isotope abundance correction

## Pitfalls

- **Input Format**: Requires specific Skyline output format with correct column headers
- **Metabolite Names**: Ensure consistent metabolite naming between Skyline and IsoCor
- **Column Mapping**: Verify column mapping for correct data transformation
- **Version Compatibility**: Check compatibility with specific Skyline and IsoCor versions
- **Data Integrity**: Missing or malformed data can cause conversion errors
- **Output Validation**: Always validate output before using in IsoCor

## Examples

### Display help
**Args:** `skyline2isocor --help`
**Explanation:** Shows available options and usage information.

### Basic conversion
**Args:** `skyline2isocor -i skyline_output.csv -o isocor_input.csv`
**Explanation:** Convert Skyline output to IsoCor input format.

### With custom mappings
**Args:** `skyline2isocor -i skyline_output.csv -o isocor_input.csv -m mappings.csv`
**Explanation:** Use custom metabolite name mappings.

### Specify columns
**Args:** `skyline2isocor -i skyline_output.csv -o isocor_input.csv --name-col Name --area-col Area`
**Explanation:** Specify column names for metabolite name and area.

### Filter by confidence
**Args:** `skyline2isocor -i skyline_output.csv -o isocor_input.csv -c 0.95`
**Explanation:** Filter results by confidence score threshold.

### Batch processing
**Args:** `skyline2isocor -d skyline_files/ -o isocor_files/`
**Explanation:** Process multiple Skyline output files in batch.

### Generate report
**Args:** `skyline2isocor -i skyline_output.csv -o isocor_input.csv --report report.txt`
**Explanation:** Generate conversion report with statistics.