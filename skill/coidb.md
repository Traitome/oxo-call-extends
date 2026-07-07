---
name: coidb
category: utility
description: Tool to obtain and maintain a database of COI metabarcode references
tags: [coidb, coi-barcode, metabarcoding, bioinformatics, taxonomy]
author: oxo-call-community
source_url: "https://github.com/johnne/coidb"
---

## Concepts

- **Tool Overview**: coidb is a tool for managing and querying databases of COI (Cytochrome Oxidase subunit I) metabarcode references, commonly used in DNA barcoding and biodiversity studies.
- **Core Function**: Downloads, updates, and maintains reference databases of COI sequences for taxonomic identification.
- **Algorithm**: Manages sequence databases with taxonomic annotations for rapid lookup and matching.
- **Input**: Optional query sequences or database configuration files.
- **Output**: COI reference database and taxonomic identification results.
- **Application**: DNA barcoding, biodiversity assessment, and species identification.
- **Installation**: Install via bioconda: `conda install -c bioconda coidb`

## Pitfalls

- **Database Updates**: Requires regular updates for current taxonomic information.
- **Sequence Quality**: Database quality depends on source data.
- **Taxonomic Coverage**: May have limited coverage for some taxa.
- **Memory Usage**: Large databases may require significant memory.
- **Network Access**: Requires internet for database downloads.

## Examples

### Download COI database
**Args:** `coidb download -o coi_database.fasta`
**Explanation:** Downloads COI reference sequences from public databases.

### Update existing database
**Args:** `coidb update -i coi_database.fasta -o updated_database.fasta`
**Explanation:** Updates existing COI database with new sequences.

### Query database
**Args:** `coidb query -d coi_database.fasta -q query.fasta -o results.tsv`
**Explanation:** Queries COI database with query sequences for taxonomic identification.

### Display help
**Args:** `coidb --help`
**Explanation:** Shows all available options and usage information.