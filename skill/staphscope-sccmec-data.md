---
name: staphscope-sccmec-data
category: utility
description: SCCmec typing database for StaphScope.
tags: [staphscope-sccmec-data, sccmec, database, staphylococcus]
author: oxo-call-community
source_url: "https://github.com/bbeckley-hub/staphscope-typing-tool"
---

## Concepts

- **Tool Overview**: staphscope-sccmec-data (v1.2.0) is the SCCmec typing database package for StaphScope.
- **Core Function**: Provides curated SCCmec cassette sequences and primer definitions for typing.
- **Database Content**: Contains SCCmec type definitions, cassette structures, and marker gene sequences.
- **Input/Output**: Automatically loaded by StaphScope during SCCmec typing; no direct command-line usage.
- **Updates**: Regularly updated with new SCCmec types from scientific literature.
- **Installation**: `conda install -c bioconda staphscope-sccmec-data` (automatically installed with staphscope).

## Pitfalls

- **Version Compatibility**: Must match StaphScope version for proper functionality.
- **Database Updates**: Outdated database may miss newly discovered SCCmec types.
- **Manual Installation**: Incorrect manual installation may cause database corruption.
- **Storage Requirements**: Requires sufficient disk space for database files.
- **Network Access**: Updates may require network access to download latest types.
- **Backup**: Regular backups recommended for custom database modifications.

## Examples

### Display database info
**Args:** `staphscope-sccmec-data --info`
**Explanation:** Show database version and statistics.

### Update database
**Args:** `staphscope-sccmec-data --update`
**Explanation:** Update database to latest version.

### List available types
**Args:** `staphscope-sccmec-data --list`
**Explanation:** List available SCCmec types in database.

### Verify database integrity
**Args:** `staphscope-sccmec-data --verify`
**Explanation:** Check database for corruption or missing files.

### Export type definitions
**Args:** `staphscope-sccmec-data --export type_II`
**Explanation:** Export specific SCCmec type definition.

### Show statistics
**Args:** `staphscope-sccmec-data --stats`
**Explanation:** Display database statistics including number of types.

### Install custom type
**Args:** `staphscope-sccmec-data --install custom_type.fasta`
**Explanation:** Add custom SCCmec type to database.

### Reset database
**Args:** `staphscope-sccmec-data --reset`
**Explanation:** Reset database to default state.
