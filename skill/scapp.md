---
name: scapp
category: assembly
description: SCAPP - Plasmid assembly in metagenomes
tags: ["scapp", "assembly", "plasmid", "metagenomics"]
author: oxo-call-community
source_url: "https://github.com/Shamir-Lab/SCAPP"
---

## Concepts

- **Tool Overview**: SCAPP (v0.1.4) is a tool for plasmid assembly from metagenomic sequencing data.
- **Core Function**: Identifies and assembles plasmid sequences from complex metagenomic samples.
- **Algorithm**: Uses coverage-based binning and assembly to reconstruct plasmid sequences.
- **Input/Output**: Accepts sequencing reads and produces plasmid contigs.
- **Metagenomic Focus**: Specifically designed for metagenomic data analysis.
- **Applications**: Plasmid discovery, antibiotic resistance gene detection, and mobile genetic element analysis.

## Pitfalls

- **Complex Samples**: May struggle with highly complex metagenomes.
- **Read Depth**: Requires sufficient coverage for plasmid detection.
- **Reference Dependence**: May need reference plasmids for comparison.
- **Computational Resources**: High memory and CPU requirements.
- **Contamination**: May include host DNA in plasmid assemblies.
- **Parameter Tuning**: Requires careful adjustment for optimal results.

## Examples

### Basic plasmid assembly
**Args:** `scapp -i reads.fastq -o plasmids.fasta`
**Explanation:** `-i` input reads; `-o` output plasmid sequences.

### With reference plasmids
**Args:** `scapp -i reads.fastq -r reference_plasmids.fasta -o plasmids.fasta`
**Explanation:** `-r` reference plasmids for improved assembly.

### Paired-end reads
**Args:** `scapp -1 reads_1.fastq -2 reads_2.fastq -o plasmids.fasta`
**Explanation:** `-1/-2` paired-end read files.

### Minimum coverage
**Args:** `scapp -i reads.fastq -c 10 -o plasmids.fasta`
**Explanation:** `-c 10` minimum coverage threshold.

### Verbose logging
**Args:** `scapp -i reads.fastq -v -o plasmids.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Output statistics
**Args:** `scapp -i reads.fastq -s stats.txt -o plasmids.fasta`
**Explanation:** `-s` outputs assembly statistics.

### Assembly graph
**Args:** `scapp -i reads.fastq -g assembly_graph.gfa -o plasmids.fasta`
**Explanation:** `-g` outputs assembly graph in GFA format.