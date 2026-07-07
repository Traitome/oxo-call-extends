---
name: sigprofilerplotting
category: utility
description: SigProfilerPlotting - Visualization tool for mutational signatures
tags: ["sigprofilerplotting", "utility", "visualization", "plotting"]
author: oxo-call-community
source_url: "https://osf.io/2aj6t/wiki/home"
---

## Concepts

- **Tool Overview**: SigProfilerPlotting (v1.4.3) visualizes mutational signatures and analyses.
- **Core Function**: Generates publication-quality plots for signature data.
- **Algorithm**: Uses matplotlib for visualization of mutational patterns.
- **Input/Output**: Accepts signature data and produces plots.
- **Visualization**: Specialized for mutational signature visualization.
- **Applications**: Publication figure generation, data exploration.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Dependency Issues**: Requires matplotlib and numpy.
- **Display Requirements**: Requires display environment for interactive use.
- **Parameter Tuning**: Requires careful adjustment for optimal visualization.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Plot signatures
**Args:** `sigprofilerplotting -i signatures.txt -o plots/`
**Explanation:** `-i` input signature file; `-o` output directory.

### Plot cosine similarity
**Args:** `sigprofilerplotting -i signatures.txt -c -o cosine_plot.pdf`
**Explanation:** `-c` plot cosine similarity matrix.

### Plot exposure
**Args:** `sigprofilerplotting -i exposure.txt -e -o exposure_plot.pdf`
**Explanation:** `-e` plot signature exposures.

### Help command
**Args:** `sigprofilerplotting --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sigprofilerplotting --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sigprofilerplotting -v -i signatures.txt -o plots/`
**Explanation:** `-v` verbose output.

### High resolution
**Args:** `sigprofilerplotting -i signatures.txt -r 300 -o plots/`
**Explanation:** `-r 300` DPI resolution.
