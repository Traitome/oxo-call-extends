---
name: snakemake-scheduler-plugin-greedy
category: programming
description: snakemake-scheduler-plugin-greedy - A greedy Snakemake scheduler plugin
tags: [snakemake-scheduler-plugin-greedy, programming, snakemake, scheduler, greedy]
author: oxo-call-community
source_url: "https://github.com/snakemake/snakemake-scheduler-plugin-greedy"
---

## Concepts

- **Tool Overview**: snakemake-scheduler-plugin-greedy (v0.1.5) - A greedy scheduler plugin for Snakemake workflows
- **Core Function**: Schedules jobs using greedy algorithm that selects jobs maximizing resource utilization
- **Input/Output**: Accepts job resource requirements; outputs scheduling decisions
- **Algorithm**: Greedy scheduling that picks jobs providing best immediate resource utilization
- **Installation**: `conda install -c bioconda snakemake-scheduler-plugin-greedy`
- **Key Features**: Resource-efficient scheduling, simple implementation, fast decision making

## Pitfalls

- **Local Optima**: Greedy approach may not find globally optimal schedule
- **Short-sighted**: May miss better long-term scheduling opportunities
- **Version Compatibility**: Requires specific Snakemake version
- **Resource Fragmentation**: Can still lead to resource fragmentation
- **Configuration**: May require tuning for specific workflows
- **Documentation**: Limited documentation available

## Examples

### Display help
**Args:** `snakemake-scheduler-plugin-greedy --help`
**Explanation:** Shows available options and usage information.

### Run Snakemake with greedy scheduler
**Args:** `snakemake --scheduler greedy -j 16`
**Explanation:** Run Snakemake with greedy scheduler.

### With resource limits
**Args:** `snakemake --scheduler greedy -j 16 --default-resources mem_mb=8000`
**Explanation:** Set default resource limits for scheduling.

### Enable debug mode
**Args:** `snakemake --scheduler greedy --scheduler-greedy-debug`
**Explanation:** Enable debug logging for the scheduler.

### With priority rules
**Args:** `snakemake --scheduler greedy --scheduler-greedy-priority rule_priority.txt`
**Explanation:** Use custom rule priority file.

### Run with executor
**Args:** `snakemake --scheduler greedy --executor slurm -j 100`
**Explanation:** Use greedy scheduler with SLURM executor.

### With custom configuration
**Args:** `snakemake --scheduler greedy --scheduler-greedy-config config.yaml`
**Explanation:** Use custom scheduler configuration.

### Show scheduler info
**Args:** `snakemake --scheduler greedy --scheduler-greedy-info`
**Explanation:** Show scheduler information and statistics.