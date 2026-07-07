---
name: lz-ani
category: utility
description: Fast and accurate tool for calculating Average Nucleotide Identity (ANI) among virus and bacteria genomes
tags: [lz-ani, utility, ANI, genomics]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/lz-ani"
---

## Concepts

- **Tool Overview**: lz-ani v1.2.3 is a fast and accurate tool for calculating Average Nucleotide Identity (ANI) between microbial genomes.
- **Core Function**: Computes ANI values to determine evolutionary relatedness between genomes.
- **Algorithm**: Uses LZ77 compression for efficient sequence comparison.
- **Input/Output**: Input: FASTA files with genome sequences; Output: ANI matrix or pairwise comparisons.
- **Installation**: `conda install -c bioconda lz-ani`
- **Key Features**: Fast computation, low memory usage, accurate ANI estimation.

## Pitfalls

- **Genome Quality**: Requires complete or nearly complete genome sequences.
- **Memory Usage**: Processing many genomes simultaneously may require significant memory.
- **Computation Time**: Comparing many genomes can be time-consuming.
- **Sequence Length**: Short sequences may produce unreliable ANI estimates.
- **Contamination**: Contaminated sequences can affect ANI calculations.
- **Parameter Tuning**: May require adjustment for different sequence types.

## Examples

### Calculate ANI between two genomes
**Args:** `lz-ani -i genome1.fasta genome2.fasta -o ani_result.txt`
**Explanation:** Computes ANI between two genomes.

### Multiple genomes
**Args:** `lz-ani -i genome1.fasta genome2.fasta genome3.fasta -o ani_matrix.txt`
**Explanation:** Computes pairwise ANI for multiple genomes.

### Output matrix
**Args:** `lz-ani -i *.fasta -m -o ani_matrix.txt`
**Explanation:** Outputs ANI values as a matrix.

### Threads
**Args:** `lz-ani -i genome1.fasta genome2.fasta -t 8 -o ani_result.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose output
**Args:** `lz-ani -i genome1.fasta genome2.fasta -v -o ani_result.txt`
**Explanation:** Outputs detailed progress information.

### Help documentation
**Args:** `lz-ani --help`
**Explanation:** Displays all available options and parameters.