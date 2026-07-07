---
name: calisp
category: proteomics
description: Estimate isotopic composition of peptides from proteomics mass spectrometry data
tags: [calisp, proteomics, mass-spectrometry, isotopic, peptide]
author: oxo-call-community
source_url: "https://github.com/kinestetika/Calisp"
---

## Concepts

- **Tool Overview**: CALISP estimates isotopic composition of peptides from proteomics mass spectrometry data.
- **Core Function**: Calculates isotopic patterns and compositions for peptide identification.
- **Input**: Mass spectrometry data (mzML, mzXML) and peptide sequences.
- **Output**: Isotopic composition estimates and patterns.
- **Application**: Proteomics analysis and peptide identification.
- **Installation**: Install via bioconda: `conda install -c bioconda calisp`

## Pitfalls

- **Mass Spec Data**: Requires high-quality mass spectrometry input.
- **Peptide Database**: Needs accurate peptide sequence database.
- **Isotopic Patterns**: Complex mixtures may be difficult to resolve.
- **Instrument Calibration**: Results depend on instrument calibration.

## Examples

### Estimate isotopic composition
**Args:** `calisp -i spectra.mzML -p peptides.fa -o isotopic_results.tsv`
**Explanation:** Estimates isotopic composition for peptides in mass spec data.

### Set mass tolerance
**Args:** `calisp -i spectra.mzML -p peptides.fa -t 0.01 -o results.tsv`
**Explanation:** Uses 0.01 Da mass tolerance for matching.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.