---
name: pretext-suite
category: alignment
description: pretext-suite is a meta-package for Pretext Hi-C contact map tools.
tags: [pretext-suite, alignment, hi-c, tools]
author: oxo-call-community
source_url: "https://github.com/wtsi-hpag/"
---

## Concepts

- **Tool Overview**: pretext-suite bundles Pretext tools.
- **Core Function**: Tool collection.
- **Algorithm**: Meta-package installation.
- **Input Format**: N/A (package).
- **Output**: N/A (package).
- **Use Case**: Hi-C analysis workflow.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Depends on individual tools.
- **Component Compatibility**: Tools must be compatible.
- **Installation Size**: May require significant space.
- **Runtime**: Depends on individual tools.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pretext-suite --help`
**Explanation:** Shows available options and usage instructions.

### Install package
**Args:** `conda install -c bioconda pretext-suite`
**Explanation:** Installs the Pretext suite of tools.

### Check versions
**Args:** `pretext-suite --version`
**Explanation:** Shows installed versions.

### List tools
**Args:** `pretext-suite --list`
**Explanation:** Lists included tools.

### Quick start
**Args:** `pretext-suite --quickstart`
**Explanation:** Shows quick start guide.

### Documentation
**Args:** `pretext-suite --docs`
**Explanation:** Opens documentation.

### Generate report
**Args:** `pretext-suite --report report.html`
**Explanation:** Generates summary report.