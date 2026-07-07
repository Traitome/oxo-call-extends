---
name: stereogene
category: statistics
description: "StereoGene: Rapid Estimation of Genomewide Correlation of Continuous or Interval Feature Data."
tags: [stereogene, genomics, statistics, correlation-analysis]
author: oxo-call-community
source_url: "http://stereogene.bioinf.fbb.msu.ru"
---
## Concepts

- **Tool Overview**: stereogene (v2.20) is a tool for rapidly estimating genome-wide correlation between continuous or interval-based genomic features.
- **Core Function**: Computes correlation matrices for genomic datasets to identify co-occurring features.
- **Algorithm**: Uses efficient matrix operations to compute correlations across genome-wide data.
- **Input/Output**: Input: Genomic feature data (BED, WIG, or custom format); Output: Correlation matrix and statistical significance.
- **Applications**: ChIP-seq peak correlation, histone modification analysis, multi-omics integration.
- **Installation**: `conda install -c bioconda stereogene` or download from official website.

## Pitfalls

- **Data Normalization**: Improper normalization affects correlation estimates.
- **Resolution**: Incorrect bin size affects correlation detection.
- **Memory Requirements**: Large genomes require significant memory.
- **Multiple Testing**: Failure to correct for multiple testing produces false positives.
- **Missing Data**: Missing values affect correlation calculations.
- **Feature Selection**: Too many features increase computational time.

## Examples

### Display help
**Args:** `stereogene --help`
**Explanation:** Shows available options and usage information.

### Basic correlation analysis
**Args:** `stereogene -i features.txt -o correlation.txt`
**Explanation:** Compute genome-wide correlation matrix.

### With specific resolution
**Args:** `stereogene -i features.txt -o correlation.txt -r 1000`
**Explanation:** Set bin resolution to 1000 bp.

### Verbose mode
**Args:** `stereogene -i features.txt -o correlation.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output heatmap
**Args:** `stereogene -i features.txt -o correlation.txt --heatmap`
**Explanation:** Generate heatmap visualization of correlations.

### Statistical testing
**Args:** `stereogene -i features.txt -o correlation.txt --test`
**Explanation:** Perform significance testing for correlations.

### Batch processing
**Args:** `stereogene -i batch/ -o results/`
**Explanation:** Process multiple feature files together.

### Filter by threshold
**Args:** `stereogene -i features.txt -o correlation.txt -c 0.7`
**Explanation:** Filter correlations with absolute value below 0.7.

### Export matrix
**Args:** `stereogene -i features.txt -o correlation.txt --matrix`
**Explanation:** Export full correlation matrix in matrix format.
