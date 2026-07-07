---
name: ucsc-checktablecoords
category: utility
description: UCSC checkTableCoords - Tool for checking table coordinates.
tags: [ucsc-checktablecoords, ucsc, quality-control, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC checkTableCoords - A tool for validating coordinate ranges in database tables.
- **Core Function**: Checks that coordinates in tables are valid and within bounds.
- **Input**: Database table or BED file.
- **Output**: Validation report.
- **Installation**: Part of UCSC utilities
- **Use Case**: Quality control, database validation, genome browser.

## Pitfalls

- **Table Format**: Requires proper table format.
- **Chromosome Names**: Requires matching chromosome names.

## Examples

### Check table coordinates
**Args:** `checkTableCoords -db=hg38 -table=myTable`
**Explanation:** Validate coordinates in database table.

### With BED file
**Args:** `checkTableCoords -bed=regions.bed -chromSizes=chrom.sizes`
**Explanation:** Check BED file coordinates.
