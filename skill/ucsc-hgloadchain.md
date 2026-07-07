---
name: ucsc-hgloadchain
category: utility
description: UCSC hgLoadChain - Tool for loading chain files into database.
tags: [ucsc-hgloadchain, ucsc, database, chain, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadChain - A tool for loading chain files into database.
- **Core Function**: Loads chain alignment data into genome browser database.
- **Input**: Chain file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, alignment data, comparative genomics.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large files.

## Examples

### Load chain to database
**Args:** `hgLoadChain -db=hg38 -table=chain input.chain`
**Explanation:** Load chain file to database.

### With options
**Args:** `hgLoadChain -db=hg38 -table=chain -verbose input.chain`
**Explanation:** Load with verbose output.
