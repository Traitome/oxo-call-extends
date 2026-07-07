---
name: lyner
category: utility
description: A chaining toolbox for working with dataframes
tags: [lyner, utility, dataframes, pandas]
author: oxo-call-community
source_url: "https://github.com/tedil/lyner"
---

## Concepts

- **Tool Overview**: lyner v0.4.3 is a chaining toolbox for working with pandas dataframes, enabling fluent method chaining.
- **Core Function**: Provides utility functions for dataframe manipulation using method chaining patterns.
- **Chaining Pattern**: Allows sequential operations on dataframes using dot notation.
- **Input/Output**: Input: pandas DataFrame; Output: Modified pandas DataFrame or analysis results.
- **Installation**: `conda install -c bioconda lyner` or `pip install lyner`
- **Key Features**: Simplifies dataframe workflows, supports method chaining, integrates with pandas.

## Pitfalls

- **Version Compatibility**: May require specific pandas versions.
- **Learning Curve**: Requires understanding of method chaining patterns.
- **Debugging**: Chained operations can be harder to debug than traditional code.
- **Performance**: Complex chains may have performance implications.
- **Documentation**: Limited documentation compared to core pandas.
- **Dependency**: Requires pandas to be installed.

## Examples

### Chain operations
**Args:** `df.pipe(lyner.chain).dropna().filter(['col1', 'col2']).run()`
**Explanation:** Chains multiple operations on dataframe.

### Load and process
**Args:** `lyner.load('data.csv').dropna().groupby('category').mean().save('output.csv')`
**Explanation:** Loads CSV, processes, and saves result.

### Filter and transform
**Args:** `df >> lyner.filter(lambda x: x['value'] > 10) >> lyner.transform(lambda x: x * 2)`
**Explanation:** Uses pipe operators for filtering and transformation.

### Aggregation
**Args:** `df >> lyner.groupby('group') >> lyner.agg({'value': 'mean'})`
**Explanation:** Groups and aggregates dataframe.

### Save output
**Args:** `lyner.load('data.csv').process().save('output.parquet')`
**Explanation:** Loads, processes, and saves to parquet format.

### Help documentation
**Args:** `lyner --help`
**Explanation:** Displays available functions and usage.