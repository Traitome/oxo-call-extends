---
name: mztosqlite
category: formatting
description: Convert proteomics data files into a SQLite database.
tags: [mztosqlite, formatting, proteomics, sqlite, database]
author: oxo-call-community
source_url: "https://github.com/galaxyproteomics/mzToSQLite"
---

## Concepts

- **Tool Overview**: mzToSQLite v2.1.1 - converts proteomics data files into SQLite databases.
- **Core Function**: Converts mzML and other proteomics data files into SQLite database format for efficient querying.
- **Input/Output**: Takes mzML/proteomics files; outputs SQLite database.
- **Installation**: `conda install -c bioconda mztosqlite`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports mzML and common proteomics formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.mzML -o output.db`
**Explanation:** Converts mzML file to SQLite database.
