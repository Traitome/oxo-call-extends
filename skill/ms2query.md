---
name: ms2query
category: utility
description: Reliable and fast MS/MS spectral based analogue search.
tags: [ms2query, utility, proteomics]
author: oxo-call-community
source_url: "https://github.com/iomega/ms2query"
---

## Concepts

- **Tool Overview**: MS2Query v1.5.4 performs fast MS/MS spectral similarity search.
- **Core Function**: Searches for analogues using MS/MS spectrum comparison.
- **Spectral Search**: Finds similar spectra from reference databases.
- **Fast Algorithm**: Optimized for rapid spectral matching.
- **Metabolomics**: Specialized for metabolomics data analysis.
- **Input/Output**: Accepts query spectra; outputs similar spectrum matches.

## Pitfalls

- **MS/MS Specific**: Designed for mass spectrometry data.
- **Database Dependence**: Requires spectral reference database.
- **Memory Requirements**: Memory usage depends on database size.
- **Parameter Tuning**: May require parameter adjustment for matching.
- **Data Quality**: Results depend on spectrum quality.
- **Computational Resources**: Large databases may require significant resources.

## Examples

### Search for analogues
**Args:** `ms2query -i query_spectra.mgf -d library.mgf -o results.txt`
**Explanation:** Searches for similar spectra in reference library.

### With custom similarity threshold
**Args:** `ms2query -i query_spectra.mgf -d library.mgf -t 0.8 -o results.txt`
**Explanation:** Uses 0.8 similarity threshold.

### Batch processing
**Args:** `ms2query -i mgf/ -d library.mgf -o results/`
**Explanation:** Processes multiple query files.

### Generate report
**Args:** `ms2query -i query_spectra.mgf -d library.mgf -r report.html -o results.txt`
**Explanation:** Generates HTML report of matches.

### Update library
**Args:** `ms2query update_library -d library.mgf -a new_spectra.mgf -o library_updated.mgf`
**Explanation:** Adds new spectra to reference library.