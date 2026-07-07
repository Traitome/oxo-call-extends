---
name: ucsc-hgloadbed
category: utility
description: UCSC hgLoadBed - Tool for loading BED files into database.
tags: [ucsc-hgloadbed, ucsc, database, bed, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgLoadBed - A tool for loading BED files into MySQL database.
- **Core Function**: Loads BED format data into genome browser database.
- **Input**: BED file.
- **Output**: Database tables.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, data loading, annotation.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large files.

## Examples

### Load BED to database
**Args:** `hgLoadBed -db=hg38 -table=myTrack input.bed`
**Explanation:** Load BED file to database.

### With options
**Args:** `hgLoadBed -db=hg38 -table=myTrack -verbose input.bed`
**Explanation:** Load with verbose output.
