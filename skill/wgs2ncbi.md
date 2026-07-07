---
name: wgs2ncbi
category: bioinformatics
description: WGS2NCBI - Whole-genome sequencing submission tool.
tags: [wgs2ncbi, data-submission, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/wgs2ncbi/"
---

## Concepts

- **Tool Overview**: WGS2NCBI - NCBI submission helper.
- **Core Function**: Prepares WGS data for NCBI submission.
- **Input**: Sequence data.
- **Output**: Submission-ready files.
- **Installation**: Install via pip or conda
- **Use Case**: Data submission, bioinformatics.

## Pitfalls

- **Network**: Requires network connectivity.
- **Complexity**: May have steep learning curve.

## Examples

### Prepare submission
**Args:** `wgs2ncbi -i genome.fasta -o submission/`
**Explanation:** Prepare NCBI submission.

### With options
**Args:** `wgs2ncbi -i genome.fasta -o submission/ -p project`
**Explanation:** Specify project.
