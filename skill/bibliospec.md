---
name: bibliospec
category: utility
description: BiblioSpec Spectral Library tool suite for proteomics
tags: [proteomics, spectral-library, mass-spectrometry]
author: oxo-call-community
source_url: "https://skyline.ms/project/home/software/BiblioSpec/begin.view"
---

## Concepts
- **Tool Overview**: BiblioSpec is a suite of tools for creating and managing spectral libraries used in targeted proteomics (SRM/PRM). It converts mass spectrometry search results into spectral library format.
- **Spectral Libraries**: Collections of previously identified peptide spectra used for targeted identification and quantification of peptides.
- **Tools Included**: `BuildSpec` (build spectral libraries), `BlibFilter` (filter libraries), `BlibToSptxt` (convert to NIST format), `BlibToTsv` (export to TSV).
- **Integration**: Works with Skyline and other targeted proteomics software.

## Pitfalls
- **Search Engine Results**: Requires properly formatted search results from tools like X!Tandem, Mascot, or MS-GF+.
- **Library Quality**: Library quality depends on the quality and FDR control of the input search results.
- **Format Compatibility**: Different downstream tools may require specific library formats.

## Examples
### Build spectral library
**Args:** `BuildSpec -in search_results.pepXML -out library.blib`
**Explanation:** Creates a spectral library from peptide identification results.

### Filter library by quality
**Args:** `BlibFilter -in library.blib -out filtered.blib -minPeptides 2`
**Explanation:** Filters library to keep only proteins with at least 2 peptide identifications.

### Export to TSV
**Args:** `BlibToTsv -in library.blib -out library.tsv`
**Explanation:** Exports spectral library to tab-separated format.
