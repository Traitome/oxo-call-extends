---
name: gget
category: bioinformatics-database
description: gget - Efficient genomic database querying tool.
tags: [gget, bioinformatics-database, API, query]
author: oxo-call-community
source_url: "https://pachterlab.github.io/gget"
---

## Concepts
- **Database Querying**: Queries genomic databases efficiently.
- **API Access**: Provides API for database access.
- **Literature Search**: Searches scientific literature.
- **Sequence Analysis**: Analyzes sequence data.
- **Gene Information**: Retrieves gene information.

## Pitfalls
- **Network Dependency**: Requires internet access.
- **Rate Limiting**: May have API rate limits.
- **Database Coverage**: Limited to supported databases.
- **Query Complexity**: Complex queries may fail.
- **Result Format**: Results may need formatting.

## Examples
### Query gene
**Args:** `gget gene -n BRCA1`
**Explanation:** Retrieves gene information for BRCA1.

### Search literature
**Args:** `gget search -q "cancer genomics" -n 10`
**Explanation:** Searches scientific literature.

### Batch query
**Args:** `gget gene -l genes.txt -o results.txt`
**Explanation:** Queries multiple genes.

### Get sequence
**Args:** `gget seq -n BRCA1 -organism human -o brca1.fasta`
**Explanation:** Retrieves gene sequence.

### Database info
**Args:** `gget info -d ensembl`
**Explanation:** Shows database information.