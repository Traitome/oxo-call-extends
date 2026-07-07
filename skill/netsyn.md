---
name: netsyn
category: utility
description: NetSyn detects conserved genomic contexts (synteny conservation) among protein targets.
tags: [netsyn, utility, synteny, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/labgem/netsyn"
---

## Concepts

- **Tool Overview**: NetSyn detects conserved genomic contexts (synteny) among protein targets.
- **Core Function**: Identifies syntenic regions across multiple genomes.
- **Algorithm**: Uses comparative genomics to find conserved gene order and context.
- **Input Format**: Accepts protein sequences and genome annotations.
- **Output**: Produces synteny conservation reports and visualizations.
- **Use Case**: Comparative genomics, evolutionary biology, and gene function prediction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Genome Quality**: Results depend on input genome quality.
- **Computational Cost**: Comparing many genomes is computationally intensive.
- **Memory Usage**: Large genome datasets require memory.
- **Annotation Quality**: Requires high-quality gene annotations.
- **False Positives**: May report false positive syntenic regions.

## Examples

### Display help
**Args:** `netsyn --help`
**Explanation:** Shows available options and usage instructions.

### Basic synteny detection
**Args:** `netsyn -i proteins.fasta -g genomes/ -o synteny/`
**Explanation:** Detects syntenic regions for protein targets.

### Multiple genomes
**Args:** `netsyn -i proteins.fasta -g genome1.fasta genome2.fasta -o synteny/`
**Explanation:** Compares synteny across multiple genomes.

### Output visualization
**Args:** `netsyn -i proteins.fasta -g genomes/ --plot -o plot.pdf`
**Explanation:** Generates synteny visualization.

### Conservation score
**Args:** `netsyn -i proteins.fasta -g genomes/ --score -o scores.tsv`
**Explanation:** Computes conservation scores.

### Filter by conservation
**Args:** `netsyn -i proteins.fasta -g genomes/ -c 0.8 -o synteny/`
**Explanation:** Filters results by minimum conservation score.

### Output BED
**Args:** `netsyn -i proteins.fasta -g genomes/ --bed -o synteny.bed`
**Explanation:** Outputs syntenic regions in BED format.