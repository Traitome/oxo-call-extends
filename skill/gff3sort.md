---
name: gff3sort
category: formatting
description: gff3sort - A Perl Script to sort gff3 files for tabix tools.
tags: [gff3sort, formatting, GFF3, tabix, sorting]
author: oxo-call-community
source_url: "https://github.com/billzt/gff3sort"
---

## Concepts
- **File Sorting**: Sorts GFF3 files.
- **Tabix Preparation**: Prepares files for tabix indexing.
- **Coordinate Sorting**: Sorts by genomic coordinates.
- **Data Organization**: Organizes annotation data.
- **Index Preparation**: Prepares files for indexing.

## Pitfalls
- **Format Compatibility**: Requires valid GFF3 format.
- **Sorting Order**: Requires correct sorting order.
- **Memory Usage**: Large files require significant memory.
- **Tabix Compatibility**: Requires tabix-compatible output.
- **Sorting Time**: May take time for large files.

## Examples
### Sort GFF3 file
**Args:** `gff3sort -i annotations.gff3 -o sorted.gff3`
**Explanation:** Sorts GFF3 file by coordinates.

### With tabix index
**Args:** `gff3sort -i annotations.gff3 -t -o sorted.gff3`
**Explanation:** Sorts and creates tabix index.

### Batch processing
**Args:** `gff3sort -l files.txt -o ./sorted/`
**Explanation:** Processes multiple GFF3 files.

### Compressed output
**Args:** `gff3sort -i annotations.gff3 -c -o sorted.gff3.gz`
**Explanation:** Outputs compressed sorted file.

### Generate report
**Args:** `gff3sort -i annotations.gff3 -r -o report.txt`
**Explanation:** Generates sorting report.