---
name: gorpipe
category: bioinformatics
description: GorPipe is a query tool for genomic data based on Genomic Ordered Relations (GOR), enabling efficient processing of ordered genomic data.
tags: [gorpipe, GOR, genomic-data, query, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gorpipe/gor"
---

## Concepts

- **Genomic Ordered Relations**: GOR is a query language designed specifically for genomic data, leveraging the inherent order of genomic coordinates.

- **Efficient Querying**: Optimized for processing large-scale genomic datasets with operations like filtering, joining, and aggregating.

- **Streaming Processing**: Processes data in a streaming fashion, enabling analysis of datasets larger than available memory.

- **Variant Analysis**: Supports variant calling, filtering, and annotation workflows.

- **Parallel Execution**: Supports parallel processing for improved performance on multi-core systems.

- **Integration**: Works with various genomic data formats including BED, VCF, and custom GOR formats.

## Pitfalls

- **Data Ordering**: GOR relies on data being ordered by genomic position. Ensure input files are properly sorted.

- **Memory Management**: While streaming reduces memory usage, complex queries may still require careful resource management.

- **Query Complexity**: Complex joins and aggregations can be computationally intensive. Optimize queries for performance.

- **Format Compatibility**: Ensure input files match expected formats. Convert files to GOR format when necessary.

- **Indexing**: Proper indexing can significantly improve query performance. Create indexes for frequently queried datasets.

## Examples

### Basic GOR query
**Args:** `gor data.gor | where CHROM='chr1' and POS between 1000000 and 2000000`
**Explanation:** Filters genomic data to include only positions on chromosome 1 between 1MB and 2MB.

### Join with variant data
**Args:** `gor variants.gor | join -snps genes.gor | select CHROM, POS, REF, ALT, GENE`
**Explanation:** Joins variant data with gene annotations and selects specific columns.

### Aggregate statistics
**Args:** `gor data.gor | group CHROM | count | sort -gc`
**Explanation:** Counts records per chromosome and sorts by count in descending order.

### Filter by quality
**Args:** `gor variants.gor | where QUAL > 30`
**Explanation:** Filters variants to include only those with quality scores above 30.

### Create index
**Args:** `gor data.gor | index -i data.gor.index`
**Explanation:** Creates an index file for faster querying of the dataset.

### Stream from URL
**Args:** `gor https://example.com/data.gor | head -100`
**Explanation:** Streams data from a remote URL and displays the first 100 records.

### Merge multiple files
**Args:** `merge gor file1.gor file2.gor file3.gor`
**Explanation:** Merges multiple GOR files into a single sorted output.