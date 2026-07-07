---
name: submission-excel2xml
category: utility
description: Generate DRA metadata XML files from Excel spreadsheet for DDBJ submission.
tags: [submission-excel2xml, ddbj, metadata, xml-generation]
author: oxo-call-community
source_url: "https://github.com/ddbj/submission-excel2xml"
---

## Concepts

- **Tool Overview**: submission-excel2xml (v3.6.2) is a tool for generating DRA metadata XML files from Excel spreadsheets.
- **Core Function**: Converts Excel-based metadata into DDBJ submission XML format.
- **Algorithm**: Parses Excel files and generates compliant XML for DRA submission.
- **Input/Output**: Input: Excel spreadsheet with metadata; Output: DRA XML submission files.
- **Applications**: Data submission to DDBJ, metadata management, bioinformatics.
- **Installation**: `conda install -c bioconda submission-excel2xml` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific Excel template format.
- **Metadata Quality**: Incomplete metadata affects submission.
- **Validation**: XML validation errors may occur.
- **Memory Requirements**: Large Excel files require significant memory.
- **Version Compatibility**: May require specific Excel version.
- **Submission Rules**: Must follow DDBJ submission guidelines.

## Examples

### Display help
**Args:** `submission-excel2xml --help`
**Explanation:** Shows available options and usage information.

### Basic XML generation
**Args:** `submission-excel2xml -i metadata.xlsx -o submission.xml`
**Explanation:** Generate DRA XML from Excel metadata.

### With validation
**Args:** `submission-excel2xml -i metadata.xlsx -o submission.xml --validate`
**Explanation:** Validate XML against DRA schema.

### Verbose mode
**Args:** `submission-excel2xml -i metadata.xlsx -o submission.xml -v`
**Explanation:** Run with detailed logging for debugging.

### Batch processing
**Args:** `submission-excel2xml -i metadata_dir/ -o submissions/`
**Explanation:** Process multiple Excel files together.

### Filter by sheet
**Args:** `submission-excel2xml -i metadata.xlsx -o submission.xml -s Sheet1`
**Explanation:** Process specific sheet from Excel file.

### Include schema
**Args:** `submission-excel2xml -i metadata.xlsx -o submission.xml --include-schema`
**Explanation:** Include XML schema in output.

### Check format
**Args:** `submission-excel2xml -i metadata.xlsx --check`
**Explanation:** Check Excel format without generating XML.

### Generate report
**Args:** `submission-excel2xml -i metadata.xlsx -o submission.xml --report`
**Explanation:** Generate comprehensive HTML report.
