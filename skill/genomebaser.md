---
name: genomebaser
category: data-management
description: GenomeBaser - Manages complete (bacterial) genomes from NCBI.
tags: [genomebaser, genome-management, ncbi, bacterial-genomics]
author: oxo-call-community
source_url: "http://github.com/mscook/GenomeBaser"
---

## Concepts
- **Genome Management**: Manages complete bacterial genomes.
- **NCBI Integration**: Integrates with NCBI databases.
- **Data Retrieval**: Retrieves genome data from NCBI.
- **Genome Annotation**: Manages genome annotations.
- **Database Management**: Maintains local genome database.

## Pitfalls
- **Network Dependency**: Requires network access for NCBI queries.
- **Data Updates**: Requires regular database updates.
- **Storage Requirements**: Large genomes require significant storage.
- **Format Compatibility**: Requires specific input/output formats.
- **Data Integrity**: Requires data validation.

## Examples
### Retrieve genome
**Args:** `genomebaser get -a NC_000913 -o ecoli.fasta`
**Explanation:** Retrieves genome by accession number.

### Search genomes
**Args:** `genomebaser search -s "Escherichia coli" -o results.txt`
**Explanation:** Searches for genomes by species name.

### Download batch
**Args:** `genomebaser batch -l accessions.txt -o ./genomes/`
**Explanation:** Downloads multiple genomes in batch.

### Update database
**Args:** `genomebaser update`
**Explanation:** Updates local genome database.

### List genomes
**Args:** `genomebaser list -o genomes.txt`
**Explanation:** Lists all genomes in local database.