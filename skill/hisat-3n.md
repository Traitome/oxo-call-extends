---
name: hisat-3n
category: alignment
description: HISAT-3N aligns nucleotide conversion sequencing reads (bisulfite-seq, SLAM-seq, etc.) using hierarchical indexing.
tags: [hisat-3n, alignment, bisulfite-seq, SLAM-seq, nucleotide-conversion]
author: oxo-call-community
source_url: "https://daehwankimlab.github.io/hisat2/hisat-3n/"
---

## Concepts

- **Nucleotide Conversion Alignment**: HISAT-3N aligns reads from nucleotide conversion sequencing technologies.

- **Hierarchical Indexing**: Uses hierarchical index and repeat index algorithms for fast alignment.

- **Standard Mode**: Aligns reads with standard-3N index only, fast and memory-efficient.

- **Repeat Mode**: Uses both standard-3N and repeat-3N indexes for higher accuracy.

- **Base Conversion**: Supports various base conversions (C→T, T→C, A→G, G→A, etc.).

- **Strand-specific Support**: Supports both strand-specific and non-strand reads.

## Pitfalls

- **Memory Requirements**: Repeat index building requires 256GB RAM for human genome.

- **Index Building Time**: Building indexes can be time-consuming for large genomes.

- **Base Conversion Spec**: Must specify `--base-change` parameter correctly.

- **Input Format**: Requires properly formatted FASTQ input files.

- **Reference Genome**: Must use appropriate reference genome matching the sequencing data.

## Examples

### Build standard HISAT-3N index for bisulfite-seq (C→T conversion)
**Args:** `hisat-3n-build --base-change C,T genome.fa genome_index`
**Explanation:** Builds a standard 3N-index for bisulfite sequencing data.

### Build repeat HISAT-3N index for SLAM-seq (T→C conversion)
**Args:** `hisat-3n-build --base-change T,C --repeat-index genome.fa genome_index`
**Explanation:** Builds a repeat 3N-index for SLAM sequencing data.

### Align bisulfite-seq reads in standard mode
**Args:** `hisat-3n --base-change C,T -x genome_index -1 reads_1.fastq -2 reads_2.fastq -S alignments.sam`
**Explanation:** Aligns paired-end bisulfite-seq reads in standard mode.

### Align SLAM-seq reads in repeat mode
**Args:** `hisat-3n --base-change T,C --repeat-index -x genome_index -U reads.fastq -S alignments.sam`
**Explanation:** Aligns single-end SLAM-seq reads using repeat mode for higher accuracy.

### With SNP-aware indexing
**Args:** `hisat-3n-build --base-change C,T --snp genome.snp genome.fa genome_index`
**Explanation:** Builds index integrated with SNP information for improved accuracy.

### With multiple threads
**Args:** `hisat-3n --base-change C,T -x genome_index -1 reads_1.fastq -2 reads_2.fastq -p 8 -S alignments.sam`
**Explanation:** Uses 8 threads for faster alignment.

### Help command
**Args:** `hisat-3n --help`
**Explanation:** Shows available options and usage information.