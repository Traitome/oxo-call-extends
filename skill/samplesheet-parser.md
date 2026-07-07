---
name: samplesheet-parser
category: utility
description: Format-agnostic parser for Illumina SampleSheet.csv files
tags: ["samplesheet-parser", "Illumina", "SampleSheet", "CSV", "parsing"]
author: oxo-call-community
source_url: "https://illumina-samplesheet.readthedocs.io"
---

## Concepts

- **Tool Overview**: samplesheet-parser (v1.2.0) is a format-agnostic parser for Illumina SampleSheet.csv files, supporting both IEM V1 and BCLConvert V2 formats.
- **Core Function**: Parses and validates Illumina Sample Sheet files, extracts sample metadata, and provides programmatic access to sample information.
- **Algorithm**: Implements flexible parsing of Sample Sheet sections, handles different format versions, and validates required fields.
- **Input Format**: Illumina SampleSheet.csv files (IEM V1 and BCLConvert V2 formats).
- **Output Format**: Parsed sample objects, JSON representations, validation reports.
- **Use Case**: Sequencing experiment management, sample tracking, pipeline automation, quality control.

## Pitfalls

- **Format compatibility**: Must specify correct format version for parsing.
- **Encoding issues**: Requires proper CSV encoding (UTF-8 recommended).
- **Missing sections**: Incomplete Sample Sheets may cause parsing errors.
- **Validation errors**: Invalid formats may produce unexpected results.
- **Barcode validation**: Does not validate barcode sequences themselves.
- **Version detection**: May require explicit version specification for ambiguous formats.

## Examples

### Parse Sample Sheet
**Args:** `samplesheet-parser parse SampleSheet.csv`
**Explanation:** Parses Sample Sheet and outputs JSON representation.

### Validate Sample Sheet
**Args:** `samplesheet-parser validate SampleSheet.csv`
**Explanation:** Validates Sample Sheet format and content.

### Extract sample data
**Args:** `samplesheet-parser extract SampleSheet.csv -o samples.json`
**Explanation:** `-o` output file for extracted sample data.

### Convert format
**Args:** `samplesheet-parser convert SampleSheet.csv -o converted.csv --to v2`
**Explanation:** Converts Sample Sheet to BCLConvert V2 format.

### List samples
**Args:** `samplesheet-parser list SampleSheet.csv`
**Explanation:** Lists all sample IDs in the Sample Sheet.

### Get header info
**Args:** `samplesheet-parser header SampleSheet.csv`
**Explanation:** Displays [Header] section content.

### Check format version
**Args:** `samplesheet-parser detect SampleSheet.csv`
**Explanation:** Detects and reports Sample Sheet format version.