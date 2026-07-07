---
name: intermine
category: data-retrieval
description: InterMine WebService client for querying integrated biological data warehouses programmatically.
tags: [intermine, data-retrieval, webservice, bioinformatics-database]
author: oxo-call-community
source_url: "http://www.intermine.org"
---

## Concepts

- **Bioinformatics Data Warehouse**: InterMine provides integrated access to diverse biological datasets.
- **WebService Client**: Enables programmatic querying of InterMine instances.
- **Data Integration**: Combines data from multiple sources (genomics, proteomics, pathways).
- **Query Builder**: Supports complex queries with filters, joins, and aggregations.
- **Output Formats**: Supports multiple output formats including JSON, XML, and CSV.

## Pitfalls

- **Service Availability**: Requires network access to InterMine server.
- **Query Complexity**: Complex queries may require careful construction.
- **Data Volume**: Large result sets may require pagination or filtering.
- **API Changes**: WebService API may change between versions.
- **Authentication**: Some InterMine instances require authentication for access.

## Examples

### Connect to InterMine instance
**Args:** `python -c "from intermine.webservice import Service; s = Service('https://www.flymine.org/flymine/service')"`
**Explanation:** Establishes connection to FlyMine web service.

### Basic gene query
**Args:** `python -c "from intermine.webservice import Service; s = Service('https://www.flymine.org/flymine/service'); q = s.new_query('Gene'); q.add_view('symbol', 'length'); print(q.rows())"`
**Explanation:** Queries gene symbols and lengths from FlyMine.

### Query with constraints
**Args:** `python -c "from intermine.webservice import Service; s = Service('https://www.flymine.org/flymine/service'); q = s.new_query('Gene'); q.add_constraint('length', '>', 10000); print(q.rows())"`
**Explanation:** Queries genes longer than 10,000 base pairs.

### Retrieve pathway information
**Args:** `python -c "from intermine.webservice import Service; s = Service('https://yeastmine.yeastgenome.org/yeastmine/service'); q = s.new_query('Pathway'); q.add_view('name', 'organism.name'); print(q.rows())"`
**Explanation:** Retrieves pathway names and associated organisms from YeastMine.

### Batch query
**Args:** `python -c "from intermine.webservice import Service; s = Service('https://www.flymine.org/flymine/service'); q = s.new_query('Gene'); q.add_list(['eve', 'ftz', 'h'], 'Gene', 'symbol'); print(q.rows())"`
**Explanation:** Queries multiple genes by symbol from a list.

### Export to CSV
**Args:** `python -c "from intermine.webservice import Service; s = Service('https://www.flymine.org/flymine/service'); q = s.new_query('Gene'); q.add_view('symbol', 'description'); q.export('csv', 'genes.csv')"`
**Explanation:** Exports query results to CSV file.