---
name: taxadb
category: taxonomy
description: Locally query the NCBI taxonomy database.
tags: [taxadb, taxonomy, ncbi, database]
author: oxo-call-community
source_url: "https://github.com/HadrienG/taxadb"
---

## Concepts

- **Tool Overview**: taxadb (v0.12.1) provides local NCBI taxonomy queries.
- **Core Function**: Fast local queries to taxonomy database.
- **Algorithm**: SQLite-based taxonomy database access.
- **Input/Output**: Input: TaxIDs/names; Output: Taxonomy information.
- **Applications**: Taxonomy lookup, sequence annotation, metagenomics.
- **Installation**: `conda install -c bioconda taxadb` or pip install.

## Pitfalls

- **Database Size**: Full NCBI taxonomy is large.
- **Update Frequency**: Local database may be outdated.
- **Memory Usage**: Large database requires memory.
- **Query Speed**: Complex queries may be slow.
- **Data Integrity**: Corrupted database affects results.
- **Index Maintenance**: Regular index updates needed.

## Examples

### Display help
**Args:** `taxadb --help`
**Explanation:** Shows available options and usage information.

### Get taxonomy lineage
**Args:** `taxadb lineage --taxid 9606`
**Explanation:** Get taxonomy lineage for human taxid.

### Search by name
**Args:** `taxadb search --name "Homo sapiens"`
**Explanation:** Search taxonomy by organism name.

### Get taxonomy tree
**Args:** `taxadb tree --taxid 9606`
**Explanation:** Get taxonomy tree structure.

### Filter sequences
**Args:** `taxadb filter --input sequences.fasta --output filtered.fasta`
**Explanation:** Add taxonomy to sequence headers.

### Batch lookup
**Args:** `taxadb batch --ids taxids.txt --output results.txt`
**Explanation:** Lookup multiple taxids.

### Export taxonomy
**Args:** `taxadb export --format csv --output taxonomy.csv`
**Explanation:** Export taxonomy database.

### Update database
**Args:** `taxadb update`
**Explanation:** Update local taxonomy database.

### Count taxa
**Args:** `taxadb count --rank species`
**Explanation:** Count species in database.
