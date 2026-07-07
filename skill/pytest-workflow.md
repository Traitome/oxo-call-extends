---
name: pytest-workflow
category: hpc
description: pytest-workflow is a pytest plugin for configuring and testing bioinformatics workflows using YAML files.
tags: [pytest-workflow, hpc, workflow, testing]
author: oxo-call-community
source_url: "https://pytest-workflow.readthedocs.io"
---

## Concepts

- **Tool Overview**: pytest-workflow tests pipelines.
- **Core Function**: Workflow testing.
- **Algorithm**: Uses pytest framework.
- **Input Format**: Accepts YAML config.
- **Output**: Produces test results.
- **Use Case**: Pipeline validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex workflows require memory.
- **YAML Syntax**: Must be correct.
- **Dependency Management**: Must be handled.
- **Runtime**: Testing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pytest-workflow --help`
**Explanation:** Shows available options and usage instructions.

### Run workflow tests
**Args:** `pytest-workflow run -i workflows/ -o results.xml`
**Explanation:** Runs workflow tests.

### With parameters
**Args:** `pytest-workflow run -i workflows/ -p params.yaml -o results.xml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pytest-workflow -v run -i workflows/ -o results.xml`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pytest-workflow -t 4 run -i workflows/ -o results.xml`
**Explanation:** Uses 4 threads for parallel processing.

### Specific workflow
**Args:** `pytest-workflow run -i workflows/my_workflow.yaml -o results.xml`
**Explanation:** Runs specific workflow.

### Generate report
**Args:** `pytest-workflow run -i workflows/ -o results.xml --report report.html`
**Explanation:** Generates HTML report.