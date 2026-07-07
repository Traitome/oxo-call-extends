---
name: sirius-csifingerid
category: metabolomics
description: SIRIUS - LC-MS/MS data analysis framework
tags: ["sirius-csifingerid", "metabolomics", "lc-msms", "identification"]
author: oxo-call-community
source_url: "https://boecker-lab.github.io/docs.sirius.github.io/"
---

## Concepts

- **Tool Overview**: SIRIUS (v5.8.6) analyzes LC-MS/MS data for metabolite identification.
- **Core Function**: Identifies metabolites using fragmentation patterns.
- **Algorithm**: Uses CSI:FingerID and CANOPUS for compound identification.
- **Input/Output**: Accepts mass spectrometry data and produces metabolite annotations.
- **Metabolite Identification**: Specialized for metabolomics analysis.
- **Applications**: Metabolomics, metabolite profiling, compound identification.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Database Requirements**: Requires reference compound databases.
- **Input Quality**: Results depend on mass spectrometry data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Run SIRIUS
**Args:** `sirius -i spectra.mzML -o results/`
**Explanation:** `-i` input spectra; `-o` output directory.

### With database
**Args:** `sirius -i spectra.mzML -d pubchem -o results/`
**Explanation:** `-d pubchem` use PubChem database.

### Run CSI:FingerID
**Args:** `sirius -i spectra.mzML --fingerid -o results/`
**Explanation:** `--fingerid` enable CSI:FingerID.

### Help command
**Args:** `sirius --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sirius --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sirius -v -i spectra.mzML -o results/`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sirius -t 8 -i spectra.mzML -o results/`
**Explanation:** `-t 8` uses 8 threads.
