---
name: neofox
category: annotation
description: NeoFox annotates mutated peptide sequences with published or novel potential neo-epitope descriptors.
tags: [neofox, annotation, neoepitope, immunology, cancer]
author: oxo-call-community
source_url: "https://github.com/tron-bioinformatics/neofox"
---

## Concepts

- **Tool Overview**: NeoFox is a tool for annotating mutated peptide sequences with neo-epitope descriptors.
- **Core Function**: Identifies and characterizes potential neo-epitopes from mutated sequences.
- **Algorithm**: Uses sequence analysis and immunological databases to predict neo-epitopes.
- **Input Format**: Accepts FASTA files with mutated peptide sequences.
- **Output**: Produces annotated neo-epitope predictions and descriptors.
- **Use Case**: Cancer immunology research, vaccine development, and immunotherapy.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Quality**: Results depend on input sequence quality.
- **Database Dependencies**: Requires immunological database access.
- **Memory Usage**: Processing large datasets requires memory.
- **Prediction Accuracy**: Predictions are probabilistic.
- **HLA Typing**: Requires accurate HLA typing information.

## Examples

### Display help
**Args:** `neofox --help`
**Explanation:** Shows available options and usage instructions.

### Basic annotation
**Args:** `neofox -i peptides.fasta -o annotations.tsv`
**Explanation:** Annotates peptide sequences.

### HLA typing
**Args:** `neofox -i peptides.fasta --hla A*02:01 -o annotations.tsv`
**Explanation:** Uses specific HLA allele for prediction.

### Multiple alleles
**Args:** `neofox -i peptides.fasta --hla A*02:01,A*03:01 -o annotations.tsv`
**Explanation:** Uses multiple HLA alleles.

### Novel epitopes
**Args:** `neofox -i peptides.fasta --novel -o annotations.tsv`
**Explanation:** Identifies novel neo-epitopes.

### Output JSON
**Args:** `neofox -i peptides.fasta --json -o annotations.json`
**Explanation:** Outputs results in JSON format.

### Score threshold
**Args:** `neofox -i peptides.fasta --threshold 0.5 -o annotations.tsv`
**Explanation:** Sets prediction score threshold.