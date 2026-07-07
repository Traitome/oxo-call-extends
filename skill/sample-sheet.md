---
name: sample-sheet
category: utility
description: Illumina Sample Sheet parsing and validation library
tags: ["sample-sheet", "Illumina", "parsing", "validation", "sequencing"]
author: oxo-call-community
source_url: "https://sample-sheet.readthedocs.io/"
---

## Concepts

- **Tool Overview**: sample-sheet (v0.13.0) is a Python library for parsing and validating Illumina Sample Sheet files, used in sequencing experiments for sample indexing and metadata management.
- **Core Function**: Parses Illumina Sample Sheet CSV files, validates format compliance, and provides programmatic access to sample metadata.
- **Algorithm**: Implements structured parsing of Sample Sheet sections ([Header], [Reads], [Data]), validates required fields, and handles various Illumina formats.
- **Input Format**: Illumina Sample Sheet CSV files, JSON representations of sample metadata.
- **Output Format**: Parsed sample objects, validated Sample Sheets, error reports.
- **Use Case**: Sequencing experiment management, sample tracking, pipeline automation, quality control.

## Pitfalls

- **Format compliance**: Requires strict adherence to Illumina Sample Sheet format.
- **Section order**: Sections must appear in correct order ([Header], [Reads], [Data]).
- **Required fields**: Missing required fields may cause parsing errors.
- **Barcode validation**: Barcodes must be valid for the sequencing chemistry.
- **Encoding**: Requires proper CSV encoding (UTF-8 recommended).
- **Version compatibility**: Different Illumina instrument models may have different formats.

## Examples

### Parse Sample Sheet
**Args:** `from sample_sheet import SampleSheet; ss = SampleSheet('SampleSheet.csv')`
**Explanation:** Parses Sample Sheet file into object.

### Access sample data
**Args:** `samples = ss.data; print(samples[0]['Sample_ID'])`
**Explanation:** Accesses sample metadata from parsed sheet.

### Validate Sample Sheet
**Args:** `ss.validate()`
**Explanation:** Validates Sample Sheet format and content.

### Get header info
**Args:** `header = ss.header; print(header['ExperimentName'])`
**Explanation:** Retrieves header information.

### Filter samples
**Args:** `filtered = [s for s in ss.data if s['Sample_Project'] == 'ProjectA']`
**Explanation:** Filters samples by project.

### Export to JSON
**Args:** `json_data = ss.to_json()`
**Explanation:** Exports Sample Sheet to JSON format.

### Check read lengths
**Args:** `reads = ss.reads; print(f"Read 1 length: {reads[0]}")`
**Explanation:** Retrieves read lengths from [Reads] section.