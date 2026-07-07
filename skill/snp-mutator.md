---
name: snp-mutator
category: simulation
description: SNP-Mutator - Generate mutated sequence files from reference genome
tags: [snp-mutator, simulation, mutation, reference, sequences]
author: oxo-call-community
source_url: "https://github.com/CFSAN-Biostatistics/snp-mutator"
---

## Concepts

- **Tool Overview**: snp-mutator (v1.2.0) - A tool for simulating mutations in sequences
- **Core Function**: Generates mutated sequences from reference with specified SNPs
- **Input/Output**: Accepts reference FASTA and SNP list; outputs mutated sequences
- **Algorithm**: Applies mutations to reference sequence
- **Installation**: `conda install -c bioconda snp-mutator`
- **Key Features**: Mutation simulation, reference modification, SNP application

## Pitfalls

- **Input Requirements**: Requires properly formatted reference and SNP files
- **SNP Format**: SNP format must be compatible with tool
- **Sequence Length**: Large sequences may be slow to process
- **Mutation Types**: Supports specific mutation types only
- **Output Naming**: Output files need proper naming conventions
- **Validation**: Requires validation of mutated sequences

## Examples

### Display help
**Args:** `snp-mutator --help`
**Explanation:** Shows available options and usage information.

### Basic mutation
**Args:** `snp-mutator -r reference.fasta -s snps.txt -o mutated.fasta`
**Explanation:** Generate mutated sequence from reference.

### With VCF input
**Args:** `snp-mutator -r reference.fasta -v variants.vcf -o mutated.fasta`
**Explanation:** Use VCF file for mutations.

### Multiple outputs
**Args:** `snp-mutator -r reference.fasta -s snps.txt -o output_dir/ --multiple`
**Explanation:** Generate multiple mutated sequences.

### With frequency
**Args:** `snp-mutator -r reference.fasta -s snps.txt -o mutated.fasta --frequency 0.5`
**Explanation:** Apply mutations with specified frequency.

### Random mutations
**Args:** `snp-mutator -r reference.fasta -o mutated.fasta --random 10`
**Explanation:** Generate random mutations.

### With annotation
**Args:** `snp-mutator -r reference.fasta -s snps.txt -o mutated.fasta --annotate`
**Explanation:** Annotate mutations in output.

### Generate report
**Args:** `snp-mutator -r reference.fasta -s snps.txt -o mutated.fasta --report`
**Explanation:** Generate mutation report.