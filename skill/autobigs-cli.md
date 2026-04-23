---
name: autobigs-cli
category: variant-calling
description: autoBIGS CLI - Tool for rapid MLST profile fetching from sequences for disease typing
tags: [mlst, typing, pathogen-identification, sequence-typing]
author: oxo-call-community
source_url: "https://github.com/Syph-and-VPD-Lab/autoBIGS.cli"
---

## Concepts

- **Tool Overview**: CLI tool for rapidly fetching MLST (Multi-Locus Sequence Typing) profiles from bacterial genome sequences for various diseases.

- **MLST Database Integration**: Interfaces with MLST databases to identify sequence types from allele profiles.

- **Rapid Typing**: Designed for quick turnaround in clinical and public health settings for outbreak investigation.

- **Multiple Pathogens**: Supports MLST schemes for various bacterial pathogens.

## Pitfalls

- **Database Updates**: MLST databases are regularly updated. Use latest database version for accurate typing.

- **Novel Alleles**: Novel alleles not in database will result in unknown sequence type. May require allele submission.

- **Assembly Quality**: Poor quality assemblies may have missing or incorrect alleles, leading to incorrect ST assignment.

- **Scheme Selection**: Must select appropriate MLST scheme for organism. Wrong scheme gives meaningless results.

## Examples

### Basic MLST typing
**Args:** `autobigs-cli --assembly genome.fasta --scheme neisseria --output mlst_results.txt`
**Explanation:** Performs MLST typing on genome assembly using Neisseria scheme.

### Type from raw reads
**Args:** `autobigs-cli --reads reads_R1.fastq.gz reads_R2.fastq.gz --scheme salmonella --output results.txt`
**Explanation:** Performs MLST directly from raw sequencing reads for Salmonella.

### Batch processing
**Args:** `autobigs-cli --batch genomes/*.fasta --scheme ecoli --output batch_results.tsv`
**Explanation:** Processes multiple genome files for E. coli MLST typing.

### Update MLST database
**Args:** `autobigs-cli --update-db --scheme all`
**Explanation:** Updates all MLST scheme databases to latest versions.

### Detailed allele report
**Args:** `autobigs-cli --assembly genome.fasta --scheme staphylococcus --verbose --output detailed.txt`
**Explanation:** Provides detailed report including individual allele calls and confidence scores.
