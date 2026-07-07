---
name: sparseassembler
category: assembly
description: SparseAssembler - Sparse k-mer graph based genome assembler
tags: [sparseassembler, assembly, k-mer-graph, memory-efficient, genome]
author: oxo-call-community
source_url: "https://github.com/yechengxi/SparseAssembler"
---

## Concepts

- **Tool Overview**: sparseassembler (v20160205) - A memory-efficient genome assembler
- **Core Function**: Assembles genomes using sparse k-mer graphs
- **Input/Output**: Accepts reads; outputs assembled contigs
- **Algorithm**: Sparse k-mer graph based assembly
- **Installation**: `conda install -c bioconda sparseassembler`
- **Key Features**: Memory-efficient, k-mer graph, genome assembly

## Pitfalls

- **Input Requirements**: Requires properly formatted reads
- **K-mer Size**: K-mer size affects assembly quality
- **Memory Usage**: Large genomes require significant memory
- **Read Coverage**: Coverage affects assembly completeness
- **Output Format**: Output format depends on configuration
- **Assembly Quality**: Assembly quality depends on input reads

## Examples

### Display help
**Args:** `SparseAssembler --help`
**Explanation:** Shows available options and usage information.

### Basic assembly
**Args:** `SparseAssembler -g 31 -f reads.fastq -o assembly`
**Explanation:** Assemble genome from reads.

### With k-mer size
**Args:** `SparseAssembler -g 31 -f reads.fastq -o assembly`
**Explanation:** Set k-mer size for assembly.

### With coverage cutoff
**Args:** `SparseAssembler -g 31 -c 5 -f reads.fastq -o assembly`
**Explanation:** Set coverage cutoff.

### With paired-end reads
**Args:** `SparseAssembler -g 31 -f reads_1.fastq reads_2.fastq -o assembly`
**Explanation:** Assemble from paired-end reads.

### Output contigs
**Args:** `SparseAssembler -g 31 -f reads.fastq -o assembly --contigs`
**Explanation:** Output assembled contigs.

### Output statistics
**Args:** `SparseAssembler -g 31 -f reads.fastq -o assembly --stats`
**Explanation:** Output assembly statistics.

### Generate report
**Args:** `SparseAssembler -g 31 -f reads.fastq -o assembly --report`
**Explanation:** Generate assembly report.

### With threads
**Args:** `SparseAssembler -g 31 -f reads.fastq -o assembly -p 8`
**Explanation:** Use multiple threads for assembly.