---
name: joltax
category: programming
description: JolTax is a high-performance, vectorized taxonomy library for Python.
tags: [joltax, programming, taxonomy, bioinformatics, python]
author: oxo-call-community
source_url: "https://github.com/SweBiTS/JolTax"
---

## Concepts

- **Tool Overview**: joltax (v0.3.0) - A high-performance, vectorized taxonomy library for Python designed for bioinformatics applications.
- **Vectorized Operations**: Uses vectorized operations for fast taxonomy lookups.
- **Taxonomy Data**: Supports NCBI taxonomy database and custom taxonomies.
- **Lineage Information**: Provides complete lineage information for taxa.
- **Python Integration**: Integrates seamlessly with Python bioinformatics workflows.
- **Memory Efficient**: Optimized memory usage for large-scale taxonomy operations.

## Pitfalls

- **Database Updates**: Taxonomy databases require regular updates.
- **Ambiguous Taxa**: Some taxonomic names may be ambiguous.
- **Memory Usage**: Large taxonomy databases require significant memory.
- **Version Compatibility**: API may change between versions.
- **Network Access**: May require network access for database updates.
- **Taxon IDs**: Requires correct taxon IDs for accurate lookups.

## Examples

### Load taxonomy database
**Args:** `import joltax; tax = joltax.Taxonomy("ncbi_taxonomy.db")`
**Explanation:** Loads NCBI taxonomy database into memory.

### Get lineage information
**Args:** `lineage = tax.get_lineage(9606)`
**Explanation:** Retrieves complete lineage for Homo sapiens (taxid 9606).

### Batch taxon lookup
**Args:** `taxa = tax.query_taxa(["Homo sapiens", "Mus musculus", "E. coli"])`
**Explanation:** Looks up multiple taxa by name in batch.

### Check taxonomic rank
**Args:** `rank = tax.get_rank(9606)`
**Explanation:** Returns the taxonomic rank for a given taxon ID.

### Find common ancestor
**Args:** `ancestor = tax.get_common_ancestor([9606, 10090])`
**Explanation:** Finds common ancestor between human and mouse.

### Export taxonomy tree
**Args:** `tree = tax.export_tree(["Homo sapiens", "Mus musculus"])`
**Explanation:** Exports taxonomy subtree for specified taxa.