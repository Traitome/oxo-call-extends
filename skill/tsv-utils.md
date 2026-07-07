---
name: tsv-utils
category: utility
description: TSV Utils - Toolkit for working with TSV (Tab-Separated Values) files.
tags: [tsv-utils, tsv, data-processing, bioinformatics, utilities]
author: oxo-call-community
source_url: "https://github.com/eBay/tsv-utils"
---

## Concepts

- **Tool Overview**: TSV Utils - A toolkit for manipulating and analyzing TSV files.
- **Core Function**: Provides utilities for filtering, sorting, joining, and analyzing TSV data.
- **Input**: TSV files, tab-separated data.
- **Output**: Processed TSV files, statistics, derived data.
- **Installation**: `conda install -c bioconda tsv-utils`
- **Use Case**: Data processing, bioinformatics pipelines, text processing.

## Pitfalls

- **Format Requirements**: Requires proper TSV formatting.
- **Memory**: Large files may require significant memory.

## Examples

### Filter TSV
**Args:** `tsv-filter -H -f '$3 > 100' data.tsv > filtered.tsv`
**Explanation:** Filter TSV file by column value.

### Sort TSV
**Args:** `tsv-sort -k 2 -t $'\t' data.tsv > sorted.tsv`
**Explanation:** Sort TSV file by second column.
