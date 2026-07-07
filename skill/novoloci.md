---
name: novoloci
category: assembly
description: NOVOLoci is a haplotype-aware assembler for complex genomic regions and small genomes using ONT/HiFi reads.
tags: [novoloci, assembly, haplotype, long-reads]
author: oxo-call-community
source_url: "https://github.com/ndierckx/NOVOLoci"
---

## Concepts

- **Tool Overview**: NOVOLoci performs haplotype-aware assembly of complex regions and small genomes.
- **Core Function**: Assembles genomes with phased haplotype information.
- **Algorithm**: Uses long reads for accurate haplotype-resolved assembly.
- **Input Format**: Accepts FASTQ reads from ONT or HiFi sequencing.
- **Output**: Produces phased assemblies and haplotype sequences.
- **Use Case**: Complex region assembly, small genome assembly, and haplotype analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Quality**: Requires high-quality long reads.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Assembly can be computationally intensive.
- **Haplotype Resolution**: May not resolve all haplotypes.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `novoloci --help`
**Explanation:** Shows available options and usage instructions.

### Assemble genome
**Args:** `novoloci -i reads.fastq -o assembly/`
**Explanation:** Runs haplotype-aware assembly.

### With reference
**Args:** `novoloci -i reads.fastq -r reference.fasta -o assembly/`
**Explanation:** Uses reference-guided assembly.

### Phased output
**Args:** `novoloci -i reads.fastq -o assembly/ --phased`
**Explanation:** Outputs phased haplotype sequences.

### Threads
**Args:** `novoloci -i reads.fastq -t 8 -o assembly/`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum coverage
**Args:** `novoloci -i reads.fastq -c 10 -o assembly/`
**Explanation:** Sets minimum coverage threshold.

### Verbose mode
**Args:** `novoloci -i reads.fastq -v -o assembly/`
**Explanation:** Runs with verbose output.