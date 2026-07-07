---
name: oxbow
category: formatting
description: Oxbow reads genomic file formats into data frames for analysis.
tags: [oxbow, formatting, genomics, data-frames]
author: oxo-call-community
source_url: "https://github.com/abdenlab/oxbow"
---

## Concepts

- **Tool Overview**: Oxbow converts genomic formats to data frames.
- **Core Function**: Reads and transforms genomic data formats.
- **Algorithm**: Uses efficient parsing and conversion.
- **Input Format**: Accepts BED, GTF, VCF, and other genomic formats.
- **Output**: Produces pandas/polars data frames.
- **Use Case**: Genomic data analysis, data transformation, and integration.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Format Support**: Limited to specific formats.
- **Data Types**: May have type conversion issues.
- **Performance**: May be slow for very large files.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "import oxbow; help(oxbow)"`
**Explanation:** Shows available options and usage instructions.

### Read BED file
**Args:** `python -c "df = oxbow.read_bed('regions.bed')"`
**Explanation:** Reads BED file into data frame.

### Read GTF file
**Args:** `python -c "df = oxbow.read_gtf('annotation.gtf')"`
**Explanation:** Reads GTF file into data frame.

### Read VCF file
**Args:** `python -c "df = oxbow.read_vcf('variants.vcf')"`
**Explanation:** Reads VCF file into data frame.

### Output format
**Args:** `python -c "df = oxbow.read_bed('regions.bed', format='polars')"`
**Explanation:** Returns Polars data frame.

### Verbose mode
**Args:** `python -c "df = oxbow.read_bed('regions.bed', verbose=True)"`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `python -c "dfs = [oxbow.read_bed(f) for f in files]"`
**Explanation:** Processes multiple files.