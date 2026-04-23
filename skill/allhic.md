---
name: allhic
category: assembly
description: Genome scaffolding based on Hi-C data for heterozygous and polyploid genomes
tags: [hic, scaffolding, polyploid, heterozygous, phasing, chromosome]
author: oxo-call-community
source_url: "https://github.com/tanghaibao/allhic"
---

## Concepts

- **Tool Overview**: ALLHiC is a Hi-C scaffolding algorithm designed for chromosome-level assembly of heterozygous diploid and polyploid genomes.
- **Core Function**: Uses Hi-C contact maps to scaffold contigs into chromosome-scale assemblies, with special handling for heterozygous and polyploid genomes.
- **Pipeline Steps**: prune → partition → rescue → optimize → build - five-step workflow for Hi-C based scaffolding.
- **Input/Output**: Input: Hi-C BAM file, contig FASTA, allele table. Output: Chromosome-scale scaffolded assemblies.
- **Installation**: Install via bioconda: `conda install -c bioconda allhic`

## Pitfalls

- **Allele Table Required**: For polyploid/heterozygous genomes, allele table is critical for proper haplotype separation.
- **Pruning Step**: The pruning step is key to ALLHiC - removes ambiguous Hi-C links from collapsed regions.
- **Chromosome Count**: Must specify expected chromosome number for partitioning step.
- **Memory Usage**: Large genomes with high heterozygosity require substantial memory for optimization.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available subcommands and options for ALLHiC.

### Prune Hi-C links
**Args:** `prune -b hic.bam -r reference.fa -a allele.table`
**Explanation:** Removes ambiguous Hi-C links from collapsed/heterozygous regions.

### Partition contigs into groups
**Args:** `partition -b hic.bam -r contigs.fa -k 12`
**Explanation:** Groups contigs into 12 chromosome clusters based on Hi-C contacts.

### Rescue unplaced contigs
**Args:** `rescue -b hic.bam -r contigs.fa -k 12`
**Explanation:** Assigns unplaced contigs to chromosome groups using Hi-C signal.

### Optimize contig ordering
**Args:** `optimize -b hic.bam -r contigs.fa -k 12`
**Explanation:** Optimizes contig order and orientation within each chromosome group.

### Build final scaffolds
**Args:** `build -b hic.bam -r contigs.fa -k 12`
**Explanation:** Constructs final chromosome-scale scaffolded assembly.

### Full pipeline for diploid
**Args:** `prune -b hic.bam -r asm.fa && allhic partition -b hic.bam -r asm.fa -k 12 && allhic optimize -b hic.bam -r asm.fa -k 12 && allhic build -b hic.bam -r asm.fa -k 12`
**Explanation:** Runs complete ALLHiC pipeline for a 12-chromosome diploid genome.
