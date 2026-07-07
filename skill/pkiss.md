---
name: pkiss
category: utility
description: pkiss predicts RNA secondary structures including pseudoknots.
tags: [pkiss, utility, rna, structure]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/pkiss"
---

## Concepts

- **Tool Overview**: pkiss predicts RNA secondary structures.
- **Core Function**: RNA structure prediction.
- **Algorithm**: Uses energy minimization methods.
- **Input Format**: Accepts RNA sequence files.
- **Output**: Produces structure prediction results.
- **Use Case**: RNA analysis, structure prediction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Long sequences require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Prediction Accuracy**: May have prediction errors.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pkiss --help`
**Explanation:** Shows available options and usage instructions.

### Predict RNA structure
**Args:** `pkiss -i rna_sequence.fasta -o structure.txt`
**Explanation:** Predicts RNA secondary structure.

### With parameters
**Args:** `pkiss -i rna_sequence.fasta -p params.yaml -o structure.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pkiss -v -i rna_sequence.fasta -o structure.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pkiss -t 4 -i rna_sequence.fasta -o structure.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pkiss -i rna_sequence.fasta -o structure.dot --dot`
**Explanation:** Outputs in DOT format.

### Generate report
**Args:** `pkiss -i rna_sequence.fasta -o structure.txt --report report.html`
**Explanation:** Generates HTML report.