---
name: biosniff
category: utility
description: Auto-detect and validate biological file formats
tags: [format-detection, file-formats, validation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cokelaer/biosniff"
---

## Concepts

- **Tool Overview**: BioSniff is a tool for automatically detecting and validating biological file formats by inspecting file structure and content.
- **Format Detection**: Identifies file formats (FASTA, FASTQ, GenBank, GFF, etc.) based on content patterns.
- **Validation**: Validates detected formats against specification.
- **Batch Processing**: Can process multiple files to identify their formats.
- **Applications**: File format identification, data preprocessing, pipeline input validation.

## Pitfalls

- **Ambiguous Formats**: Some formats may be difficult to distinguish without explicit headers.
- **Compressed Files**: May not detect formats in compressed archives.
- **Mixed Formats**: Files containing multiple formats may not be handled correctly.

## Examples

### Detect file format
**Args:** `biosniff detect -i sequence file.fa`
**Explanation:** Detects and reports the format of the input file.

### Validate file format
**Args:** `biosniff validate -i sequences.fasta --format fasta`
**Explanation:** Validates that the file conforms to FASTA format specification.

### Batch format detection
**Args:** `biosniff detect -i *.txt -o format_report.csv`
**Explanation:** Detects formats for all txt files and saves report.