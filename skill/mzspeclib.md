---
name: mzspeclib
category: formatting
description: mzSpecLib - HUPO-PSI Spectral library format library
tags: [mzspeclib, formatting, spectral-library, hupo-psi, proteomics]
author: oxo-call-community
source_url: "https://github.com/HUPO-PSI/mzSpecLib"
---

## Concepts

- **Tool Overview**: mzSpecLib v1.0.7 is the HUPO-PSI standard library format for proteomics spectral libraries. It provides a standardized format for storing, searching, and sharing mass spectrometry spectral libraries.
- **Core Function**: Implements the mzSpecLib format specification for representing spectral libraries including spectrum metadata, peptide annotations, fragment ions, and retention times.
- **Format Features**: Supports storage of consensus spectra, PSM (peptide-spectrum matches) collections, and library search results. Includes support for cross-linking and modified peptides.
- **Input Format**: Accepts mzSpecLib format files and can convert from common spectral library formats (NIST, BiblioSpec, SpectraST).
- **Output**: Produces mzSpecLib libraries with properly annotated spectra, supporting fast library search and spectrum comparison.
- **Use Case**: Library creation for database searching, spectral library sharing, reproducible proteomics research, and library comparison studies.

## Pitfalls

- **Library Curation**: Spectral libraries require careful curation. Poor quality spectra reduce search accuracy.
- **Version Compatibility**: Different library tools may support different mzSpecLib versions. Verify compatibility.
- **Modification Handling**: Consistent modification notation is critical. Use unimod modification names for standardized representation.
- **Library Size**: Large spectral libraries can be memory-intensive to search. Consider library partitioning for large datasets.
- **Decoy Spectra**: Library searches typically require decoy spectra for FDR estimation. Ensure proper decoy generation.
- **Spectra Quality**: Low-quality spectra (from poor fragmentation or low abundance) should be filtered before library creation.

## Examples

### Create spectral library
**Args:** `-i psms.tsv -o library.mzsplib`
**Explanation:** Creates a spectral library from PSM (peptide-spectrum match) results.

### Convert from NIST format
**Args:** `-i nist_library.msp -o converted.mzsplib`
**Explanation:** Converts a NIST-format spectral library to mzSpecLib format.

### Search spectra against library
**Args:** `-i experimental_spectra.mgf -l library.mzsplib -o matches.tsv`
**Explanation:** Searches experimental spectra against a spectral library.

### Display library statistics
**Args:** `-i library.mzsplib --stats`
**Explanation:** Shows statistics about the spectral library (number of spectra, modifications, etc.).

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage instructions.
