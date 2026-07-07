---
name: biogridpy
category: programming
description: Python client for the BioGRID REST API webservice
tags: [biogrid, protein-interactions, rest-api, gene-interactions]
author: oxo-call-community
source_url: "https://github.com/arvkevi/biogridpy"
---

## Concepts

- **Tool Overview**: biogridpy is a Python client for the BioGRID REST API, providing access to curated protein-protein, genetic, and chemical interactions data.
- **BioGRID Database**: Comprehensive repository of curated interactions from multiple organisms.
- **API Access**: Requires free access key from http://webservice.thebiogrid.org/
- **Result Formats**: Supports tab2, json, and other output formats for interaction data.
- **Query Parameters**: Supports gene lists, evidence types, organisms (taxonomy IDs), and more.

## Pitfalls

- **API Key Required**: Must register for a free access key before using.
- **Rate Limiting**: API rate limits may apply for large queries.
- **Configuration File**: Requires biogridpyrc configuration file with access key.
- **Data Format**: Results require proper parsing based on selected output format.

## Examples

### Initialize client
**Args:** `from biogridpy.biogrid_client import BioGRID; BG = BioGRID(config_filepath='/path/to/biogridpyrc')`
**Explanation:** Initializes BioGRID client with configuration file containing access key.

### Query interactions
**Args:** `results = BG.interactions('tab2', geneList=['RB1', 'E2F1'], taxId=9606)`
**Explanation:** Retrieves interactions for genes RB1 and E2F1 in human (taxId 9606).

### Query with evidence filter
**Args:** `results = BG.interactions('json', geneList='genes.list', evidenceList='evidence.list', includeEvidence='true')`
**Explanation:** Queries interactions with specific evidence types.

### biogridpyrc configuration
**Args:** `[BioGRID_ak]` followed by `access_key = YourAccessKeyHere`
**Explanation:** Format for the configuration file containing API access key.