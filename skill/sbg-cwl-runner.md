---
name: sbg-cwl-runner
category: workflow-management
description: CWL Runner for Seven Bridges Genomics (SBG) platform
tags: ["sbg-cwl-runner", "workflow-management", "CWL", "SBG"]
author: oxo-call-community
source_url: "https://github.com/kaushik-work/sbg-cwl-runner"
---

## Concepts

- **Tool Overview**: sbg-cwl-runner (v2018.11) is a CWL (Common Workflow Language) Runner for the Seven Bridges Genomics (SBG) platform.
- **Core Function**: Executes CWL workflows on the SBG cloud platform, enabling scalable bioinformatics analysis.
- **Algorithm**: Implements CWL execution engine optimized for SBG infrastructure.
- **Input/Output**: Accepts CWL workflow files and produces workflow execution results.
- **Cloud Integration**: Seamlessly integrates with SBG cloud storage and compute resources.
- **Applications**: Running standardized bioinformatics workflows on cloud infrastructure.

## Pitfalls

- **SBG Specific**: Designed specifically for Seven Bridges Genomics platform.
- **Cloud Dependencies**: Requires SBG account and cloud resources.
- **CWL Version**: May not support all CWL specifications.
- **Network Requirements**: Requires stable network connection to cloud services.
- **Cost Considerations**: Cloud execution may incur significant costs.
- **Authentication**: Requires proper API key configuration.

## Examples

### Run CWL workflow
**Args:** `sbg-cwl-runner workflow.cwl inputs.yml`
**Explanation:** Runs specified CWL workflow with input parameters from YAML file.

### With verbose output
**Args:** `sbg-cwl-runner --verbose workflow.cwl inputs.yml`
**Explanation:** `--verbose` enables detailed logging during execution.

### Specify project
**Args:** `sbg-cwl-runner --project my-project workflow.cwl inputs.yml`
**Explanation:** `--project` specifies SBG project for execution.

### Local execution mode
**Args:** `sbg-cwl-runner --local workflow.cwl inputs.yml`
**Explanation:** `--local` runs workflow locally instead of on SBG cloud.

### Output to specific folder
**Args:** `sbg-cwl-runner --output-folder results/ workflow.cwl inputs.yml`
**Explanation:** `--output-folder` specifies output directory for results.

### Validate workflow
**Args:** `sbg-cwl-runner --validate workflow.cwl`
**Explanation:** `--validate` validates CWL workflow syntax without execution.

### Dry run
**Args:** `sbg-cwl-runner --dry-run workflow.cwl inputs.yml`
**Explanation:** `--dry-run` simulates workflow execution without actual computation.