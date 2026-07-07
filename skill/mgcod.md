---
name: mgcod
category: annotation
description: Recognition of genetic codes (incl. multiple genetic codes in phage genomes) and genetic-code-informed annotation of coding regions in prokaryotic sequences
tags: [mgcod, annotation, genetic-code]
author: oxo-call-community
source_url: "https://github.com/gatech-genemark/Mgcod"
---

## Concepts

- **Tool Overview**: Mgcod v1.0.2 recognizes genetic codes and performs genetic-code-informed annotation of coding regions in prokaryotic sequences.
- **Core Function**: Identifies genetic codes and annotates coding regions.
- **Genetic Code Detection**: Detects multiple genetic codes in genomes.
- **Phage Support**: Special support for phage genomes with multiple genetic codes.
- **Input/Output**: Accepts prokaryotic sequences; outputs annotated coding regions.
- **Code-specific Annotation**: Uses detected genetic codes for accurate annotation.

## Pitfalls

- **Prokaryotic Focus**: Designed for prokaryotic sequences.
- **Computational Resources**: Processing large genomes may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal detection.
- **Data Quality**: Annotation accuracy depends on input sequence quality.
- **Complex Genomes**: May struggle with highly fragmented sequences.

## Examples

### Detect genetic code
**Args:** `mgcod detect -i genome.fasta -o code.txt`
**Explanation:** Detects genetic codes in prokaryotic genome.

### Annotate coding regions
**Args:** `mgcod annotate -i genome.fasta -o annotation.gff`
**Explanation:** Annotates coding regions using detected genetic codes.

### With known genetic code
**Args:** `mgcod annotate -i genome.fasta -c 11 -o annotation.gff`
**Explanation:** Uses specific genetic code (11) for annotation.

### Phage genome analysis
**Args:** `mgcod phage -i phage.fasta -o phage_annotation.gff`
**Explanation:** Analyzes phage genome with potential multiple genetic codes.

### Batch processing
**Args:** `mgcod -i genomes/ -o annotations/`
**Explanation:** Processes multiple genomes in batch mode.