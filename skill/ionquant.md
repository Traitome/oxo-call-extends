---
name: ionquant
category: proteomics
description: A label-free quantification tool for MS1 precursor intensity-based quantification
tags: [ionquant, proteomics, label-free, lfq, mass-spectrometry, ms1]
author: oxo-call-community
source_url: "https://github.com/Nesvilab/IonQuant"
---

## Concepts

- **Tool Overview**: IonQuant (v1.11.9) is a fast and comprehensive tool for label-free quantification using MS1 precursor intensity. It supports timsTOF PASEF and Orbitrap data, with FDR-controlled match-between-runs (MBR).

- **MS1 Quantification**: Extracts peptide features from MS1 scans, including m/z, retention time, and intensity information for label-free quantification.

- **Match-Between-Runs (MBR)**: Implements FDR-controlled MBR to transfer peptide identifications across runs, reducing missing values in quantitative comparisons.

- **Isobaric Labeling Support**: Also supports isobaric labeling experiments (TMT, iTRAQ) in addition to label-free quantification.

- **4D Feature Extraction**: For timsTOF data, incorporates ion mobility (1/K0) dimension for improved feature matching and quantification accuracy.

- **MaxLFQ Integration**: Implements the MaxLFQ algorithm for protein-level quantification, handling missing values and normalization.

## Pitfalls

- **Java Requirement**: Requires Java 11+. Ensure correct Java version is installed and configured.

- **MSFragger Dependency**: For full pipeline, requires MSFragger for peptide identification. PSM files must be in Philosopher's tsv format.

- **timsTOF Native Library**: On Windows, requires Visual C++ Redistributable for Visual Studio 2017 for Bruker's native library.

- **Retention Time Alignment**: Poor retention time alignment between runs can affect MBR performance. Consider using alignment tools if needed.

- **Missing Values**: Despite MBR, some peptides may still have missing values across runs. Apply appropriate imputation methods downstream.

- **Computational Speed**: Processing large datasets with many runs can be computationally intensive. Use multi-threading (`--threads`) for faster execution.

## Examples

### Basic label-free quantification
**Args:** `java -jar IonQuant.jar --specdir ./spectra/ --psm ./psm.tsv --output ./quant_results/ --threads 8`
**Explanation:** Performs MS1-based label-free quantification on spectra files using provided PSM identifications.

### With FDR-controlled MBR
**Args:** `java -jar IonQuant.jar --specdir ./spectra/ --psm ./psm.tsv --output ./quant_results/ --mbr --mbr-fdr 0.01`
**Explanation:** Enables match-between-runs with 1% FDR threshold to reduce missing values across multiple runs.

### timsTOF PASEF data
**Args:** `java -jar IonQuant.jar --specdir ./timsTOF_data/ --psm ./psm.tsv --output ./quant_results/ --imtol 0.05 --threads 12`
**Explanation:** Processes timsTOF PASEF data with ion mobility tolerance of 0.05 (1/K0 units).

### Isobaric labeling quantification
**Args:** `java -jar IonQuant.jar --specdir ./spectra/ --psm ./psm.tsv --output ./tmt_results/ --perform-isoquant 1 --isotype TMT-16`
**Explanation:** Performs isobaric quantification for TMT-16 labeled samples instead of label-free.

### Generate MSstats input
**Args:** `java -jar IonQuant.jar --specdir ./spectra/ --psm ./psm.tsv --output ./quant_results/ --msstats 1`
**Explanation:** Generates output files compatible with MSstats for downstream statistical analysis.

### Custom tolerance parameters
**Args:** `java -jar IonQuant.jar --specdir ./spectra/ --psm ./psm.tsv --output ./quant_results/ --mztol 5 --rttol 0.5 --threads 8`
**Explanation:** Adjusts MS1 mass tolerance to 5 ppm and retention time tolerance to 0.5 minutes.