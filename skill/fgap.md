---
name: fgap
category: utility
description: "FGAP: an automated gap closing tool"
tags: [fgap, utility, genome-assembly, gap-closing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/pirovc/fgap"
---

## Concepts

- **Tool Overview**: FGAP is an automated tool for closing gaps in genome assemblies by identifying and filling unresolved regions.
- **Core Function**: Closes gaps in genome assemblies using various sequencing data.
- **Input/Output**: Input: Genome assembly with gaps, supporting reads. Output: Improved assembly.
- **Algorithm**: Uses read alignment and assembly for gap closure.
- **Key Features**: Automated gap closing, multiple data support, scaffolding improvement, iterative processing, comprehensive reporting.
- **Installation**: `conda install -c bioconda fgap`

## Pitfalls

- **Gap Quality**: Results depend on initial assembly quality.
- **Read Coverage**: Requires sufficient read coverage for gap regions.
- **Assembly Complexity**: Complex gaps may be difficult to close.
- **Data Requirements**: May require multiple read types.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic gap closing
**Args:** `fgap -i assembly.fasta -r reads.fastq -o closed_assembly.fasta`
**Explanation:** Closes gaps using sequencing reads.

### With paired-end reads
**Args:** `fgap -i assembly.fasta -1 reads_1.fastq -2 reads_2.fastq -o results/`
**Explanation:** Uses paired-end data for gap closure.

### Specify gap size
**Args:** `fgap -i assembly.fasta -r reads.fastq -o results/ -m 1000`
**Explanation:** Targets gaps up to 1000bp.

### Iterative closing
**Args:** `fgap -i assembly.fasta -r reads.fastq -o results/ --iterations 3`
**Explanation:** Performs 3 iterations of gap closing.

### Report output
**Args:** `fgap -i assembly.fasta -r reads.fastq -o results/ --report`
**Explanation:** Generates detailed gap closure report.