---
name: ctyper
category: variant-calling
description: Genotyping sequence-resolved copy-number variation using pangenomes.
tags: [ctyper, variant-calling, copy-number-variation, CNV, pangenome, genotyping]
author: oxo-call-community
source_url: "https://github.com/ChaissonLab/Ctyper"
---

## Concepts

- **Tool Overview**: ctyper (v1.0.5+) is a tool for genotyping sequence-resolved copy-number variations using pangenome references.
- **Core Function**: Uses pangenome graphs to genotype structural variants and copy-number changes across populations.
- **Input/Output**: Input: BAM alignments, pangenome graph, variant catalog. Output: Genotyped CNV calls, dosage estimates.
- **Algorithm**: Aligns reads to pangenome graph and infers copy-number states using Bayesian inference.
- **Key Features**: Population-aware genotyping, handles complex structural variants, integrates with graph genome representations.
- **Installation**: `conda install -c bioconda ctyper`

## Pitfalls

- **Pangenome Index**: Requires pre-built pangenome index; time-consuming to construct.
- **Memory Usage**: Pangenome alignment requires significant memory for graph traversal.
- **Reference Compatibility**: Ensure pangenome reference matches input data.
- **Variant Catalog**: Needs comprehensive variant catalog for accurate genotyping.
- **Output Interpretation**: CNV calls should be validated with orthogonal methods.

## Examples

### Build pangenome index
**Args:** `ctyper build -r reference.fasta -v variants.vcf -o pangenome/`
**Explanation:** Build pangenome index from reference and variant catalog.

### Genotype CNVs
**Args:** `ctyper genotype -i aligned.bam -p pangenome/ -o cnv_calls.vcf`
**Explanation:** Genotype copy-number variations using pangenome reference.

### Estimate copy-number dosage
**Args:** `ctyper dosage -i aligned.bam -p pangenome/ -o dosage.tsv`
**Explanation:** Estimate copy-number dosage for each sample.
