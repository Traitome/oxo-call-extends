---
name: argutils
category: utility
description: Argutils - Functions to build matched argument parsers and config files
tags: [argutils, utility, python, argparse, config-files]
author: oxo-call-community
source_url: "https://github.com/eclarke/argutils"
---

## Concepts

- **Tool Overview**: Argutils provides functions to build matched argument parsers and configuration files for Python command-line tools. Version 0.3.2.
- **Core Function**: Synchronizes command-line arguments with configuration files, ensuring consistent parameter specification.
- **Parser-Config Sync**: Automatically generates config file templates from argument parser definitions.
- **Bidirectional Mapping**: Supports loading config files into argument parsers and saving parser arguments to config files.
- **Validation**: Ensures config file parameters match argument parser specifications.
- **Format Support**: Supports multiple config file formats (YAML, JSON, TOML, INI).
- **Installation**: `conda install -c bioconda argutils` or `pip install argutils`.

## Pitfalls

- **Python Dependency**: Python library requiring integration with argparse or other parsers.
- **Format Limitations**: Some config formats may not support all Python data types.
- **Type Conversion**: Automatic type conversion may fail for complex nested structures.
- **Default Values**: Config file defaults may override parser defaults unexpectedly.
- **Documentation**: Limited documentation for advanced use cases.

## Examples

### Generate config from parser
**Args:** `python script.py --generate-config config.yaml`
**Explanation:** Generates config file template from argument parser definition.

### Load config into parser
**Args:** `python script.py --config config.yaml`
**Explanation:** Loads arguments from config file into argument parser.

### Save parser args to config
**Args:** `python script.py --save-config output_config.yaml`
**Explanation:** Saves current parser arguments to config file.

### Validate config file
**Args:** `argutils validate --config config.yaml --schema schema.json`
**Explanation:** Validates config file against parser schema.

### Convert config formats
**Args:** `argutils convert --input config.yaml --output config.json --format json`
**Explanation:** Converts config file between different formats.

### Merge multiple configs
**Args:** `argutils merge --configs config1.yaml config2.yaml --output merged.yaml`
**Explanation:** Merges multiple config files into single configuration.