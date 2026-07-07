---
name: qiimetomaaslin
category: formatting
description: QiimeToMaaslin converts QIIME OTU tables to PCL-formatted, MaAsLin-compatible text files.
tags: [qiimetomaaslin, formatting, qiime, maaslin]
author: oxo-call-community
source_url: "https://huttenhower.sph.harvard.edu/maaslin"
---

## Concepts

- **Tool Overview**: qiimetomaaslin converts OTU tables.
- **Core Function**: Format conversion.
- **Algorithm**: Data transformation.
- **Input Format**: Accepts QIIME OTU tables.
- **Output**: Produces MaAsLin format.
- **Use Case**: Data integration.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large tables require memory.
- **Input Format**: Must be QIIME format.
- **Output Format**: Must be correct.
- **Runtime**: Conversion may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qiimetomaaslin --help`
**Explanation:** Shows available options and usage instructions.

### Convert table
**Args:** `qiimetomaaslin convert -i otu_table.txt -o maaslin_input.txt`
**Explanation:** Converts QIIME OTU table.

### With parameters
**Args:** `qiimetomaaslin convert -i otu_table.txt -p params.yaml -o maaslin_input.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qiimetomaaslin -v convert -i otu_table.txt -o maaslin_input.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qiimetomaaslin -t 4 convert -i otu_table.txt -o maaslin_input.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With metadata
**Args:** `qiimetomaaslin convert -i otu_table.txt -m metadata.txt -o maaslin_input.txt`
**Explanation:** Includes metadata.

### Generate report
**Args:** `qiimetomaaslin convert -i otu_table.txt -o maaslin_input.txt --report report.html`
**Explanation:** Generates HTML report.