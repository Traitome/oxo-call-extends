---
name: jcvi
category: assembly
description: Python utility libraries for genome assembly, annotation, and comparative genomics.
tags: [jcvi, assembly, genomics, comparative, python]
author: oxo-call-community
source_url: "https://github.com/tanghaibao/jcvi/wiki"
---

## Concepts

- **Tool Overview**: jcvi (v1.6.5) - A collection of Python utilities for genome assembly, annotation, and comparative genomics analyses.
- **Genome Assembly**: Provides tools for assembling and analyzing genome sequences.
- **Annotation**: Utilities for genome annotation and feature prediction.
- **Comparative Genomics**: Tools for comparing multiple genomes and identifying syntenic regions.
- **Synteny Analysis**: Identifies conserved genomic regions across species.
- **Visualization**: Generates visualizations of genome comparisons and assemblies.

## Pitfalls

- **Python Dependencies**: Requires specific Python packages and versions.
- **Memory Usage**: Large genome comparisons require significant memory.
- **Reference Genome**: Quality of results depends on reference genome quality.
- **Computational Time**: Comparative analyses can be computationally intensive.
- **File Format**: Requires specific input file formats.
- **Version Compatibility**: Scripts may break between versions.

## Examples

### Run genome assembly pipeline
**Args:** `python -m jcvi.assembly assembly.py config.yml`
**Explanation:** Runs genome assembly pipeline with configuration file.

### Perform synteny analysis
**Args:** `python -m jcvi.compara.synteny seqids.txt`
**Explanation:** Analyzes syntenic relationships between genomes.

### Generate dotplot
**Args:** `python -m jcvi.graphics.dotplot seq1.fasta seq2.fasta`
**Explanation:** Generates dotplot comparing two sequences.

### Annotate genome
**Args:** `python -m jcvi.annotation.annotate --genome ref.fasta --gff genes.gff`
**Explanation:** Annotates genome using GFF file.

### Compare assemblies
**Args:** `python -m jcvi.assembly.compare asm1.fasta asm2.fasta`
**Explanation:** Compares two genome assemblies.

### Run BUSCO analysis
**Args:** `python -m jcvi.assembly.busco --genome ref.fasta --lineage eukaryota`
**Explanation:** Runs BUSCO completeness assessment.