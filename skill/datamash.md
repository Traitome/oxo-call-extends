---
name: datamash
category: utility
description: GNU command-line tool performing numeric/text operations (sum, mean, stdev, groupby, crosstab, transpose) on tabular input
tags: [datamash, utility, statistics, text-processing, command-line]
author: oxo-call-community
source_url: "https://www.gnu.org/software/datamash/"
---

## Concepts

- **Tool Overview**: GNU Datamash is a command-line program performing calculations (sum, count, min, max, mean, stdev, skewness) on textual input files.
- **Core Function**: Reads input from stdin and performs one or more operations per group or on the entire input file, with rich statistical, numeric, and textual operations.
- **Primary Operations**: groupby, crosstab, transpose, reverse, check (structure validation).
- **Statistical Operations**: mean, median, q1, q3, iqr, perc, pstdev, sstdev, pvar, svar, mad, sskew, pskew, skurt, pkurt, jarque, dpo, scov, pcov, spearson, ppearson.
- **Input Format**: Tab-separated text by default; delimiter configurable via `-t`/`--field-separator` or whitespace via `-W`.
- **Grouping**: Group input by one or more fields using `-g X[,Y,Z]`; auto-sort with `-s`/`--sort`.
- **Headers**: Support input/output header lines via `--header-in`/`--header-out` or `-H` (both).
- **Installation**: `conda install -c bioconda datamash` or system package manager.

## Pitfalls

- **Input Must Be Sorted**: When using `--group`, input must be sorted by the grouping fields; otherwise use `--sort`/`-s`.
- **Locale Affects Decimals**: `LC_NUMERIC` locale determines the decimal-point character and thousands separator.
- **Strict Field Counts**: By default, transpose/reverse fail if lines have varying field counts; use `--no-strict` with `--filler` to handle.
- **Header Handling**: `--header-in` assumes the first input line is headers; forgetting it shifts results by one row.
- **NA/NaN Values**: Use `--narm` to skip NA/NaN values; otherwise they may corrupt numeric operations.
- **Output Formatting**: Use `--format` for printf-style floating point and `-R`/`--round` for fixed decimal places.

## Examples

### Sum values in first column
**Args:** `seq 10 | datamash sum 1`
**Explanation:** Pipes numbers 1-10 into datamash, which sums the first (only) field, producing 55.

### Group statistics with headers
**Args:** `datamash -H -g 2 count 3 mean 3 sstdev 3 < scores_h.txt`
**Explanation:** Groups by column 2 (Major) using input/output headers, counting records and computing mean and sample stdev of column 3 (Score).

### Sort then group
**Args:** `datamash --sort --group 1 sum 1 < input.tsv`
**Explanation:** Auto-sorts input by field 1 before grouping, equivalent to `sort -k1,1 | datamash -g 1 sum 1`.

### Cross-tabulation (pivot table)
**Args:** `datamash crosstab 2,3 < data.txt`
**Explanation:** Generates a pivot table counting occurrences of each combination of fields 2 and 3.

### Transpose rows and columns
**Args:** `datamash transpose < matrix.txt`
**Explanation:** Swaps rows and columns; fails on ragged input unless `--no-strict` is supplied.

### Descriptive statistics summary
**Args:** `datamash -H mean 1 q1 1 median 1 q3 1 iqr 1 sstdev 1 jarque 1 < file.txt`
**Explanation:** Computes mean, quartiles, IQR, sample stdev, and Jarque-Bera normality p-value for column 1.

### Use comma as field separator
**Args:** `datamash -t, -g 1 sum 2 < data.csv`
**Explanation:** Treats comma as field separator (basic CSV) and sums field 2 per group in field 1.
