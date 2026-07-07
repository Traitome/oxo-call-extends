---
name: sepp-refsilva128
category: phylogenetics
description: sepp-refsilva128 - SEPP reference package for SILVA 128
tags: ["sepp-refsilva128", "phylogenetics", "reference-database", "SILVA"]
author: oxo-call-community
source_url: "https://github.com/smirarab/sepp-refs"
---

## Concepts

- **Tool Overview**: sepp-refsilva128 (v4.5.1) provides SEPP reference package for SILVA 128 database.
- **Core Function**: Provides reference data for phylogenetic placement with SILVA taxonomy.
- **Algorithm**: Works with SEPP for accurate phylogenetic placement.
- **Input/Output**: Used as reference database for SEPP placement.
- **Reference Data**: Contains pre-built trees and alignments for SILVA 128.
- **Applications**: Metagenomics, microbial community analysis, and taxonomy classification.

## Pitfalls

- **Large File Size**: Reference database may be large.
- **Memory Usage**: May require significant memory for loading.
- **Version Compatibility**: Must match SEPP version.
- **Disk Space**: Requires sufficient disk space for database.
- **Update Frequency**: Reference database may become outdated.
- **Dependency**: Requires SEPP for usage.

## Examples

### Use with SEPP
**Args:** `run_sepp.py -a query.fasta -r silva_128 -o output/`
**Explanation:** Uses SILVA 128 reference database.

### Install reference
**Args:** `conda install -c bioconda sepp-refsilva128`
**Explanation:** Installs SILVA 128 reference package.

### Check installation
**Args:** `python -c "from sepp import refs; print(refs.available_refs())"`
**Explanation:** Lists available reference packages.

### Help documentation
**Args:** `python -m sepp --help`
**Explanation:** Shows SEPP documentation.

### Version check
**Args:** `conda list sepp-refsilva128`
**Explanation:** Shows installed version.

### Download reference
**Args:** `sepp-install-refs silva_128`
**Explanation:** Downloads and installs reference database.

### List references
**Args:** `sepp-list-refs`
**Explanation:** Lists available reference databases.