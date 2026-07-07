---
name: nextclade2
category: alignment
description: Nextclade2 performs viral genome alignment, mutation calling, clade assignment, quality checks and phylogenetic placement.
tags: [nextclade2, alignment, viral-genomics, nextstrain, clade-assignment]
author: oxo-call-community
source_url: "https://github.com/nextstrain/nextclade"
---

## Concepts

- **Tool Overview**: Nextclade2 is an integrated tool for comprehensive viral genome analysis.
- **Core Function**: Performs alignment, mutation calling, clade assignment, and quality control.
- **Algorithm**: Combines alignment, variant detection, and phylogenetic placement.
- **Input Format**: Accepts FASTA files with viral sequences and reference data.
- **Output**: Produces aligned sequences, mutations, clade assignments, and quality reports.
- **Use Case**: Viral surveillance, outbreak analysis, and phylogenetic studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Data**: Requires up-to-date reference datasets.
- **Sequence Quality**: Low-quality sequences may produce unreliable results.
- **Database Updates**: Clade definitions need regular updates.
- **Memory Usage**: Large datasets require memory.
- **Phylogenetic Placement**: May not work well for highly divergent sequences.

## Examples

### Display help
**Args:** `nextclade2 --help`
**Explanation:** Shows available options and usage instructions.

### Run complete analysis
**Args:** `nextclade2 run --input-dataset data/ --input-fasta sequences.fasta --output-dir results/`
**Explanation:** Runs complete clade analysis pipeline.

### List available datasets
**Args:** `nextclade2 dataset list`
**Explanation:** Shows available reference datasets.

### Download dataset
**Args:** `nextclade2 dataset get --name sars-cov-2 --output-dir data/`
**Explanation:** Downloads reference dataset.

### Custom reference
**Args:** `nextclade2 run --input-fasta sequences.fasta --reference ref.fasta --tree tree.nw --output-dir results/`
**Explanation:** Uses custom reference data.

### Output JSON
**Args:** `nextclade2 run --input-fasta sequences.fasta --input-dataset data/ --output-json results.json`
**Explanation:** Outputs results in JSON format.

### Verbose mode
**Args:** `nextclade2 run --input-fasta sequences.fasta --input-dataset data/ -v --output-dir results/`
**Explanation:** Enables verbose output.