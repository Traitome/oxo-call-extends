---
name: cascade-config
category: utility
description: Cascading configuration from CLI and config files
tags: [cascade-config, configuration, cli, yaml, json]
author: oxo-call-community
source_url: "https://github.com/RalfG/cascade-config"
---

## Concepts

- **Tool Overview**: cascade-config provides cascading configuration management from CLI and config files.
- **Core Function**: Merges configuration from multiple sources with precedence hierarchy.
- **Configuration Sources**: Environment variables, config files (YAML/JSON), and CLI arguments.
- **Precedence**: CLI args > Environment variables > Config files > Defaults.
- **Application**: Managing configuration for bioinformatics pipelines and tools.
- **Installation**: Install via bioconda: `conda install -c bioconda cascade-config`

## Pitfalls

- **Config Order**: Understand the cascading order for proper configuration merging.
- **File Format**: Supports YAML and JSON config formats.
- **Conflict Resolution**: Later sources override earlier ones in cascade.
- **Validation**: No built-in config validation; validate separately if needed.

## Examples

### Load configuration
**Args:** `cascade-config config.yaml --override key=value`
**Explanation:** Loads configuration from YAML file with CLI override.

### Merge multiple configs
**Args:** `cascade-config base.yaml env.yaml --override debug=true`
**Explanation:** Merges multiple config files with CLI overrides.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.