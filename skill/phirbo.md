---
name: phirbo
category: metagenomics
description: phirbo predicts prokaryotic hosts for phage sequences.
tags: [phirbo, metagenomics, phage, host-prediction]
author: oxo-call-community
source_url: "https://github.com/aziele/phirbo"
---

## Concepts

- **Tool Overview**: phirbo predicts phage hosts.
- **Core Function**: Host prediction for phages.
- **Algorithm**: Uses machine learning methods.
- **Input Format**: Accepts phage genomic sequences.
- **Output**: Produces host prediction results.
- **Use Case**: Phage host prediction, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Host Prediction**: May have prediction errors.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phirbo --help`
**Explanation:** Shows available options and usage instructions.

### Predict hosts
**Args:** `phirbo -i phage.fasta -o host_predictions.txt`
**Explanation:** Predicts phage hosts.

### With parameters
**Args:** `phirbo -i phage.fasta -p params.yaml -o host_predictions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phirbo -v -i phage.fasta -o host_predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phirbo -t 4 -i phage.fasta -o host_predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phirbo -i phage.fasta -o host_predictions.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phirbo -i phage.fasta -o host_predictions.txt --report report.html`
**Explanation:** Generates HTML report.