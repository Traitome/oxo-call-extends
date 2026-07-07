---
name: biowdl-input-converter
category: workflow
description: Convert various input formats into WDL structs for BioWDL pipelines
tags: [wdl, workflow, format-conversion, biowdl]
author: oxo-call-community
source_url: "https://biowdl-input-converter.readthedocs.io"
---

## Concepts

- **Tool Overview**: BioWDL Input Converter converts various input file formats into WDL struct format for use with BioWDL pipelines.
- **Format Support**: Converts sample sheets (CSV, TSV, JSON) to WDL input format.
- **WDL Integration**: Generates properly formatted WDL structs and input JSON files.
- **Batch Processing**: Handles multiple samples and libraries in a single conversion.
- **Applications**: Pipeline input preparation, sample sheet conversion, workflow setup.

## Pitfalls

- **Input Format Requirements**: Input files must follow expected format conventions.
- **WDL Version**: Generated files should match WDL pipeline version requirements.

## Examples

### Convert sample sheet to WDL
**Args:** `biowdl-input-converter samplesheet -i samples.csv -o samples.wdl.json`
**Explanation:** Converts sample CSV to WDL-compatible JSON input.

### Convert multiple sample sheets
**Args:** `biowdl-input-converter multi -i sample1.csv -i sample2.csv -o combined.json`
**Explanation:** Combines multiple sample sheets into single WDL input.

### Generate WDL struct
**Args:** `biowdl-input-converter struct -i samples.tsv -o samples.wdl`
**Explanation:** Generates WDL struct definition from sample table.