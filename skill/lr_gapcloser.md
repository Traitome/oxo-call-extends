---
name: lr_gapcloser
category: assembly
description: Use long sequenced reads to close gaps in assemblies.
tags: [lr_gapcloser, assembly, gap-closing, long-reads]
author: oxo-call-community
source_url: "https://github.com/CAFS-bioinformatics/LR_Gapcloser"
---

## Concepts

- **Tool Overview**: lr_gapcloser v1.0 is a tool for closing gaps in genome assemblies using long sequencing reads from technologies like PacBio or Oxford Nanopore.
- **Core Function**: Uses long reads to fill gaps in draft assemblies by aligning reads to gap flanking regions and performing local assembly.
- **Gap Types**: Handles various gap types including sequencing gaps, repeat-induced gaps, and scaffolding gaps.
- **Input/Output**: Input: FASTA assembly with N-stretches representing gaps, long reads in FASTQ format; Output: Gap-closed assembly.
- **Installation**: `conda install -c bioconda lr_gapcloser`
- **Algorithm**: Combines read alignment, consensus calling, and local assembly to close gaps efficiently.

## Pitfalls

- **Read Quality**: Low-quality reads can introduce errors into the gap-closed sequence.
- **Gap Size**: Very large gaps (>10kb) may require more computational resources and may not close completely.
- **Repeat Regions**: Complex repeat regions can cause misalignment and incorrect gap closure.
- **Memory Requirements**: Processing large assemblies with many gaps may require substantial memory.
- **Reference Bias**: The tool may prefer certain sequences over others based on read coverage.
- **Assembly Quality**: Poor-quality input assemblies with misassemblies can lead to incorrect gap closure.

## Examples

### Close gaps
**Args:** `lr_gapcloser -i assembly.fasta -l long_reads.fastq -o closed_assembly.fasta`
**Explanation:** Closes gaps in assembly using long reads.

### Minimum length
**Args:** `lr_gapcloser -i assembly.fasta -l long_reads.fastq -o closed_assembly.fasta -m 1000`
**Explanation:** Sets minimum gap length to process (1000bp).

### Threads
**Args:** `lr_gapcloser -i assembly.fasta -l long_reads.fastq -o closed_assembly.fasta -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Output intermediate files
**Args:** `lr_gapcloser -i assembly.fasta -l long_reads.fastq -o closed_assembly.fasta -d intermediate/`
**Explanation:** Saves intermediate files to specified directory for debugging.

### Gap coverage threshold
**Args:** `lr_gapcloser -i assembly.fasta -l long_reads.fastq -o closed_assembly.fasta -c 5`
**Explanation:** Requires minimum 5x coverage to close a gap.

### Help documentation
**Args:** `lr_gapcloser --help`
**Explanation:** Displays all available options and parameters.