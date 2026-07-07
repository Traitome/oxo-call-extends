---
name: ucsc-hgfindspec
category: utility
description: UCSC hgFindSpec - Tool for creating hgFindSpec files.
tags: [ucsc-hgfindspec, ucsc, configuration, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgFindSpec - A tool for creating hgFindSpec configuration files.
- **Core Function**: Generates configuration files for genome browser search.
- **Input**: Database information.
- **Output**: hgFindSpec file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser configuration, search setup.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Format Requirements**: Requires proper format specification.

## Examples

### Create hgFindSpec
**Args:** `hgFindSpec -db=hg38 > hgFindSpec.txt`
**Explanation:** Create hgFindSpec file.

### With options
**Args:** `hgFindSpec -db=hg38 -includeAll > hgFindSpec.txt`
**Explanation:** Include all tables.
