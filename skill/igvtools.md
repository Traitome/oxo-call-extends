---
name: igvtools
category: utility
description: Command line tools for IGV data preprocessing and analysis
tags: [igvtools, IGV, preprocessing, TDF, BAM]
author: oxo-call-community
source_url: "http://www.broadinstitute.org/igv/"
---

## Concepts

- **Tool Overview**: igvtools provides command-line utilities for preprocessing genomic data for IGV visualization
- **Core Function**: Converts and indexes data files for efficient IGV loading and display
- **Input/Output**: Supports BAM, SAM, WIG, BED, VCF, and other formats; outputs TDF, indexed files
- **Installation**: `conda install -c bioconda igvtools`
- **Key Features**: Sorting, indexing, coverage calculation, TDF conversion

## Pitfalls

- **Memory Settings**: May require adjusting Java heap size for large files
- **Input Requirements**: Files must be sorted by position for certain operations
- **Genome Compatibility**: Must specify correct genome build for TDF conversion
- **Index Files**: IGV requires corresponding index files for BAM/VCF
- **Java Dependencies**: Requires Java runtime environment

## Examples

### Convert WIG to TDF format
**Args:** `igvtools toTDF input.wig output.tdf hg38`
**Explanation:** Converts a WIG file to IGV's binary TDF format for faster loading.

### Compute coverage from BAM
**Args:** `igvtools count sample.bam output.tdf hg38`
**Explanation:** Computes read coverage and saves as TDF for IGV visualization.

### Index a BAM file
**Args:** `igvtools index sample.bam`
**Explanation:** Creates a BAM index file (.bai) for random access.

### Sort a BED file
**Args:** `igvtools sort input.bed output_sorted.bed`
**Explanation:** Sorts a BED file by genomic position.

### Create TDF with custom zoom levels
**Args:** `igvtools toTDF -z 5 input.wig output.tdf hg38`
**Explanation:** Creates TDF with reduced zoom levels to minimize file size.
