---
name: gamma
category: variant-calling
description: Tool for Gene Allele Mutation Microbial Assessment.
tags: [gamma, gene mutation, microbial assessment, AMR]
author: oxo-call-community
source_url: "https://github.com/rastanton/GAMMA"
---

## Concepts
- **Gene Mutation Assessment**: Assesses gene allele mutations.
- **AMR Detection**: Detects antimicrobial resistance genes.
- **Microbial Analysis**: Analyzes microbial genetic variants.
- **Allele Calling**: Calls gene alleles from sequencing data.
- **Resistance Prediction**: Predicts antimicrobial resistance.

## Pitfalls
- **Gene Coverage**: Requires sufficient gene coverage.
- **Novel Mutations**: May miss novel or rare mutations.
- **Database Dependency**: Depends on mutation database quality.
- **Mixed Infections**: Complex for mixed infections.
- **Threshold Selection**: Requires careful threshold selection.

## Examples
### Run GAMMA analysis
**Args:** `gamma -i reads.fastq -o results.txt`
**Explanation:** Performs GAMMA analysis on reads.

### With reference genes
**Args:** `gamma -i reads.fastq -r genes.fasta -o results.txt`
**Explanation:** Uses custom reference gene database.

### Specify mutations
**Args:** `gamma -i reads.fastq --mutations mutations.txt -o results.txt`
**Explanation:** Checks for specific mutations.

### Output JSON
**Args:** `gamma -i reads.fastq -o results.json -f json`
**Explanation:** Outputs results in JSON format.

### Verbose mode
**Args:** `gamma -i reads.fastq -v -o results.txt`
**Explanation:** Runs in verbose mode with detailed output.