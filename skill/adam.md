---
name: adam
category: utility
description: Genomics analysis platform built on Apache Spark, Avro, and Parquet for distributed genomic data processing
tags: [spark, parquet, genomics, distributed, big-data, bam, vcf]
author: oxo-call-community
source_url: "https://github.com/bigdatagenomics/adam"
---

## Concepts

- **Tool Overview**: ADAM is a library and command line tool that enables Apache Spark for parallelizing genomic data analysis across cluster/cloud computing environments.
- **Core Function**: Converts genomic data (BAM, VCF, FASTA, etc.) to Parquet format for efficient distributed processing, and provides genomic analysis operations.
- **Input/Output**: Input: BAM, SAM, VCF, FASTA, BED, GFF/GTF files. Output: Parquet format files for efficient columnar storage and distributed processing.
- **Schema-Based**: Uses Avro schemas to describe genomic sequences, reads, variants/genotypes, and features for consistent data representation.
- **Installation**: Install via bioconda: `conda install -c bioconda adam`

## Pitfalls

- **Spark Required**: Requires Apache Spark - `spark-submit` must be in PATH or SPARK_HOME must be set.
- **Memory Requirements**: Large datasets require proper Spark memory configuration - use `--executor-memory` and `--driver-memory` options.
- **Parquet Format**: Output is in Parquet format by default - use `-single` flag to merge sharded output files.
- **Validation Levels**: Data validation can be STRICT (fail), LENIENT (log warnings), or SILENT (ignore) - choose based on data quality.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows available command line options and subcommands for ADAM.

### Convert BAM to Parquet format
**Args:** `transform -i input.bam -o output.parquet`
**Explanation:** Converts BAM file to Parquet format for efficient distributed processing with Spark.

### Convert VCF to Parquet
**Args:** `vcf2adam -i input.vcf -o variants.parquet`
**Explanation:** Converts VCF file to ADAM Parquet format for variant data analysis.

### Convert FASTA to Parquet
**Args:** `fasta2adam -i reference.fa -o reference.parquet`
**Explanation:** Converts reference FASTA to Parquet format for efficient sequence access.

### Transform with validation
**Args:** `transform -i input.bam -o output.parquet -parquet_block_size 268435456 -parquet_compression_codec SNAPPY`
**Explanation:** Converts with custom Parquet block size (256MB) and Snappy compression for optimized storage.

### Output as single merged file
**Args:** `transform -i input.bam -o output.bam -single -format bam`
**Explanation:** Converts and outputs as single merged BAM file instead of sharded Parquet output.

### Count reads in BAM file
**Args:** `count_kmers -i reads.parquet -k 21 -o kmer_counts.parquet`
**Explanation:** Counts 21-mers in the read dataset stored in Parquet format.
