---
name: ncbi-vdb
category: utility
description: NCBI VDB is the columnar database engine used by SRA tools for storing sequencing data.
tags: [ncbi-vdb, utility, sra, database, sequencing]
author: oxo-call-community
source_url: "https://github.com/ncbi/ncbi-vdb"
---

## Concepts

- **Tool Overview**: NCBI VDB (Virtual Database) is the columnar database engine underlying NCBI's SRA tools.
- **Core Function**: Provides efficient storage and retrieval of sequencing data in a compressed, columnar format.
- **Algorithm**: Implements columnar storage with specialized compression for sequencing data characteristics.
- **Input Format**: Accepts sequencing data in various formats including FASTQ, BAM, and SRA.
- **Output**: Provides fast access to sequencing reads, alignments, and metadata.
- **Use Case**: SRA data access, sequence analysis pipelines, and large-scale sequencing data management.

## Pitfalls

- **Complex Setup**: Requires proper configuration for optimal performance.
- **Memory Usage**: Can consume significant memory for large datasets.
- **Version Compatibility**: Database format may change between versions.
- **Platform Specific**: Some features may be platform-specific.
- **Documentation**: Requires careful reading of API documentation.
- **Data Migration**: Upgrading between versions may require data migration.

## Examples

### Display help
**Args:** `vdb-config --help`
**Explanation:** Shows available configuration options.

### Configure VDB
**Args:** `vdb-config --interactive`
**Explanation:** Launches interactive configuration tool.

### Check SRA file
**Args:** `vdb-validate SRR1234567.sra`
**Explanation:** Validates SRA file integrity.

### Convert SRA to FASTQ
**Args:** `fastq-dump SRR1234567.sra`
**Explanation:** Extracts FASTQ reads from SRA file.

### Prefetch SRA data
**Args:** `prefetch SRR1234567`
**Explanation:** Downloads SRA data from NCBI.

### List database contents
**Args:** `vdb-dump SRR1234567.sra --header`
**Explanation:** Shows metadata for SRA file.