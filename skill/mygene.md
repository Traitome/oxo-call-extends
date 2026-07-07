---
name: mygene
category: annotation
description: MyGene - Python Client for MyGene.Info gene annotation services
tags: [mygene, annotation, gene, api, python, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/suLab/mygene.py"
---

## Concepts

- **Tool Overview**: MyGene v3.2.2 is a Python client for MyGene.Info services, providing programmatic access to a comprehensive gene annotation database. MyGene.Info aggregates gene information from multiple sources including NCBI, Ensembl, and UniProt.
- **Core Function**: Enables Python programs to query gene annotations by gene ID, symbol, or other identifiers. Returns rich annotation data including gene names, functions, pathways, orthologs, and cross-references.
- **API Design**: Implements RESTful API calls to MyGene.Info servers with Pythonic interface. Supports both synchronous and asynchronous queries for batch processing.
- **Input Format**: Accepts gene identifiers in various formats (Entrez ID, Ensembl ID, gene symbol) and supports batch queries for multiple genes.
- **Output**: Returns gene annotation data as Python dictionaries or pandas DataFrames, including fields like symbol, name, type, taxonomy, annotations, and cross-references.
- **Use Case**: Gene annotation pipelines, functional enrichment analysis, converting between gene ID systems, and batch gene information retrieval for bioinformatics workflows.

## Pitfalls

- **API Rate Limits**: MyGene.Info has rate limits on query frequency. Implement appropriate delays or use batch queries to avoid being blocked.
- **Network Dependency**: Requires internet connection for API queries. Offline workflows cannot use this tool.
- **Version Compatibility**: Python 2 vs Python 3 differences exist. Ensure using Python 3 for compatibility with newer versions.
- **Data Freshness**: Annotation data depends on upstream databases. Check data update dates for research requiring latest annotations.
- **Field Selection**: Requesting too many fields increases response size and parsing time. Request only needed fields for efficiency.
- **Query Syntax**: Proper query syntax is essential. Invalid queries return empty results without error messages.

## Examples

### Get gene annotation by Entrez ID
**Args:** `getgene("1017")`
**Explanation:** Retrieves complete gene annotation for gene ID 1017 (CDK2). Returns dictionary with all available fields.

### Query genes by symbol
**Args:** `query("BRCA1", species="human")`
**Explanation:** Searches for human BRCA1 gene by symbol. Returns list of matching gene objects.

### Batch query with list input
**Args:** `querymany(["1017", "1018", "1019"])`
**Explanation:** Batch query for multiple gene IDs. More efficient than individual queries for large gene sets.

### Filter output fields
**Args:** `query("TP53", species="human", fields=["symbol", "name", "pathway"])`
**Explanation:** Retrieves only specified fields to reduce output size and improve performance.

### Display help
**Args:** `help()`
**Explanation:** Shows available methods and documentation for the MyGene Python client.
