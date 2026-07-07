---
name: mavis-config
category: utility
description: Configuration validation for running MAVIS structural variant detection via Snakemake.
tags: [mavis-config, structural-variants, configuration]
author: oxo-call-community
source_url: "https://github.com/bcgsc/mavis_config.git"
---

## Concepts

- **Tool Overview**: mavis-config validates configurations for MAVIS pipeline.
- **Core Function**: Validates and prepares configuration files for MAVIS.
- **Snakemake Integration**: Works with Snakemake workflow management.
- **Schema Validation**: Validates config against predefined schema.
- **Input/Output**: Accepts YAML config files, produces validated output.
- **Installation**: `conda install -c bioconda mavis-config`

## Pitfalls

- **Configuration Complexity**: MAVIS config can be complex.
- **Dependency Versions**: Requires specific versions of dependencies.
- **Schema Changes**: Schema may change between versions.
- **Path Configuration**: Requires correct path configuration.
- **Validation Errors**: May produce cryptic validation errors.
- **Documentation**: Requires careful reading of documentation.

## Examples

### Validate config
**Args:** `mavis-config validate config.yaml`
**Explanation:** Validates configuration file against schema.

### Generate template
**Args:** `mavis-config template -o config_template.yaml`
**Explanation:** Generates configuration template.

### Check dependencies
**Args:** `mavis-config check-deps`
**Explanation:** Checks required dependencies.

### Convert config
**Args:** `mavis-config convert old_config.yaml -o new_config.yaml`
**Explanation:** Converts between config formats.

### Show schema
**Args:** `mavis-config schema`
**Explanation:** Displays configuration schema.

### Help documentation
**Args:** `mavis-config --help`
**Explanation:** Displays available commands and options.
