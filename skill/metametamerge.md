---
name: metametamerge
category: utility
description: Merging module of the MetaMeta Pipeline
tags: [metametamerge, utility, metagenomics, merging]
author: oxo-call-community
source_url: "https://github.com/pirovc/metametamerge/"
---

## Concepts

- **Tool Overview**: MetaMetaMerge v1.1 is the merging module of the MetaMeta Pipeline, designed for combining metagenomic analysis results from multiple sources.
- **Core Function**: Merges taxonomic profiles and abundance estimates from multiple metagenomic analysis tools.
- **Multi-tool Integration**: Combines results from different metagenomic profiling tools for comprehensive analysis.
- **Consensus Generation**: Generates consensus taxonomic profiles from multiple tool outputs.
- **Input/Output**: Accepts taxonomic profiles from various tools; outputs merged and consensus profiles.
- **Flexible Formatting**: Supports multiple input formats from different metagenomic tools.

## Pitfalls

- **Format Compatibility**: Requires consistent input formats from different tools.
- **Tool-specific Biases**: Different tools may have inherent biases that affect merged results.
- **Normalization**: Requires proper normalization of abundance estimates across tools.
- **Missing Data**: Some tools may not report certain taxa, affecting merging.
- **Computational Resources**: Merging large datasets may require significant computational resources.
- **Result Interpretation**: Merged results may require careful interpretation.

## Examples

### Merge taxonomic profiles
**Args:** `metametamerge -i profile1.txt profile2.txt -o merged.txt`
**Explanation:** Merges taxonomic profiles from multiple tools.

### Generate consensus
**Args:** `metametamerge -i profiles/ -o consensus.txt -c`
**Explanation:** Generates consensus profile from multiple input profiles.

### Specify format
**Args:** `metametamerge -i profile.txt -o merged.txt -f kraken`
**Explanation:** Specifies input format as Kraken-style output.

### Output detailed report
**Args:** `metametamerge -i profiles/ -o merged.txt -v`
**Explanation:** Generates verbose output with detailed merging information.

### Filter by confidence
**Args:** `metametamerge -i profiles/ -o merged.txt -t 0.8`
**Explanation:** Filters results to minimum confidence threshold of 0.8.