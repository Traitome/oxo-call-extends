---
name: hairsplitter
category: bioinformatics
description: HairSplitter recovers collapsed haplotypes from draft assemblies using long read sequencing data.
tags: [hairsplitter, haplotype, assembly, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/RolandFaure/HairSplitter"
---

## Concepts

- **Haplotype Recovery**: HairSplitter identifies and reconstructs collapsed haplotypes.

- **Long Read Analysis**: Uses long sequencing reads to resolve haplotypes.

- **Assembly Improvement**: Enhances draft assemblies by resolving haplotype diversity.

- **Phased Variants**: Identifies phased genetic variants across haplotypes.

- **Structural Variation**: Detects structural variants between haplotypes.

- **Diploid Genome Analysis**: Analyzes diploid genome structures.

## Pitfalls

- **Read Quality**: Low-quality reads may affect haplotype resolution.

- **Assembly Quality**: Results depend on initial assembly quality.

- **Computational Resources**: May require significant computational resources.

- **Memory Usage**: Large genomes may require significant memory.

- **Parameter Tuning**: May require careful parameter optimization.

## Examples

### Recover haplotypes
**Args:** `hairsplitter -a assembly.fasta -r reads.fastq -o haplotypes/`
**Explanation:** Recovers collapsed haplotypes from assembly and reads.

### Paired-end reads
**Args:** `hairsplitter -a assembly.fasta -1 reads_1.fastq -2 reads_2.fastq -o haplotypes/`
**Explanation:** Processes paired-end sequencing data.

### With reference
**Args:** `hairsplitter -a assembly.fasta -r reads.fastq -ref reference.fasta -o haplotypes/`
**Explanation:** Uses reference genome for improved phasing.

### Quality filtering
**Args:** `hairsplitter -a assembly.fasta -r reads.fastq -q 20 -o haplotypes/`
**Explanation:** Filters reads by quality score.

### Batch processing
**Args:** `for f in *.fasta; do hairsplitter -a $f -r reads.fastq -o ${f%.fasta}_haplotypes/; done`
**Explanation:** Processes multiple assembly files.

### Generate statistics
**Args:** `hairsplitter -a assembly.fasta -r reads.fastq -stats -o stats.txt`
**Explanation:** Generates haplotype recovery statistics.

### Help command
**Args:** `hairsplitter --help`
**Explanation:** Shows available options and usage information.