---
name: tabview
category: visualization
description: Curses-based command-line CSV and tabular data viewer.
tags: [tabview, csv-viewer, command-line, visualization]
author: oxo-call-community
source_url: "https://github.com/firecat53/tabview"
---

## Concepts

- **Tool Overview**: tabview (v1.4.3) is a curses-based CSV and tabular data viewer.
- **Core Function**: View and navigate tabular data in terminal.
- **Algorithm**: Uses curses library for terminal-based GUI.
- **Input/Output**: Input: CSV/Tab-delimited files; Output: Terminal display.
- **Applications**: Data inspection, quick CSV viewing, terminal-based data exploration.
- **Installation**: `conda install -c bioconda tabview` or pip install.

## Pitfalls

- **Terminal Requirements**: Requires terminal with curses support.
- **Display Size**: Limited by terminal dimensions.
- **File Size**: Very large files may be slow to load.
- **Memory Requirements**: Large datasets require significant memory.
- **Encoding**: May have issues with non-UTF-8 encodings.
- **Mouse Support**: Mouse support varies by terminal.

## Examples

### Display help
**Args:** `tabview --help`
**Explanation:** Shows available options and usage information.

### View CSV file
**Args:** `tabview data.csv`
**Explanation:** Open CSV file in interactive viewer.

### View with header
**Args:** `tabview -h data.csv`
**Explanation:** Treat first row as header.

### Verbose mode
**Args:** `tabview -v data.csv`
**Explanation:** Run with detailed logging.

### Sort by column
**Args:** `tabview -s 2 data.csv`
**Explanation:** Sort by second column.

### Filter rows
**Args:** `tabview -f "pattern" data.csv`
**Explanation:** Filter rows matching pattern.

### Export to file
**Args:** `tabview -o filtered.csv data.csv`
**Explanation:** Export viewed data to file.

### Read from stdin
**Args:** `cat data.csv | tabview`
**Explanation:** View data piped from stdin.

### Column statistics
**Args:** `tabview -c data.csv`
**Explanation:** Show column statistics.
