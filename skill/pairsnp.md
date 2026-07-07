---
name: pairsnp
category: alignment
description: pairsnp calculates pairwise SNP distance matrices from multiple sequence alignments.
tags: [pairsnp, alignment, snp-distance, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/gtonkinhill/pairsnp"
---

## Concepts

- **Tool Overview**: pairsnp computes SNP distance matrices for phylogenetic analysis.
- **Core Function**: Calculates pairwise SNP distances between sequences.
- **Algorithm**: Uses efficient SNP counting from alignments.
- **Input Format**: Accepts FASTA multiple sequence alignments.
- **Output**: Produces distance matrices in various formats.
- **Use Case**: Phylogenetics, population genetics, and evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Missing Data**: May handle gaps differently.
- **Ambiguous Bases**: May affect distance calculations.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pairsnp --help`
**Explanation:** Shows available options and usage instructions.

### Compute distance matrix
**Args:** `pairsnp -i alignment.fasta -o distances.txt`
**Explanation:** Calculates pairwise SNP distances.

### Output format
**Args:** `pairsnp -i alignment.fasta -o distances.phylip --phylip`
**Explanation:** Outputs in PHYLIP format.

### Filter by minimum SNPs
**Args:** `pairsnp -i alignment.fasta -m 10 -o distances.txt`
**Explanation:** Filters pairs with at least 10 SNPs.

### Verbose mode
**Args:** `pairsnp -v -i alignment.fasta -o distances.txt`
**Explanation:** Runs with verbose output.

### Threads
**Args:** `pairsnp -t 8 -i alignment.fasta -o distances.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Missing data handling
**Args:** `pairsnp -i alignment.fasta -m 0.1 -o distances.txt`
**Explanation:** Allows 10% missing data.