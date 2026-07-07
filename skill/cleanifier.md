---
name: cleanifier
category: qc
description: Fast lightweight tool to remove contamination using k-mers
tags: [cleanifier, qc, contamination, k-mer, sequence-cleaning]
author: oxo-call-community
source_url: "https://gitlab.com/rahmannlab/cleanifier"
---

## Concepts

- **Tool Overview**: cleanifier is a fast and lightweight tool for removing contamination from sequencing data using k-mer based approach.
- **Core Function**: Identifies and removes contaminant sequences from sequencing reads or assemblies.
- **Algorithm**: Uses k-mer frequency analysis to distinguish between target and contaminant sequences.
- **Input**: Sequencing reads (FASTQ) or assembled contigs (FASTA).
- **Output**: Cleaned sequences with contaminants removed.
- **Application**: Sequence quality control, contamination removal, and data cleaning.
- **Installation**: Install via bioconda: `conda install -c bioconda cleanifier`

## Pitfalls

- **Reference Database**: Requires contaminant reference database for comparison.
- **K-mer Selection**: Appropriate k-mer size must be chosen.
- **Sensitivity**: May miss low-level contamination.
- **False Positives**: May remove true sequences if not properly configured.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Remove contamination from reads
**Args:** `cleanifier -i reads.fastq -c contaminants.fasta -o clean_reads.fastq`
**Explanation:** Removes contaminant sequences from input reads.

### With k-mer size
**Args:** `cleanifier -i reads.fastq -c contaminants.fasta -k 21 -o clean_reads.fastq`
**Explanation:** Uses specific k-mer size for contamination detection.

### Clean assembled contigs
**Args:** `cleanifier -i assembly.fasta -c contaminants.fasta -o clean_assembly.fasta`
**Explanation:** Removes contaminant contigs from assembly.

### Display help
**Args:** `cleanifier --help`
**Explanation:** Shows all available options and usage information.