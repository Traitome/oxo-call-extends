---
name: atlas-data-import
category: utility
description: Atlas Data Import - Scripts for extracting expression and metadata from Single Cell Expression Atlas
tags: [data-import, single-cell, expression-atlas, metadata-extraction]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/atlas-data-import"
---

## Concepts

- **Tool Overview**: Scripts for programmatically extracting expression data and metadata from Single Cell Expression Atlas database.

- **API Integration**: Interfaces with Expression Atlas API to retrieve experiment data and metadata.

- **Metadata Extraction**: Extracts sample metadata, experimental conditions, and cell type annotations.

- **Expression Matrices**: Downloads or generates expression count matrices for downstream analysis.

## Pitfalls

- **API Availability**: Requires access to Expression Atlas API. Network issues can interrupt data retrieval.

- **Data Size**: Single-cell datasets can be very large. Ensure sufficient storage and memory.

- **Rate Limiting**: API may have rate limits. Implement appropriate delays for large batch requests.

- **Data Format Changes**: API responses may change over time. Monitor for format updates.

## Examples

### Extract experiment metadata
**Args:** `atlas-data-import --experiment E-MTAB-1234 --output metadata.tsv`
**Explanation:** Downloads metadata for specified Single Cell Expression Atlas experiment.

### Download expression matrix
**Args:** `atlas-data-import --experiment E-MTAB-1234 --matrix --output matrix.mtx`
**Explanation:** Downloads expression count matrix for experiment in Matrix Market format.

### Extract specific metadata fields
**Args:** `atlas-data-import --experiment E-MTAB-1234 --fields cell_type,disease,tissue --output selected_metadata.tsv`
**Explanation:** Extracts only specified metadata fields from experiment.

### Batch download multiple experiments
**Args:** `atlas-data-import --experiments E-MTAB-1234,E-MTAB-5678 --output-dir data/`
**Explanation:** Downloads data for multiple experiments to specified directory.
