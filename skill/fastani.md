---
name: fastani
category: alignment
description: "FastANI is developed for fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI)."
tags: [fastani, alignment, ANI, genome-comparison, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ParBLiSS/FastANI"
---

## Concepts

- **Tool Overview**: FastANI is a fast alignment-free tool for computing Average Nucleotide Identity (ANI) between whole genomes.
- **Core Function**: Calculates ANI values for genome comparison without sequence alignment.
- **Input/Output**: Input: Genome sequences (FASTA). Output: ANI scores, alignment mappings.
- **Algorithm**: Uses k-mer based approach for fast genome comparison.
- **Key Features**: Ultra-fast ANI calculation, alignment-free, supports multiple genomes, accurate results, parallel processing.
- **Installation**: `conda install -c bioconda fastani`

## Pitfalls

- **Genome Quality**: Requires complete or high-quality draft genomes.
- **Memory Usage**: Large datasets may require significant memory.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Computation Time**: Very large genomes may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic ANI calculation
**Args:** `fastANI -q query.fasta -r reference.fasta -o result.txt`
**Explanation:** Computes ANI between query and reference genome.

### Multiple references
**Args:** `fastANI -q query.fasta --rl reference_list.txt -o result.txt`
**Explanation:** Compares query against multiple reference genomes.

### Output mappings
**Args:** `fastANI -q query.fasta -r reference.fasta -o result.txt --visualize`
**Explanation:** Generates visualization mappings.

### Parallel processing
**Args:** `fastANI -q query.fasta -r reference.fasta -o result.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Batch mode
**Args:** `fastANI --ql query_list.txt --rl reference_list.txt -o result.txt`
**Explanation:** Processes multiple query-reference pairs.