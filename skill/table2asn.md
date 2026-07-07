---
name: table2asn
category: data-submission
description: Creates sequence records for GenBank submission from feature tables.
tags: [table2asn, genbank, sequence-submission, ncbi]
author: oxo-call-community
source_url: "https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/DOCUMENTATION/table2asn_readme.txt"
---

## Concepts

- **Tool Overview**: table2asn (v1.28.1179) prepares sequence records for GenBank submission.
- **Core Function**: Converts sequence and feature table data to GenBank format.
- **Algorithm**: Validates and formats sequence data according to GenBank standards.
- **Input/Output**: Input: FASTA + feature table; Output: GenBank submission files.
- **Applications**: Sequence data submission to NCBI GenBank.
- **Installation**: `conda install -c bioconda table2asn` or download from NCBI.

## Pitfalls

- **Format Requirements**: Strict input format requirements.
- **Validation**: Submission must pass NCBI validation.
- **Annotation Quality**: Requires complete feature annotations.
- **Taxonomy**: Correct taxonomic information required.
- **File Size**: Large submissions may have size limits.
- **Internet Access**: Submission requires internet connection.

## Examples

### Display help
**Args:** `table2asn --help`
**Explanation:** Shows available options and usage information.

### Basic submission preparation
**Args:** `table2asn -i sequence.fsa -f features.tbl -o submission.sqn`
**Explanation:** Create GenBank submission file.

### With template
**Args:** `table2asn -i sequence.fsa -f features.tbl -t template.sbt -o submission.sqn`
**Explanation:** Use submission template.

### Verbose mode
**Args:** `table2asn -i sequence.fsa -f features.tbl -o submission.sqn -v`
**Explanation:** Run with detailed logging.

### Output statistics
**Args:** `table2asn -i sequence.fsa -f features.tbl -o submission.sqn --stats`
**Explanation:** Generate submission statistics.

### Batch processing
**Args:** `for f in sequences/*.fsa; do table2asn -i $f -f ${f%.fsa}.tbl -o submissions/${f%.fsa}.sqn; done`
**Explanation:** Process multiple sequences.

### Validate only
**Args:** `table2asn -i sequence.fsa -f features.tbl -o submission.sqn -V`
**Explanation:** Validate without creating submission.

### Include source info
**Args:** `table2asn -i sequence.fsa -f features.tbl -o submission.sqn -s source.txt`
**Explanation:** Include source information.

### Generate report
**Args:** `table2asn -i sequence.fsa -f features.tbl -o submission.sqn --report`
**Explanation:** Generate submission report.
