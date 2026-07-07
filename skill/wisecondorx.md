---
name: wisecondorx
category: bioinformatics
description: WisecondorX - CNV detection tool.
tags: [wisecondorx, cnv-detection, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/CenterForMedicalGeneticsGhent/wisecondorX"
---

## Concepts

- **Tool Overview**: WisecondorX - Copy number variation detection.
- **Core Function**: Detects CNVs from sequencing data.
- **Input**: BAM file.
- **Output**: CNV calls.
- **Installation**: Install via pip
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large BAM files.
- **Complexity**: May have steep learning curve.

## Examples

### Detect CNVs
**Args:** `wisecondorx detect -i input.bam -o cnv.txt`
**Explanation:** Detect CNVs.

### With options
**Args:** `wisecondorx detect -i input.bam -o cnv.txt -t 8`
**Explanation:** Use 8 threads.
