---
name: argparse
category: programming
description: Python standard library for command-line argument parsing
tags: [argparse, programming, python, command-line]
author: oxo-call-community
source_url: "https://github.com/ThomasWaldmann/argparse/"
---

## Concepts

- **Tool Overview**: Argparse is Python's standard library module for parsing command-line arguments and creating user-friendly CLI tools. Version included with Python 3.2+.
- **Core Function**: Parses command-line arguments into Python objects for use in scripts and applications.
- **Automatic Help**: Generates help messages and usage information from argument definitions.
- **Type Validation**: Validates argument types and values, converting strings to appropriate Python types.
- **Subcommands**: Supports nested command structures with subparsers for complex CLI applications.
- **Defaults**: Allows specification of default values for optional arguments.
- **Installation**: Part of Python standard library. No separate installation needed for Python 3.2+.

## Pitfalls

- **Python Version**: Included in Python 3.2+. Use optparse for Python 2.7.
- **Error Handling**: Default error messages may be cryptic. Custom error handling improves user experience.
- **Argument Conflicts**: Mutually exclusive arguments require special group definitions.
- **Boolean Flags**: Boolean arguments require special handling (store_true/store_false).
- **Nargs Variations**: Variable argument counts (-n 3 vs -n N) can be confusing.

## Examples

### Basic argument parsing
**Args:** `python script.py --input file.txt --output result.txt`
**Explanation:** Parses input and output file paths from command line.

### Positional arguments
**Args:** `python script.py input_file output_file`
**Explanation:** Uses positional arguments for required inputs without flags.

### Optional flags
**Args:** `python script.py --verbose --count 5 input.txt`
**Explanation:** Uses optional flags for verbose mode and count parameter.

### Argument choices
**Args:** `python script.py --mode align input.fasta`
**Explanation:** Restricts argument to predefined choices (e.g., align, assemble, analyze).

### Subcommands
**Args:** `python tool.py align --input reads.fq --ref genome.fa`
**Explanation:** Uses subparsers to organize commands into logical groups.

### Help display
**Args:** `python script.py --help`
**Explanation:** Displays auto-generated help message with all arguments and usage.