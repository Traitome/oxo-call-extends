---
name: qax
category: utility
description: Qax extracts data, metadata, bibliography and provenance from Qiime2 artifacts.
tags: [qax, utility, qiime2, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/telatin/qax"
---

## Concepts

- **Tool Overview**: qax extracts Qiime2 data.
- **Core Function**: Data extraction.
- **Algorithm**: Uses Qiime2 API.
- **Input Format**: Accepts QZA/QZV files.
- **Output**: Produces extracted data.
- **Use Case**: Data analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large artifacts require memory.
- **File Format**: Must be Qiime2.
- **Dependencies**: Must be installed.
- **Runtime**: Extraction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qax --help`
**Explanation:** Shows available options and usage instructions.

### Extract data
**Args:** `qax extract -i artifact.qza -o output/`
**Explanation:** Extracts data from Qiime2 artifact.

### With parameters
**Args:** `qax extract -i artifact.qza -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qax -v extract -i artifact.qza -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qax -t 4 extract -i artifact.qza -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### List contents
**Args:** `qax list -i artifact.qza`
**Explanation:** Shows artifact contents.

### Generate report
**Args:** `qax extract -i artifact.qza -o output/ --report report.html`
**Explanation:** Generates HTML report.