---
name: mzml2isa
category: formatting
description: mzml2isa - mzML to ISA-tab parsing tool
tags: [mzml2isa, formatting, mzml, isa-tab, metabolomics]
author: oxo-call-community
source_url: "https://github.com/ISA-tools/mzml2isa"
---

## Concepts

- **Tool Overview**: mzml2isa v1.1.1 - converts mzML files to ISA-tab format.
- **Core Function**: Parses mzML mass spectrometry files and generates ISA-tab metadata files.
- **Input/Output**: Takes mzML files; outputs ISA-tab formatted metadata.
- **Installation**: `conda install -c bioconda mzml2isa`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires valid mzML files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i mzml_dir -o isa_output_dir`
**Explanation:** Converts mzML files to ISA-tab format.
