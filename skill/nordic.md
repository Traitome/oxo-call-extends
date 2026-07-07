---
name: nordic
category: drug-discovery
description: NORDic is a network-oriented package for drug repurposing analysis.
tags: [nordic, drug-discovery, drug-repurposing, network-analysis]
author: oxo-call-community
source_url: "https://github.com/clreda/NORDic"
---

## Concepts

- **Tool Overview**: NORDic performs network-based drug repurposing analysis.
- **Core Function**: Identifies potential new uses for existing drugs.
- **Algorithm**: Uses network analysis to find drug-disease connections.
- **Input Format**: Accepts drug-target networks and disease data.
- **Output**: Produces drug repurposing predictions.
- **Use Case**: Drug discovery, drug repurposing, and pharmacology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Data Quality**: Results depend on input data quality.
- **Network Complexity**: Large networks require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Predictions should be experimentally validated.
- **Interpretation**: Requires understanding of network biology.

## Examples

### Display help
**Args:** `nordic --help`
**Explanation:** Shows available options and usage instructions.

### Run drug repurposing
**Args:** `nordic -i network.txt -d disease.txt -o predictions.txt`
**Explanation:** Runs drug repurposing analysis.

### With drug list
**Args:** `nordic -i network.txt -d disease.txt -l drugs.txt -o predictions.txt`
**Explanation:** Uses specific drug list for analysis.

### Output scores
**Args:** `nordic -i network.txt -d disease.txt -o predictions.txt --scores`
**Explanation:** Outputs prediction scores.

### Number of predictions
**Args:** `nordic -i network.txt -d disease.txt -n 100 -o predictions.txt`
**Explanation:** Limits to 100 predictions.

### Threads
**Args:** `nordic -i network.txt -d disease.txt -t 8 -o predictions.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nordic -i network.txt -d disease.txt -v -o predictions.txt`
**Explanation:** Runs with verbose output.