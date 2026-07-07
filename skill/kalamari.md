---
name: kalamari
category: utility
description: A curated database of completed assemblies with taxonomy IDs for reference.
tags: [kalamari, utility, database, assemblies, taxonomy]
author: oxo-call-community
source_url: "https://github.com/lskatz/Kalamari/blob/master/README.md"
---

## Concepts

- **Tool Overview**: kalamari (v5.8.3) - A curated database of completed genome assemblies with taxonomy IDs.
- **Assembly Database**: Contains pre-computed genome assemblies.
- **Taxonomy Integration**: Links assemblies to NCBI taxonomy.
- **Reference Data**: Provides reference sequences for analysis.
- **Update Mechanism**: Regularly updated with new assemblies.
- **Search Functionality**: Allows searching by taxonomy or assembly name.

## Pitfalls

- **Database Size**: Large database requires significant storage.
- **Update Frequency**: May not include latest assemblies immediately.
- **Taxonomy Changes**: NCBI taxonomy updates may affect mappings.
- **Memory Usage**: Loading full database requires memory.
- **Version Compatibility**: Different versions may have different data.
- **Assembly Quality**: Some assemblies may have quality issues.

## Examples

### Download database
**Args:** `kalamari download`
**Explanation:** Downloads the latest Kalamari database.

### Search by taxonomy
**Args:** `kalamari search --taxon "Escherichia coli"`
**Explanation:** Searches for assemblies by taxonomic name.

### List all assemblies
**Args:** `kalamari list`
**Explanation:** Lists all available assemblies in database.

### Get assembly info
**Args:** `kalamari info --assembly GCF_000005845.2`
**Explanation:** Shows detailed information about an assembly.

### Extract sequence
**Args:** `kalamari extract --assembly GCF_000005845.2 -o genome.fasta`
**Explanation:** Extracts assembly sequence to FASTA file.

### Update database
**Args:** `kalamari update`
**Explanation:** Updates database to latest version.