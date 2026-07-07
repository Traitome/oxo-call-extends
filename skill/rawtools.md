---
name: rawtools
category: expression
description: RawTools performs scan data parsing, quantification, and quality control analysis of Thermo Orbitrap raw mass spectrometer files.
tags: [rawtools, expression, proteomics, mass-spec]
author: oxo-call-community
source_url: "https://github.com/kevinkovalchik/RawTools"
---

## Concepts

- **Tool Overview**: rawtools analyzes mass spec.
- **Core Function**: Mass spec analysis.
- **Algorithm**: Uses parsing methods.
- **Input Format**: Accepts RAW files.
- **Output**: Produces quantification data.
- **Use Case**: Proteomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **File Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rawtools --help`
**Explanation:** Shows available options and usage instructions.

### Parse raw files
**Args:** `rawtools parse -i data.raw -o quantification.txt`
**Explanation:** Parses mass spec data.

### With parameters
**Args:** `rawtools parse -i data.raw -p params.yaml -o quantification.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rawtools -v parse -i data.raw -o quantification.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rawtools -t 4 parse -i data.raw -o quantification.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Quality control
**Args:** `rawtools qc -i data.raw -o qc_report.html`
**Explanation:** Performs QC analysis.

### Generate report
**Args:** `rawtools parse -i data.raw -o quantification.txt --report report.html`
**Explanation:** Generates HTML report.