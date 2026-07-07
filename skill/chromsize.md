---
name: chromsize
category: utility
description: Get chromosome sizes from genome files
tags: [chromsize, utility, genome, chromosome, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/alejandrogzi/chromsize"
---

## Concepts

- **Tool Overview**: chromsize extracts chromosome sizes from genome FASTA files or other genomic data formats.
- **Core Function**: Quickly retrieves chromosome length information for downstream bioinformatics analyses.
- **Features**: Supports multiple input formats, can output to various formats, and handles compressed files.
- **Input**: Genome FASTA file, BED file, or other genomic files.
- **Output**: Chromosome sizes in tab-delimited format or other formats.
- **Application**: Genomic analysis, genome browser configuration, and pipeline setup.
- **Installation**: Install via bioconda: `conda install -c bioconda chromsize`

## Pitfalls

- **Input Format**: Ensure correct input format is provided.
- **Compressed Files**: May require decompression for some formats.
- **Mixed Contigs**: May include non-chromosomal sequences if not filtered.
- **Header Parsing**: Relies on correct FASTA header parsing.
- **Large Files**: May require time for very large genomes.

## Examples

### Get chromosome sizes from FASTA
**Args:** `chromsize -i genome.fasta -o chrom_sizes.txt`
**Explanation:** Extracts chromosome sizes from genome FASTA file.

### Output to BED format
**Args:** `chromsize -i genome.fasta --bed -o chrom_sizes.bed`
**Explanation:** Outputs chromosome sizes in BED format.

### From BAM file
**Args:** `chromsize -i alignments.bam -o chrom_sizes.txt`
**Explanation:** Extracts chromosome information from BAM file header.

### Display help
**Args:** `chromsize --help`
**Explanation:** Shows all available options and usage information.