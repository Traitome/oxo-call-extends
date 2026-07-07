---
name: sspace_basic
category: assembly
description: Scaffolding Pre-Assemblies After Contig Extension (SSPACE).
tags: [sspace_basic, scaffolding, assembly, genome]
author: oxo-call-community
source_url: "https://github.com/nsoranzo/sspace_basic"
---

## Concepts

- **Tool Overview**: sspace_basic (v2.1.1) is a genome scaffolding tool that extends contigs into larger scaffolds using paired-end read information.
- **Core Function**: Links contigs together based on paired-end read mappings to create longer scaffolds.
- **Algorithm**: Uses paired-end read pairs to determine contig order and orientation, filling gaps with Ns.
- **Input/Output**: Input: Assembled contigs (FASTA) and paired-end reads (FASTQ); Output: Scaffolded sequences with gap information.
- **Gap Handling**: Estimates gap sizes between contigs based on insert size distribution.
- **Installation**: `conda install -c bioconda sspace_basic` or download from GitHub.

## Pitfalls

- **Insert Size**: Incorrect insert size estimation affects scaffolding accuracy.
- **Read Quality**: Low-quality reads lead to incorrect contig connections.
- **Repeat Regions**: Repetitive sequences can cause mis-scaffolding.
- **Contig Quality**: Poor quality contigs affect scaffold reliability.
- **Paired-End Orientation**: Requires correct orientation (FR, RF, etc.) for proper scaffolding.
- **Memory Requirements**: Large datasets may require significant memory.

## Examples

### Display help
**Args:** `sspace_basic -h`
**Explanation:** Shows available options and usage information.

### Basic scaffolding
**Args:** `sspace_basic -l library.txt -s contigs.fasta -o scaffolds/`
**Explanation:** Scaffold contigs using paired-end library information.

### With multiple libraries
**Args:** `sspace_basic -l lib1.txt -l lib2.txt -s contigs.fasta -o scaffolds/`
**Explanation:** Use multiple paired-end libraries for scaffolding.

### Specify insert size
**Args:** `sspace_basic -l library.txt -s contigs.fasta -o scaffolds/ -i 300`
**Explanation:** Specify expected insert size for paired-end library.

### Minimum overlap
**Args:** `sspace_basic -l library.txt -s contigs.fasta -o scaffolds/ -m 50`
**Explanation:** Set minimum overlap between contigs.

### Gap size estimation
**Args:** `sspace_basic -l library.txt -s contigs.fasta -o scaffolds/ -g 100`
**Explanation:** Set gap size estimation parameter.

### Verbose output
**Args:** `sspace_basic -l library.txt -s contigs.fasta -o scaffolds/ -v`
**Explanation:** Run with verbose output for debugging.

### Quality filtering
**Args:** `sspace_basic -l library.txt -s contigs.fasta -o scaffolds/ -q 20`
**Explanation:** Apply quality filter to reads before scaffolding.
