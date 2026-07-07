---
name: ncbi-datasets-pyclient
category: programming
description: NCBI Datasets Python API client for accessing NCBI genomic data programmatically.
tags: [ncbi-datasets-pyclient, programming, ncbi, api, python]
author: oxo-call-community
source_url: "https://www.ncbi.nlm.nih.gov/datasets"
---

## Concepts

- **Tool Overview**: NCBI Datasets Python API client provides programmatic access to NCBI genomic data resources.
- **Core Function**: Enables Python-based retrieval of genome sequences, annotations, and metadata from NCBI databases.
- **Algorithm**: Interfaces with NCBI's Datasets API to query and download bioinformatics data.
- **Input Format**: Accepts API queries and parameters for data retrieval.
- **Output**: Returns genomic data in various formats including FASTA, GFF, and JSON.
- **Use Case**: Bioinformatics pipeline integration, automated data retrieval, and large-scale data analysis.

## Pitfalls

- **API Rate Limits**: NCBI enforces rate limits on API requests.
- **Network Dependency**: Requires internet access to NCBI servers.
- **Version Compatibility**: API may change between versions.
- **Authentication**: Some endpoints require API keys for higher rate limits.
- **Data Volume**: Large datasets can consume significant bandwidth and storage.
- **Documentation**: Requires understanding of NCBI Datasets API structure.

## Examples

### Display help
**Args:** `datasets --help`
**Explanation:** Shows available options and usage instructions.

### Download genome by accession
**Args:** `datasets download genome accession NC_000913.3 --filename genome.zip`
**Explanation:** Downloads genome sequence for specified accession.

### Download gene data
**Args:** `datasets download gene symbol BRCA1 --species human --filename brca1.zip`
**Explanation:** Downloads gene data for human BRCA1.

### List available genomes
**Args:** `datasets summary genome taxon 562 --as-json-lines`
**Explanation:** Lists available E. coli genomes in JSON format.

### Download multiple accessions
**Args:** `datasets download genome accession NC_000913.3 NC_012920.1 --filename genomes.zip`
**Explanation:** Downloads multiple genomes in batch.

### Extract downloaded data
**Args:** `datasets extract --inputfile genome.zip --outputdir genome_data/`
**Explanation:** Extracts downloaded archive to specified directory.