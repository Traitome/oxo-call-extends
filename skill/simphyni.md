---
name: simphyni
category: population-genomics
description: SimPhyni - Phylogenetic trait simulation and inference
tags: ["simphyni", "population-genomics", "phylogenetics", "simulation"]
author: oxo-call-community
source_url: "https://github.com/jpeyemi/SimPhyNI"
---

## Concepts

- **Tool Overview**: SimPhyni (v1.0.2) performs phylogenetic trait simulation and inference.
- **Core Function**: Simulates and analyzes trait evolution on phylogenetic trees.
- **Algorithm**: Uses maximum likelihood and Bayesian methods for inference.
- **Input/Output**: Accepts phylogenetic trees and trait data.
- **Phylogenetic Analysis**: Specialized for comparative phylogenetics.
- **Applications**: Evolutionary biology, trait evolution studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large trees.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on tree quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Simulate traits
**Args:** `simphyni simulate -t tree.nwk -o simulated_traits.txt`
**Explanation:** `-t` input tree; `-o` output traits.

### Infer parameters
**Args:** `simphyni infer -t tree.nwk -d traits.txt -o results.txt`
**Explanation:** `-d` trait data; infer evolutionary parameters.

### With model
**Args:** `simphyni infer -t tree.nwk -d traits.txt -m BM -o results.txt`
**Explanation:** `-m BM` use Brownian motion model.

### Help command
**Args:** `simphyni --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simphyni --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simphyni -v simulate -t tree.nwk -o traits.txt`
**Explanation:** `-v` verbose output.

### Bootstrap mode
**Args:** `simphyni infer -t tree.nwk -d traits.txt -b -o results.txt`
**Explanation:** `-b` enable bootstrap analysis.
