---
name: snk-cli
category: programming
description: SNK-CLI - Dynamically generate CLIs from Snakemake configuration files
tags: [snk-cli, programming, snakemake, cli, command-line]
author: oxo-call-community
source_url: "https://github.com/wytamma/snk-cli"
---

## Concepts

- **Tool Overview**: snk-cli (v0.7.2) - A tool for generating CLIs from Snakemake configs
- **Core Function**: Creates command-line interfaces from Snakemake workflow configurations
- **Input/Output**: Accepts Snakemake config files; outputs CLI wrapper
- **Algorithm**: Parses config files and generates argument parsing code
- **Installation**: `conda install -c bioconda snk-cli`
- **Key Features**: CLI generation, Snakemake integration, dynamic parsing

## Pitfalls

- **Config Format**: Requires specific Snakemake config format
- **Version Compatibility**: Requires specific Snakemake version
- **Complexity**: Adds additional layer to workflow development
- **Documentation**: Limited documentation available
- **Testing**: Requires thorough testing of generated CLI
- **Dependency Management**: May require additional dependencies

## Examples

### Display help
**Args:** `snk-cli --help`
**Explanation:** Shows available options and usage information.

### Generate CLI
**Args:** `snk-cli generate -c config.yaml -o workflow_cli.py`
**Explanation:** Generate CLI from config file.

### Run generated CLI
**Args:** `python workflow_cli.py --help`
**Explanation:** Show help for generated CLI.

### With custom name
**Args:** `snk-cli generate -c config.yaml -o my_workflow.py --name my_workflow`
**Explanation:** Generate CLI with custom name.

### Build executable
**Args:** `snk-cli build -c config.yaml --executable workflow.exe`
**Explanation:** Build standalone executable.

### Test CLI
**Args:** `snk-cli test -c config.yaml`
**Explanation:** Test CLI generation without writing output.

### With validation
**Args:** `snk-cli generate -c config.yaml -o workflow_cli.py --validate`
**Explanation:** Generate CLI with input validation.

### Add documentation
**Args:** `snk-cli generate -c config.yaml -o workflow_cli.py --docs`
**Explanation:** Generate CLI with documentation.