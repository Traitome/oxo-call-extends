---
name: msgf_plus
category: proteomics
description: MS-GF+ - Sensitive and universal MS/MS database search tool.
tags: [msgf_plus, proteomics, mass-spectrometry]
author: oxo-call-community
source_url: "https://msgfplus.github.io/"
---

## Concepts

- **Tool Overview**: MS-GF+ v2024.03.26 performs sensitive database searching.
- **Core Function**: Identifies peptides from MS/MS spectra using probabilistic models.
- **Sensitive Search**: Detects more peptides than other search tools.
- **Universal Application**: Works with diverse spectra and instruments.
- **Probabilistic Scoring**: Uses statistical scoring for peptide identification.
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
**Args:** `msgf_plus -s spectrum.mzML -d uniprot.fasta -o results.mzid`
**Explanation:** Searches MS/MS spectra against database.

### Specify instrument type
**Args:** `msgf_plus -s spectrum.mzML -d uniprot.fasta -inst QExactive -o results.mzid`
**Explanation:** Optimizes for QExactive instrument.

### Set enzyme specificity
**Args:** `msgf_plus -s spectrum.mzML -d uniprot.fasta -e 1 -o results.mzid`
**Explanation:** Uses semi-tryptic cleavage.

### Specify precursor tolerance
**Args:** `msgf_plus -s spectrum.mzML -d uniprot.fasta -t 10ppm -o results.mzid`
**Explanation:** Sets 10 ppm precursor tolerance.

### Process multiple files
**Args:** `msgf_plus -s mzML/ -d uniprot.fasta -o results/`
**Explanation:** Searches multiple MS files.