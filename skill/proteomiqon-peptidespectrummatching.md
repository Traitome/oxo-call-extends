---
name: proteomiqon-peptidespectrummatching
category: formatting
description: proteomiqon-peptidespectrummatching performs peptide spectrum matching using SEQUEST, Andromeda, and XTandem algorithms.
tags: [proteomiqon-peptidespectrummatching, formatting, proteomics, spectrum-matching]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/PeptideSpectrumMatching.html"
---

## Concepts

- **Tool Overview**: proteomiqon-peptidespectrummatching matches peptides to spectra.
- **Core Function**: Peptide identification.
- **Algorithm**: Uses SEQUEST, Andromeda, XTandem.
- **Input Format**: Accepts mzLite files.
- **Output**: Produces PSM results.
- **Use Case**: Mass spectrometry analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Search Sensitivity**: May affect identification.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proteomiqon-peptidespectrummatching --help`
**Explanation:** Shows available options and usage instructions.

### Match spectra
**Args:** `proteomiqon-peptidespectrummatching -i ms_data.mzLite -d peptide_db.sqlite -o psm_results.txt`
**Explanation:** Performs peptide spectrum matching.

### With parameters
**Args:** `proteomiqon-peptidespectrummatching -i ms_data.mzLite -d peptide_db.sqlite --params params.yaml -o psm_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proteomiqon-peptidespectrummatching -v -i ms_data.mzLite -d peptide_db.sqlite -o psm_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proteomiqon-peptidespectrummatching -t 4 -i ms_data.mzLite -d peptide_db.sqlite -o psm_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Algorithm selection
**Args:** `proteomiqon-peptidespectrummatching -i ms_data.mzLite -d peptide_db.sqlite --algorithm sequest -o psm_results.txt`
**Explanation:** Uses SEQUEST algorithm.

### Generate report
**Args:** `proteomiqon-peptidespectrummatching -i ms_data.mzLite -d peptide_db.sqlite -o psm_results.txt --report report.html`
**Explanation:** Generates HTML report.