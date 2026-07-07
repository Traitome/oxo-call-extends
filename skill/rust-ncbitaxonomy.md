---
name: rust-ncbitaxonomy
category: annotation
description: Tools for working with the NCBI Taxonomy database.
tags: ["rust-ncbitaxonomy", "taxonomy", "NCBI", "classification", "bioinformatics"]
author: oxo-call-community
source_url: "https://docs.rs/crate/ncbitaxonomy/1.1.0"
---

## Concepts

- **Tool Overview**: rust-ncbitaxonomy (v1.1.0) is a Rust-based toolkit for working with the NCBI Taxonomy database. It provides utilities for taxonomic classification, lineage resolution, and taxonomy-based filtering of sequence data.
- **Core Function**: Parses NCBI Taxonomy files, builds taxonomic trees, and provides efficient lookup of taxonomic information by ID or name.
- **Algorithm**: Uses tree data structures for efficient taxonomic traversal, supporting parent-child relationships and lineage queries.
- **Input Format**: NCBI Taxonomy dump files (names.dmp, nodes.dmp), sequence files with taxonomic annotations.
- **Output Format**: Taxonomic lineage information, species assignments, filtered sequence data.
- **Use Case**: Metagenomic classification, sequence taxonomy assignment, quality control of taxonomic annotations.

## Pitfalls

- **Database dependency**: Requires local NCBI Taxonomy database installation.
- **Database updates**: Taxonomy database needs regular updates to stay current.
- **Memory usage**: Loading large taxonomy databases requires significant memory.
- **Ambiguous names**: Common names may map to multiple taxa.
- **Taxonomic changes**: NCBI taxonomy IDs may change over time.
- **Parsing errors**: Malformed taxonomy files can cause parsing failures.

## Examples

### Build taxonomy index
**Args:** `ncbitaxonomy build -d /path/to/taxdump -o tax_index`
**Explanation:** `-d` NCBI taxonomy dump directory; `-o` output index directory.

### Query taxon by ID
**Args:** `ncbitaxonomy query --id 9606 -i tax_index`
**Explanation:** `--id` NCBI taxonomy ID; `-i` index directory. Returns taxon information for human.

### Get lineage
**Args:** `ncbitaxonomy lineage --id 287 --format full`
**Explanation:** Returns full taxonomic lineage for E. coli.

### Filter sequences by taxonomy
**Args:** `ncbitaxonomy filter -i sequences.fastq -t tax_index -o filtered.fastq --species "Homo sapiens"`
**Explanation:** Filters sequences belonging to Homo sapiens.

### Validate taxonomy IDs
**Args:** `ncbitaxonomy validate -i ids.txt -t tax_index`
**Explanation:** Validates a list of taxonomy IDs against the database.

### Export taxonomy tree
**Args:** `ncbitaxonomy export -t tax_index -o tree.newick`
**Explanation:** Exports taxonomy tree in Newick format.

### Search by name
**Args:** `ncbitaxonomy search --name "Escherichia coli"`
**Explanation:** Searches for taxa by scientific name.
