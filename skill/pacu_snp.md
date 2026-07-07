---
name: pacu_snp
category: hpc
description: PACU is a workflow for whole genome sequencing based phylogeny of Illumina and ONT data.
tags: [pacu_snp, hpc, phylogeny, whole-genome-sequencing]
author: oxo-call-community
source_url: "https://github.com/BioinformaticsPlatformWIV-ISP/PACU"
---

## Concepts

- **Tool Overview**: PACU performs phylogenomic analysis from sequencing data.
- **Core Function**: Generates phylogenetic trees from WGS data.
- **Algorithm**: Uses SNP calling and tree building.
- **Input Format**: Accepts FASTQ reads or BAM files.
- **Output**: Produces phylogenetic trees and SNP matrices.
- **Use Case**: Phylogenetics, outbreak analysis, and population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Workflows may take significant time.
- **Reference Selection**: Results depend on reference genome.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pacu --help`
**Explanation:** Shows available options and usage instructions.

### Run workflow
**Args:** `pacu run -i reads.fastq -r reference.fasta -o results/`
**Explanation:** Executes PACU workflow.

### With configuration
**Args:** `pacu run -c config.yaml -o results/`
**Explanation:** Uses YAML configuration file.

### Resuming run
**Args:** `pacu run --resume -c config.yaml`
**Explanation:** Resumes from last checkpoint.

### Verbose mode
**Args:** `pacu run -v -c config.yaml`
**Explanation:** Runs with verbose output.

### Dry run
**Args:** `pacu run --dry-run -c config.yaml`
**Explanation:** Shows what would be executed.

### Number of threads
**Args:** `pacu run -t 16 -c config.yaml`
**Explanation:** Uses 16 threads for parallel processing.