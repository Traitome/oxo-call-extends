---
name: lsc
category: utility
description: LSC is a long read error correction tool that offers fast correction with high sensitivity and good accuracy.
tags: [lsc, utility, error-correction, long-reads]
author: oxo-call-community
source_url: "https://www.healthcare.uiowa.edu/labs/au/LSC/"
---

## Concepts

- **Tool Overview**: lsc v2.0 is a fast and accurate error correction tool specifically designed for long sequencing reads.
- **Core Function**: Corrects sequencing errors in long reads using a reference-guided approach with high sensitivity.
- **Error Correction Strategy**: Uses a two-step process: k-mer based correction followed by alignment-based refinement.
- **Input/Output**: Input: Long reads in FASTQ format, reference genome; Output: Corrected reads in FASTQ format.
- **Installation**: `conda install -c bioconda lsc`
- **Key Features**: Fast processing, high accuracy, supports PacBio and Oxford Nanopore reads.

## Pitfalls

- **Reference Quality**: Requires a high-quality reference genome for accurate correction.
- **Memory Usage**: Processing large datasets may require significant memory.
- **Computation Time**: Can be slow for very large datasets or complex genomes.
- **Read Length**: Performance may vary with extremely long or short reads.
- **Error Rate**: Very high error rate reads may not correct well.
- **Parameter Tuning**: May require parameter adjustment for different data types.

## Examples

### Correct reads with reference
**Args:** `lsc -r reference.fasta -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects long reads using reference genome.

### K-mer size
**Args:** `lsc -r reference.fasta -i reads.fastq -o corrected.fastq -k 21`
**Explanation:** Uses k-mer size 21 for error correction.

### Threads
**Args:** `lsc -r reference.fasta -i reads.fastq -o corrected.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum quality
**Args:** `lsc -r reference.fasta -i reads.fastq -o corrected.fastq -q 20`
**Explanation:** Sets minimum base quality threshold to 20.

### Verbose output
**Args:** `lsc -r reference.fasta -i reads.fastq -o corrected.fastq -v`
**Explanation:** Outputs detailed progress information.

### Help documentation
**Args:** `lsc --help`
**Explanation:** Displays all available options and parameters.