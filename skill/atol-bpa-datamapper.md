---
name: atol-bpa-datamapper
category: utility
description: AToL BPA Data Mapper - Map data from BPA data portal for AToL Genome Engine
tags: [data-mapping, bpa-portal, metadata, genome-engine]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/atol-bpa-datamapper"
---

## Concepts

- **Tool Overview**: Maps and transforms data from the Bioplatforms Australia (BPA) data portal for use in AToL Genome Engine workflows.

- **Data Transformation**: Converts BPA portal metadata format to AToL Genome Engine compatible format.

- **Metadata Mapping**: Maps sample metadata, sequencing run information, and experimental parameters.

- **Pipeline Integration**: Prepares data for downstream assembly and annotation pipelines.

## Pitfalls

- **API Changes**: BPA portal API may change. Monitor for format updates.

- **Access Credentials**: May require BPA portal credentials for data access.

- **Data Completeness**: Not all BPA metadata fields may be populated. Handle missing data gracefully.

## Examples

### Map BPA data
**Args:** `atol-bpa-datamapper --input bpa_metadata.tsv --output mapped_data.tsv`
**Explanation:** Maps BPA portal metadata to AToL Genome Engine format.

### Specify mapping template
**Args:** `atol-bpa-datamapper --input bpa_data.tsv --template custom_template.json --output mapped.tsv`
**Explanation:** Uses custom mapping template for data transformation.

### Validate mapped data
**Args:** `atol-bpa-datamapper --input bpa_data.tsv --validate --output mapped.tsv`
**Explanation:** Validates mapped data against AToL schema before output.
