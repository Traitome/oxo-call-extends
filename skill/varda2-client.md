---
name: varda2-client
category: bioinformatics
description: VARDA2 Client - Variant Archive and Data Analysis client.
tags: [varda2-client, variant-database, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/varda2/"
---

## Concepts

- **Tool Overview**: VARDA2 Client - Client for accessing VARDA2 variant database.
- **Core Function**: Accesses and queries variant archive.
- **Input**: Query parameters.
- **Output**: Variant data.
- **Installation**: Install via pip
- **Use Case**: Variant database access, bioinformatics.

## Pitfalls

- **Network**: Requires network connectivity.
- **Authentication**: May require API credentials.

## Examples

### Query database
**Args:** `varda2-client query --gene=BRCA1 --output=results.json`
**Explanation:** Query variants by gene.

### Download data
**Args:** `varda2-client download --id=VAR001 --output=variant.vcf`
**Explanation:** Download variant data.
