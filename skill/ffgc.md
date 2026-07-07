---
name: ffgc
category: annotation
description: "Family Free Genome Comparison (FFGC) workflow"
tags: [ffgc, annotation, genome-comparison, gene-order, bioinformatics]
author: oxo-call-community
source_url: "https://gitlab.ub.uni-bielefeld.de/gi/FFGC"
---

## Concepts

- **Tool Overview**: FFGC is a workflow system for family-free gene order analysis, comparing genomes without requiring prior knowledge of gene family relationships.
- **Core Function**: Performs genome comparison using gene order analysis without gene family assignments.
- **Input/Output**: Input: Annotated genome sequences. Output: Comparison results, synteny plots.
- **Algorithm**: Uses local alignment and gene relationship establishment for comparison.
- **Key Features**: Family-free analysis, gene order comparison, workflow system, gene family inference, multiple genome support.
- **Installation**: `conda install -c bioconda ffgc`

## Pitfalls

- **Genome Annotation**: Requires well-annotated genome sequences.
- **Computational Complexity**: Large genomes may require significant resources.
- **Alignment Quality**: Results depend on sequence alignment quality.
- **Gene Relationships**: Gene relationship establishment can be complex.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic genome comparison
**Args:** `ffgc -i genome1.gbk genome2.gbk -o comparison_results/`
**Explanation:** Compares two genomes.

### Multiple genomes
**Args:** `ffgc -i genomes/ -o results/`
**Explanation:** Compares multiple genomes.

### With gene family inference
**Args:** `ffgc -i genomes/ -o results/ --infer-families`
**Explanation:** Infers gene families during comparison.

### Alignment settings
**Args:** `ffgc -i genomes/ -o results/ --aligner diamond`
**Explanation:** Uses Diamond aligner.

### Visualization
**Args:** `ffgc -i genomes/ -o results/ --plot`
**Explanation:** Generates comparison plots.