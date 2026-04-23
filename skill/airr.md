---
name: airr
category: utility
description: AIRR Community Data Representation Standard reference library for antibody and TCR sequencing data
tags: [airr, antibody, tcr, repertoire, immunoglobulin, standard]
author: oxo-call-community
source_url: "http://docs.airr-community.org"
---

## Concepts

- **Tool Overview**: The AIRR Python library implements the AIRR Community Data Representation Standard for antibody and T-cell receptor sequencing data.
- **Core Function**: Provides tools for reading, writing, validating, and converting AIRR-seq data in standardized formats.
- **Input/Output**: Input: AIRR TSV format, Change-O, IMGT, or other repertoire formats. Output: Standardized AIRR TSV format.
- **Standards Compliance**: Implements the AIRR Community minimal standards for describing and sharing adaptive immune receptor repertoire data.
- **Installation**: Install via bioconda: `conda install -c bioconda airr`

## Pitfalls

- **Format Requirements**: Output must conform to AIRR schema - non-standard fields may be dropped or cause validation errors.
- **Rearrangement Schema**: The rearrangement schema defines required and optional fields - ensure data has required fields.
- **Germline References**: Proper germline gene assignment requires compatible reference databases.
- **Validation**: Use validation tools to check data compliance before sharing or analysis.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for AIRR tools.

### Validate AIRR TSV file
**Args:** `validate input.tsv`
**Explanation:** Validates that a TSV file conforms to the AIRR rearrangement schema.

### Convert Change-O to AIRR format
**Args:** `convert -f changeo -t airr -i input.tsv -o output.tsv`
**Explanation:** Converts Change-O format repertoire data to AIRR standard format.

### Convert IMGT to AIRR format
**Args:** `convert -f imgt -t airr -i imgt_output.tsv -o airr_output.tsv`
**Explanation:** Converts IMGT/HighV-QUEST output to AIRR rearrangement format.

### Merge AIRR files
**Args:** `merge -i rep1.tsv rep2.tsv rep3.tsv -o merged.tsv`
**Explanation:** Merges multiple AIRR TSV files into a single file.

### Split by locus
**Args:** `split -i repertoire.tsv --locus IGH IGL IGK -o split_dir/`
**Explanation:** Splits repertoire data into separate files by receptor locus.

### Validate with strict mode
**Args:** `validate --strict input.tsv`
**Explanation:** Performs strict validation including optional field checks.
