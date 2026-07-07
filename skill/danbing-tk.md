---
name: danbing-tk
category: variant-calling
description: Toolkit for VNTR genotyping and repeat-pan genome graph construction
tags: [danbing-tk, variant-calling, VNTR, repeat, genotyping, pangenome]
author: oxo-call-community
source_url: "https://github.com/ChaissonLab/danbing-tk"
---

## Concepts

- **Tool Overview**: danbing-tk (v1.3.2.5+) is a toolkit for Variable Number Tandem Repeat (VNTR) genotyping and repeat-pan genome graph construction.
- **Core Function**: Genotypes VNTRs from sequencing data and constructs repeat-focused pangenome graphs.
- **Input/Output**: Input: BAM alignments, repeat definitions. Output: VNTR genotypes, repeat graphs.
- **Algorithm**: Uses read-based analysis for VNTR characterization and graph construction.
- **Key Features**: Accurate VNTR genotyping, handles complex repeats, pangenome integration.
- **Installation**: `conda install -c bioconda danbing-tk`

## Pitfalls

- **Repeat Definition**: Requires accurate VNTR repeat definitions.
- **Read Length**: Long reads preferred for complex VNTR regions.
- **Coverage**: Adequate coverage needed for accurate genotyping.
- **Complex Regions**: Highly variable VNTRs may be challenging.
- **Validation**: VNTR calls should be validated against known standards.

## Examples

### Genotype VNTRs
**Args:** `danbing genotype -i aligned.bam -r reference.fasta -o vntr_calls.tsv`
**Explanation:** Genotype VNTRs from aligned sequencing data.

### Build repeat graph
**Args:** `danbing graph -i reads.fastq -o repeat_graph.gfa --vntr vntrs.bed`
**Explanation:** Construct repeat-pan genome graph from sequencing data.

### Specify VNTR regions
**Args:** `danbing genotype -i aligned.bam -v vntr_regions.bed -o results.tsv`
**Explanation:** Genotype specific VNTR regions of interest.
