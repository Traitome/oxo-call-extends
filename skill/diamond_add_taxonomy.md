---
name: diamond_add_taxonomy
category: annotation
description: Utility to annotate DIAMOND results with NCBI taxonomy lineage.
tags: [diamond_add_taxonomy, annotation, taxonomy, diamond, ncbi]
author: oxo-call-community
source_url: "https://github.com/pvanheus/diamond_add_taxonomy"
---

## Concepts

- **Tool Overview**: diamond_add_taxonomy (v0.1.2+) is a utility for adding NCBI taxonomy information to DIAMOND sequence search results.
- **Core Function**: Annotates DIAMOND alignment output with taxonomic lineage information from NCBI taxonomy database.
- **Input/Output**: Input: DIAMOND output (format 6), NCBI taxonomy files. Output: Annotated results with taxonomy lineage.
- **Algorithm**: Maps protein accessions to taxonomic IDs using NCBI mapping files and retrieves lineage information.
- **Key Features**: NCBI taxonomy integration, DIAMOND output support, lineage annotation, batch processing, multiple output formats.
- **Installation**: `conda install -c bioconda diamond_add_taxonomy`

## Pitfalls

- **Input Requirements**: Requires DIAMOND tabular output (format 6) and NCBI taxonomy dump files.
- **Database Updates**: NCBI taxonomy database must be kept current for accurate results.
- **Memory Usage**: May require significant memory for large taxonomy databases.
- **Accession Mapping**: Depends on correct protein accession to taxon ID mapping.
- **File Format**: Input must follow DIAMOND format 6 specifications.

## Examples

### Add taxonomy to DIAMOND results
**Args:** `diamond_add_taxonomy --input diamond.out --taxonmap prot.accession2taxid --taxonnodes nodes.dmp --output annotated.out`
**Explanation:** Adds taxonomy lineage to DIAMOND search results.

### With names file for species names
**Args:** `diamond_add_taxonomy --input diamond.out --taxonmap prot.accession2taxid --taxonnodes nodes.dmp --taxonnames names.dmp --output annotated.out`
**Explanation:** Include species names in output using NCBI names.dmp file.

### Filter by taxonomy rank
**Args:** `diamond_add_taxonomy --input diamond.out --taxonmap prot.accession2taxid --taxonnodes nodes.dmp --output annotated.out --rank species`
**Explanation:** Only include species-level taxonomy information.

### Batch processing multiple files
**Args:** `diamond_add_taxonomy --input-dir diamond_results/ --taxonmap prot.accession2taxid --taxonnodes nodes.dmp --output-dir annotated_results/`
**Explanation:** Process multiple DIAMOND output files in batch.

### Generate summary statistics
**Args:** `diamond_add_taxonomy --input diamond.out --taxonmap prot.accession2taxid --taxonnodes nodes.dmp --output annotated.out --stats taxonomy_stats.txt`
**Explanation:** Generate taxonomy distribution statistics.