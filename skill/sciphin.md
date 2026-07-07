---
name: sciphin
category: variant-calling
description: SCIPhIn - Single-Cell mutation Identification via finite-sites Phylogenetic Inference
tags: ["sciphin", "variant-calling", "single-cell", "phylogenetics"]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/SCIPhI"
---

## Concepts

- **Tool Overview**: SCIPhIn (v1.0.1) is a tool for Single-Cell mutation Identification via finite-sites Phylogenetic Inference.
- **Core Function**: Identifies mutations from single-cell sequencing data using finite-sites phylogenetic models.
- **Algorithm**: Uses finite-sites model to account for multiple mutations at the same site.
- **Input/Output**: Accepts aligned reads and produces mutation calls with confidence scores.
- **Finite-Sites Model**: Accounts for the possibility of multiple mutations at the same position.
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
**Args:** `sciphin -i aligned.bam -r reference.fasta -o mutations.vcf`
**Explanation:** `-i` input BAM; `-r` reference genome; `-o` output VCF.

### With quality filtering
**Args:** `sciphin -i aligned.bam -r reference.fasta -q 20 -o mutations.vcf`
**Explanation:** `-q 20` filters mutations with quality below 20.

### Finite-sites model
**Args:** `sciphin -i aligned.bam -r reference.fasta --finite-sites -o mutations.vcf`
**Explanation:** `--finite-sites` enables finite-sites mutation model.

### Multiple cells
**Args:** `sciphin -i cell1.bam cell2.bam -r reference.fasta -o mutations.vcf`
**Explanation:** Processes multiple single-cell BAM files.

### Verbose logging
**Args:** `sciphin -i aligned.bam -r reference.fasta -v -o mutations.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Output confidence scores
**Args:** `sciphin -i aligned.bam -r reference.fasta --confidence -o mutations.vcf`
**Explanation:** `--confidence` outputs confidence scores for each mutation.

### Targeted regions
**Args:** `sciphin -i aligned.bam -r reference.fasta -t targets.bed -o mutations.vcf`
**Explanation:** `-t` BED file with target regions.