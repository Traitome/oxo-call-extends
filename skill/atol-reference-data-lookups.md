---
name: atol-reference-data-lookups
category: utility
description: AToL Reference Data Lookups - Look up reference datasets by NCBI TaxId
tags: [reference-data, ncbi-taxid, data-retrieval, taxonomy]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/atol-reference-data-lookups"
---

## Concepts

- **Tool Overview**: Retrieves reference datasets (genomes, annotations) by NCBI Taxonomy ID for AToL Genome Engine workflows.

- **TaxId-Based Lookup**: Uses NCBI Taxonomy ID to identify and retrieve appropriate reference data.

- **Database Integration**: Interfaces with reference databases to fetch latest versions of reference genomes and annotations.

- **Workflow Integration**: Designed for automated pipeline integration to select appropriate references for new species.

## Pitfalls

- **TaxId Accuracy**: Incorrect TaxId leads to wrong reference retrieval. Verify TaxId before use.

- **Database Availability**: Requires access to reference databases. Network issues can interrupt retrieval.

- **Reference Quality**: Reference quality varies. Not all organisms have high-quality references available.

- **Version Control**: References are updated. Document reference versions used for reproducibility.

## Examples

### Lookup by TaxId
**Args:** `atol-reference-data-lookups --taxid 9606 --output reference_data/`
**Explanation:** Retrieves reference genome and annotation for human (TaxId 9606).

### Get specific data types
**Args:** `atol-reference-data-lookups --taxid 10090 --types genome,annotation --output mouse_data/`
**Explanation:** Retrieves only genome and annotation for mouse (TaxId 10090).

### List available data
**Args:** `atol-reference-data-lookups --taxid 9606 --list-only`
**Explanation:** Lists available reference data for human without downloading.

### Specify database
**Args:** `atol-reference-data-lookups --taxid 9606 --database ncbi --output human_ref/`
**Explanation:** Retrieves reference data from NCBI database specifically.
