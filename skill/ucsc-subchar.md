---
name: ucsc-subchar
category: utility
description: UCSC subChar - Tool for character substitution.
tags: [ucsc-subchar, ucsc, substitution, character, text-processing]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC subChar - A tool for character substitution in files.
- **Core Function**: Substitutes characters in text files.
- **Input**: Input file, source and target characters.
- **Output**: Modified file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Text processing, character replacement, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Encoding**: Requires proper encoding handling.

## Examples

### Substitute characters
**Args:** `subChar -from=A -to=T input.txt > output.txt`
**Explanation:** Replace A with T.

### With options
**Args:** `subChar -from=AT -to=TA input.txt > output.txt`
**Explanation:** Replace multiple characters.
