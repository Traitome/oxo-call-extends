---
name: bed2gff
category: utility
description: bed2gff - Parallel BED to GFF3 format converter
tags: [format-conversion, bed, gff, annotation]
author: oxo-call-community
source_url: "https://github.com/alejandrogzi/bed2gff"
---

## Concepts

- **Tool Overview**: bed2gff converts BED format annotation files to GFF3 format using parallel processing for speed.

- **Parallel Processing**: Uses multiple threads for fast conversion of large files.

- **Format Mapping**: Maps BED fields to appropriate GFF3 attributes.

- **Standard Compliance**: Produces GFF3-compliant output for downstream tools.

## Pitfalls

- **Field Mapping**: BED and GFF3 have different field semantics. Verify conversion accuracy.

- **Feature Types**: GFF3 requires feature type specification. Ensure correct type assignment.

- **Strand Information**: Ensure strand information preserved during conversion.

## Examples

### Basic conversion
**Args:** `bed2gff --input regions.bed --output regions.gff`
**Explanation:** Converts BED file to GFF3 format.

### Parallel processing
**Args:** `bed2gff --input regions.bed --output regions.gff --threads 8`
**Explanation:** Uses 8 threads for faster conversion.

### Specify feature type
**Args:** `bed2gff --input regions.bed --output regions.gff --feature gene`
**Explanation:** Assigns 'gene' as feature type for all regions.
