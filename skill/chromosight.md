---
name: chromosight
category: hi-c
description: Detect loops and patterns in Hi-C contact maps
tags: [chromosight, hi-c, chromatin-loops, 3d-genome, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/koszullab/chromosight"
---

## Concepts

- **Tool Overview**: chromosight detects chromatin loops and other patterns in Hi-C contact maps using pattern matching.
- **Core Function**: Identifies interaction patterns (loops, stripes, borders) in Hi-C data using predefined templates.
- **Algorithm**: Uses cross-correlation with pattern templates to detect significant interactions.
- **Input**: Hi-C contact matrix in various formats (cooler, hic, bedpe).
- **Output**: Detected loops and patterns with significance scores.
- **Application**: 3D genome analysis, chromatin interaction detection, and Hi-C data interpretation.
- **Installation**: Install via bioconda: `conda install -c bioconda chromosight`

## Pitfalls

- **Resolution**: Performance depends on Hi-C resolution; higher resolution may be computationally intensive.
- **Noise Level**: Sensitive to noise in Hi-C data; requires quality filtering.
- **Pattern Templates**: Predefined templates may not capture all biological patterns.
- **Memory Usage**: May require significant memory for large contact maps.
- **Significance Threshold**: Requires careful threshold selection to balance sensitivity and specificity.

## Examples

### Detect loops in Hi-C data
**Args:** `chromosight detect -i contacts.cool -o loops.txt`
**Explanation:** Detects chromatin loops from Hi-C contact matrix.

### With custom pattern
**Args:** `chromosight detect -i contacts.cool -p custom_pattern.txt -o results.txt`
**Explanation:** Uses custom pattern template for detection.

### Visualize patterns
**Args:** `chromosight plot -i contacts.cool -o plot.png`
**Explanation:** Visualizes Hi-C contact map with detected loops.

### Display help
**Args:** `chromosight --help`
**Explanation:** Shows all available commands and options.