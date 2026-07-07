---
name: nanomonsv
category: variant-calling
description: nanomonsv - Structural variant detection from Nanopore long-read sequencing
tags: [nanomonsv, variant-calling, structural-variation, nanopore, sv, long-reads]
author: oxo-call-community
source_url: "https://github.com/friend1ws/nanomonsv"
---

## Concepts

- **Tool Overview**: nanomonsv v0.9.0 is a Python-based tool for detecting structural variations (SVs) from Oxford Nanopore long-read sequencing data. It handles deletions, insertions, inversions, and translocations.
- **Core Function**: Identifies structural variants by analyzing alignment patterns, read pair orientation, and split-read signatures in Nanopore alignments.
- **Algorithm**: Uses multiple SV detection strategies including read depth analysis, split read mapping, and discordant read pair detection optimized for long reads.
- **Input Format**: Requires sorted and indexed BAM files from Nanopore alignments and a reference genome in FASTA format.
- **Output**: Produces VCF files with structural variant calls including coordinates, SV type, and supporting evidence.
- **Use Case**: Detecting large structural variations in genomes, cancer genomics, population genetics, and de novo assembly validation.

## Pitfalls

- **Alignment Quality**: SV detection accuracy depends heavily on alignment quality. Use long-read optimized aligners.
- **Read Coverage**: Low coverage regions produce unreliable SV calls. Aim for sufficient coverage across genome.
- **Complex Regions**: Repetitive regions and segmental duplications may produce false positive calls.
- **SV Size**: Detection sensitivity varies by SV size. Very small or very large SVs may be missed.
- **False Positives**: Stringent filtering is essential. Use multiple evidence types to validate calls.
- **Reference Bias**: SV calls may be biased towards the reference genome. Consider de novo assembly for complex regions.

## Examples

### Basic SV detection
**Args:** `-b aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Detects structural variants from Nanopore alignments.

### Include breakpoints
**Args:** `-b aligned.bam -r ref.fa -o variants.vcf --breakpoint`
**Explanation:** Outputs detailed breakpoint information for each SV.

### Set minimum SV size
**Args:** `-b aligned.bam -r ref.fa -o variants.vcf -s 100`
**Explanation:** Only reports SVs larger than 100bp.

### Use multiple threads
**Args:** `-b aligned.bam -r ref.fa -o variants.vcf -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Display help
**Args:** `nanomonsv --help`
**Explanation:** Shows all available options for structural variant detection.
