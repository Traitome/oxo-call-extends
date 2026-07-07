---
name: solvebio
category: programming
description: SolveBio - Python client for SolveBio genomic data platform
tags: [solvebio, programming, api, genomic-data, python]
author: oxo-call-community
source_url: "https://docs.solvebio.com"
---

## Concepts

- **Tool Overview**: solvebio (v2.35.0) - Python client for SolveBio platform
- **Core Function**: Provides API access to SolveBio genomic data repository
- **Input/Output**: API queries; outputs genomic data and annotations
- **Algorithm**: Communicates with SolveBio API for data retrieval
- **Installation**: `conda install -c bioconda solvebio`
- **Key Features**: API access, genomic data, Python integration

## Pitfalls

- **API Configuration**: Requires proper API configuration and credentials
- **Network Connectivity**: Requires network access to SolveBio servers
- **Authentication**: Requires valid authentication tokens
- **API Version**: Must use compatible API version
- **Rate Limits**: May be subject to API rate limits
- **Data Format**: Returned data format must be properly handled

## Examples

### Display help
**Args:** `python -c "import solvebio; help(solvebio)"`
**Explanation:** Shows module documentation.

### Authenticate
**Args:** `python -c "import solvebio; solvebio.login('API_KEY')"`
**Explanation:** Authenticate with SolveBio.

### List datasets
**Args:** `python -c "import solvebio; datasets = solvebio.Dataset.all()"`
**Explanation:** List available datasets.

### Get dataset
**Args:** `python -c "import solvebio; ds = solvebio.Dataset.get('ClinVar/Variants')"`
**Explanation:** Get specific dataset.

### Query dataset
**Args:** `python -c "import solvebio; ds = solvebio.Dataset.get('ClinVar/Variants'); records = ds.query(gene='BRCA1')"`
**Explanation:** Query dataset for records.

### Download data
**Args:** `python -c "import solvebio; ds = solvebio.Dataset.get('ClinVar/Variants'); ds.download('output.tsv')"`
**Explanation:** Download dataset data.

### Create vault
**Args:** `python -c "import solvebio; vault = solvebio.Vault.create('MyVault')"`
**Explanation:** Create new vault.

### Upload file
**Args:** `python -c "import solvebio; solvebio.File.upload('data.tsv', vault='MyVault')"`
**Explanation:** Upload file to vault.