---
name: bcbio_monitor
category: utility
description: bcbio-monitor - Visualization tool for monitoring bcbio-nextgen pipeline progress
tags: [bcbio_monitor, utility, bcbio-nextgen, monitoring, visualization]
author: oxo-call-community
source_url: "https://github.com/guillermo-carrasco/bcbio-nextgen-monitor"
---

## Concepts

- **Tool Overview**: bcbio-monitor (v1.0.6) is an extension of bcbio-nextgen that provides real-time visualization and monitoring of bioinformatics analysis pipeline progress.
- **Core Function**: Tracks and visualizes the progress of bcbio-nextgen sequencing analysis pipelines.
- **Real-time Monitoring**: Provides live updates on pipeline execution status.
- **Progress Visualization**: Displays task completion status, runtime metrics, and resource usage.
- **Pipeline Integration**: Works seamlessly with bcbio-nextgen analysis pipelines.
- **Input/Output**: Monitors bcbio-nextgen runs; outputs progress reports and visualizations.
- **Installation**: `conda install -c bioconda bcbio_monitor`.

## Pitfalls

- **bcbio-nextgen Dependency**: Requires bcbio-nextgen to be installed and configured.
- **Pipeline Configuration**: Requires properly configured bcbio-nextgen project.
- **Network Access**: May require network access for remote monitoring.
- **Version Compatibility**: Ensure compatibility with bcbio-nextgen version.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Start monitoring server
**Args:** `bcbio_monitor start -d /path/to/bcbio/work/dir`
**Explanation:** Starts monitoring server for bcbio-nextgen analysis directory.

### Monitor specific project
**Args:** `bcbio_monitor watch -p project_name`
**Explanation:** Watches progress of a specific bcbio-nextgen project.

### Generate report
**Args:** `bcbio_monitor report -d /path/to/work/dir -o report.html`
**Explanation:** Generates HTML report of pipeline progress.

### Check status
**Args:** `bcbio_monitor status -d /path/to/work/dir`
**Explanation:** Shows current status of all running pipelines.

### List projects
**Args:** `bcbio_monitor list -d /path/to/work/dir`
**Explanation:** Lists all projects in the bcbio work directory.

### Stop monitoring
**Args:** `bcbio_monitor stop`
**Explanation:** Stops the monitoring server.

### Display help
**Args:** `bcbio_monitor --help`
**Explanation:** Shows all available command-line options and usage information.