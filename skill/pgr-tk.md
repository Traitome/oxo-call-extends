---
name: pgr-tk
category: programming
description: pgr-tk provides libraries for pangenomics analysis.
tags: [pgr-tk, programming, pangenomics, library]
author: oxo-call-community
source_url: "https://github.com/GeneDx/pgr-tk"
---

## Concepts

- **Tool Overview**: pgr-tk enables pangenomics analysis.
- **Core Function**: Provides Python and Rust libraries.
- **Algorithm**: Uses pangenomic data structures.
- **Input Format**: Accepts genome data files.
- **Output**: Produces pangenomic analysis results.
- **Use Case**: Pangenomics, library development.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Library Dependencies**: Requires proper library setup.
- **Language Support**: Python and Rust required.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgr-tk --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pgr-tk -i genomes/ -o pangenome_results/`
**Explanation:** Runs pangenomics analysis.

### With config
**Args:** `pgr-tk -i genomes/ -c config.yaml -o pangenome_results/`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `pgr-tk -v -i genomes/ -o pangenome_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgr-tk -t 8 -i genomes/ -o pangenome_results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pgr-tk -i genomes/ -o pangenome_results/ --format json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pgr-tk -i genomes/ -o pangenome_results/ --report report.html`
**Explanation:** Generates HTML report.