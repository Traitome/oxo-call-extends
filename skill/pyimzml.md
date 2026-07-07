---
name: pyimzml
category: utility
description: pyimzML parses and converts imzML 1.1.0 files for mass spectrometry imaging data.
tags: [pyimzml, utility, mass-spectrometry, imaging]
author: oxo-call-community
source_url: "https://github.com/alexandrovteam/pyimzML"
---

## Concepts

- **Tool Overview**: pyimzml processes imzML files.
- **Core Function**: Mass spectrometry data parsing.
- **Algorithm**: Uses XML parsing.
- **Input Format**: Accepts imzML files.
- **Output**: Produces processed data.
- **Use Case**: Imaging mass spectrometry.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Format Version**: Must be imzML 1.1.0.
- **Data Compression**: May affect reading.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyimzml --help`
**Explanation:** Shows available options and usage instructions.

### Parse imzML
**Args:** `pyimzml parse -i data.imzML -o output.txt`
**Explanation:** Parses imzML file.

### With parameters
**Args:** `pyimzml parse -i data.imzML -p params.yaml -o output.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyimzml -v parse -i data.imzML -o output.txt`
**Explanation:** Runs with verbose output.

### Convert format
**Args:** `pyimzml convert -i data.imzML -f mzML -o data.mzML`
**Explanation:** Converts imzML to mzML.

### Extract spectra
**Args:** `pyimzml extract -i data.imzML -r 100-200 -o spectra.txt`
**Explanation:** Extracts spectra in range.

### Generate report
**Args:** `pyimzml parse -i data.imzML -o output.txt --report report.html`
**Explanation:** Generates HTML report.