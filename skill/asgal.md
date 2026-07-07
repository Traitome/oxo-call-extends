---
name: asgal
category: alignment
description: ASGAL - A graph aligner for sequence alignment
tags: [asgal, alignment, graph-alignment, sequence-alignment]
author: oxo-call-community
source_url: "https://asgal.algolab.eu/"
---

## Concepts

- **Tool Overview**: ASGAL (A Graph ALigner) is a graph-based sequence aligner for accurate alignment of sequences to reference graphs. Version 1.1.8.
- **Core Function**: Aligns sequences to graph-based references instead of linear references, capturing genetic variation more effectively.
- **Graph Alignment**: Uses sequence graphs (variation graphs) as reference instead of linear sequences. Captures SNPs, indels, and structural variants.
- **Variation-Aware**: Handles known genetic variations in reference, improving alignment accuracy for divergent sequences.
- **Multiple Alignments**: Reports multiple possible alignments with scores for ambiguous mappings.
- **Input/Output**: Accepts FASTA/FASTQ sequences and graph references, outputs alignment files.
- **Installation**: `conda install -c bioconda asgal` or download from project website.

## Pitfalls

- **Graph Format**: Requires graph reference in specific format. Linear references must be converted to graphs first.
- **Memory Requirements**: Graph alignment requires significant memory for large graphs. Monitor memory usage.
- **Complexity**: Graph alignment is computationally more complex than linear alignment. Slower for large datasets.
- **Graph Construction**: High-quality graph references essential for accurate alignment. Poor graphs produce poor alignments.
- **Alignment Scoring**: Scoring parameters may need tuning for specific applications (e.g., different mismatch penalties).

## Examples

### Display help
**Args:** `asgal --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic graph alignment
**Args:** `asgal --query sequences.fasta --graph reference.gfa --output alignments.sam`
**Explanation:** Aligns query sequences to reference graph in GFA format. Outputs SAM format alignments.

### Specify scoring parameters
**Args:** `asgal --query sequences.fasta --graph reference.gfa --output alignments.sam --match 2 --mismatch -3 --gap -5`
**Explanation:** Sets custom scoring: match score 2, mismatch penalty -3, gap penalty -5.

### Enable multiple alignments
**Args:** `asgal --query sequences.fasta --graph reference.gfa --output alignments.sam --max_alignments 5`
**Explanation:** Reports up to 5 alternative alignments per query. Useful for ambiguous mappings.

### Set alignment mode
**Args:** `asgal --query sequences.fasta --graph reference.gfa --output alignments.sam --mode global`
**Explanation:** Uses global alignment mode instead of default semi-global. Different modes suit different applications.

### Filter by alignment score
**Args:** `asgal --query sequences.fasta --graph reference.gfa --output alignments.sam --min_score 50`
**Explanation:** Filters alignments with minimum score threshold of 50. Removes low-quality alignments.

### Output in different format
**Args:** `asgal --query sequences.fasta --graph reference.gfa --output alignments.paf --format paf`
**Explanation:** Outputs alignments in PAF (PAF) format instead of SAM. PAF is more compact for some applications.