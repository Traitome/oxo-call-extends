---
name: suvtk
category: utility
description: Tool to submit viral sequences to GenBank for sequence deposition.
tags: [suvtk, genbank, sequence-submission, viral-genomics]
author: oxo-call-community
source_url: "https://landerdc.github.io/suvtk/"
---

## Concepts

- **Tool Overview**: suvtk (v0.1.6) is a tool for submitting viral sequences to GenBank.
- **Core Function**: Prepares and submits viral sequence data to GenBank database.
- **Algorithm**: Validates sequence data and formats it for GenBank submission.
- **Input/Output**: Input: FASTA sequences, metadata; Output: Submission files, GenBank accessions.
- **Applications**: Viral genomics, sequence deposition, bioinformatics.
- **Installation**: `conda install -c bioconda suvtk` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific sequence format.
- **Metadata Requirements**: Missing metadata causes submission errors.
- **Validation Errors**: Sequence validation may fail.
- **Network Dependencies**: Requires network access for submission.
- **Access Requirements**: Requires GenBank submission account.
- **Format Compliance**: Must follow GenBank formatting rules.

## Examples

### Display help
**Args:** `suvtk --help`
**Explanation:** Shows available options and usage information.

### Basic submission preparation
**Args:** `suvtk prepare -i sequences.fasta -m metadata.csv -o submission/`
**Explanation:** Prepare sequences for GenBank submission.

### Validate submission
**Args:** `suvtk validate -i submission/`
**Explanation:** Validate submission files before upload.

### Verbose mode
**Args:** `suvtk prepare -i sequences.fasta -m metadata.csv -o submission/ -v`
**Explanation:** Run with detailed logging for debugging.

### Batch processing
**Args:** `suvtk prepare -i fastas/ -m metadata.csv -o submissions/`
**Explanation:** Prepare multiple sequence files for submission.

### Filter by length
**Args:** `suvtk prepare -i sequences.fasta -m metadata.csv -o submission/ -m 500`
**Explanation:** Minimum sequence length of 500.

### Include annotations
**Args:** `suvtk prepare -i sequences.fasta -m metadata.csv -a features.gff -o submission/`
**Explanation:** Include sequence annotations.

### Dry run
**Args:** `suvtk submit -i submission/ --dry-run`
**Explanation:** Test submission without uploading.

### Generate report
**Args:** `suvtk report -i submission/ -o report.html`
**Explanation:** Generate submission report.
