---
name: ig-checkflowtypes
category: utility
description: A tool for quick validation of flow cytometry-related data types for Galaxy workflows.
tags: [ig-checkflowtypes, utility, Galaxy, flow cytometry, data validation]
author: oxo-call-community
source_url: "https://github.com/ImmPortDB/ig-checkflowtypes"
---

## Concepts

- **Galaxy Data Validation**: Validates flow cytometry data types within Galaxy workflow environment.
- **ImmPort Integration**: Ensures data compatibility with ImmPort database submission requirements.
- **Format Checking**: Verifies file formats commonly used in flow cytometry analysis.
- **Metadata Validation**: Checks required metadata fields for flow cytometry experiments.
- **Workflow Integration**: Designed to be integrated into Galaxy tool wrappers and workflows.

## Pitfalls

- **Galaxy Dependencies**: Requires Galaxy environment or compatible framework.
- **Specific Formats**: Optimized for flow cytometry formats; may not work with other data types.
- **Validation Scope**: Focuses on format validation, not scientific data quality.
- **Version Compatibility**: May have compatibility issues with different Galaxy versions.
- **ImmPort Specific**: Validation rules are tailored to ImmPort submission requirements.

## Examples

### Validate flow cytometry data
**Args:** `ig-checkflowtypes --input data.fcs --type fcs`
**Explanation:** Validates FCS file for Galaxy workflow compatibility.

### Check metadata compliance
**Args:** `ig-checkflowtypes --input metadata.txt --type metadata`
**Explanation:** Validates metadata file against ImmPort requirements.

### Validate multiple files
**Args:** `ig-checkflowtypes --input *.fcs --batch`
**Explanation:** Batch validation of multiple FCS files.

### Generate validation report
**Args:** `ig-checkflowtypes --input data.fcs --report output.txt`
**Explanation:** Generates detailed validation report.

### Check file type
**Args:** `ig-checkflowtypes --input data.txt --detect`
**Explanation:** Detects and validates the file type automatically.