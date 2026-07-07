---
name: saffrontree
category: phylogenetics
description: Reference-free rapid phylogenetic tree construction from raw read data
tags: ["saffrontree", "phylogenetics", "tree construction", "reference-free", "SNP"]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/saffrontree"
---

## Concepts

- **Tool Overview**: SaffronTree (v0.1.2) is a reference-free phylogenetic tree construction tool that builds trees directly from raw sequencing reads without requiring a reference genome.
- **Core Function**: Identifies SNPs from raw reads across multiple samples and constructs phylogenetic trees based on genetic distances.
- **Algorithm**: Uses k-mer counting and SNP calling from raw reads, implements distance-based tree construction methods (NJ, UPGMA).
- **Input Format**: Raw sequencing reads (FASTQ), sample metadata, optional reference (FASTA).
- **Output Format**: Phylogenetic tree (Newick format), SNP matrix, distance matrix, visualization files.
- **Use Case**: Rapid pathogen surveillance, outbreak investigation, microbial genomics, metagenomic analysis.

## Pitfalls

- **Read quality**: Poor quality reads affect SNP calling accuracy.
- **Coverage depth**: Uneven coverage may bias SNP detection.
- **Sample diversity**: Requires sufficient genetic diversity for meaningful trees.
- **Computational resources**: Large datasets require significant memory and CPU.
- **Reference bias**: When reference is provided, may introduce reference bias.
- **K-mer selection**: K-mer size selection affects sensitivity and specificity.

## Examples

### Build tree from raw reads
**Args:** `saffrontree -r reads_*.fastq -o tree.nwk`
**Explanation:** `-r` raw FASTQ files; `-o` output tree in Newick format.

### With reference genome
**Args:** `saffrontree -r reads_*.fastq -g reference.fasta -o tree.nwk`
**Explanation:** `-g` reference genome for SNP validation.

### Specify k-mer size
**Args:** `saffrontree -r reads_*.fastq -o tree.nwk -k 31`
**Explanation:** `-k` k-mer size (default: 21).

### Output SNP matrix
**Args:** `saffrontree -r reads_*.fastq -o tree.nwk --snps snps.txt`
**Explanation:** `--snps` outputs SNP matrix to file.

### Bootstrap support
**Args:** `saffrontree -r reads_*.fastq -o tree.nwk -b 100`
**Explanation:** `-b` number of bootstrap replicates.

### Distance matrix output
**Args:** `saffrontree -r reads_*.fastq -o tree.nwk --distance distance.txt`
**Explanation:** `--distance` outputs pairwise distance matrix.

### Minimum coverage filter
**Args:** `saffrontree -r reads_*.fastq -o tree.nwk -c 10`
**Explanation:** `-c` minimum coverage for SNP calling.