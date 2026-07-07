---
name: picrust2
category: population-genomics
description: picrust2 predicts functional profiles from marker gene sequences.
tags: [picrust2, population-genomics, functional, prediction]
author: oxo-call-community
source_url: "https://github.com/picrust/picrust2"
---

## Concepts

- **Tool Overview**: picrust2 predicts functional profiles.
- **Core Function**: Phylogenetic functional prediction.
- **Algorithm**: Uses phylogenetic reconstruction methods.
- **Input Format**: Accepts marker gene sequences.
- **Output**: Produces functional prediction results.
- **Use Case**: Metagenomics, functional analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Prediction Accuracy**: May have prediction errors.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `picrust2 --help`
**Explanation:** Shows available options and usage instructions.

### Predict functions
**Args:** `picrust2 -i marker_genes.fasta -o functional_results.txt`
**Explanation:** Predicts functional profiles.

### With parameters
**Args:** `picrust2 -i marker_genes.fasta -p params.yaml -o functional_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `picrust2 -v -i marker_genes.fasta -o functional_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `picrust2 -t 4 -i marker_genes.fasta -o functional_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `picrust2 -i marker_genes.fasta -o functional_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `picrust2 -i marker_genes.fasta -o functional_results.txt --report report.html`
**Explanation:** Generates HTML report.