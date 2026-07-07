---
name: psdm
category: alignment
description: psdm computes pairwise SNP distance matrices from sequence alignments.
tags: [psdm, alignment, SNP-distance, matrix]
author: oxo-call-community
source_url: "https://github.com/mbhall88/psdm"
---

## Concepts

- **Tool Overview**: psdm calculates SNP distances.
- **Core Function**: Distance matrix computation.
- **Algorithm**: Uses alignment comparison.
- **Input Format**: Accepts FASTA/VCF files.
- **Output**: Produces distance matrix.
- **Use Case**: Phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Alignment Quality**: Affects distances.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psdm --help`
**Explanation:** Shows available options and usage instructions.

### Compute distances
**Args:** `psdm -i alignment.fasta -o distance_matrix.txt`
**Explanation:** Computes pairwise SNP distances.

### With parameters
**Args:** `psdm -i alignment.fasta --params params.yaml -o distance_matrix.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psdm -v -i alignment.fasta -o distance_matrix.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psdm -t 4 -i alignment.fasta -o distance_matrix.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Two alignments
**Args:** `psdm -i1 alignment1.fasta -i2 alignment2.fasta -o distance_matrix.txt`
**Explanation:** Compares two alignments.

### Generate report
**Args:** `psdm -i alignment.fasta -o distance_matrix.txt --report report.html`
**Explanation:** Generates HTML report.