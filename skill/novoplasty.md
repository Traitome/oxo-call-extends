---
name: novoplasty
category: assembly
description: NOVOPlasty is a de novo assembler specialized for organelle genomes and heteroplasmy calling.
tags: [novoplasty, assembly, organelle, mitochondria, chloroplast]
author: oxo-call-community
source_url: "https://github.com/ndierckx/NOVOPlasty"
---

## Concepts

- **Tool Overview**: NOVOPlasty assembles organelle genomes from sequencing data.
- **Core Function**: Performs de novo assembly of circular genomes.
- **Algorithm**: Uses seed-and-extend approach for circular genome assembly.
- **Input Format**: Accepts FASTQ reads and optional seed sequence.
- **Output**: Produces complete organelle genome sequences.
- **Use Case**: Mitochondrial assembly, chloroplast assembly, and heteroplasmy detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Circular Genome**: Designed specifically for circular genomes.
- **Seed Sequence**: Requires appropriate seed sequence.
- **Memory Usage**: Large datasets require memory.
- **Heteroplasmy**: May miss low-frequency variants.
- **Validation**: Results should be validated for circularity.

## Examples

### Display help
**Args:** `novoplasty --help`
**Explanation:** Shows available options and usage instructions.

### Assemble organelle
**Args:** `novoplasty -i reads.fastq -o genome.fasta`
**Explanation:** Assembles organelle genome from reads.

### With seed sequence
**Args:** `novoplasty -i reads.fastq -s seed.fasta -o genome.fasta`
**Explanation:** Uses seed sequence for assembly.

### Mitochondrial mode
**Args:** `novoplasty -i reads.fastq -m -o mt_genome.fasta`
**Explanation:** Optimizes for mitochondrial assembly.

### Chloroplast mode
**Args:** `novoplasty -i reads.fastq -c -o cp_genome.fasta`
**Explanation:** Optimizes for chloroplast assembly.

### Heteroplasmy detection
**Args:** `novoplasty -i reads.fastq -o genome.fasta --heteroplasmy`
**Explanation:** Detects heteroplasmic variants.

### Verbose mode
**Args:** `novoplasty -i reads.fastq -v -o genome.fasta`
**Explanation:** Runs with verbose output.