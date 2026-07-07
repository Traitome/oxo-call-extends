---
name: gvcf2bed
category: bioinformatics
description: gvcf2bed converts gVCF files into BED format, enabling visualization and further analysis of genomic variants.
tags: [gvcf2bed, VCF, BED, format-conversion, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/sndrtj/gvcf2bed"
---

## Concepts

- **Format Conversion**: gvcf2bed converts gVCF to BED format.

- **gVCF Processing**: Handles genomic VCF files with genotype information.

- **Region Extraction**: Extracts variant regions from gVCF files.

- **Interval Representation**: Converts variants to interval-based BED format.

- **Compression Support**: Handles compressed gVCF files.

- **Filtering**: Supports filtering by variant type or quality.

## Pitfalls

- **gVCF Format**: Ensure input is properly formatted gVCF.

- **Memory Usage**: Large gVCF files may require significant memory.

- **Coordinate System**: Be aware of 0-based vs 1-based coordinates.

- **Output Format**: Verify BED format meets downstream tool requirements.

- **Compression**: Handle compressed files appropriately.

## Examples

### Convert gVCF to BED
**Args:** `gvcf2bed -i input.g.vcf -o output.bed`
**Explanation:** Converts gVCF file to BED format.

### Handle compressed input
**Args:** `gvcf2bed -i input.g.vcf.gz -o output.bed`
**Explanation:** Processes compressed gVCF file.

### Filter by quality
**Args:** `gvcf2bed -i input.g.vcf -q 30 -o output.bed`
**Explanation:** Filters variants by quality score.

### Batch processing
**Args:** `for f in *.g.vcf; do gvcf2bed -i $f -o ${f%.g.vcf}.bed; done`
**Explanation:** Processes multiple gVCF files.

### Include genotype info
**Args:** `gvcf2bed -i input.g.vcf -g -o output.bed`
**Explanation:** Includes genotype information in output.

### Sort output
**Args:** `gvcf2bed -i input.g.vcf -s -o output.bed`
**Explanation:** Sorts output BED file by genomic coordinates.

### Help command
**Args:** `gvcf2bed --help`
**Explanation:** Shows available options and usage information.