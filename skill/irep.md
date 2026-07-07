---
name: irep
category: metagenomics
description: Calculate iRep replication rates from metagenome sequencing
tags: [irep, metagenomics, replication, microbial-ecology]
author: oxo-call-community
source_url: "https://github.com/christophertbrown/iRep"
---

## Concepts

- **Tool Overview**: iRep is a bioinformatics tool for calculating microbial replication rates from metagenomic sequencing data. It estimates the replication index (iRep) by analyzing read coverage patterns across bacterial genomes.
- **Core Function**: Uses read depth variation along genomes to determine replication status. Regions near the origin of replication show higher coverage than regions near the terminus.
- **Input/Output**: Accepts sorted BAM files aligned to reference genomes. Outputs replication rates and coverage profiles.
- **Installation**: `conda install -c bioconda irep` or `pip install irep`
- **Reference Genomes**: Requires high-quality reference genomes or MAGs (Metagenome-Assembled Genomes) for accurate replication rate estimation.
- **Applications**: Used in microbial ecology to study population dynamics, growth rates, and responses to environmental changes.

## Pitfalls

- **Reference Quality**: Poorly assembled or incomplete reference genomes can lead to inaccurate replication rate estimates.
- **Coverage Depth**: Insufficient sequencing coverage (<10x) may result in unreliable iRep values.
- **Contamination**: Presence of closely related species can confound coverage-based replication rate calculations.
- **GC Bias**: Uneven GC content across the genome can affect read mapping and coverage estimation.
- **Plasmid Effects**: Plasmids may have different copy numbers than the chromosome, affecting overall coverage patterns.
- **Multi-Mapping Reads**: Reads mapping to multiple locations should be properly handled to avoid coverage inflation.

## Examples

### Basic iRep calculation
**Args:** `irep -f contigs.fasta -m mapped_reads.bam -o output_dir/`
**Explanation:** Calculates replication rates for all contigs in the input fasta file using mapped reads from the BAM file.

### Specify minimum coverage
**Args:** `irep -f genome.fasta -m alignments.bam -o results/ -c 20`
**Explanation:** Sets minimum coverage threshold to 20x, filtering out low-coverage regions that could affect accuracy.

### Multiple samples comparison
**Args:** `irep -f reference.fasta -m sample1.bam sample2.bam sample3.bam -o comparison_results/`
**Explanation:** Processes multiple BAM files simultaneously to compare replication rates across different samples.

### Output detailed statistics
**Args:** `irep -f assembly.fasta -m reads.bam -o output/ -v`
**Explanation:** Runs in verbose mode, providing detailed statistics about coverage, GC content, and replication rate calculations.

### Filter by contig length
**Args:** `irep -f scaffolds.fasta -m aligned.bam -o results/ -l 5000`
**Explanation:** Only processes contigs longer than 5000 bp, excluding small contigs that may introduce noise.

### Generate coverage plots
**Args:** `irep -f genome.fasta -m mapping.bam -o output/ -p`
**Explanation:** Generates visual coverage plots showing the coverage distribution along each contig.