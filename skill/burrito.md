---
name: burrito
category: programming
description: Framework for wrapping and controlling command-line applications in Python
tags: [burrito, python, framework, command-line, wrapper]
author: oxo-call-community
source_url: "https://github.com/biocore/burrito"
---

## Concepts

- **Tool Overview**: burrito is a Python framework for wrapping and controlling command-line applications.
- **Core Function**: Provides a consistent interface for executing external tools within Python scripts.
- **Features**: Process management, input/output handling, error capturing, and tool wrapping.
- **Application**: Building bioinformatics pipelines and workflows in Python.
- **Installation**: Install via bioconda: `conda install -c bioconda burrito`

## Pitfalls

- **Python Library**: This is a Python library, not a command-line tool.
- **Command Path**: Ensure wrapped tools are in system PATH or specify full path.
- **Error Handling**: Properly handle tool exit codes and stderr output.
- **Dependency Management**: Ensure wrapped tools are installed separately.

## Examples

### Basic wrapper usage
**Args:** `from burrito.util import CommandLineApp; app = CommandLineApp('tool_command')`
**Explanation:** Creates a wrapper for a command-line tool.

### Run command with arguments
**Args:** `result = app('-i', 'input.txt', '-o', 'output.txt')`
**Explanation:** Executes the wrapped command with specified arguments.