---
name: ngsrelate
category: population-genetics
description: NgsRelate estimates pairwise relatedness from next-generation sequencing data.
tags: [ngsrelate, population-genetics, relatedness, kinship]
author: oxo-call-community
source_url: "https://github.com/ANGSD/NgsRelate"
---

## Concepts

- **Tool Overview**: NgsRelate estimates genetic relatedness between individuals from sequencing data.
- **Core Function**: Calculates pairwise relatedness coefficients.
- **Algorithm**: Uses genotype likelihoods for accurate relatedness estimation.
- **Input Format**: Accepts BAM files or genotype likelihood files.
- **Output**: Produces relatedness estimates and kinship coefficients.
- **Use Case**: Population genetics, pedigree reconstruction, and identity-by-descent analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Genotype Quality**: Results depend on genotype calling quality.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Reference Genome**: Requires indexed reference genome.
- **Sample Size**: Works best with moderate to large sample sizes.

## Examples

### Display help
**Args:** `ngsrelate --help`
**Explanation:** Shows available options and usage instructions.

### Basic relatedness estimation
**Args:** `ngsrelate -b alignments.list -o relatedness.txt`
**Explanation:** Estimates relatedness from BAM files.

### With genotype likelihoods
**Args:** `ngsrelate -gl genotype_likelihoods.glf -o relatedness.txt`
**Explanation:** Uses precomputed genotype likelihoods.

### Specify population
**Args:** `ngsrelate -b alignments.list -p population.txt -o relatedness.txt`
**Explanation:** Includes population information.

### Threads
**Args:** `ngsrelate -b alignments.list -t 8 -o relatedness.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Output matrix
**Args:** `ngsrelate -b alignments.list -m -o relatedness_matrix.txt`
**Explanation:** Outputs relatedness matrix.

### Verbose mode
**Args:** `ngsrelate -b alignments.list -v -o relatedness.txt`
**Explanation:** Runs with verbose output.