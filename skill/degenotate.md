---
name: degenotate
category: population-genomics
description: Degeneracy annotation toolkit for codons in coding sequences.
tags: [degenotate, population-genomics, annotation, codon, selection]
author: oxo-call-community
source_url: "https://github.com/harvardinformatics/degenotate"
---

## Concepts

- **Tool Overview**: degenotate is a toolkit for annotating codon degeneracy in coding sequences, essential for population genetics and selection analyses. It categorizes codon positions by their degeneracy level.
- **Core Function**: Annotates codon positions as 0-fold (non-degenerate), 2-fold, or 4-fold degenerate, enabling analyses of selective constraints and evolutionary patterns.
- **Input/Output**: Input: GFF annotation file, FASTA genome sequence. Output: Degeneracy annotations in tabular format, compatible with downstream population genetics tools.
- **Algorithm**: Uses codon table to determine degeneracy based on genetic code, identifying synonymous and non-synonymous sites.
- **Key Features**: Supports multiple genetic codes, handles overlapping genes, generates BED output, integrates with selection analysis pipelines.
- **Installation**: `conda install -c bioconda degenotate`

## Pitfalls

- **Input Requirements**: Requires properly formatted GFF3 and matching FASTA files.
- **Genetic Code**: Must specify correct genetic code for non-standard organisms.
- **Overlapping Genes**: May produce ambiguous results for overlapping coding sequences.
- **Quality Control**: Requires high-quality annotations and sequences.
- **Frame Shifts**: Will produce incorrect results if sequences have frame shifts.

## Examples

### Annotate codon degeneracy
**Args:** `degenotate --gff annotation.gff --fasta genome.fa --output degen.tsv`
**Explanation:** Annotates codon degeneracy for all coding sequences.

### With custom genetic code
**Args:** `degenotate --gff annotation.gff --fasta genome.fa --output degen.tsv --genetic-code 11`
**Explanation:** Use alternative genetic code (11 = bacterial, archaeal, plant plastid).

### Generate BED output
**Args:** `degenotate --gff annotation.gff --fasta genome.fa --output degen.bed --bed`
**Explanation:** Output results in BED format for genome browser visualization.