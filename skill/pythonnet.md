---
name: pythonnet
category: programming
description: Python.NET provides .NET and Mono integration for Python, enabling interop between Python and .NET code.
tags: [pythonnet, programming, dotnet, mono]
author: oxo-call-community
source_url: "https://pythonnet.github.io/"
---

## Concepts

- **Tool Overview**: pythonnet integrates .NET.
- **Core Function**: Language interop.
- **Algorithm**: Uses CLR hosting.
- **Input Format**: Accepts .NET assemblies.
- **Output**: Produces .NET objects.
- **Use Case**: Cross-language.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Version Compatibility**: Must match.
- **Garbage Collection**: Must be handled.
- **Runtime**: Loading may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pythonnet --help`
**Explanation:** Shows available options and usage instructions.

### Load assembly
**Args:** `pythonnet load -i library.dll -o output.py`
**Explanation:** Loads .NET assembly.

### With parameters
**Args:** `pythonnet load -i library.dll -p params.yaml -o output.py`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pythonnet -v load -i library.dll -o output.py`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pythonnet -t 4 load -i library.dll -o output.py`
**Explanation:** Uses 4 threads for parallel processing.

### Execute method
**Args:** `pythonnet exec -i library.dll -m MethodName -o result.txt`
**Explanation:** Executes .NET method.

### Generate report
**Args:** `pythonnet load -i library.dll -o output.py --report report.html`
**Explanation:** Generates HTML report.