---
name: allo
category: qc
description: Multi-mapped read rescue strategy for gene regulatory analyses that accurately allocates multi-mapped reads using probabilistic mapping and CNN
tags: [allo, multi-mapped-reads, chip-seq, atac-seq, gene-regulation, repeats]
author: oxo-call-community
source_url: "https://github.com/seqcode/allo"
---

## Concepts

- **Tool Overview**: Allo is a multi-mapped read rescue strategy designed for gene regulatory analyses, enabling accurate detection of regulatory elements in repetitive genomic regions.
- **Core Function**: Combines probabilistic mapping of multi-mapped reads with a convolutional neural network (CNN) that recognizes read distribution features of potential peaks, offering enhanced accuracy in multi-mapping read assignment.
- **Key Innovation**: Addresses the problem of discarded multi-mapped reads in ChIP-seq/ATAC-seq pipelines, enabling discovery of regulatory events in transposable elements and repetitive regions.
- **Supported Assays**: ChIP-seq, ATAC-seq, DNase-seq, RNA-seq
- **Input/Output**: Input: SAM/BAM file with multi-mapped reads. Output: Corrected alignment file with allocated multi-mapped reads.
- **Installation**: Install via bioconda: `conda install -c bioconda allo` or via pip: `pip install allo-multi`
- **Citation**: Morrissey A, Shi J, James DQ, Mahony S (2024). Accurate allocation of multimapped reads enables regulatory element analysis at repeats. Genome Research 34(6):937-951.
- **License**: MIT

## Pitfalls

- **Aligner Requirements**: Requires specific aligner settings to retain multi-mapped reads (Bowtie1/2 with --best --strata -m/-k options).
- **BWA Limitation**: BWA cannot be used for paired-end reads prior to Allo due to constraints in how it outputs multi-mapped reads.
- **CNN Models**: Pre-trained CNNs available for DNase-seq and ATAC-seq; custom training may be needed for other assays.
- **Memory Usage**: Processing large BAM files requires sufficient memory.
- **Intron Removal**: Option to remove introns based on CIGAR string splice junction information.

## Examples

### Display help information
**Args:** `allo --help`
**Explanation:** Shows available command-line options and usage instructions.

### Basic usage for ChIP-seq
**Args:** `allo -i input.sam -o output.sam -g hg38`
**Explanation:** Processes SAM file and allocates multi-mapped reads for human genome hg38.

### With peak file for supervised allocation
**Args:** `allo -i input.sam -o output.sam -g hg38 -p peaks.bed`
**Explanation:** Uses peak file to guide supervised allocation of multi-mapped reads.

### Remove introns from consideration
**Args:** `allo -i input.sam -o output.sam -g hg38 --remove_introns`
**Explanation:** Removes introns as identified by splice junction information in CIGAR strings.

### Specify custom genome size
**Args:** `allo -i input.sam -o output.sam -g custom_genome -s genome.size`
**Explanation:** Uses custom genome with provided chromosome sizes file.

### Run in verbose mode
**Args:** `allo -i input.sam -o output.sam -g hg38 -v`
**Explanation:** Runs with verbose output showing detailed processing information.

### Set maximum multi-mapping locations
**Args:** `allo -i input.sam -o output.sam -g hg38 -m 25`
**Explanation:** Sets maximum number of mapping locations to consider (default 25).

### Process paired-end data
**Args:** `allo -i input.sam -o output.sam -g hg38 --paired`
**Explanation:** Processes paired-end sequencing data.

### Output BAM format
**Args:** `allo -i input.bam -o output.bam -g hg38 --bam`
**Explanation:** Input and output in BAM format.
