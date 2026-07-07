---
name: hca-matrix-downloader
category: bioinformatics
description: HCA Matrix Downloader is a Python client for the Human Cell Atlas Data Coordination Platform matrix service.
tags: [hca-matrix-downloader, single-cell, data-download, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/hca-matrix-downloader"
---

## Concepts

- **HCA Data Access**: Downloads data from Human Cell Atlas.

- **Matrix Service**: Accesses matrix data from HCA DCP.

- **Single-Cell Data**: Handles single-cell sequencing data.

- **Data Download**: Downloads large genomic datasets.

- **API Client**: Provides API access to HCA resources.

- **Data Integration**: Facilitates data integration from HCA.

## Pitfalls

- **Network Access**: Requires network access to HCA.

- **Authentication**: May require authentication.

- **Large Files**: Downloading large files may take time.

- **Data Availability**: Data availability may vary.

- **Rate Limits**: Be aware of API rate limits.

## Examples

### Download matrix
**Args:** `hca-matrix-downloader --project-id PRJXXXX --output matrix.h5ad`
**Explanation:** Downloads matrix from HCA project.

### List projects
**Args:** `hca-matrix-downloader --list-projects`
**Explanation:** Lists available HCA projects.

### Batch download
**Args:** `for proj in PRJ1 PRJ2 PRJ3; do hca-matrix-downloader --project-id $proj --output ${proj}_matrix.h5ad; done`
**Explanation:** Downloads multiple project matrices.

### Filter by cell type
**Args:** `hca-matrix-downloader --project-id PRJXXXX --filter "cell_type=T cell" --output filtered.h5ad`
**Explanation:** Filters cells by cell type.

### Metadata download
**Args:** `hca-matrix-downloader --project-id PRJXXXX --metadata --output metadata.json`
**Explanation:** Downloads project metadata.

### Help command
**Args:** `hca-matrix-downloader --help`
**Explanation:** Shows available options and usage information.