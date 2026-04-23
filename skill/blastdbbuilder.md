---
name: blastdbbuilder
category: alignment
description: Build custom BLAST reference databases from NCBI genomes
tags: [blastdbbuilder, blast, database, ncbi, reference]
author: oxo-call-community
source_url: "https://github.com/asadprodhan/blastdbbuilder"
---

## Concepts

- **Tool Overview**: BlastDBBuilder creates custom BLAST reference databases from NCBI genome data.
- **Core Function**: Downloads and formats NCBI genomes into BLAST databases.
- **Input**: NCBI genome accessions or search queries.
- **Output**: Formatted BLAST database files ready for searching.
- **Features**: Automated download, concatenation, and database building.
- **Installation**: Install via bioconda: `conda install -c bioconda blastdbbuilder`

## Pitfalls

- **Network Required**: Requires internet connection for genome downloads.
- **Disk Space**: Large databases require significant storage.
- **NCBI Rate Limits**: Frequent downloads may be rate-limited.
- **Database Updates**: Periodically rebuild to include new genome submissions.

## Examples

### Build database from accessions
**Args:** `blastdbbuilder -a GCF_000001405.40,GCF_000001635.27 -o custom_db`
**Explanation:** Downloads specified NCBI genomes and builds BLAST database.

### Build from taxonomic group
**Args:** `blastdbbuilder -t bacteria -o bacteria_db`
**Explanation:** Downloads bacterial genomes and builds BLAST database.

### Build protein database
**Args:** `blastdbbuilder -a GCF_000001405.40 -p -o protein_db`
**Explanation:** Builds protein BLAST database from specified genome.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
