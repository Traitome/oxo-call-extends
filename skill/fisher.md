---
name: fisher
category: utility
description: "Fisher is a fast Python implementation of Fisher's Exact Test for 2x2 contingency tables, designed for genetic association studies and bioinformatics applications requiring rapid statistical testing of categorical data."
tags: [fisher, utility, statistics, fisher-exact-test, genetics, association, p-value, bioinformatics, contingency-table]
author: oxo-call-community
source_url: "https://github.com/brentp/fishers_exact_test"
---

## Concepts
- **Tool Overview**: Fisher is a high-performance Python implementation of Fisher's Exact Test for 2x2 contingency tables. It provides fast, memory-efficient exact p-value calculations for testing independence in categorical data.
- **Core Function**: Computes the exact probability of observing a particular contingency table configuration under the null hypothesis of independence using the hypergeometric distribution, returning precise p-values without large-sample approximations.
- **Statistical Foundation**: Fisher's Exact Test calculates the probability of the observed table and all more extreme tables. For a 2x2 table with values [a, b] / [c, d], the probability is: P = (a+b)!(c+d)!(a+c)!(b+d)! / (n!a!b!c!d!)
- **Input Methods**: Accepts command-line arguments (4 integers representing the 2x2 table cells), stdin input with tab/comma-separated values, or CSV file input. Supports both one-tailed and two-tailed test variants.
- **Output**: Returns odds ratio, p-value (two-tailed by default), and optionally confidence intervals. JSON output format available for programmatic parsing.
- **Comparison to Chi-squared**: Unlike chi-squared test which uses asymptotic approximations, Fisher's exact test provides accurate p-values for small sample sizes where expected cell frequencies are < 5.
- **Installation**: `conda install -c bioconda fisher` or `pip install fisher`. Requires Python 2.7+ or 3.x.

## Pitfalls
- **Sample Size Limitations**: Computational time increases exponentially with sample size. For very large samples (n > 1000 per cell), consider scipy.stats.fisher_exact or chi-squared approximation.
- **Test Direction**: Default is two-tailed test. Use `--one-tailed` or `--two-tailed` flag explicitly to specify hypothesis direction. One-tailed tests are appropriate when the research hypothesis specifies direction of association.
- **Zero-Cell Handling**: Tables with zero counts may produce undefined odds ratios or inflated p-values. Consider adding Haldane correction (adding 0.5 to all cells) for sparse tables.
- **Multiple Testing**: Running many Fisher tests without correction leads to false positives. Always apply appropriate multiple testing corrections (Bonferroni, Benjamini-Hochberg FDR) for genomic analyses.
- **Integer Overflow**: For very large counts, factorial calculations may overflow. Most implementations use log-space calculations to avoid numerical overflow issues.
- **Table Orientation**: The same table with rows/columns swapped may produce different odds ratios. Ensure consistent table orientation when comparing results across analyses.

## Examples
### Calculate p-value from command line
**Args:** `fisher 10 20 30 40`
**Explanation:** Computes Fisher's exact test for table [[10, 20], [30, 40]]. Returns odds ratio and two-tailed p-value. First two args are first row, second two args are second row.

### One-tailed test for positive association
**Args:** `fisher 10 20 30 40 --one-tail`
**Explanation:** Calculates one-tailed p-value testing if odds ratio > 1 (positive association). Appropriate when hypothesizing that exposure increases risk.

### Two-tailed test for any association
**Args:** `fisher 10 20 30 40 --two-tail`
**Explanation:** Calculates two-tailed p-value testing for any association regardless of direction. Recommended for exploratory analyses without directional hypothesis.

### Read table from stdin
**Args:** `echo -e "5\t10\n15\t20" | fisher`
**Explanation:** Pipes tab-separated table values to fisher. Each row of the contingency table on a separate line. Useful for integration in bioinformatics pipelines.

### CSV file input
**Args:** `fisher --csv association_data.csv`
**Explanation:** Reads 2x2 contingency tables from a CSV file. Each row should contain the four cell values. Useful for batch analysis of multiple tables.

### JSON output for programmatic parsing
**Args:** `fisher 10 20 30 40 --json`
**Explanation:** Returns results in JSON format with p-values, odds ratio, confidence intervals, and test parameters. Facilitates integration with automated pipelines.

### Calculate with confidence intervals
**Args:** `fisher 10 20 30 40 --ci 0.95`
**Explanation:** Computes 95% confidence interval for the odds ratio using exact binomial methods. Confidence intervals indicate precision of association estimate.

### Batch process multiple tables
**Args:** `cat tables.txt | while read line; do fisher $line; done`
**Explanation:** Processes multiple contingency tables from a file, one per line. Each line contains 4 space-separated integer values representing a 2x2 table.

### Debug mode for verification
**Args:** `fisher 10 20 30 40 --debug`
**Explanation:** Shows detailed calculation steps including intermediate probabilities and summation details. Useful for verifying correct computation or understanding the algorithm.
