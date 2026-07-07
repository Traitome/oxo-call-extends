---
name: ucsc-hgloadout
category: utility
description: UCSC hgLoadOut - Tool for loading out data into database.
tags: [ucsc-hgloadout, ucsc, database, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadOut - A tool for loading out data into database.
- **Core Function**: Loads out data tables into genome browser database.
- **Input**: Out data file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, data loading, annotation.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large files.

## Examples

### Load out data
**Args:** `hgLoadOut -db=hg38 -table=out input.txt`
**Explanation:** Load out data to database.

### With options
**Args:** `hgLoadOut -db=hg38 -table=out -verbose input.txt`
**Explanation:** Load with verbose output.
