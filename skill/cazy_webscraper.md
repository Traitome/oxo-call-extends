---
name: cazy_webscraper
category: database
description: Automates retrieving data from CAZy, builds local CAZyme SQL database, and retrieves associated protein data
tags: [cazy_webscraper, cazy, cazyme, database, sql, uniprot, genbank, pdb]
author: oxo-call-community
source_url: "https://hobnobmancer.github.io/cazy_webscraper"
---

## Concepts

- **Tool Overview**: cazy_webscraper automates data retrieval from the CAZy database and builds a local CAZyme SQL database.
- **Core Function**: Scrapes CAZy database, builds local SQL database, and retrieves associated protein sequences and structures.
- **Data Sources**: CAZy, UniProt, GenBank, and PDB for comprehensive CAZyme annotation.
- **Input**: Optional list of CAZy families or taxa to focus on.
- **Output**: Local SQL database with CAZyme information and associated sequence files.
- **Application**: Building local CAZyme databases for metagenomic analysis and enzyme discovery.
- **Installation**: Install via bioconda: `conda install -c bioconda cazy_webscraper`

## Pitfalls

- **Internet Required**: Requires network access to CAZy and other databases.
- **API Rate Limits**: May hit rate limits when scraping large amounts of data.
- **Database Size**: Local SQL database can be large depending on scope.
- **Time Consuming**: Full database download may take hours.

## Examples

### Build CAZyme database
**Args:** `cazy_webscraper --build --output cazyme_db/`
**Explanation:** Builds local CAZyme SQL database from CAZy.

### Scrape specific families
**Args:** `cazy_webscraper --families GH1 GH2 --output cazyme_db/`
**Explanation:** Scrapes only specific CAZy families.

### Retrieve protein sequences
**Args:** `cazy_webscraper --sequences --db cazyme_db/ --output sequences/`
**Explanation:** Retrieves protein sequences for entries in the database.

### Display help
**Args:** `cazy_webscraper --help`
**Explanation:** Shows all available options and usage information.