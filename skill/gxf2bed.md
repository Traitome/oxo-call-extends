---
name: gxf2bed
category: bioinformatics
description: gxf2bed is a fast converter for transforming GTF/GFF annotation files into BED format.
tags: [gxf2bed, GTF, GFF, BED, format-conversion, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/alejandrogzi/gxf2bed"
---

## Concepts

- **GTF/GFF Conversion**: gxf2bed converts GTF and GFF files to BED format.

- **Fast Processing**: Optimized for speed with large annotation files.

- **Feature Extraction**: Extracts gene, transcript, and exon features.

- **Interval Representation**: Converts annotations to interval-based BED format.

- **Compression Support**: Handles compressed input and output files.

- **Multiple Features**: Supports various feature types from GTF/GFF.

## Pitfalls

- **Format Compliance**: Requires properly formatted GTF/GFF input.

- **Memory Usage**: Very large files may require significant memory.

- **Coordinate System**: Be aware of 0-based vs 1-based coordinates.

- **Attribute Handling**: Complex attributes may require special handling.

- **Output Format**: Verify BED format meets downstream tool requirements.

## Examples

### Convert GTF to BED
**Args:** `gxf2bed -i input.gtf -o output.bed`
**Explanation:** Converts GTF file to BED format.

### Convert GFF to BED
**Args:** `gxf2bed -i input.gff -o output.bed`
**Explanation:** Converts GFF file to BED format.

### Handle compressed input
**Args:** `gxf2bed -i input.gtf.gz -o output.bed`
**Explanation:** Processes compressed GTF file.

### Extract specific features
**Args:** `gxf2bed -i input.gtf -f gene -o genes.bed`
**Explanation:** Extracts only gene features.

### Batch processing
**Args:** `for f in *.gtf; do gxf2bed -i $f -o ${f%.gtf}.bed; done`
**Explanation:** Processes multiple GTF files.

### Compressed output
**Args:** `gxf2bed -i input.gtf -o output.bed.gz`
**Explanation:** Outputs compressed BED file.

### Help command
**Args:** `gxf2bed --help`
**Explanation:** Shows available options and usage information.