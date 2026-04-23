---
name: biomaj
category: utility
description: Automates update cycle and supervision of locally mirrored databank repository
tags: [database, mirroring, bioinformatics-databases]
author: oxo-call-community
source_url: "http://biomaj.genouest.org"
---

## Concepts
- **Tool Overview**: BioMAJ automates the update cycle and supervision of locally mirrored bioinformatics databases (GenBank, UniProt, Ensembl, etc.).
- **Database Mirroring**: Downloads, updates, and maintains local copies of public bioinformatics databases.
- **Workflow**: Download → extract → format → index → announce.
- **Applications**: Local database maintenance, offline access to public databases, high-throughput annotation.

## Pitfalls
- **Storage Requirements**: Mirrored databases can be very large (terabytes).
- **Update Frequency**: Regular updates require network bandwidth and processing time.

## Examples
### Update database
**Args:** `biomaj --update genbank`
**Explanation:** Updates local GenBank database mirror.

### List available databases
**Args:** `biomaj --list`
**Explanation:** Lists configured databases for mirroring.
