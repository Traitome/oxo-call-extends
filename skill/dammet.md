---
name: dammet
category: epigenomics
description: Software to reconstruct methylomes from HTS data from ancient specimens
tags: [dammet, epigenomics, methylation, ancient-DNA, methylome]
author: oxo-call-community
source_url: "https://github.com/KHanghoj/DamMet"
---

## Concepts

- **Tool Overview**: dammet (v1.0.4+) is software for reconstructing methylomes from high-throughput sequencing data of ancient specimens.
- **Core Function**: Reconstructs DNA methylation patterns while accounting for ancient DNA damage patterns.
- **Input/Output**: Input: BAM alignments, reference genome. Output: Methylation profiles, CpG matrices.
- **Algorithm**: Uses probabilistic models to separate true methylation from damage-induced patterns.
- **Key Features**: Handles aDNA damage, deamination correction, ancient specimen analysis.
- **Installation**: `conda install -c bioconda dammet`

## Pitfalls

- **Damage Modeling**: Requires accurate damage models for reliable results.
- **Coverage Requirements**: Adequate coverage needed for methylation calling.
- **Reference Quality**: Results depend on reference genome quality.
- **Computational Complexity**: Processing can be computationally intensive.
- **Validation**: Results should be interpreted cautiously due to damage.

## Examples

### Reconstruct methylome
**Args:** `dammet -i aligned.bam -r reference.fasta -o methylation.tsv`
**Explanation:** Reconstruct methylation patterns from ancient DNA data.

### Specify damage model
**Args:** `dammet -i aligned.bam -r reference.fasta -o results.tsv --damage-model 0.03`
**Explanation:** Use custom damage rate in methylation reconstruction.

### Output per-base methylation
**Args:** `dammet -i aligned.bam -r reference.fasta -o results.tsv --per-base`
**Explanation:** Generate per-base methylation calls.
