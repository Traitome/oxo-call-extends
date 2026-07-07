---
name: ccp4srs
category: protein-structure
description: CCP4 Storage, Retrieval and Search framework for small-molecule crystallographic data
tags: [ccp4srs, ccp4, crystallography, cif, small-molecule]
author: oxo-call-community
source_url: "https://ccp4forge.rc-harwell.ac.uk/ccp4/ccp4srs"
---

## Concepts

- **Tool Overview**: CCP4SRS is part of the CCP4 suite for handling crystallographic small-molecule data.
- **Core Function**: Stores, retrieves, and searches Crystallographic Information File (CIF) library files.
- **Database Management**: Manages small-molecule crystallographic data and CIF format libraries.
- **Input**: CIF files and small-molecule structure data.
- **Output**: Structured crystallographic data and search results.
- **Application**: Protein-ligand complex analysis and crystallographic structure determination.
- **Installation**: Install via bioconda: `conda install -c bioconda ccp4srs`

## Pitfalls

- **CIF Format**: Requires properly formatted CIF files.
- **Database Setup**: May require initial database configuration.
- **Memory Usage**: Large crystallographic databases may require significant memory.
- **CCP4 Integration**: Designed to work within the CCP4 suite environment.

## Examples

### Search for small molecules
**Args:** `ccp4srs search -p "benzene" -o results.cif`
**Explanation:** Searches CCP4SRS database for benzene-related structures.

### Retrieve structure by ID
**Args:** `ccp4srs retrieve -i "COD-12345" -o structure.cif`
**Explanation:** Retrieves specific structure from database by ID.

### Build local database
**Args:** `ccp4srs build -d cif_files/ -o local_db/`
**Explanation:** Builds local CCP4SRS database from CIF files.

### Display help
**Args:** `ccp4srs --help`
**Explanation:** Shows all available options and usage information.