---
name: phytop
category: utility
description: phytop visualizes and recognizes signals of incomplete lineage sorting and hybridization.
tags: [phytop, utility, lineage-sorting, hybridization]
author: oxo-call-community
source_url: "https://github.com/zhangrengang/phytop/"
---

## Concepts

- **Tool Overview**: phytop visualizes phylogenetic signals.
- **Core Function**: Incomplete lineage sorting detection.
- **Algorithm**: Uses species tree analysis methods.
- **Input Format**: Accepts ASTRAL species tree files.
- **Output**: Produces visualization results.
- **Use Case**: Phylogenetics, hybridization analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tree Quality**: Results depend on tree quality.
- **Signal Detection**: May have detection errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phytop --help`
**Explanation:** Shows available options and usage instructions.

### Analyze species tree
**Args:** `phytop -i species_tree.newick -o analysis_results.txt`
**Explanation:** Analyzes species tree for incomplete lineage sorting.

### With parameters
**Args:** `phytop -i species_tree.newick -p params.yaml -o analysis_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phytop -v -i species_tree.newick -o analysis_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phytop -t 4 -i species_tree.newick -o analysis_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phytop -i species_tree.newick -o analysis_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phytop -i species_tree.newick -o analysis_results.txt --report report.html`
**Explanation:** Generates HTML report.