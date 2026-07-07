---
name: ucsc-tdbquery
category: utility
description: UCSC tdbQuery - Tool for querying TDB databases.
tags: [ucsc-tdbquery, ucsc, tdb, database, query]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC tdbQuery - A tool for querying TDB databases.
- **Core Function**: Queries tiled database (TDB) files.
- **Input**: TDB database file, query parameters.
- **Output**: Query results.
- **Installation**: Part of UCSC utilities
- **Use Case**: Database querying, data retrieval, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large databases.
- **Database Access**: Requires proper TDB format.

## Examples

### Query TDB database
**Args:** `tdbQuery -db=data.tdb -query="SELECT * FROM table"`
**Explanation:** Query TDB database.

### With options
**Args:** `tdbQuery -db=data.tdb -verbose -query="SELECT * FROM table"`
**Explanation:** Query with verbose output.
