---
name: staphscope-mlst-data
category: utility
description: MLST typing database for StaphScope.
tags: [staphscope-mlst-data, mlst, database, staphylococcus]
author: oxo-call-community
source_url: "https://github.com/bbeckley-hub/staphscope-typing-tool"
---

## Concepts

- **Tool Overview**: staphscope-mlst-data (v1.2.0) is the MLST (Multi-Locus Sequence Typing) database package for StaphScope.
- **Core Function**: Provides curated MLST allele sequences for Staphylococcus aureus typing.
- **Database Content**: Contains allele sequences for seven housekeeping genes (arcC, aroE, glpF, gmk, pta, tpi, yqiL).
- **Input/Output**: Automatically loaded by StaphScope during MLST typing; no direct command-line usage.
- **Updates**: Regularly updated with new alleles from PubMLST database.
- **Installation**: `conda install -c bioconda staphscope-mlst-data` (automatically installed with staphscope).

## Pitfalls

- **Version Compatibility**: Must match StaphScope version for proper functionality.
- **Database Updates**: Outdated database may miss newly discovered alleles.
- **Manual Installation**: Incorrect manual installation may cause database corruption.
- **Storage Requirements**: Requires sufficient disk space for database files.
- **Network Access**: Updates may require network access to download latest alleles.
- **Backup**: Regular backups recommended for custom database modifications.

## Examples

### Display database info
**Args:** `staphscope-mlst-data --info`
**Explanation:** Show database version and statistics.

### Update database
**Args:** `staphscope-mlst-data --update`
**Explanation:** Update database to latest version.

### List available schemes
**Args:** `staphscope-mlst-data --list`
**Explanation:** List available MLST schemes.

### Verify database integrity
**Args:** `staphscope-mlst-data --verify`
**Explanation:** Check database for corruption or missing files.

### Export alleles
**Args:** `staphscope-mlst-data --export arcC`
**Explanation:** Export specific allele sequences.

### Show statistics
**Args:** `staphscope-mlst-data --stats`
**Explanation:** Display database statistics including number of alleles per locus.

### Install custom alleles
**Args:** `staphscope-mlst-data --install custom_alleles.fasta`
**Explanation:** Add custom allele sequences to database.

### Reset database
**Args:** `staphscope-mlst-data --reset`
**Explanation:** Reset database to default state.
