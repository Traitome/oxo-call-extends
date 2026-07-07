---
name: ucsc-dbsnoop
category: utility
description: UCSC dbSnoop - Tool for snooping database tables.
tags: [ucsc-dbsnoop, ucsc, database, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC dbSnoop - A tool for inspecting database tables.
- **Core Function**: Examines database table structure and content.
- **Input**: Database connection, table name.
- **Output**: Table metadata and sample data.
- **Installation**: Part of UCSC utilities
- **Use Case**: Database inspection, debugging, data exploration.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Permissions**: May require specific database permissions.

## Examples

### Snoop database table
**Args:** `dbSnoop -db=hg38 -table=refGene`
**Explanation:** Inspect database table.

### With sample data
**Args:** `dbSnoop -db=hg38 -table=refGene -limit=10`
**Explanation:** Show first 10 rows.
