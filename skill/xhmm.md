---
name: xhmm
category: bioinformatics
description: XHMM - Copy number variation detection.
tags: [xhmm, cnv-detection, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://atgu.mgh.harvard.edu/xhmm/"
---

## Concepts

- **Tool Overview**: XHMM - Hidden Markov Model for CNV detection.
- **Core Function**: Detects copy number variations.
- **Input**: Read depth data.
- **Output**: CNV calls.
- **Installation**: Download from official site
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Complexity**: May have steep learning curve.

## Examples

### Detect CNVs
**Args:** `xhmm --matrix input.txt --cnv output.txt`
**Explanation:** Detect copy number variations.

### With options
**Args:** `xhmm --matrix input.txt --cnv output.txt -p params.txt`
**Explanation:** Use parameters file.
