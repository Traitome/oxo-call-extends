---
name: ucsc-subcolumn
category: utility
description: UCSC subColumn - Tool for column substitution.
tags: [ucsc-subcolumn, ucsc, substitution, column, text-processing]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC subColumn - A tool for column substitution in files.
- **Core Function**: Substitutes values in specific columns.
- **Input**: Input file, column index, substitution mapping.
- **Output**: Modified file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Text processing, data manipulation, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Column Index**: Requires correct column specification.

## Examples

### Substitute column values
**Args:** `subColumn -col=2 -from=old -to=new input.txt > output.txt`
**Explanation:** Replace values in column 2.

### With options
**Args:** `subColumn -col=2 -verbose -from=old -to=new input.txt > output.txt`
**Explanation:** Replace with verbose output.
