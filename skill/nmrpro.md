---
name: nmrpro
category: utility
description: NMRPro reads and processes different types of NMR spectra for analysis.
tags: [nmrpro, utility, nmr, spectroscopy]
author: oxo-call-community
source_url: "https://github.com/ahmohamed/nmrpro"
---

## Concepts

- **Tool Overview**: NMRPro processes and analyzes NMR spectra data.
- **Core Function**: Reads, processes, and visualizes NMR spectra.
- **Algorithm**: Implements various NMR processing algorithms.
- **Input Format**: Accepts various NMR data formats.
- **Output**: Produces processed spectra and analysis results.
- **Use Case**: NMR data analysis, peak identification, and spectral comparison.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **File Compatibility**: Requires specific NMR data formats.
- **Memory Usage**: Large spectra require memory.
- **Dependency**: Requires Python and related scientific libraries.
- **Documentation**: Limited documentation.
- **Performance**: May have performance considerations.

## Examples

### Display help
**Args:** `nmrpro --help`
**Explanation:** Shows available options and usage instructions.

### Read spectrum
**Args:** `nmrpro read -i spectrum.dat -o processed.nmr`
**Explanation:** Reads and processes NMR spectrum.

### Peak picking
**Args:** `nmrpro peaks -i spectrum.dat -o peaks.txt`
**Explanation:** Detects peaks in NMR spectrum.

### Baseline correction
**Args:** `nmrpro baseline -i spectrum.dat -o corrected.dat`
**Explanation:** Corrects baseline in spectrum.

### Normalize spectrum
**Args:** `nmrpro normalize -i spectrum.dat -o normalized.dat`
**Explanation:** Normalizes NMR spectrum.

### Plot spectrum
**Args:** `nmrpro plot -i spectrum.dat -o spectrum.png`
**Explanation:** Generates spectrum plot.

### Compare spectra
**Args:** `nmrpro compare -i1 spec1.dat -i2 spec2.dat -o comparison.txt`
**Explanation:** Compares two NMR spectra.