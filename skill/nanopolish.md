---
name: nanopolish
category: variant-calling
description: Nanopolish - Signal-level analysis for Oxford Nanopore sequencing data
tags: [nanopolish, variant-calling, nanopore, signal-level, methylation, eventalign]
author: oxo-call-community
source_url: "https://github.com/jts/nanopolish"
---

## Concepts

- **Tool Overview**: Nanopolish v0.14.0 is a tool for signal-level analysis of Oxford Nanopore sequencing data. It enables variant calling, methylation detection, and event alignment using raw signal data.
- **Core Function**: Analyzes raw electrical signal data to improve basecall accuracy, detect variants with high precision, and identify DNA/RNA modifications from Nanopore reads.
- **Algorithm**: Uses Hidden Markov Models to align raw signal events to reference sequences. Performs signal-level consensus calling for improved accuracy.
- **Input Format**: Requires FAST5 files containing raw signal data, basecalled FASTQ reads, and aligned BAM files. Indexing step required before analysis.
- **Output**: Produces VCF files for variant calls, TSV files for methylation calls, and eventalign output for downstream modification analysis.
- **Use Case**: High-precision variant calling, DNA methylation detection, improving consensus sequences, and signal-level analysis of Nanopore data.

## Pitfalls

- **FAST5 Requirements**: Requires access to raw FAST5 files. Basecalled-only data won't work for signal-level analysis.
- **Indexing Step**: Must run `nanopolish index` before other commands to map reads to FAST5 files.
- **Memory Usage**: Processing large datasets requires significant memory. Consider subsampling for very large files.
- **Alignment Quality**: Results depend heavily on alignment quality. Use long-read optimized aligners.
- **Computational Time**: Signal-level analysis is computationally intensive. Consider parallel processing.
- **Modified Bases**: Methylation detection requires specific basecalling models or additional processing.

## Examples

### Index reads
**Args:** `nanopolish index -d fast5_dir reads.fastq.gz`
**Explanation:** Indexes FAST5 files to map basecalled reads to their raw signal data.

### Call variants
**Args:** `nanopolish callvariants -r reference.fasta -b aligned.bam -g variants.vcf -o calls.vcf`
**Explanation:** Calls variants using signal-level data for improved accuracy.

### Detect methylation
**Args:** `nanopolish call-methylation -r reference.fasta -b aligned.bam -o methylation.tsv`
**Explanation:** Detects methylated bases from raw signal data.

### Event alignment
**Args:** `nanopolish eventalign -r reference.fasta -b aligned.bam -o events.tsv`
**Explanation:** Generates event-level alignments for downstream modification analysis.

### Consensus polishing
**Args:** `nanopolish variants --consensus polished.fasta -r reference.fasta -b aligned.bam`
**Explanation:** Generates polished consensus sequence from aligned reads.

### Display help
**Args:** `nanopolish --help`
**Explanation:** Shows all available commands and options.
