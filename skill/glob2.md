---
name: glob2
category: file-management
description: glob2 - Python glob module with pattern capture and recursive wildcards.
tags: [glob2, file-management, glob, pattern-matching]
author: oxo-call-community
source_url: "http://github.com/miracle2k/python-glob2/"
---

## Concepts
- **Pattern Matching**: Matches file patterns.
- **Recursive Wildcards**: Supports recursive directory traversal.
- **Pattern Capture**: Captures matched patterns.
- **File Discovery**: Discovers files matching criteria.
- **Python Integration**: Integrates with Python.

## Pitfalls
- **Pattern Complexity**: Complex patterns may be slow.
- **Directory Permissions**: Requires read permissions.
- **Symbolic Links**: May follow symbolic links.
- **Performance**: Large directories may be slow.
- **Path Handling**: Path separator differences.

## Examples
### Find files
**Args:** `python -c "import glob2; files = glob2.glob('**/*.txt')"`
**Explanation:** Finds all txt files recursively.

### With pattern
**Args:** `python -c "import glob2; files = glob2.glob('data/**/[0-9]*.csv')"`
**Explanation:** Uses pattern with wildcards.

### Capture groups
**Args:** `python -c "import glob2; files = glob2.glob('data/*/results.txt')"`
**Explanation:** Captures path components.

### List directories
**Args:** `python -c "import glob2; dirs = glob2.glob('**/')"`
**Explanation:** Lists all directories.

### Batch processing
**Args:** `python -c "import glob2, shutil; files = glob2.glob('**/*.fasta'); [shutil.copy(f, 'output/') for f in files]"`
**Explanation:** Processes matched files.