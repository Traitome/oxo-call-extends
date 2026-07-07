---
name: ucsc-maketablelist
category: utility
description: UCSC makeTableList - Tool for creating table lists.
tags: [ucsc-maketablelist, ucsc, database, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC makeTableList - A tool for creating database table lists.
- **Core Function**: Generates lists of database tables.
- **Input**: Database name.
- **Output**: Table list.
- **Installation**: Part of UCSC utilities
- **Use Case**: Database management, metadata extraction.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Permissions**: Requires proper permissions.

## Examples

### Create table list
**Args:** `makeTableList -db=hg38 > tables.txt`
**Explanation:** Create list of database tables.

### With options
**Args:** `makeTableList -db=hg38 -verbose > tables.txt`
**Explanation:** Create with verbose output.
