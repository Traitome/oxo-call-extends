---
name: parsnp
category: alignment
description: Parsnp performs efficient microbial core genome alignment and SNP detection.
tags: [parsnp, alignment, microbial, snp-detection]
author: oxo-call-community
source_url: "https://github.com/marbl/parsnp"
---

## Concepts

- **Tool Overview**: Parsnp aligns microbial genomes and detects SNPs.
- **Core Function**: Performs core genome alignment and SNP calling.
- **Algorithm**: Uses progressive alignment approach.
- **Input Format**: Accepts genome sequences in FASTA format.
- **Output**: Produces aligned core genome and SNP calls.
- **Use Case**: Microbial genomics, comparative analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Genome Similarity**: Works best with closely related genomes.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parsnp --help`
**Explanation:** Shows available options and usage instructions.

### Run alignment
**Args:** `parsnp -g genomes.fasta -r reference.fasta -o results/`
**Explanation:** Aligns genomes and detects SNPs.

### With output directory
**Args:** `parsnp -d genomes/ -o results/`
**Explanation:** Processes all genomes in directory.

### Verbose mode
**Args:** `parsnp -v -g genomes.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `parsnp -p 8 -g genomes.fasta -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output VCF
**Args:** `parsnp -g genomes.fasta -o results/ --vcf`
**Explanation:** Outputs SNPs in VCF format.

### Minimum alignment length
**Args:** `parsnp -m 1000 -g genomes.fasta -o results/`
**Explanation:** Sets minimum alignment length.