---
name: basic
category: expression
description: BASIC - Semi-de novo assembly of BCR and TCR genes from single-cell RNA-seq data
tags: [basic, expression, BCR, TCR, single-cell, RNA-seq]
author: oxo-call-community
source_url: "http://ttic.uchicago.edu/~aakhan/BASIC/"
---

## Concepts

- **Tool Overview**: BASIC (v1.5.1) is a semi-de novo assembly method for assembling B-cell receptor (BCR) and T-cell receptor (TCR) genes from single-cell RNA-seq data.
- **Core Function**: Assembles complete BCR and TCR sequences from scRNA-seq reads.
- **Semi-de novo Assembly**: Combines reference-guided and de novo assembly strategies.
- **BCR/TCR Reconstruction**: Reconstructs full-length variable regions of immunoglobulin and T-cell receptor genes.
- **Single-cell Analysis**: Optimized for single-cell RNA-seq data with high dropout rates.
- **Input/Output**: Accepts FASTQ files; outputs assembled BCR/TCR sequences.
- **Installation**: `conda install -c bioconda basic`.

## Pitfalls

- **Data Quality**: Requires high-quality scRNA-seq data with sufficient coverage of V(D)J regions.
- **Reference Database**: Requires appropriate V(D)J reference sequences.
- **Assembly Completeness**: May not assemble full-length sequences for all cells.
- **Ambiguity Resolution**: May have difficulty resolving highly similar alleles.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Assemble BCR/TCR from single cell
**Args:** `basic -i reads.fastq -o assembled_sequences.fasta`
**Explanation:** Assembles BCR/TCR sequences from single-cell RNA-seq data.

### Paired-end reads
**Args:** `basic -i r1.fastq -i r2.fastq -o assembled_sequences.fasta`
**Explanation:** Processes paired-end scRNA-seq reads for assembly.

### Specify reference database
**Args:** `basic -i reads.fastq -d vdj_reference/ -o assembled_sequences.fasta`
**Explanation:** Uses custom V(D)J reference database for assembly.

### Output in IMGT format
**Args:** `basic -i reads.fastq -o assembled_sequences.fasta --imgt`
**Explanation:** Outputs sequences in IMGT standardized format.

### Quality filtering
**Args:** `basic -i reads.fastq -q 20 -o assembled_sequences.fasta`
**Explanation:** Filters reads by quality score before assembly.

### Batch processing
**Args:** `basic -i samples.txt -o results/`
**Explanation:** Processes multiple samples in batch mode.

### Display help
**Args:** `basic --help`
**Explanation:** Shows all available command-line options and usage information.