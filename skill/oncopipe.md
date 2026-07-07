---
name: oncopipe
category: utility
description: Oncopipe provides functions for running Snakemake modules in cancer genomics workflows.
tags: [oncopipe, utility, snakemake, workflow-management]
author: oxo-call-community
source_url: "https://github.com/LCR-BCCRC/lcr-modules"
---

## Concepts

- **Tool Overview**: Oncopipe simplifies running Snakemake workflows for cancer analysis.
- **Core Function**: Manages and executes Snakemake modules.
- **Algorithm**: Uses Snakemake workflow engine for task management.
- **Input Format**: Accepts workflow configurations and input files.
- **Output**: Produces workflow outputs and reports.
- **Use Case**: Cancer genomics pipelines, workflow automation, and reproducible research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Snakemake Dependency**: Requires Snakemake installation.
- **Configuration**: Requires proper workflow configuration.
- **Resource Management**: Requires proper resource allocation.
- **Error Handling**: Workflow errors require debugging.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `oncopipe --help`
**Explanation:** Shows available options and usage instructions.

### Run workflow
**Args:** `oncopipe run -w workflow.smk -c config.yaml`
**Explanation:** Runs Snakemake workflow with configuration.

### List modules
**Args:** `oncopipe modules list`
**Explanation:** Lists available Snakemake modules.

### Install module
**Args:** `oncopipe modules install module_name`
**Explanation:** Installs specific Snakemake module.

### Dry run
**Args:** `oncopipe run -w workflow.smk -n`
**Explanation:** Performs dry run without execution.

### Verbose mode
**Args:** `oncopipe run -w workflow.smk -v`
**Explanation:** Runs with verbose output.

### Generate report
**Args:** `oncopipe report -w workflow.smk -o report.html`
**Explanation:** Generates workflow report.