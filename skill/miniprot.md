---
name: miniprot
category: alignment
description: Miniprot aligns a protein sequence against a genome with affine gap penalty, splicing and frameshift. It is primarily intended for annotating protein-coding genes in a new species using known genes from other species.
tags: [miniprot, alignment, gene-annotation]
author: oxo-call-community
source_url: "https://github.com/lh3/miniprot"
---

## Concepts

- **Tool Overview**: Miniprot v0.18 aligns proteins to genomes with splicing support.
- **Core Function**: Aligns protein sequences to genomic sequences.
- **Spliced Alignment**: Handles intron-exon boundaries in alignments.
- **Frameshift Detection**: Identifies frameshift mutations.
- **Input/Output**: Accepts protein and genome sequences; outputs alignments.
- **Gene Annotation**: Supports gene structure prediction workflows.

## Pitfalls

- **Protein-Genome Alignment**: Designed for protein-to-genome mapping.
- **Computational Resources**: Aligning large genomes may require significant resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal alignment.
- **Data Quality**: Alignment accuracy depends on input data quality.
- **Homology Dependence**: Works best with closely related sequences.

## Examples

### Align protein to genome
**Args:** `miniprot -d genome.fasta proteins.fasta > alignments.gff`
**Explanation:** Aligns proteins to genome and predicts gene structures.

### With frameshift detection
**Args:** `miniprot -f -d genome.fasta proteins.fasta > alignments.gff`
**Explanation:** Enables frameshift detection.

### Custom sensitivity
**Args:** `miniprot -s 10 -d genome.fasta proteins.fasta > alignments.gff`
**Explanation:** Sets sensitivity level to 10.

### Batch processing
**Args:** `miniprot -d genome.fasta fasta/*.fasta > alignments.gff`
**Explanation:** Processes multiple protein files.

### Generate GFF output
**Args:** `miniprot -g -d genome.fasta proteins.fasta > genes.gff`
**Explanation:** Outputs gene predictions in GFF format.