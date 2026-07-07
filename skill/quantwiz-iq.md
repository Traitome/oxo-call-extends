---
name: quantwiz-iq
category: utility
description: QuantWiz-IQ performs reporter-based MS/MS quantitation using iTRAQ or TMT tags from shotgun proteomics experiments.
tags: [quantwiz-iq, utility, proteomics, mass-spectrometry]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/quantwiz/"
---

## Concepts

- **Tool Overview**: quantwiz-iq quantifies proteins.
- **Core Function**: MS/MS quantitation.
- **Algorithm**: Uses reporter ions.
- **Input Format**: Accepts MS data.
- **Output**: Produces quantitation results.
- **Use Case**: Proteomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tag Type**: Must be specified.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quantwiz-iq --help`
**Explanation:** Shows available options and usage instructions.

### Run quantitation
**Args:** `quantwiz-iq quantify -i ms_data.mzML -o results.txt`
**Explanation:** Performs protein quantitation.

### With parameters
**Args:** `quantwiz-iq quantify -i ms_data.mzML -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quantwiz-iq -v quantify -i ms_data.mzML -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quantwiz-iq -t 4 quantify -i ms_data.mzML -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### iTRAQ mode
**Args:** `quantwiz-iq quantify -i ms_data.mzML -t itraq -o results.txt`
**Explanation:** Uses iTRAQ tags.

### Generate report
**Args:** `quantwiz-iq quantify -i ms_data.mzML -o results.txt --report report.html`
**Explanation:** Generates HTML report.