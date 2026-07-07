---
name: tadtool
category: epigenomics
description: Interactive tool for identifying meaningful parameters in TAD-calling algorithms for Hi-C data.
tags: [tadtool, hic, tads, epigenomics]
author: oxo-call-community
source_url: "https://github.com/vaquerizaslab/tadtool"
---

## Concepts

- **Tool Overview**: tadtool (v0.84) is an interactive TAD-calling parameter explorer.
- **Core Function**: Helps identify optimal parameters for TAD detection algorithms.
- **Algorithm**: Evaluates TAD-calling parameters across parameter space.
- **Input/Output**: Input: Hi-C contact maps; Output: Parameter evaluation.
- **Applications**: Hi-C data analysis, TAD detection optimization.
- **Installation**: `conda install -c bioconda tadtool` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large Hi-C datasets require significant memory.
- **Computational Time**: Parameter scanning can be computationally intensive.
- **Parameter Range**: Requires appropriate parameter bounds.
- **Data Quality**: Requires high-quality Hi-C data.
- **Resolution**: Depends on sequencing depth.
- **Visualization**: Requires graphical environment for interactive mode.

## Examples

### Display help
**Args:** `tadtool --help`
**Explanation:** Shows available options and usage information.

### Basic parameter exploration
**Args:** `tadtool -i hic.matrix -o parameters.txt`
**Explanation:** Explore TAD-calling parameters.

### With resolution
**Args:** `tadtool -i hic.matrix -o parameters.txt -r 10000`
**Explanation:** Use specific resolution for exploration.

### Verbose mode
**Args:** `tadtool -i hic.matrix -o parameters.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tadtool -i hic.matrix -o parameters.txt --stats`
**Explanation:** Generate statistics about parameter exploration.

### Batch processing
**Args:** `for f in matrices/*.matrix; do tadtool -i $f -o results/${f%.matrix}.txt; done`
**Explanation:** Process multiple Hi-C matrices.

### Interactive mode
**Args:** `tadtool -i hic.matrix`
**Explanation:** Launch interactive parameter exploration.

### Compare algorithms
**Args:** `tadtool -i hic.matrix -o parameters.txt -a arrowhead insulation`
**Explanation:** Compare multiple TAD-calling algorithms.

### Generate report
**Args:** `tadtool -i hic.matrix -o parameters.txt --report`
**Explanation:** Generate comprehensive parameter report.
