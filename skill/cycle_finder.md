---
name: cycle_finder
category: utility
description: A de novo analysis tool for tandem and interspersed repeats based on cycle-finding
tags: [cycle_finder, utility, repeats, tandem-repeats, interspersed-repeats]
author: oxo-call-community
source_url: "https://github.com/rkajitani/cycle_finder"
---

## Concepts

- **Tool Overview**: cycle_finder (v1.0.0+) is a de novo analysis tool for detecting tandem and interspersed repeats using cycle-finding algorithms.
- **Core Function**: Identifies repetitive DNA sequences without prior knowledge of repeat motifs.
- **Input/Output**: Input: FASTA genome sequences. Output: Repeat annotations, consensus sequences.
- **Algorithm**: Uses cycle detection in de Bruijn graphs to identify repetitive patterns.
- **Key Features**: De novo repeat detection, handles tandem and interspersed repeats, outputs consensus sequences.
- **Installation**: `conda install -c bioconda cycle_finder`

## Pitfalls

- **Memory Usage**: Large genomes may require significant memory for graph construction.
- **Sensitivity/Specificity**: Parameter tuning required for optimal repeat detection.
- **Output Volume**: May produce many repeat predictions; filtering may be necessary.
- **Complex Regions**: Highly repetitive regions may produce ambiguous results.
- **Validation**: Predicted repeats should be validated with other tools.

## Examples

### Detect repeats in genome
**Args:** `cycle_finder -i genome.fasta -o repeats.txt`
**Explanation:** Identify repetitive sequences in genome using cycle-finding.

### Specify minimum repeat length
**Args:** `cycle_finder -i genome.fasta -o repeats.txt --min-length 20`
**Explanation:** Detect repeats with minimum length of 20 base pairs.

### Generate consensus sequences
**Args:** `cycle_finder -i genome.fasta -o repeats.txt --consensus`
**Explanation:** Output consensus sequences for detected repeats.
