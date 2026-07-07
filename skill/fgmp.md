---
name: fgmp
category: utility
description: "FGMP: assessing fungal genome completeness and gene content."
tags: [fgmp, utility, fungal-genomics, genome-assessment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/stajichlab/FGMP"
---

## Concepts

- **Tool Overview**: FGMP is a tool for assessing fungal genome completeness and gene content using conserved fungal markers.
- **Core Function**: Evaluates genome completeness and gene content in fungal genomes.
- **Input/Output**: Input: Fungal genome assembly. Output: Completeness report, gene content analysis.
- **Algorithm**: Uses conserved fungal markers for genome assessment.
- **Key Features**: Fungal-specific, genome completeness, gene content analysis, phylogenetics, automated reporting.
- **Installation**: `conda install -c bioconda fgmp`

## Pitfalls

- **Fungal Specificity**: Designed specifically for fungal genomes.
- **Genome Quality**: Results depend on assembly quality.
- **Marker Selection**: Marker selection affects completeness assessment.
- **Database Dependency**: Requires updated fungal marker database.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic genome assessment
**Args:** `fgmp -i genome.fasta -o assessment_report.txt`
**Explanation:** Assesses fungal genome completeness.

### Gene content analysis
**Args:** `fgmp -i genome.fasta -o results/ --gene-content`
**Explanation:** Analyzes gene content.

### With phylogeny
**Args:** `fgmp -i genome.fasta -o results/ --phylogeny`
**Explanation:** Includes phylogenetic analysis.

### Multiple genomes
**Args:** `fgmp -i genomes/ -o results/ --batch`
**Explanation:** Assesses multiple fungal genomes.

### Detailed output
**Args:** `fgmp -i genome.fasta -o results/ --detailed`
**Explanation:** Generates detailed assessment report.