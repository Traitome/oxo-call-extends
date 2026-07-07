---
name: paraclu
category: hpc
description: Paraclu finds clusters in data attached to sequences.
tags: [paraclu, hpc, clustering, sequences]
author: oxo-call-community
source_url: "https://gitlab.com/mcfrith/paraclu"
---

## Concepts

- **Tool Overview**: Paraclu identifies clusters in sequence-associated data.
- **Core Function**: Performs clustering on genomic data.
- **Algorithm**: Uses density-based clustering approach.
- **Input Format**: Accepts sequence data with associated values.
- **Output**: Produces cluster boundaries and statistics.
- **Use Case**: ChIP-seq analysis, peak calling, sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Parameter Sensitivity**: Results depend on parameters.
- **Runtime**: Analysis may take significant time.
- **Cluster Quality**: Results depend on input data quality.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paraclu --help`
**Explanation:** Shows available options and usage instructions.

### Basic clustering
**Args:** `paraclu data.txt > clusters.txt`
**Explanation:** Performs clustering on input data.

### With threshold
**Args:** `paraclu -t 0.5 data.txt > clusters.txt`
**Explanation:** Sets cluster threshold to 0.5.

### Verbose mode
**Args:** `paraclu -v data.txt > clusters.txt`
**Explanation:** Runs with verbose output.

### Output format
**Args:** `paraclu -f gff data.txt > clusters.gff`
**Explanation:** Outputs in GFF format.

### Minimum cluster size
**Args:** `paraclu -m 10 data.txt > clusters.txt`
**Explanation:** Sets minimum cluster size to 10.

### Stranded analysis
**Args:** `paraclu -s data.txt > clusters.txt`
**Explanation:** Performs strand-specific clustering.