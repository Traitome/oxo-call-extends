---
name: savage
category: assembly
description: SAVAGE - Strain Aware VirAl GEnome assembly for reconstructing viral haplotypes
tags: ["savage", "assembly", "viral-genomics", "haplotypes"]
author: oxo-call-community
source_url: "https://github.com/HaploConduct/HaploConduct/tree/master/savage"
---

## Concepts

- **Tool Overview**: SAVAGE (v0.4.2) - Strain Aware VirAl GEnome assembly reconstructs individual viral haplotypes from mixed samples.
- **Core Function**: Identifies and assembles distinct viral strains present in a mixed population sample.
- **Algorithm**: Uses de Bruijn graph assembly with strain-aware partitioning to separate haplotypes.
- **Input/Output**: Accepts sequencing reads (FASTQ) and produces consensus sequences for each strain.
- **Haplotype Resolution**: Capable of resolving multiple strains even at high sequence similarity.
- **Applications**: Viral population analysis, quasispecies characterization, and outbreak investigation.

## Pitfalls

- **Strain Complexity**: Performance degrades with very high strain diversity.
- **Read Depth**: Requires sufficient coverage for reliable haplotype separation.
- **Computational Resources**: High memory and CPU requirements for complex samples.
- **Reference Bias**: May be influenced by reference genome choice if provided.
- **Assembly Quality**: Results depend on input read quality and error rates.
- **Parameter Sensitivity**: Requires careful tuning for optimal haplotype resolution.

## Examples

### Basic haplotype assembly
**Args:** `savage -i reads.fastq -o haplotypes.fasta`
**Explanation:** `-i` input FASTQ reads; `-o` output FASTA with haplotype sequences.

### With reference guidance
**Args:** `savage -i reads.fastq -r reference.fasta -o haplotypes.fasta`
**Explanation:** `-r` reference genome for guided assembly.

### Specify minimum frequency
**Args:** `savage -i reads.fastq -f 0.05 -o haplotypes.fasta`
**Explanation:** `-f 0.05` only reports haplotypes with frequency >= 5%.

### Quality filtering
**Args:** `savage -i reads.fastq -q 20 -o haplotypes.fasta`
**Explanation:** `-q 20` filters reads with quality below 20.

### Detailed output
**Args:** `savage -i reads.fastq -d -o ./output/`
**Explanation:** `-d` generates detailed output including intermediate files.

### Variant calling
**Args:** `savage -i reads.fastq --variants -o variants.vcf`
**Explanation:** `--variants` outputs VCF file with variant calls.

### Performance mode
**Args:** `savage -i reads.fastq -p -o haplotypes.fasta`
**Explanation:** `-p` enables performance mode for faster processing.