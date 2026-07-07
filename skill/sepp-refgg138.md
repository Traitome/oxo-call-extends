---
name: sepp-refgg138
category: phylogenetics
description: sepp-refgg138 - SEPP reference package for Greengenes 13_8
tags: ["sepp-refgg138", "phylogenetics", "reference-database", "Greengenes"]
author: oxo-call-community
source_url: "https://github.com/smirarab/sepp-refs"
---

## Concepts

- **Tool Overview**: sepp-refgg138 (v4.5.1) provides SEPP reference package for Greengenes 13_8 database.
- **Core Function**: Provides reference data for phylogenetic placement with Greengenes taxonomy.
- **Algorithm**: Works with SEPP for accurate phylogenetic placement.
- **Input/Output**: Used as reference database for SEPP placement.
- **Reference Data**: Contains pre-built trees and alignments for Greengenes 13_8.
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
**Args:** `run_sepp.py -a query.fasta -r gg_13_8 -o output/`
**Explanation:** Uses Greengenes 13_8 reference database.

### Install reference
**Args:** `conda install -c bioconda sepp-refgg138`
**Explanation:** Installs Greengenes 13_8 reference package.

### Check installation
**Args:** `python -c "from sepp import refs; print(refs.available_refs())"`
**Explanation:** Lists available reference packages.

### Help documentation
**Args:** `python -m sepp --help`
**Explanation:** Shows SEPP documentation.

### Version check
**Args:** `conda list sepp-refgg138`
**Explanation:** Shows installed version.

### Download reference
**Args:** `sepp-install-refs gg_13_8`
**Explanation:** Downloads and installs reference database.

### List references
**Args:** `sepp-list-refs`
**Explanation:** Lists available reference databases.