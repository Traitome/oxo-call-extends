---
name: tabix
category: indexing
description: Indexer for TAB-delimited genome position files enabling fast random access.
tags: [tabix, indexing, vcf, bed]
author: oxo-call-community
source_url: "https://github.com/samtools/htslib"
---

## Concepts

- **Tool Overview**: tabix (v1.11) indexes genome position files for fast retrieval.
- **Core Function**: Creates index for tab-delimited genomic coordinate files.
- **Algorithm**: Uses binary search for fast random access to genomic regions.
- **Input/Output**: Input: Tab-delimited file; Output: Indexed file (.tbi).
- **Applications**: Fast retrieval of genomic intervals, variant analysis.
- **Installation**: `conda install -c bioconda tabix` or download from htslib.

## Pitfalls

- **File Format**: Requires proper tab-delimited format with coordinate columns.
- **Sorting**: Input must be sorted by chromosome and position.
- **Index Compatibility**: Index format may vary between versions.
- **Memory Requirements**: Large files require significant memory.
- **Coordinate System**: Uses 1-based indexing.
- **Compression**: Supports gzip-compressed files only.

## Examples

### Display help
**Args:** `tabix --help`
**Explanation:** Shows available options and usage information.

### Index VCF file
**Args:** `tabix -p vcf variants.vcf.gz`
**Explanation:** Create index for gzipped VCF file.

### Index BED file
**Args:** `tabix -p bed regions.bed.gz`
**Explanation:** Create index for gzipped BED file.

### Extract region
**Args:** `tabix variants.vcf.gz chr1:1000000-2000000`
**Explanation:** Extract variants from specific genomic region.

### Multiple regions
**Args:** `tabix variants.vcf.gz chr1:1-1000000 chr2:500000-1500000`
**Explanation:** Extract from multiple regions.

### Using region file
**Args:** `tabix -R regions.txt variants.vcf.gz`
**Explanation:** Extract regions listed in file.

### Output to file
**Args:** `tabix variants.vcf.gz chr1:1-1000000 > region_variants.vcf`
**Explanation:** Save extracted variants to file.

### List sequences
**Args:** `tabix -l variants.vcf.gz`
**Explanation:** List all sequences in indexed file.

### Check index
**Args:** `tabix -c variants.vcf.gz`
**Explanation:** Check index validity.
