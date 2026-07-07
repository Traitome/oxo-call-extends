---
name: sage-proteomics
category: proteomics
description: Ultra-fast proteomics search engine for mass spectrometry data
tags: ["sage-proteomics", "proteomics", "mass spectrometry", "search engine", "MS/MS"]
author: oxo-call-community
source_url: "https://lazear.github.io/sage/"
---

## Concepts

- **Tool Overview**: SAGE (v0.14.7) is a high-performance proteomics search engine designed for fast and accurate peptide identification from mass spectrometry data.
- **Core Function**: Identifies peptides from MS/MS spectra by matching against protein databases, using advanced indexing and scoring algorithms.
- **Algorithm**: Implements fast spectral matching using precomputed fragment ion masses, supports multiple search strategies (tryptic, semi-tryptic, non-specific).
- **Input Format**: Mass spectrometry data (mzML, mzXML), protein database (FASTA), search parameters (JSON/YAML).
- **Output Format**: Identified peptides (CSV/TSV), search results (JSON), statistical reports, visualization data.
- **Use Case**: Proteomics data analysis, biomarker discovery, protein identification, quantitative proteomics.

## Pitfalls

- **Database size**: Large protein databases increase search time and memory usage.
- **Search parameters**: Incorrect parameters may miss true identifications.
- **Decoy strategy**: Proper decoy database generation is critical for FDR control.
- **Modifications**: Unspecified modifications may result in missed identifications.
- **Spectrum quality**: Poor quality spectra affect identification accuracy.
- **Computational resources**: Large datasets require significant memory.

## Examples

### Basic peptide search
**Args:** `sage search -i spectra.mzML -d proteins.fasta -o results`
**Explanation:** `-i` input mass spectrometry data; `-d` protein database; `-o` output directory.

### With modifications
**Args:** `sage search -i spectra.mzML -d proteins.fasta -o results -m carbamidomethyl@C -m oxidation@M`
**Explanation:** `-m` specifies variable modifications (e.g., oxidation on methionine).

### Semi-tryptic search
**Args:** `sage search -i spectra.mzML -d proteins.fasta -o results --semi-tryptic`
**Explanation:** `--semi-tryptic` allows semi-tryptic peptide cleavage.

### Specify FDR threshold
**Args:** `sage search -i spectra.mzML -d proteins.fasta -o results --fdr 0.01`
**Explanation:** `--fdr` sets false discovery rate threshold.

### Parallel processing
**Args:** `sage search -i spectra.mzML -d proteins.fasta -o results -t 16`
**Explanation:** `-t` number of threads for parallel processing.

### Output JSON format
**Args:** `sage search -i spectra.mzML -d proteins.fasta -o results --format json`
**Explanation:** `--format json` outputs results in JSON format.

### Generate decoy database
**Args:** `sage decoy -d proteins.fasta -o decoy.fasta`
**Explanation:** Generates decoy database for FDR estimation.