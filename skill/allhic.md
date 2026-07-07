---
name: allhic
category: assembly
description: Hi-C based genome scaffolding algorithm designed for chromosome-level assembly of heterozygous diploid and polyploid genomes
tags: [hic, scaffolding, polyploid, heterozygous, phasing, chromosome, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/tangerzhang/ALLHiC"
---

## Concepts

- **Tool Overview**: ALLHiC is a specialized Hi-C scaffolding algorithm designed for chromosome-level assembly of heterozygous diploid and polyploid genomes, addressing the challenge of distinguishing between inter-allelic and intra-haplotype Hi-C signals.
- **Core Function**: Uses Hi-C contact maps to scaffold contigs into chromosome-scale assemblies with special handling for heterozygous and polyploid genomes by removing ambiguous inter-allelic links.
- **Pipeline Steps**: prune → partition → rescue → optimize → build - five-step workflow specifically designed for polyploid Hi-C scaffolding.
- **Prune Step**: Removes inter-allelic Hi-C links and retains only the strongest signals between collapsed regions and phased contigs.
- **Partition Step**: Clusters contigs into chromosome groups based on Hi-C contacts.
- **Rescue Step**: Assigns unplaced contigs to chromosome groups using Hi-C signal density.
- **Optimize Step**: Uses genetic algorithm to optimize contig ordering and orientation within each group.
- **Build Step**: Constructs final chromosome-scale scaffolds.
- **Input/Output**: Input: Hi-C BAM file, contig FASTA, allele table. Output: Chromosome-scale scaffolded assemblies.
- **Installation**: Install via bioconda: `conda install -c bioconda allhic`
- **Citation**: Zhang X, Zhang S, Zhao Q, Ming R, Tang H (2019). Assembly of allele-aware, chromosomal scale autopolyploid genomes based on Hi-C data. Nature Plants 5(8):833-845.
- **License**: GPL-3.0

## Pitfalls

- **Allele Table Required**: For polyploid/heterozygous genomes, a properly formatted allele table is critical for proper haplotype separation.
- **Pruning Step**: The pruning step is key to ALLHiC - incorrect parameters can lead to either over-pruning (losing valid links) or under-pruning (retaining inter-allelic noise).
- **Chromosome Count**: Must specify expected chromosome number (-k parameter) for partitioning step.
- **Memory Usage**: Large genomes with high heterozygosity require substantial memory, especially during the optimization step.
- **Hi-C Quality**: Requires high-quality Hi-C data with good coverage and low dangling end rates.
- **Contig Quality**: Draft assembly should have decent N50 for effective scaffolding.

## Examples

### Display help information
**Args:** `allhic --help`
**Explanation:** Shows available subcommands and options for ALLHiC.

### Prune Hi-C links
**Args:** `allhic prune -b hic.bam -r reference.fa -a allele.table`
**Explanation:** Removes ambiguous inter-allelic Hi-C links to separate homologous chromosomes.

### Partition contigs into groups
**Args:** `allhic partition -b hic.bam -r contigs.fa -k 12`
**Explanation:** Groups contigs into 12 chromosome clusters based on Hi-C contacts.

### Rescue unplaced contigs
**Args:** `allhic rescue -b hic.bam -r contigs.fa -k 12`
**Explanation:** Assigns unplaced contigs to chromosome groups using Hi-C signal density.

### Optimize contig ordering
**Args:** `allhic optimize -b hic.bam -r contigs.fa -k 12`
**Explanation:** Optimizes contig order and orientation within each chromosome group using genetic algorithm.

### Build final scaffolds
**Args:** `allhic build -b hic.bam -r contigs.fa -k 12`
**Explanation:** Constructs final chromosome-scale scaffolded assembly.

### Full pipeline for diploid
**Args:** `allhic prune -b hic.bam -r asm.fa -a allele.table && allhic partition -b hic.bam -r asm.fa -k 12 && allhic rescue -b hic.bam -r asm.fa -k 12 && allhic optimize -b hic.bam -r asm.fa -k 12 && allhic build -b hic.bam -r asm.fa -k 12`
**Explanation:** Runs complete ALLHiC pipeline for a 12-chromosome diploid genome with allele table.

### Extract Hi-C contacts
**Args:** `allhic extract -b hic.bam -r contigs.fa --RE AAGCTT`
**Explanation:** Extracts Hi-C contacts using HindIII restriction enzyme sites.

### Prune with minimum fraction threshold
**Args:** `allhic prune -b hic.bam -r reference.fa -a allele.table --min_frac 0.1`
**Explanation:** Sets minimum fraction threshold for pruning (default 0.1).

### Partition with specific restriction enzyme
**Args:** `allhic partition -b hic.bam -r contigs.fa -k 8 -e AAGCTT`
**Explanation:** Partitions contigs into 8 groups using HindIII enzyme pattern.

### Optimize with more iterations
**Args:** `allhic optimize -b hic.bam -r contigs.fa -k 12 -m 50`
**Explanation:** Optimizes with maximum 50 iterations per group.
