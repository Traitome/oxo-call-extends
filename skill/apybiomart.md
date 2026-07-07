---
name: apybiomart
category: programming
description: apybiomart - Async pythonic interface to Ensembl BioMart
tags: [apybiomart, biomart, ensembl, python, async, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/robertopreste/apybiomart"
---

## Concepts

- **Tool Overview**: apybiomart (v0.5.3) - A Python module providing a simple asynchronous interface to Ensembl BioMart for querying genomic data.
- **Core Function**: Enables both synchronous and asynchronous queries to BioMart databases, supporting multiple queries using Python's asyncio library.
- **BioMart**: A database system that provides access to a wide range of genomic data from Ensembl and other sources.
- **Key Features**:
  - **Marts**: Different databases (e.g., ENSEMBL_MART_ENSEMBL, ENSEMBL_MART_SNP)
  - **Datasets**: Species-specific data collections within each mart
  - **Attributes**: Specific data types to retrieve (e.g., gene names, IDs, positions)
  - **Filters**: Criteria to restrict query results
- **Asynchronous Support**: Allows scheduling multiple queries concurrently using asyncio
- **Output**: Returns results as pandas DataFrames or saves to CSV files
- **Installation**: `conda install -c bioconda apybiomart` or `pip install apybiomart`

## Pitfalls

- **Internet Connection**: Requires active internet connection to access BioMart server
- **Server Availability**: BioMart service may be temporarily unavailable
- **Query Limits**: Large queries may be subject to rate limiting
- **Attribute/Filters Knowledge**: Requires knowledge of available attributes and filters for each dataset
- **Python Version**: Requires Python >= 3.4 and depends on aiohttp, pandas, requests

## Examples

### Find available marts
**Args:** `from apybiomart import find_marts; marts = find_marts()`
**Explanation:** Retrieves all available BioMart databases.

### Find datasets in a mart
**Args:** `from apybiomart import find_datasets; datasets = find_datasets(mart="ENSEMBL_MART_ENSEMBL")`
**Explanation:** Lists all datasets (species) in the specified mart.

### Synchronous query
**Args:** `from apybiomart import query; result = query(attributes=["ensembl_gene_id", "external_gene_name"], filters={"chromosome_name": ["1", "2"]}, dataset="hsapiens_gene_ensembl")`
**Explanation:** Performs synchronous query for human gene IDs and names on chromosomes 1 and 2.

### Asynchronous query
**Args:** `import asyncio; from apybiomart import aquery; result = asyncio.run(aquery(attributes=["ensembl_gene_id"], filters={"chromosome_name": "1"}, dataset="hsapiens_gene_ensembl"))`
**Explanation:** Performs asynchronous query using asyncio event loop.

### Save results to CSV
**Args:** `query(attributes=["ensembl_gene_id"], filters={}, dataset="hsapiens_gene_ensembl", save=True, output="genes.csv")`
**Explanation:** Queries and saves results directly to CSV file.

### CLI - List marts
**Args:** `apybiomart marts`
**Explanation:** Command-line interface to list available marts.

### CLI - Query
**Args:** `apybiomart query --attributes ensembl_gene_id,external_gene_name --dataset hsapiens_gene_ensembl --save --output results.csv`
**Explanation:** CLI query with results saved to CSV.