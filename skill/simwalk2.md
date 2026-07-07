---
name: simwalk2
category: population-genomics
description: SimWalk2 - Stochastic Statistical Analysis of Qualitative Traits
tags: ["simwalk2", "population-genomics", "linkage", "pedigree"]
author: oxo-call-community
source_url: "http://www.genetics.ucla.edu/software/"
---

## Concepts

- **Tool Overview**: SimWalk2 (v2.91) performs linkage analysis for qualitative traits.
- **Core Function**: Analyzes genetic linkage in pedigree data.
- **Algorithm**: Uses Markov chain Monte Carlo for linkage analysis.
- **Input/Output**: Accepts pedigree and marker data.
- **Linkage Analysis**: Specialized for genetic linkage studies.
- **Applications**: Genetic mapping, disease gene identification.

## Pitfalls

- **Memory Usage**: High memory requirements for large pedigrees.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on pedigree data quality.
- **Version Compatibility**: Legacy software, may have compatibility issues.
- **Documentation**: Limited documentation available.

## Examples

### Run linkage analysis
**Args:** `simwalk2 -p pedigree.ped -m markers.txt -o results/`
**Explanation:** `-p` pedigree file; `-m` marker data; `-o` output.

### With simulation
**Args:** `simwalk2 -p pedigree.ped -s -o results/`
**Explanation:** `-s` perform simulation.

### With parameters
**Args:** `simwalk2 -p pedigree.ped -m markers.txt -c config.par -o results/`
**Explanation:** `-c` parameter file.

### Help command
**Args:** `simwalk2 --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simwalk2 --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simwalk2 -v -p pedigree.ped -m markers.txt -o results/`
**Explanation:** `-v` verbose output.

### Multi-threaded mode
**Args:** `simwalk2 -t 8 -p pedigree.ped -m markers.txt -o results/`
**Explanation:** `-t 8` uses 8 threads.
