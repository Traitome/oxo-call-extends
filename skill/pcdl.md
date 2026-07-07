---
name: pcdl
category: formatting
description: pcdl provides PhysiCell data loader for transforming simulation output.
tags: [pcdl, formatting, physicell, simulation]
author: oxo-call-community
source_url: "https://github.com/elmbeech/physicelldataloader"
---

## Concepts

- **Tool Overview**: pcdl loads PhysiCell simulation data.
- **Core Function**: Transforms PhysiCell output to standard formats.
- **Algorithm**: Uses Python-based data transformation.
- **Input Format**: Accepts PhysiCell simulation output.
- **Output**: Produces standard format files.
- **Use Case**: Agent-based modeling, simulation analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large simulations require memory.
- **Data Format**: Requires PhysiCell-specific format.
- **Python Version**: Requires Python 3 environment.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pcdl --help`
**Explanation:** Shows available options and usage instructions.

### Load data
**Args:** `pcdl -i output/ -o processed/`
**Explanation:** Loads PhysiCell output data.

### Convert format
**Args:** `pcdl -i output/ -o processed.csv --csv`
**Explanation:** Converts to CSV format.

### Verbose mode
**Args:** `pcdl -v -i output/ -o processed/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pcdl -t 4 -i output/ -o processed/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pcdl -i output/ -o processed.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pcdl -i output/ -o report.html --report`
**Explanation:** Generates HTML report.