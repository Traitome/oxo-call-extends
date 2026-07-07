---
name: snkmt
category: programming
description: SNKMT - Terminal User Interface for monitoring Snakemake workflows
tags: [snkmt, programming, snakemake, monitoring, tui]
author: oxo-call-community
source_url: "https://github.com/cademirch/snkmt"
---

## Concepts

- **Tool Overview**: snkmt (v0.4.0) - A TUI for real-time Snakemake workflow monitoring
- **Core Function**: Provides terminal interface for monitoring workflow execution
- **Input/Output**: Connects to running Snakemake workflows; displays real-time status
- **Algorithm**: Parses Snakemake logs and displays progress in TUI
- **Installation**: `conda install -c bioconda snkmt`
- **Key Features**: Real-time monitoring, TUI interface, progress tracking

## Pitfalls

- **Terminal Compatibility**: Requires terminal with TUI support
- **Running Workflows**: Can only monitor actively running workflows
- **Log Parsing**: Relies on proper log format from Snakemake
- **Resource Usage**: May consume additional system resources
- **Connection Issues**: May lose connection to long-running workflows
- **Display Issues**: May have display issues on some terminals

## Examples

### Display help
**Args:** `snkmt --help`
**Explanation:** Shows available options and usage information.

### Monitor workflow
**Args:** `snkmt`
**Explanation:** Start TUI and monitor running workflows.

### With specific workflow
**Args:** `snkmt --workflow Snakefile`
**Explanation:** Monitor specific workflow file.

### With log file
**Args:** `snkmt --log snakemake.log`
**Explanation:** Monitor workflow from log file.

### Filter by rule
**Args:** `snkmt --filter-rule "rule_name"`
**Explanation:** Monitor specific rule execution.

### Show all jobs
**Args:** `snkmt --show-all`
**Explanation:** Display all jobs including completed ones.

### Export status
**Args:** `snkmt --export status.json`
**Explanation:** Export workflow status to JSON.