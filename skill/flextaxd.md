---
name: flextaxd
category: variant-calling
description: "Flextaxd creates custom Kraken databases from various sources including NCBI, QIIME, and CanSNPer for metagenomic classification."
tags: [flextaxd, variant-calling, metagenomics, kraken, database, bioinformatics, taxonomy]
author: oxo-call-community
source_url: "https://github.com/FOI-Bioinformatics/flextaxd"
---

## Concepts
- **Tool Overview**: Flextaxd is a tool for creating custom Kraken databases from multiple taxonomic sources, enabling flexible metagenomic classification.
- **Core Function**: Builds customized Kraken databases by integrating data from NCBI, QIIME, CanSNPer, and other taxonomic resources.
- **Input/Output**: Input: Taxonomic data sources, sequence files. Output: Custom Kraken database for metagenomic classification.
- **Data Sources**: Supports NCBI RefSeq, QIIME databases, CanSNPer for pathogen typing, and custom sequence collections.
- **Database Customization**: Allows filtering by taxonomic rank, selecting specific organisms, and adding custom sequences.
- **Kraken Compatibility**: Produces databases compatible with Kraken and Kraken2 for fast metagenomic classification.
- **Installation**: `conda install -c bioconda flextaxd` or clone from GitHub. Requires Python 3.x and Biopython.

## Pitfalls
- **Database Size**: Custom databases can become large. Consider disk space requirements before building.
- **Taxonomic Conflicts**: Different sources may have conflicting taxonomic assignments. Resolve conflicts before building.
- **Sequence Quality**: Poor quality sequences affect classification accuracy. Validate sequences before inclusion.
- **Memory Requirements**: Building large databases requires significant memory. Use server resources for large datasets.
- **Update Frequency**: Taxonomic databases require regular updates. Schedule periodic rebuilds for current taxonomy.
- **Kraken Version**: Ensure compatibility with target Kraken version. Kraken and Kraken2 have different database formats.

## Examples
### Build database from NCBI
**Args:** `flextaxd --source ncbi --taxonomy ncbi_taxonomy/ --sequences refseq/ --output kraken_db/`
**Explanation:** Builds Kraken database from NCBI RefSeq sequences.

### Include custom sequences
**Args:** `flextaxd --source ncbi --custom custom_sequences.fasta --output kraken_db/`
**Explanation:** Adds custom sequences to the database during building.

### Filter by taxonomy
**Args:** `flextaxd --source ncbi --taxonomy ncbi_taxonomy/ --filter "Bacteria" --output kraken_db/`
**Explanation:** Creates database containing only bacterial sequences.

### Build from CanSNPer
**Args:** `flextaxd --source cansnder --cansnder-data cansnder_db/ --output kraken_db/`
**Explanation:** Builds database using CanSNPer data for pathogen typing.

### Update existing database
**Args:** `flextaxd --update --db existing_db/ --new-sequences new_data.fasta --output updated_db/`
**Explanation:** Updates existing Kraken database with new sequences.
