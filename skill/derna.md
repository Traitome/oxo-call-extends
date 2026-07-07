---
name: derna
category: annotation
description: derNA - RNA sequence design for target protein sequences.
tags: [derna, annotation, rna-design, protein, codon-optimization]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/derna"
---

## Concepts

- **Tool Overview**: derna (v1.0.4+) is a tool for designing RNA sequences that encode a target protein sequence. It optimizes codon usage and considers structural constraints.
- **Core Function**: Designs optimal RNA coding sequences for given protein targets, optimizing for expression level, codon adaptation, and RNA stability.
- **Input/Output**: Input: Protein sequence (FASTA), optional codon usage table. Output: Designed RNA sequences, optimization metrics.
- **Algorithm**: Uses optimization algorithms to select codons that maximize expression while maintaining structural stability.
- **Key Features**: Codon optimization, RNA structure prediction, multiple design strategies, supports custom codon tables, visualization.
- **Installation**: `conda install -c bioconda derna`

## Pitfalls

- **Input Requirements**: Requires valid protein sequence in FASTA format.
- **Organism Specificity**: Codon optimization requires organism-specific codon usage data.
- **Structure Prediction**: RNA structure predictions may not always be accurate.
- **Design Constraints**: Complex constraints may limit design space.
- **Expression Context**: Designed sequences may perform differently in different expression systems.

## Examples

### Design RNA sequence for protein
**Args:** `derna --protein target.fa --output rna_design.fa`
**Explanation:** Designs RNA sequence encoding the target protein.

### With organism-specific codon usage
**Args:** `derna --protein target.fa --output rna_design.fa --organism yeast`
**Explanation:** Optimize codon usage for yeast expression.

### With structure constraints
**Args:** `derna --protein target.fa --output rna_design.fa --structure --free-energy -50`
**Explanation:** Design RNA with target free energy constraint.