---
name: ucsc-hgsqldump
category: utility
description: UCSC hgSqlDump - Tool for dumping SQL database.
tags: [ucsc-hgsqldump, ucsc, database, sql, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgSqlDump - A tool for dumping SQL database tables.
- **Core Function**: Exports database tables to SQL dump files.
- **Input**: Database name and table.
- **Output**: SQL dump file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Database backup, data export, migration.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large tables.

## Examples

### Dump database table
**Args:** `hgSqlDump -db=hg38 -table=knownGene > dump.sql`
**Explanation:** Dump database table to SQL file.

### With options
**Args:** `hgSqlDump -db=hg38 -table=knownGene -verbose > dump.sql`
**Explanation:** Dump with verbose output.
