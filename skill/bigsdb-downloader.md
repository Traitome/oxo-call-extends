---
name: bigsdb-downloader
category: utility
description: BIGSdb Downloader for downloading bacterial genome databases
tags: [database, bacterial-genomes, download]
author: oxo-call-community
source_url: "https://github.com/kjolley/BIGSdb_downloader"
---

## Concepts
- **Tool Overview**: BIGSdb Downloader downloads isolate databases from BIGSdb (Bacterial Isolate Genome Sequence Database) servers for local analysis.
- **BIGSdb**: A web-based database system for storing and querying bacterial isolate genome sequences and associated metadata.
- **Use Case**: Useful for downloading large collections of bacterial genomes with standardized metadata for epidemiological studies.

## Pitfalls
- **Network Dependency**: Requires stable internet connection for downloading large databases.
- **Storage**: Downloaded databases can be large; ensure sufficient disk space.

## Examples
### Download database
**Args:** `bigsdb-downloader --database pubmlst_neisseria_isolates --output neisseria/`
**Explanation:** Downloads the Neisseria isolate database from PubMLST.
