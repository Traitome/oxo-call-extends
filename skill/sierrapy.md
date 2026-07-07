---
name: sierrapy
category: utility
description: sierrapy - Client for HIVdb Sierra GraphQL webservice
tags: ["sierrapy", "utility", "HIV", "graphql"]
author: oxo-call-community
source_url: "https://github.com/hivdb/sierra-client/tree/master/python"
---

## Concepts

- **Tool Overview**: sierrapy (v0.4.3) is a Python client for HIVdb Sierra service.
- **Core Function**: Interacts with Stanford HIVdb Sierra GraphQL API.
- **Algorithm**: Implements GraphQL queries for resistance data.
- **Input/Output**: Accepts HIV sequences and queries remote database.
- **Web Service Client**: Requires internet connection for remote queries.
- **Applications**: HIV drug resistance analysis, research, and clinical support.

## Pitfalls

- **Network Requirements**: Requires internet connection.
- **Rate Limiting**: May be subject to API rate limits.
- **Service Availability**: Depends on remote service availability.
- **Version Compatibility**: Different versions may have breaking changes.
- **Authentication**: May require API keys for some operations.
- **Documentation**: Limited documentation available.

## Examples

### Query drug resistance
**Args:** `sierrapy query -i hiv_sequence.fasta -o results.json`
**Explanation:** Queries Sierra service for resistance predictions.

### Multiple sequences
**Args:** `sierrapy query -i sequences.fasta -o results.json`
**Explanation:** Processes multiple sequences.

### Get gene list
**Args:** `sierrapy genes`
**Explanation:** Lists available genes in the database.

### Help command
**Args:** `sierrapy --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sierrapy --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sierrapy -v query -i sequence.fasta -o results.json`
**Explanation:** `-v` verbose output.

### Specify API URL
**Args:** `sierrapy -u https://api.example.com query -i sequence.fasta -o results.json`
**Explanation:** `-u` custom API URL.
