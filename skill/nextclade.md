---
name: nextclade
category: alignment
description: Nextclade performs viral genome alignment, mutation calling, clade assignment, quality checks and phylogenetic placement.
tags: [nextclade, alignment, viral-genomics, nextstrain, clade-assignment]
author: oxo-call-community
source_url: "https://github.com/nextstrain/nextclade"
---

## Concepts

- **Tool Overview**: Nextclade is a comprehensive tool for viral genome analysis and classification.
- **Core Function**: Aligns sequences, calls mutations, assigns clades, and performs quality checks.
- **Algorithm**: Combines sequence alignment with phylogenetic tree placement.
- **Input Format**: Accepts FASTA files and reference datasets.
- **Output**: Produces aligned sequences, mutation reports, clade assignments, and quality metrics.
- **Use Case**: Viral surveillance, outbreak tracking, and genomic epidemiology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Datasets**: Requires compatible reference data.
- **Sequence Quality**: Poor quality sequences affect results.
- **Clade Definitions**: Requires up-to-date clade definitions.
- **Memory Usage**: Large datasets require memory.
- **Phylogenetic Accuracy**: Depends on tree quality.

## Examples

### Display help
**Args:** `nextclade --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `nextclade --input-fasta sequences.fasta --input-dataset data/ --output-dir results/`
**Explanation:** Runs complete analysis pipeline.

### Download dataset
**Args:** `nextclade dataset get sars-cov-2 --output-dir data/`
**Explanation:** Downloads reference dataset for SARS-CoV-2.

### Custom reference
**Args:** `nextclade --input-fasta sequences.fasta --reference ref.fasta --tree tree.nw --output-dir results/`
**Explanation:** Uses custom reference files.

### Output TSV
**Args:** `nextclade --input-fasta sequences.fasta --input-dataset data/ --output-tsv results.tsv`
**Explanation:** Outputs results in TSV format.

### Output tree
**Args:** `nextclade --input-fasta sequences.fasta --input-dataset data/ --output-tree tree.nw`
**Explanation:** Outputs phylogenetic tree with placements.

### Quiet mode
**Args:** `nextclade --input-fasta sequences.fasta --input-dataset data/ -q --output-dir results/`
**Explanation:** Runs in quiet mode with minimal output.