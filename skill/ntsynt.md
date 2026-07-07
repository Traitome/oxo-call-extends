---
name: ntsynt
category: alignment
description: ntSynt detects multi-genome synteny blocks using minimizer graph mapping.
tags: [ntsynt, alignment, synteny, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/bcgsc/ntsynt"
---

## Concepts

- **Tool Overview**: ntSynt identifies synteny blocks across multiple genomes.
- **Core Function**: Detects conserved syntenic regions using minimizer graphs.
- **Algorithm**: Uses minimizer-based graph mapping for synteny detection.
- **Input Format**: Accepts FASTA genome sequences.
- **Output**: Produces synteny block coordinates and visualizations.
- **Use Case**: Comparative genomics, evolutionary analysis, and genome alignment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Genome Quality**: Results depend on genome assembly quality.
- **Memory Usage**: Large genomes require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ntsynt --help`
**Explanation:** Shows available options and usage instructions.

### Detect synteny
**Args:** `ntsynt -i genome1.fasta -i2 genome2.fasta -o synteny.txt`
**Explanation:** Detects synteny between two genomes.

### Multiple genomes
**Args:** `ntsynt -i genome1.fasta -i2 genome2.fasta -i3 genome3.fasta -o synteny.txt`
**Explanation:** Analyzes synteny across multiple genomes.

### Minimizer size
**Args:** `ntsynt -i genome1.fasta -i2 genome2.fasta -k 21 -o synteny.txt`
**Explanation:** Sets minimizer k-mer size to 21.

### Output visualization
**Args:** `ntsynt -i genome1.fasta -i2 genome2.fasta -o synteny.txt --plot`
**Explanation:** Generates synteny plot.

### Threads
**Args:** `ntsynt -i genome1.fasta -i2 genome2.fasta -t 8 -o synteny.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `ntsynt -i genome1.fasta -i2 genome2.fasta -v -o synteny.txt`
**Explanation:** Runs with verbose output.