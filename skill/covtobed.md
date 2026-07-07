---
name: covtobed
category: formatting
description: Convert coverage tracks from BAM files into BED files for genomic coverage analysis
tags: [covtobed, coverage, bam, bed, genomics, sequencing, coverage-analysis]
author: oxo-call-community
source_url: "https://github.com/telatin/covtobed"
---

## Concepts

- **Tool Overview**: covtobed computes coverage from BAM alignments and converts the coverage track into a BED file, making it easy to identify covered regions in a genome.
- **Core Function**: Generates BED files showing genomic regions with sequencing coverage, with filtering options for coverage depth and region length.
- **Algorithm**: Scans BAM alignments to calculate per-base coverage, then outputs contiguous covered regions as BED features.
- **Input**: Sorted BAM file with index (.bai)
- **Output**: BED file with coverage regions (chr, start, end, name with coverage depth)
- **Application**: Identifying covered genomic regions, target enrichment assessment, coverage uniformity analysis, variant calling region definition.
- **Installation**: Install via bioconda: `conda install -c bioconda covtobed`

## Pitfalls

- **BAM Sorting**: Input BAM must be coordinate-sorted for correct operation.
- **Index Requirement**: Requires corresponding .bai index file.
- **Coverage Threshold**: Default minimum coverage is 0, which may include low-quality regions. Adjust based on application needs.
- **Physical Coverage**: Requires paired-end alignments to compute physical (fragment-based) coverage.
- **Invalid Alignments**: By default includes all alignments. Use `-d` flag to filter duplicates and failed QC reads.

## Examples

### Basic conversion (BAM to BED)
**Args:** `covtobed alignments.bam > coverage.bed`
**Explanation:** Converts BAM coverage track to BED file, outputting all covered regions.

### Filter by minimum coverage
**Args:** `covtobed -m 10 alignments.bam > coverage.bed`
**Explanation:** Only includes regions with at least 10x coverage depth.

### Filter by maximum coverage
**Args:** `covtobed -x 500 alignments.bam > coverage.bed`
**Explanation:** Excludes regions with coverage above 500x (useful for filtering PCR duplicates).

### Filter by minimum region length
**Args:** `covtobed -l 100 alignments.bam > coverage.bed`
**Explanation:** Only includes covered regions at least 100bp in length.

### Combined filters
**Args:** `covtobed -m 10 -x 200 -l 50 alignments.bam > coverage.bed`
**Explanation:** Applies multiple filters: min 10x coverage, max 200x, min 50bp length.

### Discard invalid alignments
**Args:** `covtobed -d alignments.bam > coverage.bed`
**Explanation:** Skips duplicates, failed QC reads, and non-primary alignments.

### Physical coverage (paired-end)
**Args:** `covtobed --physical-coverage alignments.bam > coverage.bed`
**Explanation:** Computes physical coverage based on fragment length rather than read overlap.

### Skip low-quality mappings
**Args:** `covtobed -q 20 alignments.bam > coverage.bed`
**Explanation:** Ignores alignments with mapping quality below 20.

### Output per-strand coverage
**Args:** `covtobed --output-strands alignments.bam > coverage.bed`
**Explanation:** Reports coverage statistics separately for forward and reverse strands.
