---
name: ucsc-hgloadoutjoined
category: utility
description: UCSC hgLoadOutJoined - Tool for loading out joined data.
tags: [ucsc-hgloadoutjoined, ucsc, database, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadOutJoined - A tool for loading out joined data into database.
- **Core Function**: Loads joined data tables into genome browser database.
- **Input**: Joined data file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, data integration, annotation.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large files.

## Examples

### Load out joined data
**Args:** `hgLoadOutJoined -db=hg38 -table=out input.txt`
**Explanation:** Load out joined data to database.

### With options
**Args:** `hgLoadOutJoined -db=hg38 -table=out -verbose input.txt`
**Explanation:** Load with verbose output.
