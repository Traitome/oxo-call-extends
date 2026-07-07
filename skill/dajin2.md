---
name: dajin2
category: variant-calling
description: One-step genotyping tools for targeted long-read sequencing
tags: [dajin2, variant-calling, genotyping, long-read, targeted-sequencing]
author: oxo-call-community
source_url: "https://github.com/akikuno/DAJIN2/blob/0.9.2/README.md"
---

## Concepts

- **Tool Overview**: dajin2 (v0.9.2+) is a one-step genotyping tool designed for targeted long-read sequencing data.
- **Core Function**: Performs rapid genotyping of target regions directly from long-read sequencing data.
- **Input/Output**: Input: BAM/FASTQ long-read data, target region definitions. Output: Genotype calls, allele frequencies.
- **Algorithm**: Uses alignment-based genotyping with statistical inference for accurate variant detection.
- **Key Features**: One-step analysis, handles mixed populations, supports long-read data.
- **Installation**: `conda install -c bioconda dajin2`

## Pitfalls

- **Target Definition**: Requires proper definition of target regions.
- **Read Quality**: Works best with high-quality long reads.
- **Coverage**: Adequate coverage needed for accurate genotyping.
- **Reference Bias**: May have reference bias with certain variant types.
- **Validation**: Results should be validated with orthogonal methods.

## Examples

### Run one-step genotyping
**Args:** `dajin2 -i reads.fastq -r reference.fasta -t targets.bed -o genotypes.txt`
**Explanation:** Perform one-step genotyping on targeted regions from long reads.

### Specify allele frequency threshold
**Args:** `dajin2 -i reads.fastq -r reference.fasta -t targets.bed -o results.txt --min-freq 0.1`
**Explanation:** Set minimum allele frequency threshold for genotyping.

### Output detailed report
**Args:** `dajin2 -i reads.fastq -r reference.fasta -t targets.bed -o results.txt --report`
**Explanation:** Generate detailed genotyping report with statistics.
