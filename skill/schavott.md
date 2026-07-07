---
name: schavott
category: assembly
description: Schavott - Real-time assembly and scaffolding of bacterial genomes using MinION sequencing
tags: ["schavott", "assembly", "MinION", "real-time"]
author: oxo-call-community
source_url: "http://github.com/emilhaegglund/schavott"
---

## Concepts

- **Tool Overview**: Schavott (v0.5.0) provides real-time assembly and scaffolding of bacterial genomes using MinION sequencing data.
- **Core Function**: Assembles bacterial genomes from real-time nanopore sequencing data.
- **Algorithm**: Uses streaming assembly approach for real-time processing.
- **Input/Output**: Accepts sequencing reads and produces genome assemblies.
- **Real-Time Processing**: Processes reads as they arrive from the sequencer.
- **Applications**: Rapid bacterial genome assembly, real-time sequencing analysis, and pathogen detection.

## Pitfalls

- **MinION Specific**: Designed specifically for Oxford Nanopore MinION data.
- **Real-Time Constraints**: Requires fast processing for real-time analysis.
- **Read Quality**: Results depend on read quality and accuracy.
- **Computational Resources**: May require significant compute resources.
- **Assembly Completeness**: May not produce complete assemblies for complex genomes.
- **Parameter Tuning**: Requires careful adjustment for optimal results.

## Examples

### Basic assembly
**Args:** `schavott -i reads.fastq -o assembly.fasta`
**Explanation:** `-i` input reads; `-o` output assembly.

### Real-time mode
**Args:** `schavott --stream -i /dev/stdin -o assembly.fasta`
**Explanation:** `--stream` enables real-time streaming mode.

### With reference
**Args:** `schavott -i reads.fastq -r reference.fasta -o assembly.fasta`
**Explanation:** `-r` reference genome for guided assembly.

### Scaffolding
**Args:** `schavott -i reads.fastq --scaffold -o scaffolds.fasta`
**Explanation:** `--scaffold` enables scaffolding of contigs.

### Verbose logging
**Args:** `schavott -i reads.fastq -v -o assembly.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Quality filtering
**Args:** `schavott -i reads.fastq -q 10 -o assembly.fasta`
**Explanation:** `-q 10` filters reads with quality below 10.

### Output statistics
**Args:** `schavott -i reads.fastq -s stats.txt -o assembly.fasta`
**Explanation:** `-s` outputs assembly statistics.