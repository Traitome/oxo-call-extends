---
name: ucsc-autosql
category: utility
description: UCSC autoSql - Tool for defining table schemas in UCSC format.
tags: [ucsc-autosql, ucsc, schema-definition, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC autoSql - A tool for defining table schemas for UCSC genome browser.
- **Core Function**: Creates and manipulates autoSql schema definitions.
- **Input**: autoSql schema files, table definitions.
- **Output**: Schema files, database table definitions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser data submission, schema definition, data integration.

## Pitfalls

- **Schema Syntax**: Requires correct autoSql syntax.
- **Compatibility**: Schema must be compatible with UCSC browser.

## Examples

### Create schema
**Args:** `autoSql schema.as table.txt`
**Explanation:** Create table from autoSql schema.

### Validate schema
**Args:** `autoSql -validate schema.as`
**Explanation:** Validate autoSql schema syntax.
