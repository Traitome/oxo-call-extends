---
name: phame
category: population-genomics
description: phame derives SNP matrices and phylogenetic trees from genomic data.
tags: [phame, population-genomics, snp, phylogeny]
author: oxo-call-community
source_url: "https://github.com/LANL-Bioinformatics/PhaME"
---

## Concepts

- **Tool Overview**: phame analyzes genomic variation.
- **Core Function**: Derives SNP matrices and trees.
- **Algorithm**: Uses SNP-based phylogenetic analysis.
- **Input Format**: Accepts reads, contigs, or genomes.
- **Output**: Produces SNP matrices and phylogenies.
- **Use Case**: Phylogenetics, SNP analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Genome**: Requires proper reference genome.
- **SNP Calling**: May miss low-frequency variants.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phame --help`
**Explanation:** Shows available options and usage instructions.

### Analyze reads
**Args:** `phame -i reads.fastq -r ref.fasta -o snp_matrix.txt`
**Explanation:** Derives SNP matrix from reads.

### With contigs
**Args:** `phame -i contigs.fasta -r ref.fasta -o snp_matrix.txt`
**Explanation:** Derives SNP matrix from contigs.

### Verbose mode
**Args:** `phame -v -i reads.fastq -r ref.fasta -o snp_matrix.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phame -t 4 -i reads.fastq -r ref.fasta -o snp_matrix.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phame -i reads.fastq -r ref.fasta -o snp_matrix.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phame -i reads.fastq -r ref.fasta -o snp_matrix.txt --report report.html`
**Explanation:** Generates HTML report.