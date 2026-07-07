---
name: biothings_client
category: programming
description: Python Client for BioThings API services for biological data annotation
tags: [biothings, API, programming, annotation, gene-annotation]
author: oxo-call-community
source_url: "https://github.com/biothings/biothings_client.py"
---

## Concepts

- **Tool Overview**: BioThings Client is a Python library for accessing BioThings API services, which provide integrated access to biological annotation data.
- **BioThings Hub**: Centralized API hub aggregating data from multiple biological databases.
- **Data Types**: Access to gene, variant, drug, disease, and pathway annotations.
- **Batch Queries**: Supports batch querying for efficient data retrieval.
- **Applications**: Gene annotation, variant annotation, drug-target mapping, data enrichment.

## Pitfalls

- **Network Dependency**: Requires internet connection for API access.
- **Rate Limits**: API has rate limiting; batch operations should be throttled.
- **Data Freshness**: Data is as current as the BioThings Hub database updates.

## Examples

### Query gene annotation
**Args:** `from biothings_client import get_client; gene_client = get_client('gene'); gene_client.query("BRCA1")`
**Explanation:** Queries gene information for BRCA1.

### Batch gene lookup
**Args:** `gene_client.querymany(["BRCA1", "TP53", "EGFR"], scopes="symbol")`
**Explanation:** Batch queries multiple genes by symbol.

### Variant annotation
**Args:** `var_client = get_client('variant'); var_client.query("chr17:g.41244969:T>G")`
**Explanation:** Queries variant annotation for genomic position.

### Drug annotation
**Args:** `drug_client = get_client('drug'); drug_client.query("aspirin")`
**Explanation:** Queries drug information for aspirin.