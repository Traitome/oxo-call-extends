---
name: probamconvert
category: formatting
description: probamconvert converts peptide identification files to proBAM or proBED format.
tags: [probamconvert, formatting, proteomics, mass-spectrometry]
author: oxo-call-community
source_url: "https://github.com/Biobix/proBAMconvert"
---

## Concepts

- **Tool Overview**: probamconvert transforms proteomics data.
- **Core Function**: Format conversion.
- **Algorithm**: Uses proteomics data mapping methods.
- **Input Format**: Accepts mzIdentML/pepXML/mzTAB files.
- **Output**: Produces proBAM/proBED files.
- **Use Case**: Proteomics data integration.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Format Compatibility**: Must use supported formats.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proBAMconvert --help`
**Explanation:** Shows available options and usage instructions.

### Convert format
**Args:** `proBAMconvert -i peptides.mzid -o output.probam`
**Explanation:** Converts peptide identification file to proBAM format.

### With parameters
**Args:** `proBAMconvert -i peptides.mzid -p params.yaml -o output.probam`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proBAMconvert -v -i peptides.mzid -o output.probam`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proBAMconvert -t 4 -i peptides.mzid -o output.probam`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proBAMconvert -i peptides.mzid -o output.probed --probed`
**Explanation:** Outputs in proBED format.

### Generate report
**Args:** `proBAMconvert -i peptides.mzid -o output.probam --report report.html`
**Explanation:** Generates HTML report.