---
name: mitos
category: annotation
description: MITOS is a tool for the annotation of metazoan mitochondrial genomes.
tags: [mitos, annotation, mitochondrial]
author: oxo-call-community
source_url: "http://mitos.bioinf.uni-leipzig.de"
---

## Concepts

- **Tool Overview**: MITOS v2.1.10 annotates metazoan mitochondrial genomes.
- **Core Function**: Identifies and annotates mitochondrial genes.
- **Metazoan Specific**: Specialized for animal mitochondrial genomes.
- **Gene Annotation**: Automatically identifies tRNA, rRNA, and protein-coding genes.
- **Input/Output**: Accepts genome sequences; outputs annotated features.
- **Mitochondrial Genomics**: Supports complete mtDNA annotation workflows.

## Pitfalls

- **Metazoan Specific**: Designed for animal mitochondria.
- **Computational Resources**: Annotation may require significant resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal annotation.
- **Data Quality**: Results depend on input sequence quality.
- **Reference Databases**: Requires appropriate annotation databases.

## Examples

### Annotate mitochondrial genome
**Args:** `mitos.py -i genome.fasta -o annotation/`
**Explanation:** Runs mitochondrial genome annotation.

### With genetic code
**Args:** `mitos.py -i genome.fasta -g 5 -o annotation/`
**Explanation:** Uses genetic code 5 (invertebrate mitochondrial).

### Verbose output
**Args:** `mitos.py -i genome.fasta -o annotation/ -v`
**Explanation:** Shows detailed annotation progress.

### Batch processing
**Args:** `mitos.py -i fasta/ -o annotations/`
**Explanation:** Processes multiple genome files.

### Generate report
**Args:** `mitos.py -i genome.fasta -o annotation/ -r report.html`
**Explanation:** Generates annotation report.