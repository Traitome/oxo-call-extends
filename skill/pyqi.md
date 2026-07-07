---
name: pyqi
category: utility
description: pyqi is a Python framework for building command-line interfaces for bioinformatics tools.
tags: [pyqi, utility, cli, interface]
author: oxo-call-community
source_url: "http://bipy.github.io/pyqi"
---

## Concepts

- **Tool Overview**: pyqi builds CLI interfaces.
- **Core Function**: Interface generation.
- **Algorithm**: Uses argparse.
- **Input Format**: Accepts command arguments.
- **Output**: Produces CLI tools.
- **Use Case**: Tool development.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex interfaces require memory.
- **Argument Parsing**: Must be correct.
- **Help Text**: Should be clear.
- **Runtime**: Execution may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyqi --help`
**Explanation:** Shows available options and usage instructions.

### Run command
**Args:** `pyqi run -i input.txt -o output.txt`
**Explanation:** Executes tool with input/output.

### With parameters
**Args:** `pyqi run -i input.txt -p params.yaml -o output.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyqi -v run -i input.txt -o output.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyqi -t 4 run -i input.txt -o output.txt`
**Explanation:** Uses 4 threads for parallel processing.

### List commands
**Args:** `pyqi list`
**Explanation:** Shows available commands.

### Generate report
**Args:** `pyqi run -i input.txt -o output.txt --report report.html`
**Explanation:** Generates HTML report.