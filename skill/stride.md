---
name: stride
category: assembly
description: The StriDe Assembler integrates string and de Bruijn graph by decomposing reads within error-prone regions, while extending paired-end reads into long reads for assembly through repetitive regions.
tags: [stride, genome-assembly, de-bruijn-graph, paired-end]
author: oxo-call-community
source_url: "https://github.com/ythuang0522/StriDe"
---

## Concepts

- **Tool Overview**: stride (v1.0) is a hybrid genome assembler that combines string graph and de Bruijn graph approaches for improved assembly through repetitive regions.
- **Core Function**: Integrates string graph and de Bruijn graph assembly strategies to handle both error-prone and repetitive regions.
- **Algorithm**: Decomposes reads within error-prone regions while extending paired-end reads into long reads for assembly through repetitive regions.
- **Input/Output**: Input: Paired-end sequencing reads (FASTQ); Output: Assembled contigs/scaffolds.
- **Applications**: Genome assembly, metagenomics assembly, handling complex genomic regions.
- **Installation**: `conda install -c bioconda stride` or download from GitHub.

## Pitfalls

- **Read Quality**: Low-quality reads affect assembly accuracy.
- **Repetitive Regions**: Highly repetitive genomes are challenging.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Assembly of large genomes can be slow.
- **Parameter Tuning**: Incorrect parameters affect assembly quality.
- **Paired-end Orientation**: Requires correct library orientation.

## Examples

### Display help
**Args:** `stride --help`
**Explanation:** Shows available options and usage information.

### Basic genome assembly
**Args:** `stride -i reads.fastq -o results/`
**Explanation:** Assemble genome from sequencing reads.

### With paired-end reads
**Args:** `stride -1 read1.fastq -2 read2.fastq -o results/`
**Explanation:** Use paired-end reads for assembly.

### Verbose mode
**Args:** `stride -i reads.fastq -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output scaffolds
**Args:** `stride -i reads.fastq -o results/ --scaffold`
**Explanation:** Generate scaffold-level assembly.

### Custom k-mer size
**Args:** `stride -i reads.fastq -o results/ -k 31`
**Explanation:** Use k-mer size of 31 for de Bruijn graph.

### Batch processing
**Args:** `stride -i batch/ -o results/`
**Explanation:** Process multiple sequencing samples together.

### Filter by coverage
**Args:** `stride -i reads.fastq -o results/ -m 5`
**Explanation:** Minimum coverage threshold of 5x.

### Generate report
**Args:** `stride -i reads.fastq -o results/ --report`
**Explanation:** Generate comprehensive HTML report.
