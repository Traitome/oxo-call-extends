---
name: orthodb
category: annotation
description: OrthoDB provides an interface to the OrthoDB REST API for orthology analysis.
tags: [orthodb, annotation, orthology, comparative-genomics]
author: oxo-call-community
source_url: "https://www.ezlab.org/orthodb_v12_userguide.html"
---

## Concepts

- **Tool Overview**: OrthoDB provides access to orthology data via REST API.
- **Core Function**: Queries orthology relationships between genes.
- **Algorithm**: Uses REST API queries to OrthoDB database.
- **Input Format**: Accepts gene IDs and species identifiers.
- **Output**: Produces orthology relationships and annotations.
- **Use Case**: Comparative genomics, orthology analysis, and gene annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **API Rate Limits**: May be subject to rate limiting.
- **Network Dependency**: Requires internet connection.
- **Data Availability**: Depends on OrthoDB database updates.
- **Response Time**: API calls may have latency.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "import orthodb; help(orthodb)"`
**Explanation:** Shows available options and usage instructions.

### Query orthologs
**Args:** `python -c "from orthodb import OrthoDB; odb = OrthoDB(); orthologs = odb.get_orthologs('ENSG00000130203')"`
**Explanation:** Retrieves orthologs for a gene.

### With species
**Args:** `python -c "orthologs = odb.get_orthologs('ENSG00000130203', species=['human', 'mouse'])"`
**Explanation:** Filters orthologs by species.

### Get gene info
**Args:** `python -c "info = odb.get_gene_info('ENSG00000130203')"`
**Explanation:** Retrieves gene information.

### Batch query
**Args:** `python -c "orthologs = odb.get_orthologs_batch(['ENSG00000130203', 'ENSG00000163083'])"`
**Explanation:** Queries multiple genes.

### Verbose mode
**Args:** `python -c "odb = OrthoDB(verbose=True)"`
**Explanation:** Runs with verbose output.

### Save results
**Args:** `python -c "orthologs.to_csv('orthologs.csv')"`
**Explanation:** Saves results to CSV.