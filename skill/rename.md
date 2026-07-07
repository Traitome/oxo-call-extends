---
name: rename
category: utility
description: Rename is a Perl-powered file rename script with many helpful built-in functions.
tags: [rename, utility, file-rename, perl]
author: oxo-call-community
source_url: "http://plasmasturm.org/code/rename"
---

## Concepts

- **Tool Overview**: rename renames files.
- **Core Function**: Batch file renaming.
- **Algorithm**: Uses Perl regex methods.
- **Input Format**: Accepts file patterns.
- **Output**: Produces renamed files.
- **Use Case**: File management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Pattern Complexity**: Affects renaming.
- **File Permissions**: May affect operation.
- **Parameters**: Must be configured.
- **Runtime**: Renaming may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rename --help`
**Explanation:** Shows available options and usage instructions.

### Simple rename
**Args:** `rename 's/old/new/' *.txt`
**Explanation:** Renames files using regex substitution.

### With numbering
**Args:** `rename 's/(\d+)/sprintf("%03d",$1)/e' file*.txt`
**Explanation:** Adds zero-padding to numbered files.

### Lowercase conversion
**Args:** `rename 'y/A-Z/a-z/' *.TXT`
**Explanation:** Converts filenames to lowercase.

### Dry run
**Args:** `rename -n 's/old/new/' *.txt`
**Explanation:** Shows what would be renamed.

### Force overwrite
**Args:** `rename -f 's/old/new/' *.txt`
**Explanation:** Forces overwrite of existing files.

### Verbose mode
**Args:** `rename -v 's/old/new/' *.txt`
**Explanation:** Shows each rename operation.