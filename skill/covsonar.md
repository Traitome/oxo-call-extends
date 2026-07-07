---
name: covsonar
category: utility
description: Database-driven system for handling SARS-CoV-2 genomic sequences and screening genomic profiles
tags: [covsonar, sars-cov-2, database, genomic-sequences, variant-tracking, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rki-mf1/covsonar"
---

## Concepts

- **Tool Overview**: covsonar (also known as sonar) is a database-driven system for storing, querying, and analyzing SARS-CoV-2 genomic sequences and mutations. Developed by RKI (Robert Koch Institute) for pathogen genomics surveillance.
- **Core Function**: Manages genomic sequence databases, enables mutation screening, and supports genomic profiling for variant tracking.
- **Algorithm**: Uses SQLite database backend for efficient storage and querying of sequences, mutations, and metadata.
- **Input**: FASTA sequences, VCF files, lineage data, metadata tables.
- **Output**: Query results, filtered sequence sets, VCF exports, mutation reports.
- **Application**: SARS-CoV-2 genomic surveillance, variant of concern tracking, mutation screening, wastewater-based epidemiology.
- **Installation**: Install via bioconda: `conda install -c bioconda covsonar`

## Pitfalls

- **Database Initialization**: Requires proper database setup before first use.
- **Sequence Format**: Input sequences must be properly formatted FASTA.
- **Metadata Requirements**: Complete metadata (dates, locations, lineages) improves analysis value.
- **Database Updates**: Regular updates needed for current variant definitions.
- **Accession Management**: Be careful when removing sequences as it affects downstream analysis continuity.

## Examples

### Check version
**Args:** `sonar --version`
**Explanation:** Verifies installation and shows the installed version of covsonar.

### Add sequences to database
**Args:** `sonar add --acc ACC1 ACC2 --file sequences.fasta --db mydb`
**Explanation:** Adds one or more sequences to the database with specified accessions.

### Remove sequences from database
**Args:** `sonar remove --acc ACC1 ACC5 --db mydb`
**Explanation:** Removes specific sequences by accession number from the database.

### Remove sequences from file
**Args:** `sonar remove --file to_delete.txt --db mydb`
**Explanation:** Removes all accessions listed in a file (one per line) from the database.

### Query mutations
**Args:** `sonar query --mut S:N501Y --db mydb`
**Explanation:** Queries database for sequences containing a specific mutation (S:N501Y in this case).

### Export database to VCF
**Args:** `sonar export --db mydb --out variants.vcf`
**Explanation:** Exports the database contents to VCF format for downstream analysis.

### Search with lineage filter
**Args:** `sonar query --lineage B.1.617.2 --db mydb`
**Explanation:** Retrieves all sequences belonging to a specific Pango lineage.

### Filter by date range
**Args:** `sonar query --from 2022-01-01 --to 2022-03-31 --db mydb`
**Explanation:** Filters sequences by collection date range.
