---
name: psm_fragments
category: utility
description: psm_fragments validates peptide-spectrum matches (PSM) against ion fragmentation data.
tags: [psm_fragments, utility, mass-spectrometry, PSM-validation]
author: oxo-call-community
source_url: "https://github.com/galaxyproteomics/psm_fragments"
---

## Concepts

- **Tool Overview**: psm_fragments validates PSM data.
- **Core Function**: Fragment ion validation.
- **Algorithm**: Uses fragmentation matching.
- **Input Format**: Accepts mass spec data.
- **Output**: Produces validation results.
- **Use Case**: Proteomics validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Fragmentation Model**: Affects validation.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psm_fragments --help`
**Explanation:** Shows available options and usage instructions.

### Validate PSM
**Args:** `psm_fragments -i psm.txt -f fragments.txt -o validation.txt`
**Explanation:** Validates PSM against fragmentation data.

### With parameters
**Args:** `psm_fragments -i psm.txt -f fragments.txt -p params.yaml -o validation.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psm_fragments -v -i psm.txt -f fragments.txt -o validation.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psm_fragments -t 4 -i psm.txt -f fragments.txt -o validation.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `psm_fragments -i psm.txt -f fragments.txt -o validation.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `psm_fragments -i psm.txt -f fragments.txt -o validation.txt --report report.html`
**Explanation:** Generates HTML report.