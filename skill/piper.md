---
name: piper
category: programming
description: piper is a lightweight Python toolkit for building command line pipelines.
tags: [piper, programming, pipeline, python]
author: oxo-call-community
source_url: "https://github.com/databio/pypiper"
---

## Concepts

- **Tool Overview**: piper builds robust command line pipelines.
- **Core Function**: Pipeline construction and execution.
- **Algorithm**: Uses workflow management methods.
- **Input Format**: Accepts pipeline configuration files.
- **Output**: Produces pipeline execution results.
- **Use Case**: Workflow automation, pipeline building.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex pipelines require memory.
- **Configuration Errors**: May have setup issues.
- **Pipeline Robustness**: May fail unexpectedly.
- **Runtime**: Execution may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `piper --help`
**Explanation:** Shows available options and usage instructions.

### Run pipeline
**Args:** `piper -i pipeline.yaml -o results/`
**Explanation:** Executes command line pipeline.

### With parameters
**Args:** `piper -i pipeline.yaml -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `piper -v -i pipeline.yaml -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `piper -t 4 -i pipeline.yaml -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `piper -i pipeline.yaml -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `piper -i pipeline.yaml -o results/ --report report.html`
**Explanation:** Generates HTML report.