---
name: blacksheep-outliers
category: expression
description: Differential extreme values analysis for omics data
tags: [blacksheep, outliers, differential, expression, extreme-values]
author: oxo-call-community
source_url: "https://github.com/ruggleslab/blackSheep/"
---

## Concepts

- **Tool Overview**: blackSheep performs differential extreme value analysis on omics data.
- **Core Function**: Identifies features with extreme values that differ between sample groups.
- **Input**: Feature matrix (expression, methylation, etc.) and sample annotations.
- **Output**: Features with significantly different extreme value distributions.
- **Application**: Finding outlier features in cancer vs normal comparisons.
- **Installation**: Install via bioconda: `conda install -c bioconda blacksheep-outliers`

## Pitfalls

- **Sample Groups**: Requires clear group annotations for differential analysis.
- **Missing Data**: Handle missing values before analysis.
- **Multiple Testing**: Apply appropriate correction for multiple comparisons.
- **Outlier Definition**: Adjust outlier fraction parameter based on analysis goals.

## Examples

### Run differential extreme analysis
**Args:** `blackSheep -i expression.tsv -a annotations.tsv -o results/`
**Explanation:** Identifies features with differential extreme values between groups.

### Set outlier fraction
**Args:** `blackSheep -i expression.tsv -a annotations.tsv -f 0.1 -o results/`
**Explanation:** Uses 10% as the extreme value fraction threshold.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
