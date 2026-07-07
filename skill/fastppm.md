---
name: fastppm
category: programming
description: "Fast Perfect Phylogeny Mixture Regression using Tree-Structured Dual Dynamic Programming"
tags: [fastppm, programming, phylogeny, mixture-model, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/fastppm"
---

## Concepts

- **Tool Overview**: fastppm is a C++/Python library for fast estimation of unknown frequency matrices given variant and total read counts over an n-clonal tree.
- **Core Function**: Performs Perfect Phylogeny Mixture Regression using Tree-Structured Dual Dynamic Programming.
- **Input/Output**: Input: Variant read counts, tree structure. Output: Frequency matrix, clonal structure.
- **Algorithm**: Uses tree-structured dual dynamic programming for efficient computation.
- **Key Features**: Fast computation, tree-structured optimization, mixture modeling, Python bindings, large dataset support.
- **Installation**: `conda install -c bioconda fastppm`

## Pitfalls

- **Tree Structure**: Requires predefined tree structure.
- **Memory Usage**: Large datasets may require significant memory.
- **Computation Time**: Complex analyses may require substantial processing time.
- **Data Quality**: Requires high-quality input data.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic usage
**Args:** `fastppm -i variants.txt -t tree.newick -o frequencies.txt`
**Explanation:** Estimates frequency matrix from variant data.

### Python API
**Args:** `python -c "from fastppm import fastppm; result = fastppm(variants, tree)"`
**Explanation:** Uses Python API for analysis.

### With regularization
**Args:** `fastppm -i variants.txt -t tree.newick -o frequencies.txt -r 0.1`
**Explanation:** Applies regularization to the optimization.

### Verbose output
**Args:** `fastppm -i variants.txt -t tree.newick -o frequencies.txt -v`
**Explanation:** Generates verbose output.

### Batch processing
**Args:** `fastppm -i variants_list.txt -t tree.newick -o results/ --batch`
**Explanation:** Processes multiple datasets in batch mode.