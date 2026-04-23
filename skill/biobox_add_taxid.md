---
name: biobox_add_taxid
category: annotation
description: CAMI amber utility for adding taxid from GTDB and BAT outputs
tags: [taxonomy, taxid, gtdb, cami]
author: oxo-call-community
source_url: "https://github.com/SantaMcCloud/biobox_add_taxid"
---

## Concepts
- **Tool Overview**: biobox_add_taxid is a utility script for adding taxonomy IDs (taxids) to output files from GTDB and BAT (Bin Annotation Tool), used in CAMI benchmarking.
- **CAMI**: Critical Assessment of Metagenome Interpretation, a community benchmarking challenge for metagenomics tools.
- **Taxonomy Mapping**: Converts GTDB and BAT taxonomy strings to NCBI taxonomy IDs.

## Pitfalls
- **Input Format**: Requires properly formatted GTDB or BAT output files.
- **Taxonomy Database**: Needs NCBI taxonomy database for ID mapping.

## Examples
### Add taxids to GTDB output
**Args:** `biobox_add_taxid -i gtdb_output.tsv -d gtdb -o with_taxids.tsv`
**Explanation:** Adds NCBI taxonomy IDs to GTDB taxonomy output.
