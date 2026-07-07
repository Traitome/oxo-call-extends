---
name: rabix-bunny
category: hpc
description: Rabix Bunny is an open-source executor for the Common Workflow Language (CWL) that runs workflows locally from the command line.
tags: [rabix-bunny, hpc, workflow, cwl]
author: oxo-call-community
source_url: "https://github.com/rabix/bunny"
---

## Concepts

- **Tool Overview**: rabix-bunny executes workflows.
- **Core Function**: CWL execution.
- **Algorithm**: Uses workflow engine.
- **Input Format**: Accepts CWL files.
- **Output**: Produces workflow results.
- **Use Case**: Workflow automation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large workflows require memory.
- **CWL Version**: Must be compatible.
- **Parameters**: Must be configured.
- **Runtime**: Execution may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rabix-bunny --help`
**Explanation:** Shows available options and usage instructions.

### Run workflow
**Args:** `rabix-bunny run -i workflow.cwl -j inputs.json -o output/`
**Explanation:** Executes CWL workflow.

### With parameters
**Args:** `rabix-bunny run -i workflow.cwl -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rabix-bunny -v run -i workflow.cwl -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rabix-bunny -t 4 run -i workflow.cwl -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### Debug mode
**Args:** `rabix-bunny run -i workflow.cwl -d -o output/`
**Explanation:** Runs in debug mode.

### Generate report
**Args:** `rabix-bunny run -i workflow.cwl -o output/ --report report.html`
**Explanation:** Generates HTML report.