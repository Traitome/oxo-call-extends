---
name: sciphi
category: variant-calling
description: SCIPhI - Single-cell mutation identification via phylogenetic inference
tags: ["sciphi", "variant-calling", "single-cell", "phylogenetics"]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/SCIPhI"
---

## Concepts

- **Tool Overview**: SCIPhI (v0.1.7) is a tool for single-cell mutation identification via phylogenetic inference.
- **Core Function**: Identifies mutations from single-cell sequencing data using phylogenetic methods.
- **Algorithm**: Uses Bayesian phylogenetic inference to call variants from single-cell data.
- **Input/Output**: Accepts aligned reads and produces mutation calls with confidence scores.
- **Single-Cell Focus**: Specifically designed for single-cell sequencing data analysis.
- **Applications**: Cancer genomics, somatic mutation detection, and clonal evolution analysis.

## Pitfalls

- **Computational Resources**: High memory and CPU requirements.
- **Phylogenetic Assumptions**: Assumes tree-like evolutionary relationships.
- **Read Depth**: Requires sufficient sequencing depth per cell.
- **Allelic Dropout**: May miss heterozygous variants due to dropout.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **False Positives**: May report false mutations from sequencing errors.

## Examples

### Basic mutation calling
**Args:** `sciphi -i aligned.bam -r reference.fasta -o mutations.vcf`
**Explanation:** `-i` input BAM; `-r` reference genome; `-o` output VCF.

### With quality filtering
**Args:** `sciphi -i aligned.bam -r reference.fasta -q 20 -o mutations.vcf`
**Explanation:** `-q 20` filters mutations with quality below 20.

### Phylogenetic tree
**Args:** `sciphi -i aligned.bam -r reference.fasta --tree -o tree.nwk`
**Explanation:** `--tree` outputs phylogenetic tree.

### Multiple cells
**Args:** `sciphi -i cell1.bam cell2.bam -r reference.fasta -o mutations.vcf`
**Explanation:** Processes multiple single-cell BAM files.

### Verbose logging
**Args:** `sciphi -i aligned.bam -r reference.fasta -v -o mutations.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Output confidence scores
**Args:** `sciphi -i aligned.bam -r reference.fasta --confidence -o mutations.vcf`
**Explanation:** `--confidence` outputs confidence scores for each mutation.

### Targeted regions
**Args:** `sciphi -i aligned.bam -r reference.fasta -t targets.bed -o mutations.vcf`
**Explanation:** `-t` BED file with target regions.