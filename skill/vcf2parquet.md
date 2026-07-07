---
name: vcf2parquet
category: bioinformatics
description: vcf2parquet - VCF to Parquet format converter.
tags: [vcf2parquet, vcf-processing, parquet, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vcf2parquet/"
---

## Concepts

- **Tool Overview**: vcf2parquet - A tool for converting VCF to Parquet format.
- **Core Function**: Converts VCF files to Parquet columnar storage format.
- **Input**: VCF file.
- **Output**: Parquet file.
- **Installation**: Install via pip
- **Use Case**: Format conversion, data analytics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Dependencies**: Requires pyarrow.

## Examples

### Convert to Parquet
**Args:** `vcf2parquet -i input.vcf -o output.parquet`
**Explanation:** Convert VCF to Parquet.

### With options
**Args:** `vcf2parquet -i input.vcf -o output.parquet -t 8`
**Explanation:** Use 8 threads.
