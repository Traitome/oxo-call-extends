---
name: physher
category: population-genomics
description: physher provides multi-algorithmic phylogenetic inference framework.
tags: [physher, population-genomics, phylogenetic, inference]
author: oxo-call-community
source_url: "https://github.com/4ment/physher"
---

## Concepts

- **Tool Overview**: physher performs phylogenetic inference.
- **Core Function**: Multi-algorithmic phylogenetic inference.
- **Algorithm**: Uses multiple phylogenetic algorithms.
- **Input Format**: Accepts phylogenetic data files.
- **Output**: Produces phylogenetic inference results.
- **Use Case**: Phylogenetics, phylogenetic inference.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Algorithm Selection**: Requires proper algorithm selection.
- **Runtime**: Inference may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `physher --help`
**Explanation:** Shows available options and usage instructions.

### Infer phylogeny
**Args:** `physher -i phylogenetic_data.txt -o inference_results.txt`
**Explanation:** Performs phylogenetic inference.

### With parameters
**Args:** `physher -i phylogenetic_data.txt -p params.yaml -o inference_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `physher -v -i phylogenetic_data.txt -o inference_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `physher -t 4 -i phylogenetic_data.txt -o inference_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `physher -i phylogenetic_data.txt -o inference_results.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `physher -i phylogenetic_data.txt -o inference_results.txt --report report.html`
**Explanation:** Generates HTML report.