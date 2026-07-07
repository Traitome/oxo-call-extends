---
name: pafpy
category: alignment
description: pafpy is a lightweight Python library for working with PAF format files.
tags: [pafpy, alignment, paf, python]
author: oxo-call-community
source_url: "https://github.com/mbhall88/pafpy"
---

## Concepts

- **Tool Overview**: pafpy provides Python bindings for PAF format parsing.
- **Core Function**: Reads and manipulates PAF alignment files.
- **Algorithm**: Uses efficient parsing and object-oriented design.
- **Input Format**: Accepts PAF format alignment files.
- **Output**: Produces alignment objects and data structures.
- **Use Case**: Alignment analysis, bioinformatics pipelines, and Python scripting.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Format Support**: Limited to PAF format.
- **Performance**: May be slow for very large files.
- **API Changes**: API may change between versions.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "import pafpy; help(pafpy)"`
**Explanation:** Shows available options and usage instructions.

### Read PAF file
**Args:** `python -c "from pafpy import PafFile; paf = PafFile('alignments.paf')"`
**Explanation:** Reads PAF file.

### Iterate records
**Args:** `python -c "for record in paf: print(record)"`
**Explanation:** Iterates through alignment records.

### Filter records
**Args:** `python -c "filtered = [r for r in paf if r.mapq >= 30]"`
**Explanation:** Filters by mapping quality.

### Write records
**Args:** `python -c "paf.write('filtered.paf', filtered)"`
**Explanation:** Writes records to file.

### Verbose mode
**Args:** `python -c "paf = PafFile('alignments.paf', verbose=True)"`
**Explanation:** Runs with verbose output.

### Statistics
**Args:** `python -c "stats = paf.statistics(); print(stats)"`
**Explanation:** Computes alignment statistics.