---
name: blksheep
category: expression
description: Differential extreme values analysis package
tags: [blksheep, outliers, differential, expression]
author: oxo-call-community
source_url: "https://github.com/ruggleslab/blackSheep"
---

## Concepts

- **Tool Overview**: blksheep is the Python package for differential extreme values analysis.
- **Core Function**: Identifies features with significantly different extreme value distributions between groups.
- **Input**: Feature matrix and sample group annotations.
- **Output**: Ranked list of features with differential extreme values.
- **Related**: Same functionality as blacksheep-outliers in different package format.
- **Installation**: Install via bioconda: `conda install -c bioconda blksheep`

## Pitfalls

- **Package Overlap**: blksheep and blacksheep-outliers provide similar functionality.
- **Data Format**: Ensure feature matrix and annotations use compatible formats.
- **Group Size**: Small groups may have limited statistical power.

## Examples

### Run analysis
**Args:** `blksheep -i features.tsv -a groups.tsv -o results/`
**Explanation:** Performs differential extreme values analysis on feature matrix.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
