---
name: graphtyper
category: bioinformatics
description: GraphTyper performs population-scale genotyping using pangenome graphs for efficient variant discovery and genotyping.
tags: [graphtyper, genotyping, pangenome, population-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/DecodeGenetics/graphtyper"
---

## Concepts

- **Pangenome Graph Genotyping**: GraphTyper uses pangenome graphs to genotype populations efficiently.

- **Variant Discovery**: Identifies genetic variants from sequencing data using graph-based approaches.

- **Population-Scale Analysis**: Designed for large-scale population genotyping studies.

- **Graph Construction**: Builds pangenome graphs from multiple reference sequences.

- **Genotype Calling**: Calls genotypes for multiple samples simultaneously.

- **Efficiency**: Optimized for speed and memory usage with parallel processing support.

## Pitfalls

- **Graph Construction**: Building pangenome graphs requires significant computational resources.

- **Reference Selection**: Choose appropriate reference sequences for graph construction.

- **Memory Requirements**: Processing large populations may require significant memory.

- **Variant Quality**: Low-quality variants may be called. Apply quality filters.

- **Parameter Tuning**: Adjust parameters based on sequencing technology and population characteristics.

## Examples

### Build pangenome graph
**Args:** `graphtyper build -r reference.fasta -v variants.vcf -o graph.gfa`
**Explanation:** Builds a pangenome graph from a reference and variant calls.

### Genotype samples
**Args:** `graphtyper genotype -g graph.gfa -i reads.bam -o genotypes.vcf`
**Explanation:** Genotypes samples using the pangenome graph.

### Call variants
**Args:** `graphtyper call -g graph.gfa -i reads.bam -o variants.vcf`
**Explanation:** Calls variants from aligned reads using the pangenome graph.

### Phase genotypes
**Args:** `graphtyper phase -i genotypes.vcf -o phased.vcf`
**Explanation:** Phases genotype calls to determine haplotypes.

### Parallel processing
**Args:** `graphtyper genotype -g graph.gfa -i reads.bam -t 8 -o genotypes.vcf`
**Explanation:** Uses 8 threads for parallel genotyping.

### Generate statistics
**Args:** `graphtyper stats -i genotypes.vcf -o stats.txt`
**Explanation:** Generates statistics about the genotyping results.

### Filter variants
**Args:** `graphtyper filter -i variants.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters variants with quality score below 30.