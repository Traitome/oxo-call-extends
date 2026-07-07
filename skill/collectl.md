---
name: collectl
category: utility
description: Light-weight performance monitoring tool for system metrics
tags: [collectl, performance-monitoring, system-metrics, bioinformatics, hpc]
author: oxo-call-community
source_url: "https://collectl.sourceforge.net"
---

## Concepts

- **Tool Overview**: collectl is a lightweight performance monitoring tool capable of reporting interactively or logging system metrics to disk for later analysis.
- **Core Function**: Collects and reports system performance metrics including CPU, memory, disk, network, and application-specific statistics.
- **Algorithm**: Gathers system metrics from kernel interfaces and exposes them in various formats for analysis.
- **Input**: System performance counters and application metrics.
- **Output**: Performance data in text, CSV, or interactive display format.
- **Application**: HPC cluster monitoring, bioinformatics pipeline performance tracking, and system optimization.
- **Installation**: Install via bioconda: `conda install -c bioconda collectl`

## Pitfalls

- **Sampling Rate**: High sampling rates may impact system performance.
- **Disk Space**: Continuous logging can consume significant disk space.
- **Metric Selection**: Selecting too many metrics increases overhead.
- **Output Format**: Different formats have different parsing requirements.
- **Permissions**: May require elevated privileges for some metrics.

## Examples

### Monitor system interactively
**Args:** `collectl -i 1`
**Explanation:** Displays system metrics every 1 second interactively.

### Log to file
**Args:** `collectl -sCDN -oT -f system_log`
**Explanation:** Logs CPU, disk, and network metrics to file.

### Export to CSV
**Args:** `collectl -sC -oT -f cpu_metrics --csv`
**Explanation:** Exports CPU metrics in CSV format.

### Display help
**Args:** `collectl --help`
**Explanation:** Shows all available options and usage information.