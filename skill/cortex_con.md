---
name: cortex_con
category: assembly
description: Cortex consensus genome assembler
tags: [cortex_con, genome-assembly, de-novo-assembly, graph-based-assembly]
author: oxo-call-community
source_url: "http://cortexassembler.sourceforge.net/index.html"
---

## Concepts

- **Tool Overview**: Cortex-var/Cortex-con is a graph-based genome assembler designed for consensus assembly and variant calling from sequencing data.
- **Core Function**: Performs de novo genome assembly using de Bruijn graph construction.
- **Algorithm**: Uses de Bruijn graph approach with colored de Bruijn graphs for population-scale analysis.
- **Input**: Sequencing reads (FASTQ), reference genome (optional).
- **Output**: Assembled contigs, consensus sequences, variant calls.
- **Application**: Genome assembly, variant detection, population genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cortex_con`

## Pitfalls

- **Memory Usage**: Large k-mer sizes require significant memory.
- **k-mer Selection**: Choosing appropriate k-mer size is critical.
- **Read Quality**: Requires high-quality reads for accurate assembly.
- **Complex Genomes**: Highly repetitive genomes may cause graph complexity.
- **Computational Resources**: Assembly of large genomes is computationally intensive.

## Examples

### Assemble reads
**Args:** `cortex_con -k 31 -s reads.fastq -o assembly.cortex`
**Explanation:** Assembles reads using k-mer size 31.

### Build consensus
**Args:** `cortex_con -k 31 -i assembly.cortex -c consensus.fasta`
**Explanation:** Generates consensus sequence from assembly graph.

### With paired reads
**Args:** `cortex_con -k 31 -1 reads_1.fastq -2 reads_2.fastq -o assembly.cortex`
**Explanation:** Assembles paired-end reads.

### Variant calling
**Args:** `cortex_con -k 31 -r reference.fasta -s reads.fastq -v variants.vcf`
**Explanation:** Calls variants against reference genome.

### Display help
**Args:** `cortex_con --help`
**Explanation:** Shows all available options and usage information.