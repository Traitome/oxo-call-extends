---
name: riassigner
category: programming
description: RIAssigner calculates retention indices for GC-MS data.
tags: [riassigner, programming, gc-ms, retention-index]
author: oxo-call-community
source_url: "https://github.com/RECETOX/RIAssigner"
---

## Concepts

- **Tool Overview**: riassigner calculates retention indices.
- **Core Function**: GC-MS retention index calculation.
- **Algorithm**: Uses chromatographic methods.
- **Input Format**: Accepts mass spectrometry data.
- **Output**: Produces retention indices.
- **Use Case**: Metabolomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Affects calculation.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `riassigner --help`
**Explanation:** Shows available options and usage instructions.

### Calculate RI
**Args:** `riassigner calculate -i peaks.csv -o ri_results.csv`
**Explanation:** Calculates retention indices.

### With parameters
**Args:** `riassigner calculate -i peaks.csv -p params.yaml -o ri_results.csv`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `riassigner -v calculate -i peaks.csv -o ri_results.csv`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `riassigner -t 4 calculate -i peaks.csv -o ri_results.csv`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `riassigner calculate -i peaks.csv -r reference.csv -o ri_results.csv`
**Explanation:** Uses reference standards.

### Generate plot
**Args:** `riassigner calculate -i peaks.csv -o ri_results.csv --plot plot.png`
**Explanation:** Generates visualization plot.