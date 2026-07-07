---
name: csvtk
category: utility
description: Cross-platform, efficient and practical CSV/TSV toolkit with 57 subcommands for data manipulation and visualization
tags: [csvtk, CSV, TSV, utility, data-manipulation, bioinformatics, format-conversion,表格处理]
author: oxo-call-community
source_url: "https://github.com/shenwei356/csvtk"
---

## Concepts

- **Tool Overview**: csvtk (v0.37.0) - A cross-platform, efficient, and practical CSV/TSV toolkit with 57 subcommands.
- **Core Function**: Provides convenient data manipulation for CSV/TSV files including viewing, cutting, filtering, sorting, joining, formatting, and plotting. Designed for rapid data investigation and easy integration into analysis pipelines.
- **Features**: Cross-platform (Linux/Windows/Mac), lightweight with no dependencies, fast with multi-CPU support, supports gzipped input/output, handles xz/zstd/bzip2/lz4 formats, supports fuzzy field selection and column name matching.
- **Input/Output**: CSV/TSV files, supports STDIN/pipe, gzip compression.
- **Application**: Bioinformatics data processing (OTU tables, metadata, annotation files), data science workflows, spreadsheet automation.
- **Installation**: `conda install -c bioconda csvtk` or download binaries from GitHub releases.

## Pitfalls

- **Header Required**: By default assumes input has header row; use `-H` flag for files without headers.
- **TSV Format**: By default handles CSV; use `-t` flag for tab-delimited files.
- **Column Names**: Column names should be unique; do not mix column numbers and names in the same operation.
- **Consistent Columns**: All lines must have same number of fields; use `-I/--ignore-illegal-row` to skip inconsistent rows.
- **Quote Handling**: If bare double quotes exist in fields, use `-l` flag or `csvtk fix-quotes` to fix.
- **Delimiter Detection**: Do not mix column numbers and names in the same `-f` argument.

## Examples

### View headers
**Args:** `csvtk headers -t data.tsv`
**Explanation:** Print column names of a tab-delimited file for inspection before further processing.

### Pretty print table
**Args:** `csvtk pretty data.csv`
**Explanation:** Convert CSV to readable format with proper alignment for console viewing.

### Select columns
**Args:** `csvtk cut -f 2,3,5 data.csv -o output.csv`
**Explanation:** Select specific columns by column numbers (2nd, 3rd, and 5th columns).

### Select columns by name with pattern
**Args:** `csvtk cut -F -f 'OE*' otu_table.csv -o output.csv`
**Explanation:** Use fuzzy matching with `-F` flag to select all columns starting with "OE" prefix.

### Filter rows by numeric value
**Args:** `csvtk filter -f "2-5>0" data.csv`
**Explanation:** Keep only rows where columns 2 through 5 all have values greater than 0.

### Search text in columns
**Args:** `csvtk grep -f Taxonomy -r -p "Bacteroidetes" data.csv`
**Explanation:** Find rows where the Taxonomy column contains "Bacteroidetes", using `-r` for regex matching.

### Transpose table
**Args:** `csvtk transpose data.csv -o transposed.csv`
**Explanation:** Swap rows and columns to facilitate different analysis workflows.

### Join multiple files
**Args:** `csvtk join -k 1 file1.csv file2.csv -o merged.csv`
**Explanation:** Join two CSV files on the first column (key column).

### Sort by multiple columns
**Args:** `csvtk sort -k col1:nr -k col2:n data.csv -o sorted.csv`
**Explanation:** Sort by col1 in descending numeric order, then by col2 in ascending numeric order.

### Convert CSV to Markdown
**Args:** `csvtk csv2md data.csv -o data.md`
**Explanation:** Convert CSV to Markdown table format for documentation or reporting.

### Statistical summary
**Args:** `csvtk stat data.csv`
**Explanation:** Display basic statistics including number of columns and rows in the file.

### Create new column with regex
**Args:** `csvtk mutate -p "(.+?)\." -n group data.csv -o with_group.csv`
**Explanation:** Create new "group" column by extracting text before the first period from existing column.

### Frequency count
**Args:** `csvtk freq -f species data.csv`
**Explanation:** Count occurrences of each unique value in the specified column.

### Random sample
**Args:** `csvtk sample -n 100 data.csv -o sampled.csv`
**Explanation:** Randomly select 100 rows from the file for quick inspection.
