---
name: eider
category: formatting
description: "Command line bioinformatics tools for DuckDB."
tags: [eider, formatting, DuckDB, data-management, bioinformatics-database]
author: oxo-call-community
source_url: "https://github.com/heuermh/eider"
---

## Concepts

- **Tool Overview**: Eider is a collection of command-line tools that integrate bioinformatics data processing with DuckDB, an embedded analytical database.
- **Core Function**: Provides efficient querying and manipulation of bioinformatics data using DuckDB's SQL interface and columnar storage.
- **Input/Output**: Input: VCF, GFF, BED, and other bioinformatics formats. Output: Query results, filtered data, statistical summaries.
- **Algorithm**: Leverages DuckDB's vectorized query execution engine for fast data processing and analysis.
- **Key Features**: SQL-based querying, efficient data filtering, format conversion, statistical analysis, integration with bioinformatics workflows.
- **Installation**: `conda install -c bioconda eider`

## Pitfalls

- **Database Size**: Large datasets require careful memory management.
- **SQL Knowledge**: Requires basic SQL knowledge for effective use.
- **Format Support**: Not all bioinformatics formats may be supported.
- **Performance**: Query performance depends on data size and complexity.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Query VCF file
**Args:** `eider query "SELECT * FROM variants.vcf WHERE QUAL > 30"`
**Explanation:** Queries VCF file using SQL to filter high-quality variants.

### Convert format
**Args:** `eider convert input.vcf output.parquet`
**Explanation:** Converts VCF to Parquet format for efficient storage.

### Statistical summary
**Args:** `eider stats variants.vcf`
**Explanation:** Generates statistical summary of variant data.

### Join datasets
**Args:** `eider query "SELECT a.*, b.info FROM variants.vcf a JOIN annotations.gff b ON a.chrom = b.chrom"`
**Explanation:** Joins VCF variants with GFF annotations.

### Export results
**Args:** `eider export "SELECT * FROM variants.vcf" -o filtered.vcf`
**Explanation:** Exports query results to VCF format.