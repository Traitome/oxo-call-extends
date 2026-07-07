---
name: ucsc-hubcheck
category: utility
description: UCSC hubCheck - Tool for checking track hubs.
tags: [ucsc-hubcheck, ucsc, hub, track, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hubCheck - A tool for validating track hubs.
- **Core Function**: Validates track hub configuration and data.
- **Input**: Hub URL or directory.
- **Output**: Validation report.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser, track hub validation, quality control.

## Pitfalls

- **URL Access**: Requires network access for remote hubs.
- **Format Requirements**: Requires proper hub format.

## Examples

### Check track hub
**Args:** `hubCheck hub.txt`
**Explanation:** Validate track hub configuration.

### With options
**Args:** `hubCheck -verbose hub.txt`
**Explanation:** Validate with verbose output.
