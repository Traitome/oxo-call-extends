---
name: picopore
category: qc
description: picopore reduces Oxford Nanopore Technologies dataset sizes.
tags: [picopore, qc, nanopore, compression]
author: oxo-call-community
source_url: "https://github.com/scottgigante/picopore"
---

## Concepts

- **Tool Overview**: picopore compresses nanopore datasets.
- **Core Function**: Lossless data compression.
- **Algorithm**: Uses efficient compression methods.
- **Input Format**: Accepts nanopore data files.
- **Output**: Produces compressed results.
- **Use Case**: Data compression, storage optimization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Compression Ratio**: May vary by dataset.
- **Runtime**: Compression may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `picopore --help`
**Explanation:** Shows available options and usage instructions.

### Compress data
**Args:** `picopore -i nanopore_data/ -o compressed_data/`
**Explanation:** Compresses nanopore datasets.

### With parameters
**Args:** `picopore -i nanopore_data/ -p params.yaml -o compressed_data/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `picopore -v -i nanopore_data/ -o compressed_data/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `picopore -t 4 -i nanopore_data/ -o compressed_data/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `picopore -i nanopore_data/ -o compressed_data/ --format hdf5`
**Explanation:** Outputs in HDF5 format.

### Generate report
**Args:** `picopore -i nanopore_data/ -o compressed_data/ --report report.html`
**Explanation:** Generates HTML report.