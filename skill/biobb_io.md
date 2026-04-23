---
name: biobb_io
category: utility
description: BioBB module for fetching data to be consumed by other BioBB blocks
tags: [bioexcel, data-fetching, api, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_io"
---

## Concepts
- **Tool Overview**: biobb_io provides BioExcel Building Blocks for fetching data from external databases and APIs (PDB, PDBe, RCSB, etc.).
- **Data Sources**: Protein Data Bank, UniProt, AlphaFold DB, and other structural biology databases.
- **Applications**: Automated structure retrieval, pipeline data input, database querying.

## Pitfalls
- **Network Dependency**: Requires internet connectivity for database access.
- **API Changes**: External APIs may change, affecting data retrieval.

## Examples
### Fetch PDB structure
**Args:** `biobb_io.pdb --pdb_code 1ABC --output structure.pdb`
**Explanation:** Downloads a PDB structure from RCSB PDB.

### Fetch AlphaFold model
**Args:** `biobb_io.alphafold --uniprot_id P12345 --output model.pdb`
**Explanation:** Downloads an AlphaFold predicted structure.
