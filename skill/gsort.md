---
name: gsort
category: bioinformatics
description: gsort sorts genomic files according to a genome file, enabling efficient genomic data processing.
tags: [gsort, genome-sort, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/brentp/gsort"
---

## Concepts

- **Genomic Sorting**: gsort sorts genomic files based on genome coordinates.

- **Coordinate Ordering**: Orders genomic features by chromosome and position.

- **Genome File**: Uses a genome file to determine sort order.

- **Efficient Processing**: Optimized for fast sorting of large genomic files.

- **Format Support**: Supports BED, GFF, VCF, and other genomic formats.

- **Stream Processing**: Can process files in a streaming manner.

## Pitfalls

- **Genome File Matching**: Ensure genome file matches input file's chromosome naming.

- **Memory Usage**: Sorting large files may require significant memory.

- **Output Format**: Be aware of output format requirements.

- **Compression**: Handle compressed input/output appropriately.

- **Chromosome Order**: Verify chromosome ordering matches expectations.

## Examples

### Sort BED file
**Args:** `gsort input.bed genome.txt > sorted.bed`
**Explanation:** Sorts a BED file according to genome order.

### Sort with compression
**Args:** `gsort <(gunzip -c input.bed.gz) genome.txt | gzip > sorted.bed.gz`
**Explanation:** Handles compressed input and output.

### Sort VCF file
**Args:** `gsort input.vcf genome.txt > sorted.vcf`
**Explanation:** Sorts a VCF file according to genome coordinates.

### Sort GFF file
**Args:** `gsort input.gff genome.txt > sorted.gff`
**Explanation:** Sorts a GFF annotation file.

### Batch sorting
**Args:** `for f in *.bed; do gsort $f genome.txt > sorted_$f; done`
**Explanation:** Sorts multiple BED files in batch.

### Check chromosome order
**Args:** `gsort --check input.bed genome.txt`
**Explanation:** Checks if file is already sorted.

### Help command
**Args:** `gsort --help`
**Explanation:** Shows available options and usage information.