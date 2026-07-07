---
name: pastml
category: population-genomics
description: PastML performs ancestral character reconstruction and visualization on phylogenetic trees.
tags: [pastml, population-genomics, phylogenetics, ancestral-reconstruction]
author: oxo-call-community
source_url: "https://pastml.pasteur.fr"
---

## Concepts

- **Tool Overview**: PastML reconstructs and visualizes ancestral characters.
- **Core Function**: Performs ancestral state reconstruction.
- **Algorithm**: Uses maximum likelihood and parsimony methods.
- **Input Format**: Accepts phylogenetic trees and annotations.
- **Output**: Produces visualizations and reconstructed states.
- **Use Case**: Evolutionary biology, phylogeography.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large trees require memory.
- **Tree Quality**: Results depend on input tree quality.
- **Method Selection**: Different methods produce different results.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pastml --help`
**Explanation:** Shows available options and usage instructions.

### Reconstruct ancestral states
**Args:** `pastml -t tree.nwk -d data.csv -o output/`
**Explanation:** Performs ancestral character reconstruction.

### With visualisation
**Args:** `pastml -t tree.nwk -d data.csv -o output/ --html`
**Explanation:** Generates HTML visualization.

### Verbose mode
**Args:** `pastml -v -t tree.nwk -d data.csv -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pastml -p 4 -t tree.nwk -d data.csv -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### Method selection
**Args:** `pastml -m MPPA -t tree.nwk -d data.csv -o output/`
**Explanation:** Uses maximum parsimony method.

### Output format
**Args:** `pastml -t tree.nwk -d data.csv -o output.json --json`
**Explanation:** Outputs in JSON format.