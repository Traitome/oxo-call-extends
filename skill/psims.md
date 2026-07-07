---
name: psims
category: utility
description: psims provides writers and controlled vocabulary management for PSI-MS standards (mzML, mzIdentML).
tags: [psims, utility, mass-spectrometry, mzML]
author: oxo-call-community
source_url: "https://mobiusklein.github.io/psims/docs/build/html/"
---

## Concepts

- **Tool Overview**: psims handles mass spectrometry data formats.
- **Core Function**: File writing and vocabulary management.
- **Algorithm**: Uses controlled vocabulary.
- **Input Format**: Accepts mass spec data.
- **Output**: Produces mzML/mzIdentML files.
- **Use Case**: Mass spectrometry data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Vocabulary Version**: Affects compatibility.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psims --help`
**Explanation:** Shows available options and usage instructions.

### Write mzML
**Args:** `psims write -i data.json -o output.mzML`
**Explanation:** Writes data to mzML format.

### With parameters
**Args:** `psims write -i data.json -p params.yaml -o output.mzML`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psims -v write -i data.json -o output.mzML`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psims -t 4 write -i data.json -o output.mzML`
**Explanation:** Uses 4 threads for parallel processing.

### List vocabularies
**Args:** `psims vocab list`
**Explanation:** Lists available controlled vocabularies.

### Generate report
**Args:** `psims write -i data.json -o output.mzML --report report.html`
**Explanation:** Generates HTML report.