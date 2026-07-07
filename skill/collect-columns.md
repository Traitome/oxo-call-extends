---
name: collect-columns
category: utility
description: Retrieve columns from multiple tables into a single output table
tags: [collect-columns, data-processing, table-manipulation, bioinformatics, utility]
author: oxo-call-community
source_url: "https://github.com/biowdl/collect-columns"
---

## Concepts

- **Tool Overview**: collect-columns is a utility tool for extracting specific columns from multiple table files and combining them into a single output table.
- **Core Function**: Merges selected columns from multiple input tables into one consolidated table, maintaining row correspondence.
- **Algorithm**: Processes tabular data files, extracting specified columns and joining them based on row indices or key columns.
- **Input**: Multiple table files (TSV, CSV) with column specifications.
- **Output**: Combined table with extracted columns from all input files.
- **Application**: Data integration, comparative analysis, and report generation.
- **Installation**: Install via bioconda: `conda install -c bioconda collect-columns`

## Pitfalls

- **Row Alignment**: Requires consistent row ordering across input files.
- **Column Indices**: Column numbering may be 0-based or 1-based depending on implementation.
- **Delimiter Consistency**: All input files should use the same delimiter.
- **Header Handling**: May require consistent header treatment across files.
- **Missing Data**: Missing values in input files may cause alignment issues.

## Examples

### Collect columns from multiple files
**Args:** `collect-columns -i file1.tsv file2.tsv file3.tsv -c 2 -o combined.tsv`
**Explanation:** Extracts column 2 from each file and combines into single output.

### With custom delimiter
**Args:** `collect-columns -i *.csv -d comma -c 1,3 -o output.tsv`
**Explanation:** Processes CSV files, extracting columns 1 and 3.

### With header preservation
**Args:** `collect-columns -i file1.tsv file2.tsv -c 2 --header -o combined.tsv`
**Explanation:** Preserves header row in combined output.

### Display help
**Args:** `collect-columns --help`
**Explanation:** Shows all available options and usage information.