---
name: metapub
category: programming
description: Pubmed / NCBI / eutils interaction library, handling the metadata of pubmed papers.
tags: [metapub, programming, pubmed, ncbi]
author: oxo-call-community
source_url: "https://metapub.org"
---

## Concepts

- **Tool Overview**: MetaPub v0.7.4 is a Python library for interacting with PubMed, NCBI, and E-Utilities to retrieve and process publication metadata.
- **Core Function**: Provides programmatic access to PubMed and NCBI databases for literature mining and meta-analysis.
- **API Integration**: Interfaces with NCBI E-Utilities API for querying and retrieving publication data.
- **Metadata Extraction**: Extracts publication metadata including authors, affiliations, keywords, and citation information.
- **Input/Output**: Accepts search queries; outputs structured publication metadata in various formats.
- **Automation**: Enables automated literature searches and metadata collection for bioinformatics workflows.

## Pitfalls

- **API Rate Limits**: Subject to NCBI API rate limits; may require API key for higher throughput.
- **Network Dependencies**: Requires stable internet connection for API access.
- **Data Volume**: Large queries may return substantial amounts of data.
- **Query Complexity**: Complex queries may require careful construction for optimal results.
- **Data Format**: May require data parsing and transformation for downstream analysis.
- **Service Availability**: Dependent on NCBI service availability.

## Examples

### Search PubMed
**Args:** `metapub search "metagenomics" --limit 10`
**Explanation:** Searches PubMed for publications related to metagenomics.

### Get publication details
**Args:** `metapub fetch --pmid 28953945`
**Explanation:** Retrieves detailed metadata for a specific PubMed ID.

### Export to CSV
**Args:** `metapub search "CRISPR" --output results.csv`
**Explanation:** Searches and exports results to CSV format.

### Batch fetch
**Args:** `metapub batch --pmids pmids.txt --output results.json`
**Explanation:** Fetches metadata for multiple PubMed IDs in batch.

### Advanced search
**Args:** `metapub search "(metagenomics) AND (human microbiome)" --since 2020`
**Explanation:** Performs advanced search with multiple criteria.