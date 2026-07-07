---
name: pyham
category: utility
description: pyham analyzes Hierarchical Orthologous Groups (HOGs) for comparative genomics.
tags: [pyham, utility, orthologs, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/DessimozLab/pyham"
---

## Concepts

- **Tool Overview**: pyham analyzes orthologous groups.
- **Core Function**: HOG analysis.
- **Algorithm**: Uses phylogenetic trees.
- **Input Format**: Accepts OrthoXML/PhyloXML files.
- **Output**: Produces HOG annotations.
- **Use Case**: Comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tree Quality**: Results depend on input tree.
- **Orthology Predictions**: May have errors.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyham --help`
**Explanation:** Shows available options and usage instructions.

### Analyze HOGs
**Args:** `pyham analyze -i orthoxml.xml -t tree.newick -o results.txt`
**Explanation:** Analyzes hierarchical orthologous groups.

### With parameters
**Args:** `pyham analyze -i orthoxml.xml -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyham -v analyze -i orthoxml.xml -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyham -t 4 analyze -i orthoxml.xml -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Export to CSV
**Args:** `pyham export -i results.txt -o hogs.csv`
**Explanation:** Exports results to CSV.

### Generate report
**Args:** `pyham analyze -i orthoxml.xml -o results.txt --report report.html`
**Explanation:** Generates HTML report.