---
name: argh
category: programming
description: Argh - Simple argparse wrapper for Python command-line applications
tags: [argh, utility, python, command-line, argument-parsing]
author: oxo-call-community
source_url: "https://github.com/wbolster/argh"
---

## Concepts

- **Tool Overview**: Argh is a Python library that provides a simple wrapper around argparse for building user-friendly command-line interfaces. Version 0.26.1.
- **Core Function**: Simplifies creating command-line tools by allowing direct function decorated with argument specifications.
- **Decorator-based API**: Uses decorators to define commands and arguments directly on Python functions.
- **Automatic Help Generation**: Automatically generates help messages and usage documentation from function signatures.
- **Nested Commands**: Supports hierarchical command structures with subcommands.
- **Type Annotations**: Integrates with Python type hints for argument type inference.
- **Installation**: `conda install -c bioconda argh` or `pip install argh`.

## Pitfalls

- **Python Version**: Requires Python 3.6+. Some features may need newer Python versions.
- **Argparse Dependency**: Built on top of argparse; understanding argparse helps debugging.
- **Complex Arguments**: Very complex argument structures may be harder to customize.
- **Docstring Conflicts**: Function docstrings may conflict with generated help text.
- **Namespace Limitations**: Single namespace for arguments may cause conflicts in large applications.

## Examples

### Basic command function
**Args:** `argh dispatch_command my_function --input file.txt --output result.txt`
**Explanation:** Dispatches a function decorated with @argh decorators as a command-line tool.

### Define command with arguments
**Args:** `mytool process --input data.csv --format csv --verbose`
**Explanation:** Runs a function decorated with argument definitions for input path, format, and verbose flag.

### Entry point configuration
**Args:** `python -m mymodule --input file.txt`
**Explanation:** Uses argh with Python module entry points for easy tool installation.

### Subcommand support
**Args:** `mytool run analyze --input data.fasta`
**Explanation:** Defines nested commands with subparsers for organizing complex CLI tools.

### Help generation
**Args:** `mytool --help`
**Explanation:** Displays auto-generated help message including all commands and arguments.