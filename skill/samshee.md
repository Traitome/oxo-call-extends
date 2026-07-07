---
name: samshee
category: utility
description: Schema-agnostic parser and writer for Illumina Sample Sheets v2
tags: ["samshee", "Illumina", "SampleSheet", "parsing", "BCLConvert"]
author: oxo-call-community
source_url: "https://github.com/lit-regensburg/samshee"
---

## Concepts

- **Tool Overview**: Samshee (v0.2.14) is a schema-agnostic parser and writer for Illumina Sample Sheets v2, supporting flexible manipulation of sample metadata.
- **Core Function**: Parses, validates, and generates Illumina Sample Sheet v2 files, enabling programmatic management of sequencing experiments.
- **Algorithm**: Implements structured parsing of Sample Sheet sections, validates against v2 schema, and supports flexible output generation.
- **Input Format**: Illumina SampleSheet.csv v2 files, JSON representations.
- **Output Format**: SampleSheet.csv files, JSON, validation reports.
- **Use Case**: Sequencing experiment management, sample tracking, pipeline automation, format conversion.

## Pitfalls

- **Schema validation**: Requires valid v2 schema compliance.
- **Section order**: Sections must appear in correct order.
- **Required fields**: Missing required fields may cause errors.
- **Encoding**: Requires proper CSV encoding.
- **Version compatibility**: Designed for v2 format only.
- **Barcode validation**: Does not validate barcode sequences.

## Examples

### Parse Sample Sheet
**Args:** `samshee parse SampleSheet.csv -o parsed.json`
**Explanation:** Parses Sample Sheet and outputs JSON.

### Validate Sample Sheet
**Args:** `samshee validate SampleSheet.csv`
**Explanation:** Validates Sample Sheet against v2 schema.

### Generate Sample Sheet
**Args:** `samshee generate -i metadata.json -o SampleSheet.csv`
**Explanation:** Generates Sample Sheet from JSON metadata.

### Merge Sample Sheets
**Args:** `samshee merge sheet1.csv sheet2.csv -o merged.csv`
**Explanation:** Merges multiple Sample Sheets.

### Extract samples
**Args:** `samshee extract SampleSheet.csv -c Sample_Project=ProjectA -o filtered.csv`
**Explanation:** Extracts samples matching criteria.

### Update metadata
**Args:** `samshee update SampleSheet.csv -f "Sample_ID=NEW_ID" -o updated.csv`
**Explanation:** Updates specified fields in Sample Sheet.

### Convert to JSON
**Args:** `samshee convert SampleSheet.csv -o metadata.json --format json`
**Explanation:** Converts Sample Sheet to JSON format.