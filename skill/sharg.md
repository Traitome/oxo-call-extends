---
name: sharg
category: formatting
description: sharg - Modern C++ argument parser
tags: ["sharg", "formatting", "argument-parser", "C++"]
author: oxo-call-community
source_url: "https://docs.seqan.de/sharg/1.2.2/index.html"
---

## Concepts

- **Tool Overview**: sharg (v1.2.2) is a modern argument parser for C++ tools.
- **Core Function**: Parses command-line arguments for C++ applications.
- **Algorithm**: Uses type-safe argument parsing with validation.
- **Input/Output**: Accepts command-line arguments and produces parsed values.
- **Argument Parsing**: Focuses on robust command-line interface development.
- **Applications**: C++ software development, bioinformatics tools, and CLI applications.

## Pitfalls

- **Compile-time Errors**: May require careful template usage.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.
- **Complexity**: May be complex for simple use cases.
- **Dependency**: Requires SeqAn library.
- **Learning Curve**: May require time to learn API.

## Examples

### Basic usage
**Args:** `#include <sharg/all.hpp>; int main(int argc, char ** argv) { sharg::parser parser{"program", argc, argv}; }`
**Explanation:** Basic parser setup.

### Add option
**Args:** `parser.add_option(input_file, "input", 'i', "Input file");`
**Explanation:** Adds input file option.

### Add flag
**Args:** `parser.add_flag(verbose, "verbose", 'v', "Enable verbose output");`
**Explanation:** Adds boolean flag.

### Parse arguments
**Args:** `parser.parse();`
**Explanation:** Parses command-line arguments.

### Validation
**Args:** `parser.add_option(input_file, "input", 'i', "Input file").check(sharg::input_file_validator{});`
**Explanation:** Adds input file with validation.

### Version information
**Args:** `parser.info.version = "1.0.0";`
**Explanation:** Sets version information.

### Help text
**Args:** `parser.info.description = "My program description";`
**Explanation:** Sets program description.