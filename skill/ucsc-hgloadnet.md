---
name: ucsc-hgloadnet
category: utility
description: UCSC hgLoadNet - Tool for loading net files into database.
tags: [ucsc-hgloadnet, ucsc, database, net, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadNet - A tool for loading net alignment files into database.
- **Core Function**: Loads net alignment data into genome browser database.
- **Input**: Net file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, net alignment, comparative genomics.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large files.

## Examples

### Load net to database
**Args:** `hgLoadNet -db=hg38 -table=net input.net`
**Explanation:** Load net file to database.

### With options
**Args:** `hgLoadNet -db=hg38 -table=net -verbose input.net`
**Explanation:** Load with verbose output.
