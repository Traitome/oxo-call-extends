---
name: ganon
category: metagenomics
description: Ganon2 classifies genomic sequences against large sets of references efficiently.
tags: [ganon, metagenomics, taxonomic classification, sequence analysis]
author: oxo-call-community
source_url: "https://github.com/pirovc/ganon"
---

## Concepts
- **Large-scale Classification**: Classifies sequences against large reference sets.
- **Efficient Indexing**: Uses efficient indexing for large databases.
- **Taxonomic Profiling**: Provides taxonomic profiling of samples.
- **NCBI/GTDB Support**: Supports NCBI and GTDB taxonomies.
- **Hierarchical Classification**: Supports hierarchical classification.

## Pitfalls
- **Database Size**: Large databases require significant storage.
- **Memory Usage**: High memory usage for large queries.
- **Index Building**: Building index can be time-consuming.
- **Classification Sensitivity**: May miss distant relatives.
- **Database Updates**: Requires regular database updates.

## Examples
### Build database
**Args:** `ganon build --references genomes.fasta -o ganon_db`
**Explanation:** Builds ganon database from reference genomes.

### Classify reads
**Args:** `ganon classify -d ganon_db -r reads_1.fastq -r reads_2.fastq -o results/`
**Explanation:** Classifies metagenomic reads.

### Taxonomic profiling
**Args:** `ganon profile -d ganon_db -r reads.fastq -o profile.txt`
**Explanation:** Generates taxonomic profile.

### Update database
**Args:** `ganon update -d ganon_db -o ganon_db_updated`
**Explanation:** Updates existing database.

### Export results
**Args:** `ganon export -i results.ganon -o results.tsv`
**Explanation:** Exports classification results.