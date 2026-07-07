---
name: stripepy-hic
category: visualization
description: StripePy recognizes architectural stripes in 3C and Hi-C contact maps using geometric reasoning.
tags: [stripepy-hic, hic-analysis, chromatin-structure, visualization]
author: oxo-call-community
source_url: "https://stripepy.readthedocs.io/"
---

## Concepts

- **Tool Overview**: stripepy-hic (v1.3.0) is a tool for identifying architectural stripes in Hi-C contact maps using geometric reasoning.
- **Core Function**: Detects and analyzes stripe patterns in 3D genome organization from Hi-C data.
- **Algorithm**: Uses geometric reasoning and pattern recognition to identify stripe patterns.
- **Input/Output**: Input: Hi-C contact matrix; Output: Stripe annotations and visualizations.
- **Applications**: 3D genome analysis, chromatin architecture studies, genome organization.
- **Installation**: `conda install -c bioconda stripepy-hic` or download from GitHub.

## Pitfalls

- **Matrix Quality**: Poor quality Hi-C matrices affect stripe detection.
- **Resolution**: Stripe detection depends on matrix resolution.
- **Noise**: Noise in Hi-C data affects pattern recognition.
- **Memory Requirements**: Large matrices require significant memory.
- **Computational Time**: Processing large matrices can be slow.
- **Parameter Tuning**: Incorrect parameters affect stripe detection.

## Examples

### Display help
**Args:** `stripepy-hic --help`
**Explanation:** Shows available options and usage information.

### Basic stripe detection
**Args:** `stripepy-hic -i hic_matrix.txt -o stripes.txt`
**Explanation:** Detect stripes in Hi-C contact matrix.

### With visualization
**Args:** `stripepy-hic -i hic_matrix.txt -o stripes.txt --plot`
**Explanation:** Detect stripes and generate visualization.

### Verbose mode
**Args:** `stripepy-hic -i hic_matrix.txt -o stripes.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Custom parameters
**Args:** `stripepy-hic -i hic_matrix.txt -o stripes.txt -t 0.5`
**Explanation:** Use custom threshold for stripe detection.

### Batch processing
**Args:** `stripepy-hic -i matrices/ -o results/`
**Explanation:** Process multiple Hi-C matrices together.

### Filter by size
**Args:** `stripepy-hic -i hic_matrix.txt -o stripes.txt -m 10000`
**Explanation:** Minimum stripe size of 10000 bp.

### Include statistics
**Args:** `stripepy-hic -i hic_matrix.txt -o stripes.txt --stats`
**Explanation:** Generate statistics about detected stripes.

### Generate report
**Args:** `stripepy-hic -i hic_matrix.txt -o stripes.txt --report`
**Explanation:** Generate comprehensive HTML report.
