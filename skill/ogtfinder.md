---
name: ogtfinder
category: utility
description: OGTFinder predicts optimal growth temperature for prokaryotes using proteome features.
tags: [ogtfinder, utility, temperature-prediction, prokaryotes]
author: oxo-call-community
source_url: "https://github.com/SC-Git1/OGTFinder"
---

## Concepts

- **Tool Overview**: OGTFinder predicts optimal growth temperature from proteomes.
- **Core Function**: Predicts optimal growth temperature for prokaryotic organisms.
- **Algorithm**: Uses machine learning on proteome-derived features.
- **Input Format**: Accepts FASTA proteome sequences.
- **Output**: Produces predicted optimal growth temperature.
- **Use Case**: Microbial ecology, metagenomics, and evolutionary studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Training Data**: Model trained on specific taxa.
- **Sequence Quality**: Results depend on input sequence quality.
- **Prediction Range**: Limited to known temperature ranges.
- **Confidence**: Predictions have associated uncertainty.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `ogtfinder --help`
**Explanation:** Shows available options and usage instructions.

### Predict OGT
**Args:** `ogtfinder -i proteome.fasta -o result.txt`
**Explanation:** Predicts optimal growth temperature.

### Multiple proteomes
**Args:** `ogtfinder -i proteome1.fasta proteome2.fasta -o results.txt`
**Explanation:** Predicts OGT for multiple proteomes.

### Output confidence
**Args:** `ogtfinder -i proteome.fasta -o result.txt --confidence`
**Explanation:** Includes confidence interval in output.

### Verbose mode
**Args:** `ogtfinder -i proteome.fasta -v -o result.txt`
**Explanation:** Runs with verbose output.

### Model information
**Args:** `ogtfinder --model-info`
**Explanation:** Shows model details and training information.

### Batch processing
**Args:** `ogtfinder -d proteomes/ -o results.txt`
**Explanation:** Processes all proteomes in directory.

### Output format
**Args:** `ogtfinder -i proteome.fasta -o results.csv --csv`
**Explanation:** Outputs results in CSV format.