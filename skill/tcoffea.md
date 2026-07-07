---
name: tcoffea
category: genomics
description: Coffea genomics tools - utilities for analyzing coffee (Coffea) genome sequences and variations.
tags: [tcoffea, coffea, coffee, plant-genomics, arabica, canephora, genome-analysis]
author: oxo-call-community
source_url: "https://github.com/cafetgenomics/tcoffea"
---

## Concepts

- **Tool Overview**: tcoffea - A toolkit for Coffee (Coffea genus) genomics analysis, specifically designed for working with Coffea arabica and Coffea canephora genome data.
- **Core Function**: Provides utilities for analyzing coffee genome sequences, including gene annotation, variant calling, and comparative genomics between coffee species.
- **Species Focus**: Primarily supports Coffea arabica (tetraploid) and Coffea canephora (diploid progenitor) genome analyses.
- **Input**: Coffee genome sequences in FASTA format, annotation files (GFF3), and variation data (VCF).
- **Installation**: `pip install tcoffea` or from GitHub repository
- **Use Case**: Coffee breeding research, caffeine biosynthesis pathways, stress response studies in coffee plants.

## Pitfalls

- **Species-Specific**: Designed specifically for Coffea species - not applicable to other plant genomics analyses.
- **Reference Genome**: Requires Coffea reference genome for alignment and variant calling - not included in package.
- **Ploidy Consideration**: Coffea arabica is tetraploid (4x) - analysis methods must account for polyploidy.
- **Data Availability**: Coffee genome annotations may be incomplete or vary between different genome versions.

## Examples

### Coffee genome indexing
**Args:** `tcoffea index -g coffea_genome.fasta -o index/`
**Explanation:** Build genome index for Coffea reference sequence.

### Gene annotation extraction
**Args:** `tcoffea extract-genes -g annotation.gff3 -o genes.fasta`
**Explanation:** Extract coding sequences for annotated genes from coffee genome.

### Variant calling
**Args:** `tcoffea call-variants -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants against coffee reference genome from aligned reads.

### Comparative analysis
**Args:** `tcoffea compare -s1 arabica.gff3 -s2 canephora.gff3 -o comparison/`
**Explanation:** Compare gene annotations between C. arabica and C. canephora genomes.
