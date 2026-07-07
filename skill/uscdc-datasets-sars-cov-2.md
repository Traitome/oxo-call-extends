---
name: uscdc-datasets-sars-cov-2
category: database
description: USCDC SARS-CoV-2 Dataset - Public COVID-19 genomic data.
tags: [uscdc-datasets-sars-cov-2, sars-cov-2, covid-19, genomics]
author: oxo-call-community
source_url: "https://www.cdc.gov/"
---

## Concepts

- **Tool Overview**: USCDC SARS-CoV-2 datasets - Access to public COVID-19 genomic data.
- **Core Function**: Provides access to SARS-CoV-2 sequencing data.
- **Input**: Query parameters.
- **Output**: Genomic sequences and metadata.
- **Installation**: Web-based or API access
- **Use Case**: Viral genomics, pandemic research, bioinformatics.

## Pitfalls

- **Network**: Requires network connectivity.
- **Data Volume**: Large datasets may require significant storage.

## Examples

### Download data
**Args:** `uscdc-datasets-sars-cov-2 download -o sars_cov_2_data/`
**Explanation:** Download SARS-CoV-2 datasets.

### Query data
**Args:** `uscdc-datasets-sars-cov-2 query --region=US --output=results.csv`
**Explanation:** Query datasets by region.
