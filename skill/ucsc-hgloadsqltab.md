---
name: ucsc-hgloadsqltab
category: utility
description: UCSC hgLoadSqlTab - Tool for loading SQL tab data.
tags: [ucsc-hgloadsqltab, ucsc, database, sql, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadSqlTab - A tool for loading tab-delimited data into database.
- **Core Function**: Loads tab-delimited data into MySQL database tables.
- **Input**: Tab-delimited file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, data loading, annotation.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Format Requirements**: Requires proper tab-delimited format.

## Examples

### Load SQL tab data
**Args:** `hgLoadSqlTab -db=hg38 -table=myTable input.txt`
**Explanation:** Load tab-delimited data to database.

### With options
**Args:** `hgLoadSqlTab -db=hg38 -table=myTable -verbose input.txt`
**Explanation:** Load with verbose output.
