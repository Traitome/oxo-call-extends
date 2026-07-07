---
name: rfplasmid
category: assembly
description: RFPlasmid predicts plasmid contigs from assemblies using machine learning.
tags: [rfplasmid, assembly, plasmid-prediction, machine-learning]
author: oxo-call-community
source_url: "https://github.com/aldertzomer/RFPlasmid"
---

## Concepts

- **Tool Overview**: rfplasmid predicts plasmids.
- **Core Function**: Plasmid contig prediction.
- **Algorithm**: Uses random forest methods.
- **Input Format**: Accepts assembly contigs.
- **Output**: Produces plasmid predictions.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Contig Quality**: Affects prediction.
- **Parameters**: Must be configured.
- **Runtime**: Prediction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rfplasmid --help`
**Explanation:** Shows available options and usage instructions.

### Predict plasmids
**Args:** `rfplasmid predict -i contigs.fasta -o predictions.txt`
**Explanation:** Predicts plasmid contigs from assembly.

### With parameters
**Args:** `rfplasmid predict -i contigs.fasta -p params.yaml -o predictions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rfplasmid -v predict -i contigs.fasta -o predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rfplasmid -t 4 predict -i contigs.fasta -o predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With model
**Args:** `rfplasmid predict -i contigs.fasta -m model.pt -o predictions.txt`
**Explanation:** Uses custom trained model.

### Generate report
**Args:** `rfplasmid predict -i contigs.fasta -o predictions.txt --report report.html`
**Explanation:** Generates HTML report.