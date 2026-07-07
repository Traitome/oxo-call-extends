---
name: moreutils
category: utility
description: Collection of Unix utilities including sponge, ts, vidir, and others.
tags: [moreutils, utility]
author: oxo-call-community
source_url: "https://joeyh.name/code/moreutils/"
---

## Concepts

- **Tool Overview**: moreutils v0.5.7 provides additional Unix utilities for everyday tasks.
- **Core Function**: Collection of useful command-line utilities.
- **sponge**: Reads input before writing to same file.
- **ts**: Adds timestamp to each line of input.
- **vidir**: Edit directory contents in text editor.
- **Input/Output**: Various utilities with different input/output formats.

## Pitfalls

- **Unix Specific**: Designed for Unix-like systems.
- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for each utility.
- **Shell Compatibility**: Some utilities may require specific shells.
- **File Permissions**: May require appropriate permissions.
- **Memory Requirements**: Depends on specific utility usage.

## Examples

### Use sponge to modify file in-place
**Args:** `cat file.txt | grep pattern | sponge file.txt`
**Explanation:** Filters file contents and writes back to same file.

### Add timestamps to log file
**Args:** `command | ts >> logfile.txt`
**Explanation:** Prepends timestamp to each output line.

### Edit directory contents
**Args:** `vidir /path/to/directory`
**Explanation:** Opens directory listing in text editor for modification.

### Combine lines from multiple files
**Args:** `combine file1.txt file2.txt`
**Explanation:** Merges corresponding lines from multiple files.

### Convert newline formats
**Args:** `fromdos < windows.txt > unix.txt`
**Explanation:** Converts Windows line endings to Unix format.