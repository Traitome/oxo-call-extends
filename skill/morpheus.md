---
name: morpheus
category: utility
description: Mass spectrometry-based proteomics database search algorithm
tags: [morpheus, utility, proteomics]
author: oxo-call-community
source_url: "https://github.com/cwenger/Morpheus/"
---

## Concepts

- **Tool Overview**: Morpheus v290 performs proteomics database search from mass spectrometry data.
- **Core Function**: Identifies peptides from MS/MS spectra using database search.
- **Database Search**: Matches experimental spectra against protein databases.
- **Mass Spectrometry**: Designed for MS/MS data analysis.
- **Peptide Identification**: Determines peptide sequences from spectral data.
- **Input/Output**: Accepts MS/MS data; outputs identified peptides.

## Pitfalls

- **Proteomics Specific**: Designed for mass spectrometry data.
- **Memory Requirements**: Memory usage depends on database size.
- **Parameter Tuning**: May require parameter adjustment for optimal search.
- **Data Quality**: Results depend on MS data quality.
- **Database Dependence**: Requires protein sequence database.
- **Computational Resources**: Large databases may require significant resources.

## Examples

### Run database search
**Args:** `morpheus -i ms_data.mzML -d uniprot.fasta -o results.txt`
**Explanation:** Performs peptide identification from MS/MS data.

### With decoy database
**Args:** `morpheus -i ms_data.mzML -d uniprot.fasta -decoy -o results.txt`
**Explanation:** Uses decoy database for FDR estimation.

### Custom enzyme
**Args:** `morpheus -i ms_data.mzML -d uniprot.fasta -e trypsin -o results.txt`
**Explanation:** Specifies enzyme for digestion.

### Verbose output
**Args:** `morpheus -i ms_data.mzML -d uniprot.fasta -v -o results.txt`
**Explanation:** Shows detailed search progress.

### Batch processing
**Args:** `morpheus -i mzML/ -d uniprot.fasta -o results/`
**Explanation:** Processes multiple MS files.