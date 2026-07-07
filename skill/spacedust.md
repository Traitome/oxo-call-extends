---
name: spacedust
category: comparative-genomics
description: Spacedust - De novo discovery of conserved gene clusters in microbial genomes
tags: [spacedust, comparative-genomics, gene-clusters, microbial, synteny]
author: oxo-call-community
source_url: "https://github.com/soedinglab/spacedust"
---

## Concepts

- **Tool Overview**: spacedust (v2.e56c505) - A gene cluster discovery tool
- **Core Function**: Finds conserved gene clusters in microbial genomes
- **Input/Output**: Accepts microbial genomes; outputs gene cluster predictions
- **Algorithm**: De novo discovery using spaced seeds
- **Installation**: `conda install -c bioconda spacedust`
- **Key Features**: Gene cluster discovery, microbial genomes, de novo detection

## Pitfalls

- **Input Requirements**: Requires properly formatted microbial genomes
- **Gene Annotation**: Requires gene annotations for cluster detection
- **Cluster Parameters**: Cluster detection parameters affect results
- **Memory Usage**: Large genomes require significant memory
- **Output Format**: Output format depends on configuration
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `spacedust --help`
**Explanation:** Shows available options and usage information.

### Basic cluster discovery
**Args:** `spacedust -i genomes.fasta -o clusters.tsv`
**Explanation:** Discover gene clusters from genomes.

### With gene annotations
**Args:** `spacedust -i genomes.fasta -g annotations.gff -o clusters.tsv`
**Explanation:** Use gene annotations for discovery.

### With cluster size
**Args:** `spacedust -i genomes.fasta -o clusters.tsv --min-size 3`
**Explanation:** Set minimum cluster size.

### With conservation threshold
**Args:** `spacedust -i genomes.fasta -o clusters.tsv --conservation 0.8`
**Explanation:** Set conservation threshold.

### Output detailed results
**Args:** `spacedust -i genomes.fasta -o clusters.tsv --detailed`
**Explanation:** Output detailed cluster information.

### Output statistics
**Args:** `spacedust -i genomes.fasta -o clusters.tsv --stats`
**Explanation:** Output discovery statistics.

### Generate report
**Args:** `spacedust -i genomes.fasta -o clusters.tsv --report`
**Explanation:** Generate discovery report.