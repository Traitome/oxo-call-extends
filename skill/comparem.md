---
name: comparem
category: utility
description: Toolbox for comparative genomics analysis
tags: [comparem, comparative-genomics, aai, anm, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dparks1134/CompareM"
---

## Concepts

- **Tool Overview**: CompareM is a comprehensive toolbox for comparative genomics, providing tools for calculating Average Amino acid Identity (AAI), Average Nucleotide Identity (ANI), and other genomic comparison metrics.
- **Core Function**: Computes various genomic comparison metrics including AAI, ANI, and gene content similarity for taxonomic classification and evolutionary analysis.
- **Algorithm**: Uses sequence alignment and identity calculations to quantify genomic similarity between organisms.
- **Input**: Genome sequences in FASTA format, protein or nucleotide sequences.
- **Output**: Identity matrices, similarity scores, and comparative analysis reports.
- **Application**: Taxonomic classification, species delineation, and evolutionary relationship analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda comparem`

## Pitfalls

- **Computational Time**: Pairwise comparisons scale quadratically with number of genomes.
- **Sequence Quality**: Results depend on genome assembly and annotation quality.
- **Threshold Selection**: Taxonomic thresholds may vary between groups.
- **Gene Prediction**: AAI calculations depend on accurate gene prediction.
- **Memory Usage**: Large genome sets require significant memory.

## Examples

### Calculate AAI matrix
**Args:** `comparem aai -i genomes/ -o aai_matrix.txt`
**Explanation:** Calculates Average Amino acid Identity between all genomes.

### Calculate ANI
**Args:** `comparem ani -i genome1.fasta genome2.fasta -o ani_result.txt`
**Explanation:** Computes Average Nucleotide Identity between two genomes.

### Taxonomic classification
**Args:** `comparem classify -i query.fasta -r reference_db/ -o classification.txt`
**Explanation:** Classifies query genome based on AAI/ANI thresholds.

### Display help
**Args:** `comparem --help`
**Explanation:** Shows all available options and usage information.