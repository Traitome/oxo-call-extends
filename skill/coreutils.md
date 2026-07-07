---
name: coreutils
category: utility
description: GNU Core Utilities - basic file, shell and text manipulation tools
tags: [coreutils, gnu, file-manipulation, text-processing, shell-tools]
author: oxo-call-community
source_url: "http://www.gnu.org/software/coreutils/"
---

## Concepts

- **Tool Overview**: GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system, providing essential commands for everyday use.
- **Core Function**: Provides fundamental Unix/Linux commands for file management, text processing, and shell operations.
- **Key Tools**: Includes cat, cp, mv, rm, ls, mkdir, rmdir, chmod, chown, sort, grep, sed, awk, head, tail, wc, cut, paste, etc.
- **Input/Output**: Text files, directories, standard input/output streams.
- **Application**: Scripting, file management, text processing, data manipulation, system administration.
- **Installation**: Install via bioconda: `conda install -c bioconda coreutils`

## Pitfalls

- **Version Differences**: Options may vary between GNU and BSD versions.
- **File Permissions**: Some commands require root privileges.
- **Recursive Operations**: Use caution with `-r` flag to avoid accidental deletion.
- **Locale Settings**: Sorting behavior may vary by locale.
- **Encoding Issues**: Text processing commands may have issues with non-ASCII characters.

## Examples

### Count lines, words, and characters
**Args:** `wc -l input.txt`
**Explanation:** Counts lines in a file.

### Sort file contents
**Args:** `sort input.txt -o sorted.txt`
**Explanation:** Sorts lines alphabetically and saves to output.

### Concatenate files
**Args:** `cat file1.txt file2.txt > combined.txt`
**Explanation:** Combines multiple files into one.

### Extract columns
**Args:** `cut -f 1,3 -d ',' data.csv`
**Explanation:** Extracts columns 1 and 3 from CSV file.

### Find unique lines
**Args:** `sort input.txt | uniq`
**Explanation:** Displays unique lines from sorted input.

### Display file head
**Args:** `head -n 10 input.txt`
**Explanation:** Shows first 10 lines of a file.