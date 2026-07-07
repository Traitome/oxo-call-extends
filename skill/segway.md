---
name: segway
category: functional-genomics
description: segway - Pattern discovery and identification in functional genomics data
tags: ["segway", "functional-genomics", "pattern-discovery", "chromatin"]
author: oxo-call-community
source_url: "http://segway.hoffmanlab.org/"
---

## Concepts

- **Tool Overview**: segway (v3.0.4) discovers patterns in functional genomics data.
- **Core Function**: Identifies and annotates patterns in genomic data.
- **Algorithm**: Uses hidden Markov models for pattern recognition.
- **Input/Output**: Accepts genomic track data and produces segmentation annotations.
- **Pattern Discovery**: Focuses on chromatin state segmentation.
- **Applications**: Epigenomics, chromatin analysis, and functional genomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Training Data**: Requires appropriate training data for model building.
- **Reference Genome**: Requires proper reference genome setup.
- **Documentation**: Some features have limited documentation.

## Examples

### Train model
**Args:** `segway train -i tracks.txt -l labels.txt -m model.segway`
**Explanation:** `-i` input tracks; `-l` labels; `-m` output model.

### Predict
**Args:** `segway predict -i tracks.txt -m model.segway -o predictions.bed`
**Explanation:** `-i` input tracks; `-m` model; `-o` output predictions.

### Verbose logging
**Args:** `segway train -i tracks.txt -v -m model.segway`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `segway train -i tracks.txt -t 8 -m model.segway`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `segway --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `segway --version`
**Explanation:** Shows current version.

### Evaluate
**Args:** `segway evaluate -i predictions.bed -t truth.bed -o metrics.txt`
**Explanation:** Evaluates predictions against truth data.