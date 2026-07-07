---
name: mpra-data-access-portal
category: utility
description: Saturation mutagenesis MPRA data access portal.
tags: [mpra-data-access-portal, utility, mpra]
author: oxo-call-community
source_url: "https://mpra.gs.washington.edu/satMutMPRA"
---

## Concepts

- **Tool Overview**: MPRA Data Access Portal v0.1.17 provides access to saturation mutagenesis MPRA data.
- **Core Function**: Facilitates access to high-throughput MPRA experimental data.
- **MPRA Data**: Specialized for Massively Parallel Reporter Assay data.
- **Saturation Mutagenesis**: Supports saturation mutagenesis experiment data.
- **Data Query**: Enables querying and retrieval of MPRA datasets.
- **Input/Output**: Accepts query parameters; outputs MPRA data and metadata.

## Pitfalls

- **MPRA Specific**: Designed for MPRA experiment data.
- **Network Dependence**: Requires network access for data retrieval.
- **Data Availability**: Depends on data availability in the portal.
- **Query Complexity**: May require learning query syntax.
- **Data Quality**: Results depend on underlying data quality.
- **Version Compatibility**: Some options may vary between versions.

## Examples

### Access MPRA data
**Args:** `mpra-portal query -g gene_name -o results.txt`
**Explanation:** Queries MPRA data for specific gene.

### Download dataset
**Args:** `mpra-portal download -d dataset_id -o data/`
**Explanation:** Downloads MPRA dataset.

### List available datasets
**Args:** `mpra-portal list`
**Explanation:** Shows available MPRA datasets.

### Search by experiment type
**Args:** `mpra-portal search -t saturation_mutagenesis -o results.txt`
**Explanation:** Searches for saturation mutagenesis experiments.

### Generate report
**Args:** `mpra-portal report -d dataset_id -o report.html`
**Explanation:** Generates dataset summary report.