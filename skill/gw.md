---
name: gw
category: bioinformatics
description: gw is a command-line tool for viewing and analyzing genomic sequencing data and VCF files.
tags: [gw, VCF, genomic-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/kcleal/gw"
---

## Concepts

- **Genomic Data Viewer**: gw provides a command-line interface for viewing genomic data.

- **VCF Analysis**: Analyzes and visualizes VCF files.

- **Variant Filtering**: Filters variants based on various criteria.

- **Region Selection**: Views specific genomic regions.

- **Quality Assessment**: Assesses variant quality.

- **Interactive Mode**: Supports interactive exploration of data.

## Pitfalls

- **File Size**: Large files may require significant memory.

- **VCF Format**: Requires properly formatted VCF input.

- **Reference Genome**: Ensure VCF matches reference genome.

- **Filter Complexity**: Complex filters may be computationally intensive.

- **Output Interpretation**: Interpret results carefully.

## Examples

### View VCF file
**Args:** `gw view input.vcf`
**Explanation:** Views VCF file content.

### View specific region
**Args:** `gw view input.vcf -r chr1:1000000-2000000`
**Explanation:** Views variants in a specific genomic region.

### Filter by quality
**Args:** `gw view input.vcf -q 30`
**Explanation:** Filters variants by quality score.

### Interactive mode
**Args:** `gw view input.vcf -i`
**Explanation:** Opens interactive viewer.

### Generate statistics
**Args:** `gw stats input.vcf`
**Explanation:** Generates VCF statistics.

### Convert to BED
**Args:** `gw convert input.vcf -f bed -o output.bed`
**Explanation:** Converts VCF to BED format.

### Help command
**Args:** `gw --help`
**Explanation:** Shows available options and usage information.