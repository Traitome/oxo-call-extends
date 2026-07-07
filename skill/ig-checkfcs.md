---
name: ig-checkfcs
category: utility
description: A tool for quick validation of FCS (Flow Cytometry Standard) data files used in flow cytometry experiments.
tags: [ig-checkfcs, utility, FCS, flow cytometry, ImmPort]
author: oxo-call-community
source_url: "https://github.com/ImmPortDB/ig-checkfcs"
---

## Concepts

- **FCS File Validation**: Checks the integrity and format of FCS files used in flow cytometry.
- **ImmPort Integration**: Designed for validating data submitted to the ImmPort database.
- **Format Compliance**: Ensures FCS files meet the FCS 3.1 standard specifications.
- **Basic Sanity Checks**: Validates file structure, data types, and metadata integrity.
- **Error Reporting**: Provides clear error messages for invalid or corrupted files.

## Pitfalls

- **FCS Version**: May not support older FCS versions (pre-3.0).
- **File Corruption**: Cannot recover data from severely corrupted FCS files.
- **Binary Data**: Limited ability to validate binary data content, mainly checks structure.
- **Compressed Files**: May require decompression before validation.
- **Metadata Only**: Focuses on metadata validation; does not validate actual cytometry data quality.

## Examples

### Check FCS file integrity
**Args:** `ig-checkfcs input.fcs`
**Explanation:** Validates the FCS file format and reports any issues.

### Check multiple files
**Args:** `ig-checkfcs file1.fcs file2.fcs file3.fcs`
**Explanation:** Validates multiple FCS files in a single run.

### Output detailed report
**Args:** `ig-checkfcs --verbose input.fcs`
**Explanation:** Provides detailed validation information and warnings.

### Check directory of FCS files
**Args:** `ig-checkfcs --dir fcs_files/`
**Explanation:** Validates all FCS files in the specified directory.

### Generate JSON report
**Args:** `ig-checkfcs --json input.fcs -o report.json`
**Explanation:** Outputs validation results in JSON format for programmatic processing.