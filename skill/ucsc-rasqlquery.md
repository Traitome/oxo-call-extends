---
name: ucsc-rasqlquery
category: utility
description: UCSC raSqlQuery - Tool for SQL querying.
tags: [ucsc-rasqlquery, ucsc, sql, query, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC raSqlQuery - A tool for SQL querying.
- **Core Function**: Executes SQL queries on databases.
- **Input**: SQL query.
- **Output**: Query results.
- **Installation**: Part of UCSC utilities
- **Use Case**: Database querying, data retrieval, bioinformatics.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Permissions**: Requires proper permissions.

## Examples

### Execute SQL query
**Args:** `raSqlQuery -db=hg38 "SELECT * FROM refGene LIMIT 10"`
**Explanation:** Execute SQL query.

### With options
**Args:** `raSqlQuery -db=hg38 -verbose "SELECT * FROM refGene LIMIT 10"`
**Explanation:** Execute with verbose output.
