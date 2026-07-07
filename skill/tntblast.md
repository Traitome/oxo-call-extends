---
name: tntblast
category: analysis
description: TNT-BLAST - Transposon-targeted BLAST search tool.
tags: [tntblast, blast, transposon, sequence-search, homology]
author: oxo-call-community
source_url: "https://github.com/compbio/tntblast"
---

## Concepts

- **Tool Overview**: TNT-BLAST - A specialized BLAST tool for searching transposon sequences in genomic data.
- **Core Function**: Performs BLAST searches optimized for transposon detection and analysis.
- **Input**: Query sequences (FASTA), database sequences, transposon profiles.
- **Output**: BLAST alignments, transposon matches, annotation results.
- **Installation**: `pip install tntblast` or `conda install -c bioconda tntblast`
- **Use Case**: Transposon identification, homology search, genome annotation.

## Pitfalls

- **Database Size**: Large databases require significant memory.
- **Sensitivity**: Adjust parameters based on expected similarity.

## Examples

### Search transposons
**Args:** `tntblast -q query.fasta -d genome_db -o blast_results/`
**Explanation:** Search for transposon sequences in genome database.

### Custom parameters
**Args:** `tntblast -q sequence.fasta -d db -e 1e-10 -o sensitive_results/`
**Explanation:** Perform sensitive BLAST search with custom e-value threshold.
