---
name: ucsc-dbtrash
category: utility
description: UCSC dbTrash - Tool for managing database trash.
tags: [ucsc-dbtrash, ucsc, database, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC dbTrash - A tool for managing database trash/recycle bin.
- **Core Function**: Manages deleted database objects in a trash bin.
- **Input**: Database connection.
- **Output**: Trash management operations.
- **Installation**: Part of UCSC utilities
- **Use Case**: Database maintenance, recovery, cleanup.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Permissions**: May require specific database permissions.

## Examples

### Empty trash
**Args:** `dbTrash -db=hg38 -empty`
**Explanation:** Empty database trash.

### List trash
**Args:** `dbTrash -db=hg38 -list`
**Explanation:** List items in trash.
