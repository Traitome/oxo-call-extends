---
name: earlgrey-partea
category: annotation
description: "Pangenome transposable element annotation pipeline using EarlGrey."
tags: [earlgrey-partea, annotation, pangenome, transposable-elements, TE-annotation]
author: oxo-call-community
source_url: "https://github.com/TobyBaril/EarlGreyParTEA"
---

## Concepts

- **Tool Overview**: EarlGrey ParTEA extends EarlGrey for pangenome-scale transposable element annotation, processing multiple genomes in parallel.
- **Core Function**: Performs cross-species TE clustering and generates comprehensive repeat annotations across multiple genomes.
- **Input/Output**: Input: Multiple genome assemblies (FASTA). Output: Combined TE annotations, cross-species TE clusters.
- **Algorithm**: Extends EarlGrey with parallel processing and cross-species clustering algorithms.
- **Key Features**: Pangenome TE annotation, parallel processing, cross-species clustering, comparative analysis.
- **Installation**: `conda install -c bioconda earlgrey-partea`

## Pitfalls

- **Computation Resources**: Pangenome analysis requires significant computational resources.
- **Genome Completeness**: Incomplete genomes may affect clustering accuracy.
- **Memory Usage**: Multiple genomes require substantial RAM.
- **Species Diversity**: Highly divergent species may produce fragmented clusters.
- **Output Size**: Comprehensive pangenome annotations can be very large.

## Examples

### Basic pangenome TE annotation
**Args:** `--genomes genomes.txt --output pangenome_te.gff`
**Explanation:** Annotates TEs across multiple genomes in pangenome mode.

### With clustering
**Args:** `--genomes genomes.txt --output pangenome_te.gff --cluster`
**Explanation:** Performs cross-species TE clustering.

### Parallel processing
**Args:** `--genomes genomes.txt --output pangenome_te.gff --threads 16`
**Explanation:** Uses 16 threads for parallel processing across genomes.

### Generate statistics
**Args:** `--genomes genomes.txt --output pangenome_te.gff --stats stats.txt`
**Explanation:** Generates statistics about TE content across pangenome.

### Output clusters
**Args:** `--genomes genomes.txt --output pangenome_te.gff --clusters clusters.txt`
**Explanation:** Outputs cross-species TE cluster information.