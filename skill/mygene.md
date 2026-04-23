---
name: mygene
category: annotation
description: Python Client for MyGene.Info services.
tags: [mygene, annotation, gene, api, python]
author: oxo-call-community
source_url: "https://github.com/suLab/mygene.py"
---

## Concepts

- **Tool Overview**: MyGene v3.2.2 - Python client for MyGene.Info gene annotation services.
- **Core Function**: Provides programmatic access to gene annotation data through the MyGene.Info API.
- **Input/Output**: Takes gene identifiers or queries; returns gene annotation data in JSON format.
- **Installation**: `conda install -c bioconda mygene`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **API Access**: Requires internet connection for API queries.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `getgene("1017")`
**Explanation:** Retrieves gene annotation for gene ID 1017.

### Query genes
**Args:** `query("BRCA1", species="human")`
**Explanation:** Queries for BRCA1 gene in human.
