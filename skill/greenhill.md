---
name: greenhill
category: bioinformatics
description: GreenHill performs de novo chromosomal-level scaffolding and phasing using Hi-C data for genome assembly.
tags: [greenhill, genome-assembly, Hi-C, scaffolding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ShunOuchi/GreenHill"
---

## Concepts

- **Hi-C Scaffolding**: GreenHill uses Hi-C data to scaffold contigs into chromosome-scale assemblies.

- **Chromosome-Level Assembly**: Generates chromosome-scale assemblies from fragmented contigs.

- **Phasing**: Performs haplotype phasing using Hi-C interaction data.

- **De Novo Assembly**: Supports de novo genome assembly from raw sequencing data.

- **Integration**: Integrates with various assemblers and scaffolders.

- **Quality Assessment**: Provides metrics for evaluating assembly quality and contiguity.

## Pitfalls

- **Hi-C Quality**: Results depend on the quality of Hi-C data. Poor Hi-C data will produce poor scaffolds.

- **Contig Quality**: Low-quality contigs will affect scaffolding accuracy.

- **Computational Resources**: Processing large genomes with Hi-C data may require significant memory.

- **Parameter Tuning**: Adjust parameters based on genome size and complexity.

- **Visualization**: Complex assemblies may require visualization tools for validation.

## Examples

### Basic scaffolding
**Args:** `greenhill scaffold -c contigs.fasta -h hic_data.bam -o scaffolds.fasta`
**Explanation:** Scaffolds contigs using Hi-C data.

### Perform phasing
**Args:** `greenhill phase -c contigs.fasta -h hic_data.bam -o phased.fasta`
**Explanation:** Phases haplotypes using Hi-C interaction data.

### De novo assembly
**Args:** `greenhill assemble -i reads.fastq -o assembly.fasta`
**Explanation:** Performs de novo genome assembly from sequencing reads.

### Specify chromosome number
**Args:** `greenhill scaffold -c contigs.fasta -h hic_data.bam -n 24 -o scaffolds.fasta`
**Explanation:** Specifies expected number of chromosomes for scaffolding.

### Generate statistics
**Args:** `greenhill stats -i scaffolds.fasta -o stats.txt`
**Explanation:** Generates assembly statistics including N50 and contiguity metrics.

### Batch processing
**Args:** `greenhill batch -d samples/ -o results/`
**Explanation:** Processes multiple samples in a directory.

### Visualize Hi-C interactions
**Args:** `greenhill visualize -h hic_data.bam -o heatmap.png`
**Explanation:** Creates a Hi-C interaction heatmap.