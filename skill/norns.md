---
name: norns
category: programming
description: norns is a simple YAML-based configuration module for Python.
tags: [norns, programming, yaml, configuration]
author: oxo-call-community
source_url: "https://github.com/simonvh/norns"
---

## Concepts

- **Tool Overview**: norns provides YAML-based configuration management for Python projects.
- **Core Function**: Loads and manages configuration settings from YAML files.
- **Algorithm**: Parses YAML configuration files into Python objects.
- **Input Format**: Accepts YAML configuration files.
- **Output**: Produces configuration objects.
- **Use Case**: Application configuration, settings management, and parameter handling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **YAML Syntax**: Requires valid YAML syntax.
- **File Path**: Configuration file path must be correct.
- **Type Conversion**: Automatic type conversion may fail.
- **Dependency**: Requires PyYAML library.
- **Documentation**: Limited documentation.

## Examples

### Install package
**Args:** `pip install norns`
**Explanation:** Installs norns package.

### Import module
**Args:** `from norns import Config`
**Explanation:** Imports Config class from norns.

### Load configuration
**Args:** `config = Config('config.yaml')`
**Explanation:** Loads configuration from YAML file.

### Get value
**Args:** `value = config.get('section.key')`
**Explanation:** Retrieves configuration value.

### Default value
**Args:** `value = config.get('section.key', default='default')`
**Explanation:** Retrieves value with default fallback.

### Update configuration
**Args:** `config.set('section.key', 'new_value')`
**Explanation:** Updates configuration value.

### Save configuration
**Args:** `config.save('config.yaml')`
**Explanation:** Saves configuration to file.