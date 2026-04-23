---
name: w4mclassfilter
category: qc
description: Filter Workflow4Metabolomics feature list, optionally imputing NA values.
tags: [w4mclassfilter, qc]
author: oxo-call-community
source_url: "https://github.com/HegemanLab/w4mclassfilter"
---

## Concepts

- **Tool Overview**: w4mclassfilter (v0.98.19) - Filter Workflow4Metabolomics dataMatrix, sampleMetadata, and variableMetadata files by sample-class, eliminating zero-variance rows and columns from the data-matrix and, optionally, imputing NA values. MIT Licence allows redistribution.
- **Core Function**: Filter Workflow4Metabolomics feature list, optionally imputing NA values.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda w4mclassfilter`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
