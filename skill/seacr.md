---
name: seacr
category: peak-calling
description: SEACR - Peak calling for CUT&RUN and chromatin profiling data
tags: ["seacr", "peak-calling", "CUT&RUN", "chromatin"]
author: oxo-call-community
source_url: "https://github.com/FredHutch/SEACR"
---

## Concepts

- **Tool Overview**: SEACR (v1.3) calls peaks and enriched regions from sparse CUT&RUN or chromatin profiling data.
- **Core Function**: Identifies enriched regions in chromatin profiling experiments.
- **Algorithm**: Uses statistical methods to detect significant peaks in sparse data.
- **Input/Output**: Accepts bedgraph files and produces peak calls in BED format.
- **Sparse Data**: Specifically designed for data with many zero-coverage regions.
- **Applications**: ChIP-seq, CUT&RUN, and chromatin accessibility analysis.

## Pitfalls

- **Input Format**: Requires specific input format (bedgraph from paired-end sequencing).
- **Dependencies**: Requires R and Bedtools to be installed.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Quality**: Results depend on sequencing depth and quality.
- **False Positives**: May incorrectly call peaks.
- **False Negatives**: May miss true peaks.

## Examples

### Basic peak calling
**Args:** `SEACR_1.3.sh -i treatment.bg -c control.bg -o peaks`
**Explanation:** `-i` treatment bedgraph; `-c` control bedgraph; `-o` output prefix.

### Without control
**Args:** `SEACR_1.3.sh -i treatment.bg --norm -o peaks`
**Explanation:** `--norm` normalizes without control.

### Stringent mode
**Args:** `SEACR_1.3.sh -i treatment.bg -c control.bg -s stringent -o peaks`
**Explanation:** `-s stringent` uses more stringent threshold.

### Relaxed mode
**Args:** `SEACR_1.3.sh -i treatment.bg -c control.bg -s relaxed -o peaks`
**Explanation:** `-s relaxed` uses less stringent threshold.

### Verbose logging
**Args:** `SEACR_1.3.sh -i treatment.bg -c control.bg -v -o peaks`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `SEACR_1.3.sh --help`
**Explanation:** Shows available options and usage information.

### Version check
**Args:** `SEACR_1.3.sh --version`
**Explanation:** Shows current version.