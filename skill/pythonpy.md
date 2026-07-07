---
name: pythonpy
category: programming
description: pythonpy is a command-line tool that allows Python one-liners with easy access to stdin/stdout.
tags: [pythonpy, programming, command-line, one-liner]
author: oxo-call-community
source_url: "https://github.com/Russell91/pythonpy"
---

## Concepts

- **Tool Overview**: pythonpy runs one-liners.
- **Core Function**: Command-line Python.
- **Algorithm**: Uses Python interpreter.
- **Input Format**: Accepts stdin.
- **Output**: Produces stdout.
- **Use Case**: Quick scripting.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex scripts require memory.
- **Syntax Errors**: Must be avoided.
- **Dependency Import**: Must be available.
- **Runtime**: Execution may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pythonpy --help`
**Explanation:** Shows available options and usage instructions.

### Run script
**Args:** `pythonpy -c "print('Hello')"`
**Explanation:** Executes Python one-liner.

### With parameters
**Args:** `pythonpy -p params.yaml -c "print(x)"`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pythonpy -v -c "print('Hello')"`
**Explanation:** Runs with verbose output.

### Read stdin
**Args:** `echo "test" | pythonpy -c "print(input().upper())"`
**Explanation:** Reads from stdin.

### Import module
**Args:** `pythonpy -c "import math; print(math.pi)"`
**Explanation:** Uses Python module.

### Generate report
**Args:** `pythonpy -c "print('done')" --report report.html`
**Explanation:** Generates HTML report.