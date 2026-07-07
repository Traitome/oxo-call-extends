---
name: pstrain
category: metagenomics
description: pstrain is an iterative microbial strain profiling algorithm for shotgun metagenomic sequencing data.
tags: [pstrain, metagenomics, strain-profiling, microbiome]
author: oxo-call-community
source_url: "https://github.com/wshuai294/PStrain"
---

## Concepts

- **Tool Overview**: pstrain profiles microbial strains.
- **Core Function**: Strain-level profiling.
- **Algorithm**: Uses iterative mapping.
- **Input Format**: Accepts metagenomic reads.
- **Output**: Produces strain profiles.
- **Use Case**: Metagenomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Strain Diversity**: May affect detection.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pstrain --help`
**Explanation:** Shows available options and usage instructions.

### Profile strains
**Args:** `pstrain -i reads.fastq -r reference.fasta -o strain_profiles.txt`
**Explanation:** Profiles microbial strains from metagenomic data.

### With parameters
**Args:** `pstrain -i reads.fastq -r reference.fasta -p params.yaml -o strain_profiles.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pstrain -v -i reads.fastq -r reference.fasta -o strain_profiles.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pstrain -t 4 -i reads.fastq -r reference.fasta -o strain_profiles.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Iteration count
**Args:** `pstrain -i reads.fastq -r reference.fasta -n 10 -o strain_profiles.txt`
**Explanation:** Uses 10 iterations.

### Generate report
**Args:** `pstrain -i reads.fastq -r reference.fasta -o strain_profiles.txt --report report.html`
**Explanation:** Generates HTML report.