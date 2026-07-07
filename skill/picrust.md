---
name: picrust
category: population-genomics
description: picrust predicts functional profiles from 16S rRNA sequences.
tags: [picrust, population-genomics, functional, 16s]
author: oxo-call-community
source_url: "http://picrust.github.com"
---

## Concepts

- **Tool Overview**: picrust predicts functional profiles.
- **Core Function**: Phylogenetic functional prediction.
- **Algorithm**: Uses phylogenetic reconstruction methods.
- **Input Format**: Accepts 16S rRNA sequences.
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
**Args:** `picrust --help`
**Explanation:** Shows available options and usage instructions.

### Predict functions
**Args:** `picrust -i 16s_sequences.fasta -o functional_results.txt`
**Explanation:** Predicts functional profiles from 16S sequences.

### With parameters
**Args:** `picrust -i 16s_sequences.fasta -p params.yaml -o functional_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `picrust -v -i 16s_sequences.fasta -o functional_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `picrust -t 4 -i 16s_sequences.fasta -o functional_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `picrust -i 16s_sequences.fasta -o functional_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `picrust -i 16s_sequences.fasta -o functional_results.txt --report report.html`
**Explanation:** Generates HTML report.