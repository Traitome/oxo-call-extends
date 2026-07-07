---
name: ncbi-datasets-pylib
category: utility
description: NCBI Datasets Python library for easily gathering data from across NCBI databases.
tags: [ncbi-datasets-pylib, utility, ncbi, python, api]
author: oxo-call-community
source_url: "https://www.ncbi.nlm.nih.gov/datasets"
---

## Concepts

- **Tool Overview**: ncbi-datasets-pylib is the Python library component of NCBI Datasets for programmatic data access.
- **Core Function**: Enables Python-based retrieval of genomic data, metadata, and annotations from NCBI databases.
- **Algorithm**: Provides high-level API wrappers around NCBI's RESTful services for simplified data access.
- **Input Format**: Accepts API queries, taxonomic identifiers, and accession numbers.
- **Output**: Returns structured data objects and file downloads in standard bioinformatics formats.
- **Use Case**: Automated data retrieval, bioinformatics pipeline integration, and large-scale genomic analysis.

## Pitfalls

- **API Rate Limits**: NCBI enforces rate limits on API requests.
- **Network Dependency**: Requires internet access to NCBI servers.
- **Version Compatibility**: API and library interfaces may change between versions.
- **Authentication**: Some endpoints require API keys for higher rate limits.
- **Data Volume**: Large datasets can consume significant bandwidth and storage.
- **Error Handling**: Network errors require robust exception handling in scripts.

## Examples

### Display help
**Args:** `python -c "from ncbi.datasets import ApiClient; help(ApiClient)"`
**Explanation:** Shows available options and API documentation.

### Download genome by accession
**Args:** `datasets download genome accession NC_000913.3 --filename genome.zip`
**Explanation:** Downloads genome sequence for specified accession.

### List available genomes
**Args:** `datasets summary genome taxon 562 --as-json-lines`
**Explanation:** Lists available E. coli genomes in JSON format.

### Download gene data
**Args:** `datasets download gene symbol BRCA1 --species human --filename brca1.zip`
**Explanation:** Downloads gene data for human BRCA1.

### Batch download
**Args:** `datasets download genome accession NC_000913.3 NC_012920.1 --filename genomes.zip`
**Explanation:** Downloads multiple genomes in batch.

### Extract downloaded archive
**Args:** `datasets extract --inputfile genome.zip --outputdir genome_data/`
**Explanation:** Extracts downloaded archive to specified directory.