---
name: ucsc-hgloadwiggle
category: utility
description: UCSC hgLoadWiggle - Tool for loading wiggle data into database.
tags: [ucsc-hgloadwiggle, ucsc, database, wiggle, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadWiggle - A tool for loading wiggle data into database.
- **Core Function**: Loads wiggle track data into genome browser database.
- **Input**: Wiggle file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, visualization, epigenomics.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large files.

## Examples

### Load wiggle data
**Args:** `hgLoadWiggle -db=hg38 -table=wiggle input.wig`
**Explanation:** Load wiggle data to database.

### With options
**Args:** `hgLoadWiggle -db=hg38 -table=wiggle -verbose input.wig`
**Explanation:** Load with verbose output.
