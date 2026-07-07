---
name: igblast-parser
category: utility
description: A parser for IgBLAST output files, converting results into structured CSV format for downstream analysis and visualization.
tags: [igblast-parser, utility, CSV, immunoglobulin, TCR]
author: oxo-call-community
source_url: "https://github.com/aerijman/igblast-parser"
---

## Concepts

- **Output Parsing**: Extracts key information from IgBLAST text output including V/D/J gene assignments and CDR regions.
- **Structured Formatting**: Converts unstructured text output into structured CSV format for easy analysis.
- **Batch Processing**: Handles multiple IgBLAST output files in a single run.
- **Annotation Extraction**: Extracts detailed annotations including identity scores, CDR sequences, and junction information.
- **Downstream Integration**: Produces output compatible with spreadsheet tools and bioinformatics pipelines.

## Pitfalls

- **Input Format**: Requires properly formatted IgBLAST output files; malformed output may cause parsing errors.
- **Output Compatibility**: CSV format may require additional processing for specialized analysis tools.
- **Gene Nomenclature**: Relies on consistent gene naming conventions from IgBLAST.
- **Missing Fields**: Some fields may be empty if IgBLAST couldn't identify certain gene segments.
- **Large Datasets**: May require memory optimization for very large output files.

## Examples

### Basic parsing
**Args:** `igblast-parser --input igblast_output.txt --output results.csv`
**Explanation:** Parses IgBLAST output and converts to CSV format.

### Batch processing
**Args:** `igblast-parser --input *.txt --output batch_results.csv`
**Explanation:** Processes multiple IgBLAST output files simultaneously.

### With custom fields
**Args:** `igblast-parser --input input.txt --output results.csv --fields V_gene,D_gene,J_gene,CDR3`
**Explanation:** Specifies which fields to include in the output CSV.

### Extract CDR sequences
**Args:** `igblast-parser --input igblast.txt --output cdrs.csv --extract-cdrs`
**Explanation:** Extracts only CDR region sequences for further analysis.

### Summary statistics
**Args:** `igblast-parser --input input.txt --output stats.csv --summary`
**Explanation:** Generates summary statistics for the IgBLAST results.