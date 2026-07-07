---
name: burrito-fillings
category: programming
description: Application controllers for burrito bioinformatics framework
tags: [burrito-fillings, burrito, python, bioinformatics, framework]
author: oxo-call-community
source_url: "https://github.com/biocore/burrito-fillings"
---

## Concepts

- **Tool Overview**: burrito-fillings provides application controllers for the burrito bioinformatics framework.
- **Core Function**: Manages external tool execution and input/output handling in bioinformatics pipelines.
- **Features**: Wraps command-line tools with consistent interface, handles file conversions.
- **Application**: Building reproducible bioinformatics workflows and pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda burrito-fillings`

## Pitfalls

- **Python Library**: This is a Python library, not a command-line tool.
- **Burrito Dependency**: Requires burrito framework for full functionality.
- **Tool Wrapping**: Requires knowledge of wrapped tools' command-line interfaces.
- **Error Handling**: Proper error handling required for pipeline robustness.

## Examples

### Use application controller
**Args:** `from burrito_fillings.application import Application; app = Application('tool_name')`
**Explanation:** Creates an application controller for a bioinformatics tool.

### Run tool with arguments
**Args:** `result = app(['--input', 'data.fastq', '--output', 'result.txt'])`
**Explanation:** Executes wrapped tool with specified arguments.