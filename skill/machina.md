---
name: machina
category: programming
description: Metastatic And Clonal History INtegrative Analysis
tags: [machina, programming, cancer, metastasis]
author: oxo-call-community
source_url: "https://github.com/raphael-group/machina"
---

## Concepts

- **Tool Overview**: machina v1.2 is a computational framework for inferring migration patterns between primary tumor and metastases.
- **Core Function**: Integrates DNA sequencing data to reconstruct metastatic spread patterns.
- **Integrative Approach**: Combines multiple types of sequencing data for comprehensive analysis.
- **Input/Output**: Input: Variant data from multiple tumor samples; Output: Inferred migration trees.
- **Installation**: `conda install -c bioconda machina`
- **Key Features**: Multi-sample analysis, supports different sequencing technologies, visualizes results.

## Pitfalls

- **Sample Availability**: Requires samples from both primary and metastatic sites.
- **Data Quality**: Poor-quality sequencing affects inference accuracy.
- **Computational Complexity**: Can be slow for large numbers of samples.
- **Memory Usage**: May require significant memory for complex analyses.
- **Model Complexity**: Results can be difficult to interpret without domain knowledge.
- **Assumptions**: Relies on assumptions about clonal evolution and metastasis.

## Examples

### Run MACHINA analysis
**Args:** `machina -i variant_data.txt -o results/`
**Explanation:** Runs integrative analysis on variant data.

### With multiple samples
**Args:** `machina -i sample1.txt sample2.txt sample3.txt -o results/`
**Explanation:** Analyzes data from multiple tumor samples.

### Threads
**Args:** `machina -i variant_data.txt -t 4 -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output trees
**Args:** `machina -i variant_data.txt -f newick -o trees.nwk`
**Explanation:** Outputs migration trees in Newick format.

### Verbose mode
**Args:** `machina -i variant_data.txt -v -o results/`
**Explanation:** Outputs detailed analysis information.

### Help documentation
**Args:** `machina --help`
**Explanation:** Displays all available options and parameters.