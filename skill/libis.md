---
name: libis
category: methylation
description: LiBis - Low-input Bisulfite sequencing alignment library
tags: [libis, methylation, bisulfite-seq, alignment, DNA-methylation]
author: oxo-call-community
source_url: "https://github.com/Dangertrip/LiBis"
---

## Concepts

- **Bisulfite Sequencing**: Analysis of bisulfite-treated DNA
- **Low-input**: Optimized for low-input samples
- **Methylation Analysis**: Detection of DNA methylation patterns
- **Alignment**: Aligns bisulfite-converted reads
- **Cytosine Conversion**: Handles C-to-T conversion
- **Reference Mapping**: Maps reads to reference genome

## Pitfalls

- **Input Quality**: Poor quality reads affect mapping
- **Bisulfite Conversion**: Incomplete conversion affects results
- **Strand Bias**: Strand-specific biases may occur
- **Memory Usage**: Requires significant memory for large datasets
- **Computational Resources**: Alignment is computationally intensive
- **Reference Genome**: Requires appropriate reference genome

## Examples

### Align bisulfite reads
**Args:** `libis align -i reads.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Aligns bisulfite-treated reads to reference.

### Single-end mode
**Args:** `libis align -f reads.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Processes single-end bisulfite reads.

### Paired-end mode
**Args:** `libis align -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o aligned.bam`
**Explanation:** Processes paired-end bisulfite reads.

### Set mismatch rate
**Args:** `libis align -i reads.fastq -r reference.fasta -m 0.05 -o aligned.bam`
**Explanation:** Sets maximum mismatch rate.

### Output statistics
**Args:** `libis stats -i aligned.bam`
**Explanation:** Shows alignment statistics.

### Sort BAM
**Args:** `libis sort -i aligned.bam -o sorted.bam`
**Explanation:** Sorts aligned BAM file.