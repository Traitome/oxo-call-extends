---
name: qiime-default-reference
category: utility
description: QIIME default reference data files for microbial ecology analysis.
tags: [qiime-default-reference, utility, qiime, reference]
author: oxo-call-community
source_url: "http://www.qiime.org"
---

## Concepts

- **Tool Overview**: qiime-default-reference provides reference data.
- **Core Function**: Reference management.
- **Algorithm**: Data retrieval.
- **Input Format**: Accepts configuration.
- **Output**: Produces reference files.
- **Use Case**: QIIME analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Reference Version**: Must match.
- **Download**: Requires network.
- **Runtime**: Installation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qiime-default-reference --help`
**Explanation:** Shows available options and usage instructions.

### Install reference
**Args:** `qiime-default-reference install -o reference_dir/`
**Explanation:** Installs default reference data.

### With parameters
**Args:** `qiime-default-reference install -p params.yaml -o reference_dir/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qiime-default-reference -v install -o reference_dir/`
**Explanation:** Runs with verbose output.

### List references
**Args:** `qiime-default-reference list`
**Explanation:** Shows available references.

### Update reference
**Args:** `qiime-default-reference update -o reference_dir/`
**Explanation:** Updates reference data.

### Generate report
**Args:** `qiime-default-reference install -o reference_dir/ --report report.html`
**Explanation:** Generates HTML report.