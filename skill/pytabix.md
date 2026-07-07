---
name: pytabix
category: utility
description: PyTabix provides fast random access to sorted files compressed with bgzip and indexed by tabix.
tags: [pytabix, utility, tabix, bgzip]
author: oxo-call-community
source_url: "https://github.com/slowkow/pytabix"
---

## Concepts

- **Tool Overview**: pytabix indexes files.
- **Core Function**: Tabix indexing.
- **Algorithm**: Uses bgzip/tabix.
- **Input Format**: Accepts sorted files.
- **Output**: Produces indexed files.
- **Use Case**: Fast access.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **File Sorting**: Must be sorted.
- **Index Files**: Must exist.
- **Runtime**: Indexing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pytabix --help`
**Explanation:** Shows available options and usage instructions.

### Index file
**Args:** `pytabix index -i data.txt -o data.txt.gz`
**Explanation:** Creates tabix index.

### With parameters
**Args:** `pytabix index -i data.txt -p params.yaml -o data.txt.gz`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pytabix -v index -i data.txt -o data.txt.gz`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pytabix -t 4 index -i data.txt -o data.txt.gz`
**Explanation:** Uses 4 threads for parallel processing.

### Query index
**Args:** `pytabix query -i data.txt.gz -r chr1:1-1000 -o result.txt`
**Explanation:** Queries indexed file.

### Generate report
**Args:** `pytabix index -i data.txt -o data.txt.gz --report report.html`
**Explanation:** Generates HTML report.