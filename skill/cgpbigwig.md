---
name: cgpbigwig
category: genomics
description: BigWig manipulation tools using libBigWig and htslib for efficient genomic data processing
tags: [cgpbigwig, bigwig, genomics, htslib, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cancerit/cgpBigWig"
---

## Concepts

- **Tool Overview**: cgpBigWig provides efficient BigWig file manipulation tools using libBigWig and htslib libraries.
- **Core Function**: Enables creation, querying, and manipulation of BigWig format files for genomic data.
- **Features**: BigWig file creation, region extraction, statistics calculation, and format conversion.
- **Input**: BED, WIG, or other genomic data formats.
- **Output**: BigWig files or extracted data in various formats.
- **Application**: Genomic data analysis, visualization preparation, and data processing pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda cgpbigwig`

## Pitfalls

- **File Size**: BigWig files can be very large, requiring sufficient storage.
- **Memory Usage**: Processing large BigWig files may require significant memory.
- **Index Requirement**: BigWig files must be properly indexed for efficient access.
- **Coordinate System**: Requires correct chromosome naming and coordinate conventions.

## Examples

### Create BigWig from BED
**Args:** `cgpBigWig bed2bw -i input.bed -o output.bw -g genome.fa.fai`
**Explanation:** Converts BED file to BigWig format.

### Extract region from BigWig
**Args:** `cgpBigWig extract -i input.bw -c chr1 -s 1000 -e 2000 -o region.txt`
**Explanation:** Extracts data from specified genomic region.

### Get statistics
**Args:** `cgpBigWig stats -i input.bw -c chr1 -s 1 -e 1000000`
**Explanation:** Calculates statistics for specified region.

### Display help
**Args:** `cgpBigWig --help`
**Explanation:** Shows all available options and usage information.