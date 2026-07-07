---
name: textinput
category: utility
description: Python library for efficient text input processing, extending fileinput functionality
tags: [textinput, utility, python, fileinput]
author: oxo-call-community
source_url: "http://www.ebi.ac.uk/~hoffman/software/textinput/"
---

## Concepts

- **Tool Overview**: textinput is a Python library extending the standard fileinput module for text processing
- **Core Function**: Provides efficient iteration over lines from multiple input streams (files, stdin)
- **Python Module**: Imported as `import textinput` and used within Python scripts
- **Input/Output**: Handles multiple input files, supports stdin, outputs to stdout or files
- **In-place Editing**: Supports modifying files in-place like `sed -i`
- **Installation**: `pip install textinput` or included in some bioinformatics toolchains

## Pitfalls

- **Python Version**: Requires Python 3.x; not compatible with Python 2
- **In-place Editing Risk**: Using in-place mode without proper backup can cause data loss
- **Newline Handling**: Lines include trailing newlines; use `.strip()` for clean comparisons
- **Stdin Limitations**: stdin can only be read once without explicit reset

## Examples

### Iterate over multiple files
**Args:** `import textinput; for line in textinput.input(files=['a.txt', 'b.txt']): print(line, end='')`
**Explanation:** Import textinput and iterate over lines from multiple files using input() function.

### Read from stdin
**Args:** `import textinput; for line in textinput.input(): print(line.strip())`
**Explanation:** Read lines from stdin when no files are specified, strip whitespace from each line.

### In-place file editing
**Args:** `import textinput; with textinput.input('data.txt', inplace=True) as f: [print(line.replace('old', 'new'), end='') for line in f]`
**Explanation:** Modify file in-place by replacing text, with print() writing back to file.

### Track file and line information
**Args:** `import textinput; with textinput.input(files=['log1.txt', 'log2.txt']) as f: [print(f"{textinput.filename()}:{textinput.filelineno()}: {line}", end='') for line in f]`
**Explanation:** Track current filename and line number while processing multiple files.

### Handle compressed files
**Args:** `import textinput; with textinput.input(files=['data.gz'], openhook=textinput.hook_compressed) as f: [print(line, end='') for line in f]`
**Explanation:** Transparently read gzip/bzip2 compressed files using hook_compressed.