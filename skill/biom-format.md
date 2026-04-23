---
name: biom-format
category: metagenomics
description: Biological Observation Matrix (BIOM) format for microbiome data
tags: [biom, microbiome, otu-table, community-data]
author: oxo-call-community
source_url: "https://github.com/biocore/biom-format"
---

## Concepts
- **Tool Overview**: biom-format provides tools for working with the Biological Observation Matrix (BIOM) format, a standard format for representing microbiome and other community data.
- **BIOM Format**: HDF5 or JSON-based format storing OTU tables, taxonomy, sample metadata, and observation metadata in a single file.
- **Operations**: Convert between formats, add/remove metadata, subset tables, merge tables, summarize data.
- **Applications**: Microbiome analysis, metagenomics, amplicon sequencing, ecological diversity studies.

## Pitfalls
- **Format Versions**: BIOM 1.0 (JSON) and 2.0 (HDF5) have different capabilities.
- **Metadata Handling**: Metadata must be properly formatted for successful addition.

## Examples
### Convert text table to BIOM
**Args:** `biom convert -i otu_table.txt -o otu_table.biom --to-hdf5 --table-type "OTU table"`
**Explanation:** Converts tab-delimited OTU table to BIOM format.

### Add sample metadata
**Args:** `biom add-metadata -i otu_table.biom -o with_metadata.biom -m sample_metadata.txt`
**Explanation:** Adds sample metadata to BIOM table.

### Summarize BIOM table
**Args:** `biom summarize-table -i otu_table.biom`
**Explanation:** Reports summary statistics of BIOM table.

### Convert BIOM to TSV
**Args:** `biom convert -i otu_table.biom -o otu_table.tsv --to-tsv`
**Explanation:** Converts BIOM to tab-delimited format.
