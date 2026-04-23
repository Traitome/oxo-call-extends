---
name: aakomp
category: qc
description: amino acid k-mer-based genome completeness assessment
tags: [aakomp, qc, genome, completeness, k-mer]
author: oxo-call-community
source_url: "https://github.com/bcgsc/aakomp"
---

## Concepts

- **Tool Overview**: Assesses genome assembly completeness using amino acid k-mer analysis. Version 1.0.0.
- **Core Function**: Evaluates genome completeness by comparing amino acid k-mer profiles against reference databases or expectations.
- **Input/Output**: Input is a genome assembly (FASTA); output is a completeness assessment report.
- **Installation**: Install via bioconda: `conda install -c bioconda aakomp`
- **Platform Support**: Linux (x86_64) and macOS (x86_64)
- **K-mer Based**: Uses amino acid k-mers rather than nucleotide k-mers for completeness assessment, which is more robust to sequencing errors and assembly fragmentation.

## Pitfalls

- **Version Differences**: Early version (1.0.0). Options may change in future releases.
- **Reference Database**: May require a reference database for comparison. Ensure database is appropriate for your organism.
- **Amino Acid Translation**: Requires gene prediction or translation step if input is nucleotide assembly.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Assess genome completeness
**Args:** `genome_assembly.fasta`
**Explanation:** Analyzes the genome assembly and outputs completeness assessment based on amino acid k-mer content.

### Run with specific k-mer size
**Args:** `-k 7 genome.fasta -o completeness_report.txt`
**Explanation:** Uses 7-mers for amino acid analysis. K-mer size affects sensitivity and specificity of completeness assessment.

### Compare against reference database
**Args:** `--reference-db ref_db.fasta genome.fasta -o report.txt`
**Explanation:** Compares the assembly's amino acid k-mer profile against a reference database for more accurate completeness estimation.
