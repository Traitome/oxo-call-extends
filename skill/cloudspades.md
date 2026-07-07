---
name: cloudspades
category: assembly
description: SPAdes module for genome assembly from linked read technologies (10x, Tellseq, Haplotagging)
tags: [cloudspades, spades, genome-assembly, linked-reads, 10x-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ablab/spades/tree/cloudspades-ismb"
---

## Concepts

- **Tool Overview**: cloudSPAdes is a specialized module of the SPAdes assembler designed for genome assembly from linked read technologies such as 10x Genomics, Tellseq, and Haplotagging.
- **Core Function**: Assembles genomes from linked read sequencing data by leveraging the long-range information provided by barcode-linked reads.
- **Algorithm**: Uses barcode information to group reads originating from the same DNA molecule, enabling more accurate assembly of repetitive regions.
- **Input**: Linked read FASTQ files with barcode information (10x Genomics, Tellseq, or Haplotagging format).
- **Output**: Assembled contigs and scaffolds in FASTA format.
- **Application**: De novo genome assembly, especially for complex genomes with high repeat content.
- **Installation**: Install via bioconda: `conda install -c bioconda cloudspades`

## Pitfalls

- **Barcode Information**: Requires properly formatted barcode information in reads.
- **Data Quality**: Linked read data must have high quality barcodes for accurate grouping.
- **Computational Resources**: May require significant resources for large genomes.
- **Memory Usage**: May require significant memory for assembly.
- **Parameter Tuning**: May require adjustment of assembly parameters.

## Examples

### Assemble genome from 10x reads
**Args:** `cloudspades -1 read1.fastq -2 read2.fastq -o assembly/`
**Explanation:** Assembles genome from 10x Genomics linked reads.

### With barcode whitelist
**Args:** `cloudspades -1 read1.fastq -2 read2.fastq --whitelist barcodes.txt -o assembly/`
**Explanation:** Uses custom barcode whitelist for read grouping.

### With Tellseq data
**Args:** `cloudspades --tellseq -1 read1.fastq -2 read2.fastq -o assembly/`
**Explanation:** Processes Tellseq linked read data.

### Display help
**Args:** `cloudspades --help`
**Explanation:** Shows all available options and usage information.