---
name: chado-tools
category: database
description: Tools for accessing and managing CHADO genome database schema
tags: [chado-tools, chado, database, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/chado-tools"
---

## Concepts

- **Tool Overview**: chado-tools provides utilities for accessing and managing data in CHADO genome database schema.
- **Core Function**: Enables querying, loading, and managing genomic data in CHADO databases.
- **Features**: Data import/export, query building, schema management, and data validation.
- **Input**: Genomic data files (FASTA, GFF, VCF, etc.) and database queries.
- **Output**: Query results, database exports, and validation reports.
- **Application**: Genome annotation management and comparative genomics data integration.
- **Installation**: Install via bioconda: `conda install -c bioconda chado-tools`

## Pitfalls

- **Database Setup**: Requires CHADO database schema installation and configuration.
- **PostgreSQL Dependencies**: Requires PostgreSQL database server.
- **Permissions**: Requires appropriate database user permissions.
- **Data Integrity**: Ensure data consistency during bulk imports.

## Examples

### Load GFF into CHADO
**Args:** `chado-tools load --file annotation.gff --format gff`
**Explanation:** Loads GFF annotation file into CHADO database.

### Query genes by organism
**Args:** `chado-tools query --organism "E. coli" --feature-type gene`
**Explanation:** Queries all genes for specified organism.

### Export data to GFF
**Args:** `chado-tools export --output genes.gff --feature-type gene`
**Explanation:** Exports gene features from CHADO to GFF format.

### Display help
**Args:** `chado-tools --help`
**Explanation:** Shows all available options and usage information.