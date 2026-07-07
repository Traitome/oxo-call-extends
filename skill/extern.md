---
name: extern
category: programming
description: "Extern is an opinionated version of Python's subprocess, making it just that little bit more convenient to run shell commands from within Python code."
tags: [extern, programming, subprocess, shell-commands, Python]
author: oxo-call-community
source_url: "https://pypi.python.org/pypi/extern/"
---

## Concepts

- **Tool Overview**: Extern is a Python library that provides a simplified interface for running shell commands, building on Python's subprocess module.
- **Core Function**: Executes shell commands from Python code with simplified syntax and automatic output capture.
- **Input/Output**: Input: Shell command strings. Output: Command output, return codes, error handling.
- **Algorithm**: Wraps subprocess functionality with convenient utilities for command execution and result handling.
- **Key Features**: Simplified syntax, automatic output capture, error handling, command chaining, shell integration.
- **Installation**: `conda install -c bioconda extern`

## Pitfalls

- **Shell Injection**: Potentially vulnerable to shell injection if not used carefully.
- **Command Security**: Requires careful handling of user input in commands.
- **Error Handling**: Default behavior may hide errors if not configured properly.
- **Platform Dependence**: Commands may behave differently on different operating systems.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic command execution
**Args:** `from extern import run; result = run("ls -l")`
**Explanation:** Runs shell command and captures output.

### With error handling
**Args:** `from extern import run; result = run("invalid_command", check=False)`
**Explanation:** Runs command without raising exception on failure.

### Capture output
**Args:** `from extern import run; output = run("echo 'Hello'").stdout`
**Explanation:** Captures command output.

### Command chaining
**Args:** `from extern import run; result = run("cat file.txt | grep pattern")`
**Explanation:** Runs piped commands.

### Batch execution
**Args:** `from extern import run; results = [run(cmd) for cmd in commands]`
**Explanation:** Executes multiple commands in sequence.