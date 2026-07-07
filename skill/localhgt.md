---
name: localhgt
category: comparative-genomics
description: LocalHGT - Ultrafast horizontal gene transfer detection from large microbial communities
tags: [localhgt, comparative-genomics, HGT, horizontal-gene-transfer, microbial, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/deepomicslab/LocalHGT"
---

## Concepts

- **Horizontal Gene Transfer**: Detection of horizontal gene transfer events
- **Microbial Communities**: Analysis of microbial community data
- **Phylogenetic Analysis**: Phylogenetic-based HGT detection
- **Large Scale**: Designed for large-scale datasets
- **Fast Algorithm**: Ultrafast detection algorithm
- **Evolutionary Analysis**: Evolutionary analysis of gene transfer

## Pitfalls

- **Sequence Quality**: Poor quality sequences affect detection
- **Phylogenetic Signal**: Requires strong phylogenetic signal
- **Computational Time**: May be slow for very large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive predictions
- **Memory Usage**: Memory-intensive for large datasets

## Examples

### Detect HGT
**Args:** `localhgt -i genomes/ -o hgt_results.txt`
**Explanation:** Detects horizontal gene transfer events.

### Single genome pair
**Args:** `localhgt -i genome1.fasta genome2.fasta -o hgt.txt`
**Explanation:** Analyzes HGT between two genomes.

### Threads
**Args:** `localhgt -i genomes/ -o hgt_results.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### E-value threshold
**Args:** `localhgt -i genomes/ -o hgt_results.txt -e 1e-10`
**Explanation:** Sets E-value threshold to 1e-10.

### Output format
**Args:** `localhgt -i genomes/ -o hgt_results.json -f json`
**Explanation:** Outputs results in JSON format.

### Verbose output
**Args:** `localhgt -i genomes/ -o hgt_results.txt -v`
**Explanation:** Provides detailed output.