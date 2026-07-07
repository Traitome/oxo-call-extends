---
name: msstitch
category: proteomics
description: MS proteomics post-processing utilities for peptide and protein quantification.
tags: [msstitch, proteomics, mass-spectrometry]
author: oxo-call-community
source_url: "https://github.com/lehtiolab/msstitch"
---

## Concepts

- **Tool Overview**: msstitch v3.20 provides proteomics post-processing utilities.
- **Core Function**: Combines, filters, and processes MS-based proteomics results.
- **Peptide Level**: Works with peptide identification results.
- **Protein Level**: Aggregates peptide results to protein level.
- **Quantification**: Supports label-free quantification workflows.
- **Input/Output**: Accepts search results; outputs processed data.

## Pitfalls

- **Proteomics Specific**: Designed for mass spectrometry data.
- **File Format**: Requires compatible input file formats.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for processing.
- **Data Quality**: Results depend on input data quality.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Create decoy database
**Args:** `msstitch createdb -i proteins.fasta -o proteins_with_decoy.fasta`
**Explanation:** Adds decoy sequences to database.

### Combine PSMs
**Args:** `msstitch combine_psm -i search1.tsv search2.tsv -o combined.tsv`
**Explanation:** Combines PSM files from multiple searches.

### Protein rollup
**Args:** `msstitch protein_rollup -i peptides.tsv -o proteins.tsv`
**Explanation:** Aggregates peptides to protein level.

### Filter by q-value
**Args:** `msstitch filter -i results.tsv -q 0.01 -o filtered.tsv`
**Explanation:** Filters results by q-value threshold.

### Batch processing
**Args:** `msstitch combine_psm -i tsv/ -o combined/`
**Explanation:** Processes multiple PSM files.