---
name: grep
category: bioinformatics
description: grep searches input files for lines containing matches to specified patterns, essential for text processing in bioinformatics workflows.
tags: [grep, text-processing, bioinformatics]
author: oxo-call-community
source_url: "https://www.gnu.org/software/grep/"
---

## Concepts

- **Pattern Matching**: grep searches text files for lines matching specified patterns using regular expressions.

- **Regular Expressions**: Supports powerful regular expression patterns for flexible searching.

- **Multiple File Search**: Can search multiple files simultaneously.

- **Output Control**: Provides various output options including line numbers, context, and highlighting.

- **Case Insensitivity**: Supports case-insensitive matching for flexible searching.

- **Recursive Search**: Can search recursively through directories.

## Pitfalls

- **Pattern Complexity**: Complex regular expressions can be difficult to debug. Test patterns carefully.

- **Performance**: Searching very large files can be slow. Use appropriate options for performance.

- **Encoding Issues**: Be aware of file encoding. Some encodings may cause unexpected behavior.

- **Line Endings**: Different line ending formats (Windows vs Unix) can affect matching.

- **Special Characters**: Special characters in patterns need to be escaped properly.

## Examples

### Basic pattern search
**Args:** `grep "pattern" input.txt`
**Explanation:** Searches for "pattern" in input.txt and prints matching lines.

### Case-insensitive search
**Args:** `grep -i "pattern" input.txt`
**Explanation:** Searches for "pattern" case-insensitively.

### Show line numbers
**Args:** `grep -n "pattern" input.txt`
**Explanation:** Shows line numbers for matching lines.

### Recursive search
**Args:** `grep -r "pattern" directory/`
**Explanation:** Searches recursively through all files in a directory.

### Show context
**Args:** `grep -A 2 -B 2 "pattern" input.txt`
**Explanation:** Shows 2 lines before and after matching lines.

### Count matches
**Args:** `grep -c "pattern" input.txt`
**Explanation:** Counts the number of lines matching the pattern.

### Invert match
**Args:** `grep -v "pattern" input.txt`
**Explanation:** Shows lines that do NOT match the pattern.