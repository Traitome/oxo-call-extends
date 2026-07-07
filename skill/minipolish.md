---
name: minipolish
category: utility
description: A tool for Racon polishing miniasm assemblies.
tags: [minipolish, utility, assembly]
author: oxo-call-community
source_url: "https://github.com/rrwick/Minipolish"
---

## Concepts

- **Tool Overview**: MiniPolish v0.2.1 polishes miniasm assemblies using Racon.
- **Core Function**: Improves assembly quality through polishing.
- **Assembly Polishing**: Refines sequence assemblies for accuracy.
- **Racon Integration**: Uses Racon for consensus calling.
- **Input/Output**: Accepts miniasm assemblies; outputs polished sequences.
- **Long-read Assembly**: Supports long-read assembly improvement.

## Pitfalls

- **miniasm Specific**: Designed for miniasm assemblies.
- **Computational Resources**: Polishing may require significant resources.
- **Memory Requirements**: Memory usage depends on assembly size.
- **Parameter Tuning**: May require parameter adjustment for optimal polishing.
- **Data Quality**: Results depend on input data quality.
- **Racon Dependency**: Requires Racon for polishing.

## Examples

### Polish assembly
**Args:** `minipolish assembly.gfa reads.fastq > polished.gfa`
**Explanation:** Polishes miniasm assembly with Racon.

### Multiple polishing rounds
**Args:** `minipolish -r 3 assembly.gfa reads.fastq > polished.gfa`
**Explanation:** Runs 3 rounds of polishing.

### With paired reads
**Args:** `minipolish assembly.gfa reads_1.fastq reads_2.fastq > polished.gfa`
**Explanation:** Uses paired-end reads for polishing.

### Batch processing
**Args:** `minipolish assembly.gfa fastq/*.fastq > polished.gfa`
**Explanation:** Processes multiple read files.

### Generate FASTA output
**Args:** `minipolish assembly.gfa reads.fastq | gfa2fasta > polished.fasta`
**Explanation:** Generates FASTA format output.