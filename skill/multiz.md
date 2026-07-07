---
name: multiz
category: alignment
description: MultiZ is a multiple DNA sequence aligner developed by Penn State Miller Lab for comparative genomics.
tags: [multiz, multiple-sequence-alignment, dna-alignment, comparative-genomics, phylogenetics]
author: oxo-call-community
source_url: "http://www.bx.psu.edu/miller_lab/"
---

## Concepts

- **Tool Overview**: MultiZ v11.2 is a multiple DNA sequence aligner developed at Penn State University by the Miller Lab. It produces whole-genome multiple alignments across multiple species for comparative genomics analysis.
- **Core Function**: Performs efficient multiple genome alignment without requiring a reference sequence. Uses a graph-based approach to handle rearrangements, duplications, and species-specific insertions.
- **Algorithm**: Employs a two-stage approach: first identifies homologous regions using a reference genome, then extends to multiple species alignment using progressive alignment strategies.
- **Input Format**: Accepts multiple FASTA or multi-FASTA files, one per species/genome. Requires genome assemblies in chromosome-level or scaffold-level format.
- **Output**: Produces alignments in MAF (Multiple Alignment Format) or MultiZ native format. Contains per-base alignment coordinates and conservation scores.
- **Applications**: Comparative genomics, evolutionary analysis, conserved element identification, phylogenetic modeling, and genome annotation transfer between species.

## Pitfalls

- **Genome Quality**: Draft genomes with many contigs or gaps produce fragmented alignments. Use chromosome-level assemblies when possible for meaningful conservation analysis.
- **Reference Choice**: While MultiZ doesn't require a reference for final output, the alignment quality depends heavily on the reference genome choice. Use a high-quality, well-annotated reference.
- **Computational Requirements**: Whole-genome alignment of many mammalian genomes requires substantial memory (64GB+) and CPU time (days). Plan resources accordingly.
- **Synteny Breaking**: Genomes with extensive rearrangements (e.g., plants) produce fragmented alignments. Consider using synteny-aware tools for highly rearranged genomes.
- **Coordinate Systems**: Output coordinates depend on the reference genome used. Different references produce incompatible coordinate systems across analyses.
- **MAF Processing**: MAF format requires specialized tools (like maftools, hawaii, or pytasks) for downstream analysis. Ensure compatibility with your analysis pipeline.

## Examples

### Basic multiple genome alignment
**Args:** `multiz genomes/ species.txt output.maf`
**Explanation:** Aligns genomes listed in species.txt file. Each genome should be in a separate multi-FASTA file in the genomes/ directory.

### Specify reference genome
**Args:** `multiz genomes/ species.txt ref=hg38 output.maf`
**Explanation:** Sets hg38 as the reference genome for coordinate system. Reference should be high-quality and present in the species list.

### Produce species-specific alignment blocks
**Args:** `multiz genomes/ species.txt output.maf --blocks`
**Explanation:** Generates alignment blocks containing only species present at each position. Useful for identifying species-specific conserved regions.

### Use threading for faster alignment
**Args:** `multiz genomes/ species.txt -t 16 output.maf`
**Explanation:** Uses 16 threads for parallel processing. Significant speedup for large genomes but increases memory consumption proportionally.

### Extract conserved regions
**Args:** `multiz Maf2Cons --alignment output.maf --organism human --minlength 100`
**Explanation:** Converts MAF alignment to conservation scores. Identifies conserved elements at least 100bp long in human.

### Convert MAF to FASTA alignment
**Args:** `maf_parse output.maf | maf2fasta --ref human > alignment.fa`
**Explanation:** Converts MAF format to FASTA alignment format for phylogenetic tools. Requires maftools or similar utilities.
