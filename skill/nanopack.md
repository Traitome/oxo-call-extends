---
name: nanopack
category: qc
description: A meta package for several long read processing and analysis tools.
tags: [nanopack, qc, nanopore, meta-package, long-reads]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanopack"
---

## Concepts

- **Tool Overview**: NanoPack v1.1.1 - meta package for Nanopore processing tools.
- **Core Function**: Bundles multiple Nanopore QC and processing tools (NanoPlot, NanoFilt, NanoComp, etc.).
- **Input/Output**: Provides access to various Nanopore analysis tools.
- **Installation**: `conda install -c bioconda nanopack`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Components**: Includes NanoPlot, NanoFilt, NanoComp, NanoStat, NanoGet, NanoLyse, NanoMath.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available tools in the package.

### Access component tools
**Args:** `NanoPlot --help`
**Explanation:** Access NanoPlot tool from the package.
