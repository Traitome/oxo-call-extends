---
name: bioservices
category: programming
description: Access to Biological Web Services from Python
tags: [bioservices, web-services, programming, API, bioinformatics]
author: oxo-call-community
source_url: "https://bioservices.readthedocs.io/"
---

## Concepts

- **Tool Overview**: BioServices provides a Python interface to various biological web services, enabling programmatic access to databases and analysis tools.
- **Service Integration**: Access to NCBI, UniProt, KEGG, Reactome, BioModels, and many other biological databases.
- **Web Service Protocols**: Supports REST, SOAP, and other web service protocols.
- **Unified Interface**: Consistent Python API across different biological databases and services.
- **Applications**: Data retrieval, pathway analysis, protein interaction queries, literature search.

## Pitfalls

- **Network Dependency**: Requires internet connection to access web services.
- **Rate Limiting**: Some services may have rate limits or require API keys.
- **Service Availability**: External services may be temporarily unavailable.

## Examples

### Access UniProt
**Args:** `from bioservices import UniProt; u = UniProt(); u.search("BRCA1")`
**Explanation:** Searches UniProt database for BRCA1 protein.

### Query KEGG
**Args:** `from bioservices import KEGG; k = KEGG(); k.list("pathway:eco00232")`
**Explanation:** Lists compounds in a KEGG pathway.

### Reactome Pathway Analysis
**Args:** `from bioservices import Reactome; r = Reactome(); r.query("cancer")`
**Explanation:** Queries Reactome database for pathway information.

### BioModels API
**Args:** `from bioservices import BioModels; b = BioModels(); b.get_model("BIOMD0000000001")`
**Explanation:** Retrieves a specific model from BioModels database.