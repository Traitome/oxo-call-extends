---
name: parnas
category: population-genomics
description: PaRNaS performs representative taxon sampling from phylogenetic trees.
tags: [parnas, population-genomics, phylogenetics, taxon-sampling]
author: oxo-call-community
source_url: "https://github.com/flu-crew/parnas"
---

## Concepts

- **Tool Overview**: PaRNaS selects representative taxa from phylogenetic trees.
- **Core Function**: Performs taxon sampling for phylogenetic analysis.
- **Algorithm**: Uses tree-based sampling strategies.
- **Input Format**: Accepts phylogenetic trees in Newick format.
- **Output**: Produces selected taxa list.
- **Use Case**: Phylogenetic analysis, taxon selection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large trees require memory.
- **Tree Quality**: Results depend on input tree quality.
- **Sampling Strategy**: Different strategies produce different results.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parnas --help`
**Explanation:** Shows available options and usage instructions.

### Sample taxa
**Args:** `parnas -t tree.nwk -n 100 -o selected.txt`
**Explanation:** Selects 100 representative taxa.

### With metadata
**Args:** `parnas -t tree.nwk -m metadata.txt -o selected.txt`
**Explanation:** Uses metadata for stratified sampling.

### Verbose mode
**Args:** `parnas -v -t tree.nwk -n 100 -o selected.txt`
**Explanation:** Runs with verbose output.

### Sampling strategy
**Args:** `parnas -t tree.nwk -s random -n 100 -o selected.txt`
**Explanation:** Uses random sampling strategy.

### Output format
**Args:** `parnas -t tree.nwk -n 100 -o selected.json --json`
**Explanation:** Outputs in JSON format.

### Minimum distance
**Args:** `parnas -t tree.nwk -d 0.1 -o selected.txt`
**Explanation:** Sets minimum distance between selected taxa.