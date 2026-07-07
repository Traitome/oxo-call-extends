---
name: gtfparse
category: bioinformatics
description: gtfparse is a Python library for parsing GTF files and extracting genomic features into pandas DataFrames.
tags: [gtfparse, python, GTF-parsing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/openvax/gtfparse"
---

## Concepts

- **GTF Parsing**: gtfparse parses GTF (Gene Transfer Format) files.

- **DataFrame Output**: Extracts genomic features into pandas DataFrames.

- **Feature Extraction**: Extracts genes, transcripts, exons, and other features.

- **Coordinate Handling**: Properly handles genomic coordinates.

- **Attribute Parsing**: Parses GTF attributes into separate columns.

- **Filtering**: Supports filtering by feature type, gene, etc.

## Pitfalls

- **GTF Format**: Ensure input files are properly formatted GTF.

- **Memory Usage**: Large GTF files may require significant memory.

- **Attribute Consistency**: Inconsistent attributes across features can cause issues.

- **Coordinate System**: Be aware of 0-based vs 1-based coordinate systems.

- **Version Compatibility**: Ensure compatibility with pandas versions.

## Examples

### Parse GTF file
**Args:** `from gtfparse import read_gtf; df = read_gtf('genes.gtf')`
**Explanation:** Reads GTF file into a pandas DataFrame.

### Extract genes only
**Args:** `df = read_gtf('genes.gtf', filter_feature_type='gene')`
**Explanation:** Extracts only gene features from GTF.

### Extract transcripts
**Args:** `df = read_gtf('genes.gtf', filter_feature_type='transcript')`
**Explanation:** Extracts only transcript features.

### Filter by gene name
**Args:** `df = read_gtf('genes.gtf'); df = df[df['gene_name'] == 'BRCA1']`
**Explanation:** Filters DataFrame by specific gene name.

### Get exons for a gene
**Args:** `exons = df[(df['feature'] == 'exon') & (df['gene_name'] == 'BRCA1')]`
**Explanation:** Extracts exons for a specific gene.

### Write to CSV
**Args:** `df.to_csv('features.csv', index=False)`
**Explanation:** Saves parsed features to CSV file.

### Parse with custom attributes
**Args:** `df = read_gtf('genes.gtf', usecols=['gene_id', 'gene_name', 'start', 'end'])`
**Explanation:** Reads only specified columns from GTF.