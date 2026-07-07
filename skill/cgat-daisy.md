---
name: cgat-daisy
category: benchmarking
description: System to design and execute benchmarks for bioinformatics tools
tags: [cgat-daisy, benchmarking, bioinformatics, performance-testing]
author: oxo-call-community
source_url: "https://github.com/cgat-developers/cgat-daisy"
---

## Concepts

- **Tool Overview**: CGAT-Daisy is a system to design and execute benchmarks for bioinformatics tools and pipelines.
- **Core Function**: Provides framework for defining, running, and analyzing benchmark experiments.
- **Features**: Benchmark definition, execution management, result collection, and performance analysis.
- **Input**: Benchmark configuration files and test datasets.
- **Output**: Performance metrics, timing results, and comparison reports.
- **Application**: Evaluating bioinformatics tool performance and comparing different methods.
- **Installation**: Install via bioconda: `conda install -c bioconda cgat-daisy`

## Pitfalls

- **Test Data Quality**: Benchmark results depend on test dataset quality and representativeness.
- **Resource Allocation**: Ensure consistent compute resources across benchmark runs.
- **Reproducibility**: Requires careful environment setup for reproducible results.
- **Runtime Variability**: Performance may vary between runs due to system load.

## Examples

### Create benchmark definition
**Args:** `cgat-daisy init my_benchmark`
**Explanation:** Creates a new benchmark project with template files.

### Run benchmark
**Args:** `cgat-daisy run benchmark.yml`
**Explanation:** Executes benchmark defined in configuration file.

### Generate report
**Args:** `cgat-daisy report --input results/ --output report.html`
**Explanation:** Generates HTML report from benchmark results.

### Display help
**Args:** `cgat-daisy --help`
**Explanation:** Shows all available options and usage information.