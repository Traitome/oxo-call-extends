---
name: scxmatch
category: single-cell
description: scxmatch - Single-cell cross match test implementation
tags: ["scxmatch", "single-cell", "statistics", "testing"]
author: oxo-call-community
source_url: "https://github.com/bionetslab/scxmatch"
---

## Concepts

- **Tool Overview**: scxmatch (v0.1.1) is a Python implementation for single-cell cross match test.
- **Core Function**: Implements Rosenbaum's test for single-cell data analysis.
- **Algorithm**: Uses permutation-based testing for statistical significance.
- **Input/Output**: Accepts gene expression matrices and produces test statistics.
- **Statistical Testing**: Designed for hypothesis testing in single-cell data.
- **Applications**: Differential expression analysis, marker gene identification.

## Pitfalls

- **Computational Resources**: May require significant compute resources.
- **Memory Usage**: High memory requirements for large datasets.
- **Statistical Power**: Depends on sample size and effect size.
- **Multiple Testing**: Requires proper correction for multiple comparisons.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Documentation**: Some features have limited documentation.

## Examples

### Basic test
**Args:** `import scxmatch; result = scxmatch.crossmatch(data, groups)`
**Explanation:** Performs cross match test on data.

### With permutations
**Args:** `result = scxmatch.crossmatch(data, groups, n_permutations=1000)`
**Explanation:** `-n_permutations` specifies number of permutations.

### Verbose mode
**Args:** `result = scxmatch.crossmatch(data, groups, verbose=True)`
**Explanation:** Enables verbose output for debugging.

### Save results
**Args:** `scxmatch.save(result, 'results.csv')`
**Explanation:** Saves results to CSV file.

### Load results
**Args:** `result = scxmatch.load('results.csv')`
**Explanation:** Loads previously saved results.

### Plot results
**Args:** `scxmatch.plot(result, 'plot.png')`
**Explanation:** Generates visualization of results.

### Help command
**Args:** `scxmatch --help`
**Explanation:** Shows available commands and options.