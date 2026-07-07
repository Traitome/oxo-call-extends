---
name: semibin
category: metagenomics
description: semibin - Metagenomic binning with siamese neural networks
tags: ["semibin", "metagenomics", "binning", "neural-networks"]
author: oxo-call-community
source_url: "https://semibin.readthedocs.io"
---

## Concepts

- **Tool Overview**: semibin (v2.2.1) performs metagenomic binning using siamese neural networks.
- **Core Function**: Bins metagenomic contigs into genome bins using deep learning.
- **Algorithm**: Uses siamese neural networks for similarity-based binning.
- **Input/Output**: Accepts assembled contigs and produces genome bins.
- **Deep Learning**: Leverages neural networks for improved binning accuracy.
- **Applications**: Metagenomics, microbiome analysis, and genome reconstruction.

## Pitfalls

- **Computational Resources**: Requires significant compute resources (GPU recommended).
- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on assembly quality.
- **Training Data**: Requires appropriate training data for model building.
- **Software Dependencies**: Requires PyTorch and other ML libraries.

## Examples

### Bin metagenome
**Args:** `semibin bin -i contigs.fasta -o bins/`
**Explanation:** `-i` input contigs; `-o` output directory for bins.

### With abundance info
**Args:** `semibin bin -i contigs.fasta -a abundance.txt -o bins/`
**Explanation:** `-a` abundance file for better binning.

### Verbose logging
**Args:** `semibin bin -i contigs.fasta -v -o bins/`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `semibin bin -i contigs.fasta -t 8 -o bins/`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Help command
**Args:** `semibin --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `semibin --version`
**Explanation:** Shows current version.

### Evaluate bins
**Args:** `semibin evaluate -i bins/ -o evaluation.txt`
**Explanation:** Evaluates bin quality.