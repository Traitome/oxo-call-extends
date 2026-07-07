---
name: goat
category: utility
description: GoaT CLI provides command line access to the Genomes on a Tree database for querying taxon metadata across the tree of life.
tags: [goat, taxon, metadata, tree-of-life, genomics]
author: oxo-call-community
source_url: "https://github.com/genomehubs/goat-cli"
---

## Concepts

- **Taxon Metadata Query**: GoaT CLI queries the Genomes on a Tree (GoaT) database to retrieve metadata for any taxon across the tree of life. It supports queries by NCBI taxon ID or common/scientific names.

- **API Integration**: The tool accesses GoaT API endpoints to search against taxon and assembly indexes, providing access to genome-relevant metadata like genome size, chromosome number, and assembly span.

- **Batch Processing**: Supports batch queries through input files containing multiple taxon identifiers (up to 500 entries per file), enabling efficient processing of large taxon lists.

- **Tree of Life Integration**: Designed for biodiversity genomics projects like the Darwin Tree of Life and Earth BioGenome Project, providing standardized taxonomic metadata retrieval.

- **Output Formats**: Results are returned in TSV format for easy integration with downstream bioinformatics workflows and analysis pipelines.

## Pitfalls

- **API Rate Limits**: The GoaT API may have rate limits. For large-scale queries, use batch mode with input files rather than repeated single queries.

- **Taxon Identifier Requirements**: Input must be valid NCBI taxon IDs or properly formatted scientific names. Ambiguous or misspelled names may return unexpected results.

- **File Size Constraints**: Batch input files are limited to 500 entries. Split larger lists into multiple files if needed.

- **Network Dependencies**: Requires internet connectivity to access the GoaT API. Offline usage is not supported.

- **Data Currency**: Database contents may not reflect real-time updates. Verify critical taxonomic information with primary sources for publication.

## Examples

### Search for a single taxon by name
**Args:** `search Homo sapiens`
**Explanation:** Queries the GoaT database for Homo sapiens and returns taxon metadata including genome statistics, assembly information, and sequencing project details.

### Query using NCBI taxon ID
**Args:** `search 9606`
**Explanation:** Uses NCBI taxon ID (9606 for Homo sapiens) to retrieve metadata. Taxon IDs provide more precise matching than common names.

### Batch query from file
**Args:** `search --file taxa_list.txt`
**Explanation:** Processes multiple taxa from a text file, with one taxon identifier per line. Supports up to 500 entries per file.

### Retrieve all descendant taxa
**Args:** `search --lineage Mammalia`
**Explanation:** Returns metadata for all taxa within the Mammalia lineage. This is useful for comparative genomics studies across a taxonomic group.

### Output results to file
**Args:** `search Drosophila --output drosophila_metadata.tsv`
**Explanation:** Saves query results to a TSV file for downstream analysis. The output includes columns for taxon ID, name, genome size, and assembly status.

### Get tool version
**Args:** `--version`
**Explanation:** Displays the current GoaT CLI version. Useful for troubleshooting and ensuring compatibility with API requirements.
