---
name: insurveyor
category: variant-calling
description: An insertion caller for Illumina paired-end whole-genome sequencing data that detects insertions using reference-guided assembly and de novo assembly approaches.
tags: [insurveyor, variant-calling, insertion-detection, WGS]
author: oxo-call-community
source_url: "https://github.com/kensung-lab/INSurVeyor"
---

## Concepts

- **Insertion Detection**: INSurVeyor detects insertions from paired-end WGS data using three distinct algorithms based on sequence similarity to reference.
- **Reference-guided Assembly**: When inserted sequence is similar to reference, uses reference-guided assembly to produce exact inserted sequence.
- **De novo Assembly**: When inserted sequence is novel, employs de novo assembly approach to reconstruct insertions.
- **Breakpoint Identification**: Identifies precise insertion breakpoints and characterizes insertion sequences.
- **Output Formats**: Generates VCF files with insertion calls and FASTA files with inserted sequences.

## Pitfalls

- **Read Quality**: Requires high-quality paired-end reads for accurate breakpoint identification.
- **Insertion Size**: Very large insertions may require additional computational resources.
- **Reference Similarity**: Performance varies based on similarity between inserted and reference sequences.
- **Complex Regions**: Repetitive regions and low-complexity sequences may affect accuracy.
- **Memory Requirements**: Large genomes or multiple samples may require significant memory.

## Examples

### Basic insertion calling
**Args:** `INSurVeyor -i input.bam -r reference.fasta -o output_prefix`
**Explanation:** Detects insertions from aligned reads using default parameters.

### With quality filtering
**Args:** `INSurVeyor -i input.bam -r reference.fasta -o output_prefix -q 30`
**Explanation:** Filters reads with mapping quality ≥ 30 before insertion detection.

### Specify minimum insertion size
**Args:** `INSurVeyor -i input.bam -r reference.fasta -o output_prefix -m 50`
**Explanation:** Only reports insertions longer than 50 base pairs.

### Enable de novo assembly mode
**Args:** `INSurVeyor -i input.bam -r reference.fasta -o output_prefix --denovo`
**Explanation:** Forces de novo assembly approach for all insertions.

### Output FASTA with inserted sequences
**Args:** `INSurVeyor -i input.bam -r reference.fasta -o output_prefix --fasta`
**Explanation:** Generates FASTA file containing all detected insertion sequences.

### Process multiple BAM files
**Args:** `INSurVeyor -i sample1.bam sample2.bam -r reference.fasta -o cohort_output`
**Explanation:** Processes multiple samples and generates combined results.