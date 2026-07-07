---
name: ucsc-hgloadmaf
category: utility
description: UCSC hgLoadMaf - Tool for loading MAF files into database.
tags: [ucsc-hgloadmaf, ucsc, database, maf, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadMaf - A tool for loading MAF alignment files into database.
- **Core Function**: Loads MAF multiple alignment data into genome browser database.
- **Input**: MAF file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, multiple alignment, comparative genomics.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large files.

## Examples

### Load MAF to database
**Args:** `hgLoadMaf -db=hg38 -table=maf input.maf`
**Explanation:** Load MAF file to database.

### With options
**Args:** `hgLoadMaf -db=hg38 -table=maf -verbose input.maf`
**Explanation:** Load with verbose output.
