---
name: mashpit
category: utility
description: Sketch-based surveillance platform for pathogen monitoring and tracking.
tags: [mashpit, surveillance, pathogen, MinHash]
author: oxo-call-community
source_url: "https://github.com/tongzhouxu/mashpit"
---

## Concepts

- **Tool Overview**: Mashpit is a sketch-based surveillance platform for pathogen monitoring.
- **Core Function**: Enables rapid identification and tracking of pathogens using MinHash.
- **Surveillance Pipeline**: Integrates sequence sketching, comparison, and clustering.
- **Database Integration**: Supports building and querying reference databases of pathogen genomes.
- **Phylogenetic Analysis**: Provides tree-based visualization of relationships.
- **Installation**: `conda install -c bioconda mashpit` or via GitHub repository.

## Pitfalls

- **Database Maintenance**: Reference database requires regular updates for new strains.
- **Computational Resources**: Large databases may require significant storage and computation.
- **False Positives**: Threshold settings affect sensitivity and specificity.
- **Data Quality**: Poor quality sequences can produce unreliable results.
- **Network Requirements**: Database queries may require network access or local installation.
- **Version Compatibility**: Ensure compatibility with Mash tool versions.

## Examples

### Initialize database
**Args:** `mashpit init -d my_db`
**Explanation:** Creates new surveillance database.

### Add reference sequences
**Args:** `mashpit add -d my_db -f genomes/*.fasta`
**Explanation:** Adds genome sequences to database.

### Query database
**Args:** `mashpit query -d my_db -q query.fasta`
**Explanation:** Searches database for matching sequences.

### Build phylogenetic tree
**Args:** `mashpit tree -d my_db -o tree.nwk`
**Explanation:** Generates phylogenetic tree from database.

### Update database
**Args:** `mashpit update -d my_db -f new_genomes/*.fasta`
**Explanation:** Adds new sequences to existing database.

### Export distances
**Args:** `mashpit dist -d my_db -o distances.csv`
**Explanation:** Exports distance matrix from database.
