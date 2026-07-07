---
name: pasta
category: alignment
description: PASTA performs multiple sequence alignment using the Practical Alignment using Sate and TrAnsitivity algorithm.
tags: [pasta, alignment, sequence-alignment, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/smirarab/pasta"
---

## Concepts

- **Tool Overview**: PASTA aligns multiple sequences efficiently.
- **Core Function**: Performs progressive multiple sequence alignment.
- **Algorithm**: Uses SATé and transitivity for alignment.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces aligned sequences.
- **Use Case**: Phylogenetics, comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Similarity**: Works best with similar sequences.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `run_pasta.py --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `run_pasta.py -i input.fasta -o output/`
**Explanation:** Aligns sequences using PASTA.

### With guidance tree
**Args:** `run_pasta.py -i input.fasta -t tree.nwk -o output/`
**Explanation:** Uses existing guidance tree.

### Verbose mode
**Args:** `run_pasta.py -v -i input.fasta -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `run_pasta.py -p 8 -i input.fasta -o output/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `run_pasta.py -i input.fasta -o output.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Maximum iterations
**Args:** `run_pasta.py -i input.fasta -m 10 -o output/`
**Explanation:** Sets maximum iterations.