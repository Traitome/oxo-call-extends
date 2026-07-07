---
name: pyonsite
category: utility
description: PyOnSite is a mass spectrometry tool for post-translational modification localization.
tags: [pyonsite, utility, mass-spectrometry, ptm]
author: oxo-call-community
source_url: "https://www.github.com/bigbio/onsite"
---

## Concepts

- **Tool Overview**: pyonsite localizes PTMs.
- **Core Function**: PTM localization.
- **Algorithm**: Uses mass spec data.
- **Input Format**: Accepts mass spec files.
- **Output**: Produces localization results.
- **Use Case**: Proteomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Search Parameters**: Affect localization.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyonsite --help`
**Explanation:** Shows available options and usage instructions.

### Localize PTMs
**Args:** `pyonsite localize -i spectra.mzML -d database.fasta -o results.txt`
**Explanation:** Identifies PTM locations.

### With parameters
**Args:** `pyonsite localize -i spectra.mzML -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyonsite -v localize -i spectra.mzML -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyonsite -t 4 localize -i spectra.mzML -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Filter by score
**Args:** `pyonsite localize -i spectra.mzML -s 0.95 -o results.txt`
**Explanation:** Filters by localization score.

### Generate report
**Args:** `pyonsite localize -i spectra.mzML -o results.txt --report report.html`
**Explanation:** Generates HTML report.