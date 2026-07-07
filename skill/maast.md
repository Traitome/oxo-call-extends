---
name: maast
category: variant-calling
description: Microbial agile accurate SNP Typer
tags: [maast, variant-calling, SNP, microbial]
author: oxo-call-community
source_url: "https://github.com/zjshi/Maast"
---

## Concepts

- **Tool Overview**: maast v1.0.8 is a fast and accurate SNP typing tool for microbial genomes.
- **Core Function**: Identifies and types SNPs in microbial sequences for strain identification and tracking.
- **Algorithm**: Uses efficient alignment and variant calling optimized for microbial genomes.
- **Input/Output**: Input: FASTQ reads or FASTA sequences; Output: SNP calls with typing information.
- **Installation**: `conda install -c bioconda maast`
- **Key Features**: High accuracy, fast performance, supports multiple microbial species.

## Pitfalls

- **Reference Genome**: Requires high-quality reference genome for accurate SNP calling.
- **Read Quality**: Low-quality reads can affect SNP calling accuracy.
- **Memory Usage**: Processing large datasets may require significant memory.
- **Computation Time**: Can be slow for very large genomes or datasets.
- **Parameter Tuning**: May require adjustment for different microbial species.
- **Contamination**: Contaminated sequences can affect SNP typing results.

## Examples

### SNP typing from reads
**Args:** `maast -i reads.fastq -r reference.fasta -o snp_calls.txt`
**Explanation:** Performs SNP typing from sequencing reads.

### SNP typing from assembly
**Args:** `maast -i assembly.fasta -r reference.fasta -o snp_calls.txt`
**Explanation:** Performs SNP typing from genome assembly.

### Threads
**Args:** `maast -i reads.fastq -r reference.fasta -t 8 -o snp_calls.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `maast -i reads.fastq -r reference.fasta -f vcf -o snp_calls.vcf`
**Explanation:** Outputs results in VCF format.

### Minimum quality
**Args:** `maast -i reads.fastq -r reference.fasta -q 30 -o snp_calls.txt`
**Explanation:** Sets minimum base quality threshold to 30.

### Help documentation
**Args:** `maast --help`
**Explanation:** Displays all available options and parameters.