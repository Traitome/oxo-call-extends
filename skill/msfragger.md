---
name: msfragger
category: proteomics
description: Ultrafast, comprehensive peptide identification for mass spectrometry proteomics.
tags: [msfragger, proteomics, mass-spectrometry]
author: oxo-call-community
source_url: "https://github.com/Nesvilab/MSFragger"
---

## Concepts

- **Tool Overview**: MSFragger v4.2 performs ultrafast peptide identification.
- **Core Function**: Searches MS/MS spectra against protein databases.
- **Fast Search**: Optimized for rapid database searching.
- **Open Search**: Supports large precursor mass tolerance.
- **Glycopeptide Analysis**: Handles N-linked and O-linked glycopeptides.
- **Input/Output**: Accepts MS data and database; outputs peptide identifications.

## Pitfalls

- **Proteomics Specific**: Designed for mass spectrometry data.
- **Database Requirement**: Requires protein sequence database.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for search.
- **Computational Resources**: Large datasets may require significant resources.
- **FDR Control**: Requires post-processing for false discovery rate control.

## Examples

### Run database search
**Args:** `msfragger -i raw_data/ -d uniprot.fasta -o results.tsv`
**Explanation:** Searches MS/MS spectra against database.

### Open modification search
**Args:** `msfragger -i raw_data/ -d uniprot.fasta -open_mod -o results.tsv`
**Explanation:** Performs open modification search.

### Glycopeptide identification
**Args:** `msfragger -i raw_data/ -d uniprot.fasta -glyco -o results.tsv`
**Explanation:** Identifies glycopeptides.

### With timsTOF data
**Args:** `msfragger -i tims_data/ -d uniprot.fasta -o results.tsv`
**Explanation:** Processes timsTOF PASEF data.

### Specify enzyme cleavage
**Args:** `msfragger -i raw_data/ -d uniprot.fasta -enzyme trypsin -o results.tsv`
**Explanation:** Uses trypsin cleavage rules.