---
name: gor_pyspark
category: programming
description: gor_pyspark provides Python helper functions for integrating GOR (Genomic Ordered Relations) with PySpark for scalable genomic data processing.
tags: [gor_pyspark, GOR, PySpark, genomic-data, programming]
author: oxo-call-community
source_url: "https://github.com/gorpipe/gor-pyspark"
---

## Concepts

- **GOR-PySpark Integration**: Bridges GOR query language with PySpark's distributed computing capabilities for large-scale genomic analysis.

- **Distributed Processing**: Enables processing of genomic data across Spark clusters for improved scalability.

- **Data Conversion**: Provides utilities for converting between GOR format and Spark DataFrames.

- **Query Optimization**: Optimizes GOR queries for execution on Spark clusters.

- **Variant Analysis**: Supports variant filtering, annotation, and statistical analysis at scale.

- **Reproducibility**: Facilitates reproducible genomic analysis workflows using Spark's lineage tracking.

## Pitfalls

- **Cluster Configuration**: Requires proper Spark cluster configuration for optimal performance.

- **Data Partitioning**: Poor partitioning can significantly impact performance. Partition data by chromosome when possible.

- **Memory Management**: Large datasets require careful memory management. Consider broadcast joins for small lookup tables.

- **Serialization**: Ensure proper serialization of genomic data when transferring between nodes.

- **Version Compatibility**: Check compatibility between gor_pyspark, PySpark, and GOR versions.

## Examples

### Initialize GOR Spark session
**Args:** `from gor_pyspark import GORSession; gor = GORSession(spark)`
**Explanation:** Creates a GOR session integrated with an existing Spark session.

### Read GOR file into DataFrame
**Args:** `df = gor.read.gor('data.gor')`
**Explanation:** Reads a GOR file and returns it as a Spark DataFrame.

### Execute GOR query
**Args:** `result = gor.execute('gor data.gor | where CHROM="chr1"')`
**Explanation:** Executes a GOR query and returns the result as a DataFrame.

### Write DataFrame to GOR format
**Args:** `df.write.gor('output.gor')`
**Explanation:** Writes a Spark DataFrame to GOR format for downstream analysis.

### Join with variant data
**Args:** `variants = gor.read.gor('variants.gor'); genes = gor.read.gor('genes.gor'); joined = variants.join(genes, on=['CHROM', 'POS'])`
**Explanation:** Joins variant and gene DataFrames on genomic coordinates.

### Filter and aggregate
**Args:** `result = df.filter(df.QUAL > 30).groupBy('CHROM').count()`
**Explanation:** Filters variants by quality and counts variants per chromosome.

### Broadcast small DataFrame
**Args:** `from pyspark.sql.functions import broadcast; joined = df.join(broadcast(small_df), on='ID')`
**Explanation:** Broadcasts a small DataFrame for efficient join operations.