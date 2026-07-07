---
name: gtdb_to_taxdump
category: bioinformatics
description: gtdb_to_taxdump converts GTDB taxonomy data into NCBI-style taxdump format for compatibility with bioinformatics tools.
tags: [gtdb_to_taxdump, taxonomy, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/nick-youngblut/gtdb_to_taxdump"
---

## Concepts

- **Taxonomy Conversion**: Converts GTDB taxonomy to NCBI taxdump format.

- **NCBI Compatibility**: Makes GTDB taxonomy compatible with NCBI tools.

- **Taxdump Format**: Generates names.dmp and nodes.dmp files.

- **Lineage Information**: Preserves taxonomic lineage information.

- **Database Integration**: Enables integration with existing bioinformatics pipelines.

- **Custom Taxonomy**: Supports creation of custom taxonomy databases.

## Pitfalls

- **Database Compatibility**: Ensure compatibility with target tools.

- **Version Matching**: Match GTDB version with tool expectations.

- **Large Files**: Taxdump files can be large for complete databases.

- **Memory Usage**: Processing large taxonomies may require significant memory.

- **Result Verification**: Verify converted taxonomy is correct.

## Examples

### Convert GTDB to taxdump
**Args:** `gtdb_to_taxdump -i gtdb_taxonomy.tsv -o taxdump/`
**Explanation:** Converts GTDB taxonomy to NCBI taxdump format.

### Include genome information
**Args:** `gtdb_to_taxdump -i gtdb_taxonomy.tsv -g genomes.tsv -o taxdump/`
**Explanation:** Includes genome information in conversion.

### Create custom taxdump
**Args:** `gtdb_to_taxdump -i custom_taxonomy.tsv -o custom_taxdump/`
**Explanation:** Creates taxdump from custom taxonomy file.

### Filter by rank
**Args:** `gtdb_to_taxdump -i gtdb_taxonomy.tsv -r species -o taxdump/`
**Explanation:** Filters taxonomy by specific rank.

### Generate lineage file
**Args:** `gtdb_to_taxdump -i gtdb_taxonomy.tsv -l -o lineage.txt`
**Explanation:** Generates lineage information file.

### Validate taxdump
**Args:** `gtdb_to_taxdump -i gtdb_taxonomy.tsv -v -o taxdump/`
**Explanation:** Validates the generated taxdump files.

### Help command
**Args:** `gtdb_to_taxdump --help`
**Explanation:** Shows available options and usage information.