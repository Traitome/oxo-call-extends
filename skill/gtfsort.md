---
name: gtfsort
category: bioinformatics
description: gtfsort sorts GTF files by chromosome, position, and feature type using a lexicographically-based index ordering algorithm.
tags: [gtfsort, GTF-sorting, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/alejandrogzi/gtfsort"
---

## Concepts

- **GTF Sorting**: gtfsort sorts GTF files by genomic coordinates.

- **Lexicographic Ordering**: Uses lexicographic ordering for chromosome names.

- **Coordinate Sorting**: Sorts by position within each chromosome.

- **Feature Type**: Optionally sorts by feature type.

- **Efficient Algorithm**: Optimized for large GTF files.

- **Stream Processing**: Supports streaming for memory efficiency.

## Pitfalls

- **Memory Usage**: Sorting very large files may require significant memory.

- **Chromosome Naming**: Ensure consistent chromosome naming.

- **Coordinate System**: Be aware of 0-based vs 1-based coordinates.

- **Output Format**: Verify output format matches expectations.

- **Compression**: Handle compressed files appropriately.

## Examples

### Sort GTF file
**Args:** `gtfsort -i input.gtf -o sorted.gtf`
**Explanation:** Sorts GTF file by chromosome and position.

### Sort with compression
**Args:** `gtfsort -i input.gtf.gz -o sorted.gtf.gz`
**Explanation:** Handles compressed input and output.

### Sort by feature type
**Args:** `gtfsort -i input.gtf -o sorted.gtf -f`
**Explanation:** Sorts by feature type in addition to coordinates.

### Batch sorting
**Args:** `for f in *.gtf; do gtfsort -i $f -o sorted_$f; done`
**Explanation:** Sorts multiple GTF files in batch.

### Check sorted status
**Args:** `gtfsort -c input.gtf`
**Explanation:** Checks if GTF file is already sorted.

### Custom chromosome order
**Args:** `gtfsort -i input.gtf -o sorted.gtf -k chrom_order.txt`
**Explanation:** Uses custom chromosome ordering file.

### Help command
**Args:** `gtfsort --help`
**Explanation:** Shows available options and usage information.