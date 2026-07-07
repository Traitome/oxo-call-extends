---
name: olga
category: programming
description: OLGA computes generation probability of amino acid and nucleotide CDR3 sequences from V(D)J recombination models.
tags: [olga, programming, immunology, vdj-recombination]
author: oxo-call-community
source_url: "https://github.com/zsethna/OLGA"
---

## Concepts

- **Tool Overview**: OLGA estimates generation probabilities of immune receptor sequences.
- **Core Function**: Computes likelihood of CDR3 sequence generation.
- **Algorithm**: Uses generative models of V(D)J recombination.
- **Input Format**: Accepts CDR3 sequences and V(D)J gene information.
- **Output**: Produces generation probabilities and likelihood scores.
- **Use Case**: Immunology research, repertoire analysis, and vaccine design.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Model Parameters**: Requires trained model parameters.
- **Sequence Quality**: Results depend on input sequence quality.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Probability computation can be intensive.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `python -m olga --help`
**Explanation:** Shows available options and usage instructions.

### Compute probability
**Args:** `python -m olga compute -i cdr3_sequences.txt -o probabilities.txt`
**Explanation:** Computes generation probabilities for CDR3 sequences.

### With model
**Args:** `python -m olga compute -i sequences.txt -m model.pkl -o results.txt`
**Explanation:** Uses custom model for probability computation.

### Generate sequences
**Args:** `python -m olga generate -n 1000 -o generated.txt`
**Explanation:** Generates synthetic CDR3 sequences.

### Verbose mode
**Args:** `python -m olga compute -i sequences.txt -v -o results.txt`
**Explanation:** Runs with verbose output.

### Python usage
**Args:** `python -c "from olga import ProbabilityComputer; pc = ProbabilityComputer()"`
**Explanation:** Uses OLGA in Python script.

### Batch processing
**Args:** `python -m olga batch -d sequences/ -o results/`
**Explanation:** Processes multiple sequence files.