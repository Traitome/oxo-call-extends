---
name: xengsort
category: bioinformatics
description: XengSort - Read classification tool.
tags: [xengsort, read-classification, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/XengSort"
---

## Concepts

- **Tool Overview**: XengSort - Fast read classification tool.
- **Core Function**: Classifies sequencing reads.
- **Input**: FASTQ reads.
- **Output**: Classification results.
- **Installation**: Install via conda or source
- **Use Case**: Read classification, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Classify reads
**Args:** `xengsort classify -i reads.fastq -o classified.txt`
**Explanation:** Classify reads.

### With options
**Args:** `xengsort classify -i reads.fastq -o classified.txt -t 8`
**Explanation:** Use 8 threads.
